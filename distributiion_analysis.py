import os
import csv
import sys

'''
这份文件用于分析数据集中每个类在各个子数据集中的分布情况。
'''

class_list=["Pupil","Surgical Tape","Hand","Eye Retractors","Iris","Skin","Cornea","Hydrodissection Cannula","Viscoelastic Cannula","Capsulorhexis Cystotome","Rycroft Cannula","Bonn Forceps","Primary Knife","Phacoemulsifier Handpiece","Lens Injector","I/A Handpiece","Secondary Knife","Micromanipulator","I/A Handpiece Handle","Capsulorhexis Forceps","Rycroft Cannula Handle","Phacoemulsifier Handpiece Handle","Capsulorhexis Cystotome Handle","Secondary Knife Handle","Lens Injector Handle","Suture Needle","Needle Holder","Charleux Cannula","Primary Knife Handle","Vitrectomy Handpiece","Mendez Ring","Marker","Hydrodissection Cannula Handle","Troutman Forceps","Cotton","Iris Hooks","ssim","blpx"]
class_list.remove('ssim')
class_list.remove('blpx')

def get_list_of_files_new(path):
    # 统计每个子数据集中的文件名，并且返回由文件名组成的列表
    path = os.path.join('./dataset/', path)
    files_name_stas = []
    for subdir in os.listdir(path):
        if subdir.startswith('.'):
            continue
        else:
            subdir_path = os.path.join(path, subdir)
            if os.path.isdir(subdir_path):
                for file in os.listdir(subdir_path):                    
                    if not file.startswith('.') and not file.startswith('label_'):
                        files_name_stas.append(file)
    print("Number of files in ", path, " is ", len(files_name_stas))
    return files_name_stas

def stastics_each_class():
    """
    统计每个类在各个子数据集中的分布百分比。
    """
    class_distributions = {} # 用于存储每个类在各子数据集中的分布百分比
    for class_name in class_list:
        print("==================================")
        print("Processing class: ", class_name)
        distributions = [] # 存储当前类在各子数据集中的百分比
        for path in ["train/blacklist", "train/whitelist", "test/blacklist", "test/whitelist"]:
            files = get_list_of_files_new(path)
            files = [file[6:] if file.startswith('label_') or file.startswith('image_') else file for file in files]
            percentage = count_and_percentage(files, class_name) # 获取百分比
            distributions.append(percentage)
        class_distributions[class_name] = distributions

    print("-----------------Class Distributions-----------------")
    # Check if the class distributions are imbalanced
    imbalance_report = check_imbalance(class_distributions, threshold=20) # 阈值可以根据需要调整

    print("-----------------Imbalance Report-----------------")
    for class_name, report in imbalance_report.items():
        print(f"Class: {class_name}, Imbalance Report: {report}")


def count_and_percentage(files, class_name):
    """
    计算每个类在子数据集中的分布百分比。
    """
    total_count = 0
    match_count = 0
    with open('./data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_count += 1
            file_name = os.path.basename(row['img_path'])
            # 如果文件名在当前子数据集中，并且当前行的标签不为0（表示存在该类），则匹配数加一
            if file_name in files and row[class_name] != '0':
                match_count += 1

    # 计算百分比
    if len(files) > 0:
        print("Number of matched files in ", class_name, " is ", match_count)
        percentage = match_count / len(files) * 100
    else:
        percentage = 0
    # 返回计算的百分比
    print("Percentage of ", class_name, " in the dataset is ", percentage, "%")
    print("-----------------------------------")
    return percentage

def check_imbalance(class_distributions, threshold=0.2):
    """
    检查每个类的分布是否不均匀。
    
    参数:
    - class_distributions: Dictionary,键是类名,值是该类在各个子数据集中的占比列表。
    - threshold: float,用于判断分布是否不均匀的阈值。
    
    返回:
    - imbalance_report: 字典，记录每个类是否可能分布不均匀，以及其占比的最大和最小值。
    """
    imbalance_report = {}
    for class_name, distributions in class_distributions.items():
        # ["train/blacklist", "train/whitelist", "test/blacklist", "test/whitelist"]
        conditions = {
            # 条件一：黑名单和白名单中的分布差异超过阈值
            "1": (abs(distributions[0] - distributions[1]) > threshold and (abs(distributions[2] - distributions[3]) > threshold)),
            # 条件二：只有在白名单中有数据，而黑名单中没有数据
            "2": (distributions[0] == 0 and distributions[2] == 0) and (not (distributions[1] ==0) )and (not (distributions[3] == 0)),  
            # 条件三：只有在黑名单中有数据，而白名单中没有数据
            "3": (distributions[1] == 0 and distributions[3] == 0) and (not (distributions[0] ==0) )and (not (distributions[2] == 0)),
        }
        if any(conditions.values()):
            imbalance_report[class_name] = {
            # 'is_imbalanced': True,
            'distribution': distributions,
            }
            if conditions["1"]:
                imbalance_report[class_name]['reason'] = "条件一：黑名单和白名单中的分布差异超过阈值"
            elif conditions["2"]:
                imbalance_report[class_name]['reason'] = "条件二：只有在白名单中有数据，而黑名单中没有数据"
            elif conditions["3"]:
                imbalance_report[class_name]['reason'] = "条件三：只有在黑名单中有数据，而白名单中没有数据"

    return imbalance_report
        
if __name__ == '__main__':
    stastics_each_class()

    
        

    

    


    
