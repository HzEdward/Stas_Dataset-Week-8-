# Overfitting Analysis 

## 1.异常分布总结

Only two class I found quite interesting and should be make sure that all of these is well distributed:

**["train/blacklist", "train/whitelist", "test/blacklist", "test/whitelist"]**



**1. Class: Surgical Tape**

[26.25, 0.0, 15.0, 0.0]

Surgical tape do not have anything in the whitelist. so it's possible that surgical tape will be recognised as a blacklist straight away as soon as you see it

**2. Class: Eye Retractors**

[67.5, 11.875, 77.5, 7.5]

Eye Retractors has significantly more blacklist than whitelist



解决方法：

1. 提取更多的Surgical tape和eye retractors的白名单值
2. 进行数据增强



## 2. 过拟合可能性分析

### 2.1. 相关资料

ref: https://aws.amazon.com/cn/what-is/overfitting/

https://www.zhihu.com/question/420045883



### 2.2. 异常情况

模型训练效果特别好





