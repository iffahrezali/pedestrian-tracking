# Introduction to Computer Vision for Pedestrian Tracking
Apart from existing applications of computer vision including robotics, surveillance and automotive safety, pedestrian detection remains one of the major challenges in the field. It is formulated as the problem of automatically identifying and locating the pedestrians in images or videos. In the past, many techniques have been proposed to solve this problem accurately and efficiently. However, the variations in images such as body attire and pose, occlusion, different illumination parameters in different scenarios and clutter present in the background poses challenges in attaining high accuracy. An increasing number of challenging public datasets has driven much of the progress of pedestrian tracking few years back. To continue the rapid rate of innovation, this project aims to improve the overall performance of the existing methods by combining the Histogram of Oriented Gradients (HOG) and Haar-like features with particle filtering. 

# Disclaimer
This project is my Final Year Project (FYP) in fulfillment of Electrical and Electronics Engineering at Universti Malaysia Sarawak (UNIMAS). In this project, the particle filtering is omitted due to time and computational limitations.

# General Framework of Pedestrian Tracking
![Proposed Method Flowchart](https://user-images.githubusercontent.com/92578072/140056962-e73a1744-470e-4d8b-a0e4-1879cc4e7ff5.png)

# Results
The pedestrian tracking algorithm based on simulation and optimization by using Python programming language for design and implementation of the system is analyzed. The results obtained suggest that the performance of the proposed method is satisfactory for Advanced Driver-Assistance System (ADAS) implementation.

![00081](https://user-images.githubusercontent.com/92578072/140053031-8076216c-06aa-4d2c-bb79-ff1724505be7.jpg)
![00095](https://user-images.githubusercontent.com/92578072/140053037-2bc1ea6d-140d-4807-b682-8c7d08eebd20.jpg)

## Analysis of Results
To evaluate the pedestrian tracking results, numerical accuracy assessment is expected to be done by comparing the number of pedestrians identified manually and automatically by the proposed method. Confusion matrix is used to evaluate the performance of the methods in this project.

### Confusion Matrix of the Method
| Methods | Haar-like features | HOG | Combination of method |
| --------------|------------|-------------|---------|
| True positive (TP) | 26 | 22 | 120 |
| False positive (FP) | 73| 73 | 289 |
| False negative (FN)| 153 | 157| 59 |
| Total pedestrians | 179 | 179 | 179|

### Reliability
| Methods| Haar-like features | HOG | Combination of method |
| --------------|------------|-------------|---------|
| Precision (%) | 26.26 | 14.53 | 10.32 |
| Recall (%) | 23.16 | 12.29 | 8.73 |
| Quality (%)| 29.34 | 67.04 | 25.64 |

### F-1 Score
| Methods| Haar-like features | HOG | Combination of method |
| --------------|------------|-------------|---------|
| F-1 score (%) | 18.71 | 16.06 | 40.82 |

The results obtained indicate that when using a combination of Haar-like features and HOG method, the number of correct detections is increased. Although the proposed method has the most pedestrians correctly detected, the number of false positives or incorrect pedestrian detections is the highest, with a difference of 216. It suggests that the proposed approach detecting irrelevant items. In comparison to Haar-like features and HOG method, the proposed approach has the least number of 94 and 98 undetected pedestrians respectively, out of 179 total pedestrians in the video. Even under most favourable conditions, the proposed method is far from perfect. However, high false positive is not necessarily bad. Some extra false positives or false alarms are better than saving some false negative. In other words, for precaution measures, it is better to get non-pedestrians labelled as pedestrians over leaving pedestrians labelled as non-pedestrians.
