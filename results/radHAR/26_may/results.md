
With LR along x axis reset and jitter augmenatation:
Final model: model.pt
Test MAE: 5.0201 cm 
Test MAE per joint (cm):
SpineBase: 2.2810
SpineMid: 0.9884
Neck: 0.4983
Head: 1.9048
ShoulderLeft: 2.6595
ElbowLeft: 6.7679
WristLeft: 9.8149
ShoulderRight: 2.9416
ElbowRight: 6.6566
WristRight: 9.5108
HipLeft: 3.0174
KneeLeft: 5.5318
AnkleLeft: 7.9842
FootLeft: 8.9386
HipRight: 3.0021
KneeRight: 5.3515
AnkleRight: 8.2126
FootRight: 9.1199
SpineShoulder: 0.1994


stgcn++ socres with x axis reset and jitter augmenatation and 100 epochs:
Best validation checkpoint: checkpoint_87.pt
Validation accuracy: 0.9246
Test macro F1: 0.8805
Test accuracy: 0.8780
{'boxing': 0.8569434881210327, 'jack': 0.9241774082183838, 'jump': 0.8317241668701172, 'squats': 0.9461593627929688, 'walk': 0.8436806797981262}

stgcn++ socres with 200 epochs
Best validation checkpoint: checkpoint_142.pt
Validation accuracy: 0.9419
Test macro F1: 0.8724
Test accuracy: 0.8706
{'boxing': 0.8640569448471069, 'jack': 0.9213793277740479, 'jump': 0.7986440658569336, 'squats': 0.9483240246772766, 'walk': 0.8298368453979492}