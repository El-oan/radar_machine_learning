# Radar ML

This repository aims at implementing three different deep learning algorithms, PointNet, a tweaked PointNet, and an SK-DGCNN network, to classify human activity from radar point clouds.

## Repository Structure

- **`src/`**: contains all the code for the models: the architecture, the data preparation, and the training pipelines. Each notebook contains a model applied to a specific dataset.
- **`datasets/`**: contains all the radar datasets used in this project.
- **`results/`**: contains the graphs and plots obtained from the trials of the different architectures. It contains training and validation losses, gradients, and F1/accuracy plots for multiple checkpoints across epochs.
- **`papers/`**: contains the papers I read and used.
- **`checkpoints/`**: contains the model-weight checkpoints for every model and every dataset, used to save results and run inference to measure scores.

## Models

The repository currently focuses on three point-cloud architectures:

| Model | Description |
| --- | --- |
| PointNet | Original PointNet classifier architecture. |
| Tweaked PointNet | PointNet improved with attention along the time dimension. |
| SK-DGCNN | Skeleton-aware Dynamic Graph CNN used on radar point clouds taht predicts a skeleton from the radar cloud, followed by a second netwrodk that predicts the activity class from the skeleton. |


### RadHAR

RadHAR, also called MMActivity, comes from the 2019 RadHAR paper. It contains five classes: walking, jumping, jumping jacks, squats, and boxing. The original dataset contains 93 minutes of recording and eight raw features: `x`, `y`, `z`, `range`, `velocity`, `doppler_bin`, `bearing`, and `intensity`. The radar used is a TI IWR1443 mmWave radar. There is a time dimension in the recordings.

| Split | Files | Frames |
| --- | ---: | ---: |
| Train | 142 | 128,947 |
| Test | 58 | 38,685 |
| Total | 200 | 167,632 |


### ModelNet40

ModelNet40 is used by the original 2017 PointNet paper. It contains 40 classes, such as airplane, bathtub, bed.. etc. The dataset only has three features: `x`, `y`, and `z`. It is not a radar dataset, but it is useful to validate PointNet on a standard point-coordinates dataset.

| Split | Samples |
| --- | ---: |
| Train | 9,843 |
| Test | 2,468 |
| Total | 12,311 |

### RaDataTouille

RaDataTouille is the dataset we recorded ourselves using our radar. It uses six features: `x`, `y`, `z`, `snr`, `velocity`, and `noise`. The available labels are `sit` and `stand up`. We used the radar TI xWR68xx AOP at 60 GHz.

| Split | Records | Frames |
| --- | ---: | ---: |
| Train | 13 | 20,031 |
| Test | 6 | 7,380 |
| Total | 19 | 27,411 |


### DGUHA

DGUHA is the Dongguk University Human Activity dataset. It contains both radar points and recordings from Kinect, used to draw the user skeleton. It has seven classes: running, jumping, sitting down and standing up, both upper limb extension, falling forward, right limb extension, and left limb extension. The radar points used in this repository have three features: `x`, `y`, and `z`. Each clip has 400 frames and 25 points per frame.

| Split | Clips | Frames |
| --- | ---: | ---: |
| Train | 607 | 242,800 |
| Test | 161 | 64,400 |
| Total | 768 | 307,200 |

The dataset is available to download at: <https://drive.google.com/file/d/1wBEGb_rIJLsroDIDYG0_OJ_cb8f_MR3Q/view?usp=sharing>

### MARS

MARS (mmWave-based Assistive Rehabilitation System for Smart Healthcare) contains radar data and Kinect skeleton data for rehabilitation movements. The features are `x`, `y`, `z`, `Doppler velocity`, and `intensity`. The dataset has ten movement classes: left upper limb extension, right upper limb extension, both upper limb extension, left front lunge, right front lunge, squad, left side lunge, right side lunge, left limb extension, and right limb extension.

| Split | Recordings | Frames |
| --- | ---: | ---: |
| Train | 29 | 28,221 |
| Test | 10 | 11,801 |
| Total | 39 | 40,022 |


