import os
import csv
import sys

class_list=["Pupil","Surgical Tape","Hand","Eye Retractors","Iris","Skin","Cornea","Hydrodissection Cannula","Viscoelastic Cannula","Capsulorhexis Cystotome","Rycroft Cannula","Bonn Forceps","Primary Knife","Phacoemulsifier Handpiece","Lens Injector","I/A Handpiece","Secondary Knife","Micromanipulator","I/A Handpiece Handle","Capsulorhexis Forceps","Rycroft Cannula Handle","Phacoemulsifier Handpiece Handle","Capsulorhexis Cystotome Handle","Secondary Knife Handle","Lens Injector Handle","Suture Needle","Needle Holder","Charleux Cannula","Primary Knife Handle","Vitrectomy Handpiece","Mendez Ring","Marker","Hydrodissection Cannula Handle","Troutman Forceps","Cotton","Iris Hooks","ssim","blpx"]
class_list.remove('ssim')
class_list.remove('blpx')

def get_list_of_files_new(path):
    path = os.path.join('./dataset', path)
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
    return files_name_stas

# read the csv file and check if the file names in 'img_path' column exist in the files list
def count_and_percentage(files):
    print("length of files list: ", len(files))
    total_count = 0
    match_count_surgical_tape = 0
    match_count_hand = 0
    match_count_eye_retractors = 0
    with open('./data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_count += 1
            file_name = os.path.basename(row['img_path'])
            if file_name in files and row['Surgical Tape'] == '0':
                # print(f"{file_name} exists in the files list and its 'Viscoelastic' value is '0'")
                match_count_surgical_tape += 1
            if file_name in files and row['Hand'] == '0':
                # print(f"{file_name} exists in the files list and its 'Hand' value is '0'")
                match_count_hand += 1
            if file_name in files and row['Eye Retractors'] == '0':
                match_count_eye_retractors += 1
            
    print("total count: ", total_count)
    if match_count_surgical_tape == 0:
        print("warning: Surgical Tape has no match")
    else: 
        print(f"Surgical tape: count: {match_count_surgical_tape}, percentage: {match_count_surgical_tape / len(files) * 100}%")
    if match_count_hand == 0:
        print("warning: Hand has no match")
    else:
        print(f"Hand: count: {match_count_hand}, percentage: {match_count_hand / len(files) * 100}%")
    if match_count_eye_retractors == 0:
        print("warning: Eye Retractors has no match")
    else:
        print(f"Eye Retractors: count: {match_count_eye_retractors}, percentage: {match_count_eye_retractors / len(files) * 100}%")
    print("------------------------")

def count_and_percentage_new(files, class_name):
    # print(f"length of files list: {class_name}: ", len(files))
    total_count = 0
    match_count = 0
    with open('./data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_count += 1
            file_name = os.path.basename(row['img_path'])
            if file_name in files and row[class_name] == '0':
                match_count += 1
    if match_count == 0:
        print(f"warning: {class_name} has no match")
    else:
        print(f"{class_name}: percentage: {match_count / len(files) * 100}%")
    print("------------------------")

def stastics_each_directory():
    for path in ["train/blacklist", "train/whitelist", "test/blacklist", "test/whitelist"]:
        print(f"{path}: ")
        files = get_list_of_files_new(path)
        files = [file[6:] if file.startswith('label_') or file.startswith('image_') else file for file in files]
        print(f"length of {path}: ", len(files))
        for class_name in class_list:
            count_and_percentage_new(files, class_name)

def stastics_each_class():
    for class_name in class_list:
        print(f"{class_name}: ")
        for path in ["train/blacklist", "train/whitelist", "test/blacklist", "test/whitelist"]:
            print(f"{path}: ")
            files = get_list_of_files_new(path)
            files = [file[6:] if file.startswith('label_') or file.startswith('image_') else file for file in files]
            count_and_percentage_new(files, class_name)
        print("------------------------")
        print("------------------------")
        print("/n")
        
def stastics_each_class_adjust():
    """
    Calculate the statistics for each class in different subsets of the dataset.
    
    Returns:
        None
    """
    class_distributions = {} # 用于存储每个类在各子数据集中的分布百分比
    for class_name in class_list:
        distributions = [] # 存储当前类在各子数据集中的百分比
        for path in ["train/blacklist", "train/whitelist", "test/blacklist", "test/whitelist"]:
            files = get_list_of_files_new(path)
            files = [file[6:] if file.startswith('label_') or file.startswith('image_') else file for file in files]
            percentage = count_and_percentage_new(files, class_name) # 获取百分比
            distributions.append(percentage)
        class_distributions[class_name] = distributions

    # Check if the class distributions are imbalanced
    imbalance_report = check_imbalance(class_distributions, threshold=20) # 阈值可以根据需要调整
    for class_name, report in imbalance_report.items():
        print(f"Class: {class_name}, Imbalance Report: {report}")

def count_and_percentage_new(files, class_name):
    total_count = 0
    match_count = 0
    with open('./data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_count += 1
            file_name = os.path.basename(row['img_path'])
            if file_name in files and row[class_name] == '0':
                match_count += 1
    # 计算百分比
    if len(files) > 0:
        percentage = match_count / len(files) * 100
    else:
        percentage = 0
    # 返回计算的百分比
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
        if (abs(distributions[0] - distributions[1]) > threshold) and (abs(distributions[2] - distributions[3]) > threshold):
            imbalance_report[class_name] = {
                'is_imbalanced': True,
                'distribution': distributions,
                'train/blacklist': distributions[0],
                'train/whitelist': distributions[1],
                'test/blacklist': distributions[2],
                'test/whitelist': distributions[3],
            }
            break
        else: 
            imbalance_report[class_name] = {
                'is_imbalanced': False,
                'distribution': distributions,
                'train/blacklist': distributions[0],
                'train/whitelist': distributions[1],
                'test/blacklist': distributions[2],
                'test/whitelist': distributions[3],
            }

            



        # max_distribution = max(distributions)
        # min_distribution = min(distributions)
        # # 如果最大和最小占比之差超过阈值，认为该类分布可能不均匀
        # if max_distribution - min_distribution > threshold:
        #     imbalance_report[class_name] = {
        #         'is_imbalanced': True,
        #         'max_distribution': max_distribution,
        #         'min_distribution': min_distribution
        #     }
        # else:
        #     # imbalance_report[class_name] = {
        #     #     'is_imbalanced': False,
        #     #     'max_distribution': max_distribution,
        #     #     'min_distribution': min_distribution
        #     # }
        #     continue
    
    return imbalance_report

        
if __name__ == '__main__':
    stastics_each_class_adjust()



        

    

    


    
