This repo aims at ilmplementing 3 different deep learning alogrithm (PointNet, a twekaed pointet, and SK-DGCNN network) to classify human activity (running, standing etc) from radar points clouds. 
this repository is organized as such:

src/ -> contains all the code of the models: the architecture, the data preparation and the training pipelines. each notebook contains a model applied a specifid dataset.

datasets/ -> contains all the radar datasets. teh dataset we used are those ones:
radHAR (also called MMActivity): from the 2019 radHAR paper. contains 5 classes (walking, jumping, jumping jacks, squats, and boxing),  93 minutes of recording, and 8 features: x,y,z, range, velocity, Doppler bin, bearing, and intensity. the radar used is a TI IWR1443 mmWave radar. There is a time dimension for the recordings

ModelNET40: used by the original 2017 pointnet paper, contains 40 classes (40 items, such as plane, bathtub etc). The datseat only has 3 features (x, y and z)

RaDAtaTouille: the dataset we recordered ourselves using our radar. It uses 6 features: x,y, z, snr, velocity and noise.

DGUHA: this dataset contains both radar points and recoding from kinect (used to draw the suer skeleton). It has 7 classes which are . The radar points only have three features: x, y and z. It is availble to downaload at https://drive.google.com/file/d/1wBEGb_rIJLsroDIDYG0_OJ_cb8f_MR3Q/view?usp=sharing

results/ -> contains the graphs and plots obtained form all the trials of the different architecture. It contains training and validation losses and gradient, and F1/accuracy plots for multiple checkpiints across epochs.

papers/ -> contains the papers I read and used.

checkpoints/ -> contains the model weights checkpoints of every models for every dataset, to save results and inference to measure the scores.

