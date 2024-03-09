# Overfitting Analysis 

## 1. Distribution for each class

Class: Pupil, Imbalance Report: {'is_imbalanced': False, 'distribution': [0.625, 0.0, 0.0, 0.0]}
**Class: Surgical Tape, Imbalance Report: {'is_imbalanced': False, 'distribution': [26.25, 0.0, 15.0, 0.0]}**
Class: Hand, Imbalance Report: {'is_imbalanced': False, 'distribution': [86.875, 83.75, 87.5, 72.5]}
**Class: Eye Retractors, Imbalance Report: {'is_imbalanced': True, 'distribution': [67.5, 11.875, 77.5, 7.5]}**
Class: Iris, Imbalance Report: {'is_imbalanced': False, 'distribution': [0.0, 0.0, 0.0, 0.0]}
Class: Skin, Imbalance Report: {'is_imbalanced': False, 'distribution': [0.0, 0.0, 0.0, 0.0]}
Class: Cornea, Imbalance Report: {'is_imbalanced': False, 'distribution': [0.0, 0.0, 0.0, 0.0]}
Class: Hydrodissection Cannula, Imbalance Report: {'is_imbalanced': False, 'distribution': [92.5, 93.125, 95.0, 90.0]}
Class: Viscoelastic Cannula, Imbalance Report: {'is_imbalanced': False, 'distribution': [94.375, 94.375, 100.0, 95.0]}
Class: Capsulorhexis Cystotome, Imbalance Report: {'is_imbalanced': False, 'distribution': [94.375, 89.375, 87.5, 95.0]}
Class: Rycroft Cannula, Imbalance Report: {'is_imbalanced': False, 'distribution': [85.625, 89.375, 92.5, 92.5]}
Class: Bonn Forceps, Imbalance Report: {'is_imbalanced': False, 'distribution': [99.375, 79.375, 97.5, 75.0]}
Class: Primary Knife, Imbalance Report: {'is_imbalanced': False, 'distribution': [96.875, 91.875, 95.0, 90.0]}
Class: Phacoemulsifier Handpiece, Imbalance Report: {'is_imbalanced': False, 'distribution': [83.125, 90.625, 72.5, 87.5]}
Class: Lens Injector, Imbalance Report: {'is_imbalanced': False, 'distribution': [91.25, 93.125, 100.0, 97.5]}
Class: I/A Handpiece, Imbalance Report: {'is_imbalanced': False, 'distribution': [66.25, 84.375, 60.0, 90.0]}
Class: Secondary Knife, Imbalance Report: {'is_imbalanced': False, 'distribution': [100.0, 95.625, 100.0, 90.0]}
Class: Micromanipulator, Imbalance Report: {'is_imbalanced': False, 'distribution': [66.25, 86.875, 67.5, 87.5]}
Class: I/A Handpiece Handle, Imbalance Report: {'is_imbalanced': False, 'distribution': [96.25, 97.5, 92.5, 100.0]}
Class: Capsulorhexis Forceps, Imbalance Report: {'is_imbalanced': False, 'distribution': [96.875, 92.5, 97.5, 95.0]}
Class: Rycroft Cannula Handle, Imbalance Report: {'is_imbalanced': False, 'distribution': [97.5, 100.0, 97.5, 100.0]}
Class: Phacoemulsifier Handpiece Handle, Imbalance Report: {'is_imbalanced': False, 'distribution': [96.875, 100.0, 100.0, 100.0]}
Class: Capsulorhexis Cystotome Handle, Imbalance Report: {'is_imbalanced': False, 'distribution': [99.375, 96.25, 95.0, 97.5]}
Class: Secondary Knife Handle, Imbalance Report: {'is_imbalanced': False, 'distribution': [100.0, 96.875, 100.0, 97.5]}
Class: Lens Injector Handle, Imbalance Report: {'is_imbalanced': False, 'distribution': [100.0, 98.125, 100.0, 97.5]}
Class: Suture Needle, Imbalance Report: {'is_imbalanced': False, 'distribution': [99.375, 96.25, 100.0, 97.5]}
Class: Needle Holder, Imbalance Report: {'is_imbalanced': False, 'distribution': [100.0, 100.0, 100.0, 100.0]}
Class: Charleux Cannula, Imbalance Report: {'is_imbalanced': False, 'distribution': [100.0, 100.0, 100.0, 100.0]}
Class: Primary Knife Handle, Imbalance Report: {'is_imbalanced': False, 'distribution': [100.0, 99.375, 100.0, 97.5]}
Class: Vitrectomy Handpiece, Imbalance Report: {'is_imbalanced': False, 'distribution': [100.0, 100.0, 100.0, 100.0]}
Class: Mendez Ring, Imbalance Report: {'is_imbalanced': False, 'distribution': [100.0, 100.0, 100.0, 100.0]}
Class: Marker, Imbalance Report: {'is_imbalanced': False, 'distribution': [89.375, 100.0, 72.5, 100.0]}
Class: Hydrodissection Cannula Handle, Imbalance Report: {'is_imbalanced': False, 'distribution': [100.0, 100.0, 100.0, 100.0]}
Class: Troutman Forceps, Imbalance Report: {'is_imbalanced': False, 'distribution': [99.375, 94.375, 100.0, 92.5]}
Class: Cotton, Imbalance Report: {'is_imbalanced': False, 'distribution': [100.0, 100.0, 100.0, 100.0]}
Class: Iris Hooks, Imbalance Report: {'is_imbalanced': False, 'distribution': [93.125, 100.0, 97.5, 100.0]}



Conclusion:

Only two class I found quite interesting and should be make sure that all of these is well distributed:

​        \# ["train/blacklist", "train/whitelist", "test/blacklist", "test/whitelist"]

**Class: Surgical Tape, Imbalance Report: {'is_imbalanced': False, 'distribution': [26.25, 0.0, 15.0, 0.0]}**

surgical tape do not have anything in the whitelist

**Class: Eye Retractors, Imbalance Report: {'is_imbalanced': True, 'distribution': [67.5, 11.875, 77.5, 7.5]}**

Eye Retractors has more blacklist than whitelist



extract more  Eye Retractors  and surgical tape from the whitelist.



Overfitting（过拟合):

ref: https://aws.amazon.com/cn/what-is/overfitting/

https://www.zhihu.com/question/420045883









