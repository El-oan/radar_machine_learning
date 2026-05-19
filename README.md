this is the repo containing the code and data for our comparative study.


the repos is organized as such:

src/ -> contains the code of the models: the architecture, the data preparation and the training pipeline
the code test the pointnet architecture (V1: original pointnet, V2: attention added) on mutiple datasets

data/ -> contains the radar datasets. there is the dataset radHAR (also called MMActivity) used by the 2019 radHAR paper. the ModelNET40 dataset, used by the original 2017 pointnet paper, and RaDAtaTouille, the dataset we recorders ourselves using our radar.

radHAR: 5 classes (walking, jumping, jumping jacks, squats, and boxing),  93 minutes of recording (features: x,y,z, range, velocity, Doppler bin, bearing, and intensity)
ModelNET40: 40 classes (40 items, such as plane, bathtub etc)
RaDAtaTouille: 2 classes (sat and standing up), (features: x,y,z, velocity, noise, snr)

results/ -> contains the graphs and plots obtained form all the trials of the different architecture, loss and gradient plots, and F1/accuracy plots.

papers/ -> contains the papers we read and used

checkpoints/ -> contains the model weights checkpoints of some models, to save results and do quick inference to measure the scores

