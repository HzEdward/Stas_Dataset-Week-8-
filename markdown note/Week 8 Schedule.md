---

## Stage 1: Assessing Model Overfitting 

### 1. Validate Segmentation Class Distribution 

Ensure all segmented classes, especially rare classes, are presented in both the training and testing datasets with a considerable percentage. This includes analysing source errors such as mismatched frames and the scarcity of rare classes. 

The distribution of all error source of mislabelled frames **should be kept roughtly the same** to prevent undersampling.

mislabelled 原因：oversampling

Rare_class missing

帧数缺少

### 2. Dataset Expansion 
I suppose to double both the training and testing dataset. I would expand the dataset to enhance model robustness through: 

原来：200个黑名单数据

trainning dataset:  320  (160个黑名单数据，160个白名单数据)

validation dataset: 80（40个黑名单数据，40个白名单数据）

Step 1: 加入100个白名单数据，50个是Surgical Tape, 50个是是eye_retractors

Training Dataset: + 总共80个（40个Surgical Tape，40个eye_retractors）

Validation Dataset: +总共20个（10个Surgical Tape，10个eye_retractors）

所以目前：

trainning dataset:  400  (160个黑名单数据，240个白名单数据)

validation dataset: 100（40个黑名单数据，60个白名单数据）





Step 2: Data Argumentation



#### 2.1. **Data Augmentation**   

Implement real-world scenario limitations, including simultaneous image and mask flipping, slight rotations, etc., to prevent unrealistic training scenarios. 

在医学图像处理中，确实需要谨慎选择数据增强方法，以确保它们符合实际情况并不会引入不合理的变化。以下是一些可能不合适的数据增强方法：

1. **随机颜色变换**：对医学图像进行随机的颜色变换可能会导致图像失真，使得图像不再反映真实的生理或解剖特征。
  
2. **几何扭曲**：对于医学图像而言，随机的几何扭曲可能导致图像的形态不再符合真实情况，从而影响后续的分析和诊断。

3. **变形过度**：过度的变形可能会使图像失真，从而无法准确地反映患者的生理结构或病变情况。

4. **异常噪声添加**：添加过多或不合理的噪声可能会模糊图像，使得其中的细节无法被正确识别或分析。

5. **过度模糊**：过度模糊可能会导致图像失真，丢失重要的细节信息，从而影响后续的分析和诊断。

6. **不自然的光照变化**：如果模拟的光照变化不符合医学图像的实际情况，可能会导致图像中的结构变得不清晰或不可辨认。

7. **不合理的裁剪和缩放**：不合理的裁剪和缩放可能会丢失图像中重要的信息或导致图像失真，从而影响后续的分析和诊断。

在医学图像处理中，最好选择那些能够保留图像中重要信息并与实际情况相符的数据增强方法。最好与医学领域的专业人士一起合作，以确保所选择的方法符合医学实践的要求。

现实的数据增强方式有：

1. **强度调整**：调整图像的亮度和对比度，以模拟不同的光照条件。

2. **噪声添加**：向图像添加噪声，如高斯噪声或椒盐噪声，以模拟真实世界中的图像噪声。

3. **模糊**：应用不同程度的模糊，模拟图像在不同条件下的清晰度变化，例如运动模糊或高斯模糊。

4. **变形**：对图像进行变形或扭曲，以模拟不同姿势或视角下的图像变化。

5. **裁剪和缩放**：对图像进行裁剪和缩放，以模拟不同尺寸和分辨率的图像。

6. **增强对比度**：增强图像的对比度，以突出图像中的细节。

7. **色彩变换**：改变图像的色彩空间或色彩分布，以模拟不同的成像设备或光源条件。

   

#### **2.2. Incorporate More Whitelist Variants**  （不考虑）

Select additional whitelist data variants with higher miou scores (>50%) from the entire dataset. （周二周三）

​     After testing on the expansion dataset, if validation results remain **significantly high (above 0.85)**, it suggests the model may not be overfitting. if it is not over-fitting, directly go for the comparative analysis and consider the model's potential **generalizability** to other image segmentation datasets, especially those with mislabeled data.

​        

## Stage 2: Addressing Overfitting 

If overfitting is confirmed, then try:
1. **Simplify the Model:** Experiment with a shallower architecture, such as ResNet 18, to reduce complexity.

2. **Implement Dropout:** Introduce dropout during training to randomly deactivate a fraction of neurons, reducing over-reliance on specific features (Reference: [Neural Network Dropout](https://baotramduong.medium.com/neural-network-dropout-57b501bbb578)).

3. **Cross-validation:** Employ cross-validation to ensure the model's performance is consistent across different subsets of the dataset.

4. **Early Stopping:** Terminate training when validation performance ceases to improve, preventing overfitting.

   

## Comparative Analysis

**思考方向：**

1. 方法是新的，结果是好的。

2. 总结出一般规律 （理论化）。解释并且有一般规律。

3. 具有很大的应用范围

   

1. **Blacklist Evaluation on Cataract Dataset:**

   - Apply the blacklist model to the entire Cataract dataset. Ensure the model identifies all blacklisted images annotated by the author and manually verify any new mislabeled images detected.

   - Compare the performance improvements:

     - My blacklist Vs. unfiltered dataset 
     - Author blacklist Vs. My blacklist
     
     **Note: author's model was trained on the full dataset without blacklist filtering so improvement is very likely to have**
     
     

2. **Model Generalizability:**

   - Test the model's generalizability on other datasets with mislabeled data.
   - Compare its performance to that on other mislabeled datasets to identify areas for further improvement, such as incorporating **training dynamics** to better identify mislabeled frames during training.



原来数据集：

训练集



长期需要培养的习惯：

1. Kaggle 
2. 新的论文
3. 概率数理统计+算法+新的论文（CCF A 一区）
4. 与深度学习、数学专业人交流



周日计划：

下午

1. 完成overfitting的判断，构建数据集+跑代码

晚上：

1. 思考Future direction
2. 完成Ring的练习



日程：

3:00 - 4:30 

5:00 - 6:30 

7:30- 9:00 

9:30- 11:00

1点前睡觉😴



