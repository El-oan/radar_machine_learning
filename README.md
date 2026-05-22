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
| Tweaked PointNet | PointNet improved with attention over the time dimension. |
| SK-DGCNN | Skeleton-aware Dynamic Graph CNN used on radar point clouds, especially for skeleton regression/classification experiments. |


### RadHAR

RadHAR, also called MMActivity, comes from the 2019 RadHAR paper. It contains five classes: walking, jumping, jumping jacks, squats, and boxing. The original dataset contains 93 minutes of recording and eight raw features: `x`, `y`, `z`, `range`, `velocity`, `doppler_bin`, `bearing`, and `intensity`. The radar used is a TI IWR1443 mmWave radar. There is a time dimension in the recordings. In this repository, the local RadHAR folder is 882 MB and contains 200 files with 167,632 radar frames: 142 train files with 128,947 frames and 58 test files with 38,685 frames. The current RadHAR PointNetV2 notebook starts from the eight raw features, then updates the model input to four features: `x`, `y`, `z`, and `velocity`.

### ModelNet40

ModelNet40 is used by the original 2017 PointNet paper. It contains 40 classes, such as airplane, bathtub, bed, and chair. The dataset only has three features: `x`, `y`, and `z`. It is not a radar dataset, but it is useful to validate PointNet on a standard point-cloud benchmark. In this repository, the local ModelNet40 folder is 9.1 GB and contains 12,311 mesh samples: 9,843 train samples and 2,468 test samples. Each mesh is treated as one frame/sample.

### RaDataTouille

RaDataTouille is the dataset we recorded ourselves using our radar. It uses six features: `x`, `y`, `z`, `snr`, `velocity`, and `noise`. The available labels are `sit` and `stand_up`. In this repository, the local RaDataTouille folder is 31 MB and contains 19 records with 27,411 recorded frames: 13 train records with 20,031 frames and 6 test records with 7,380 frames. The recorder configuration is for a TI xWR68xx AOP platform at 60 GHz.

### DGUHA

DGUHA is the Dongguk University Human Activity dataset. It contains both radar points and recordings from Kinect, used to draw the user skeleton. It has seven classes: running, jumping, sitting down and standing up, both upper limb extension, falling forward, right limb extension, and left limb extension.

The radar points used in this repository have three features: `x`, `y`, and `z`. The radar used in the original dataset is a TI IWR1443BOOST mmWave radar, with a Microsoft Kinect v4 sensor for skeleton data. The local active files use the AHC-augmented point clouds, with shape `(samples, 3, 400, 25, 2)` before the notebook transposes them to `(samples, 400, 25, 3)`. Each clip has 400 frames and 25 points per frame. In this repository, the local DGUHA folder is 1.4 GB and contains 768 clips with 307,200 frames total: 607 train clips with 242,800 frames and 161 test clips with 64,400 frames.

The dataset is available to download at: <https://drive.google.com/file/d/1wBEGb_rIJLsroDIDYG0_OJ_cb8f_MR3Q/view?usp=sharing>

### MARS

MARS stands for mmWave-based Assistive Rehabilitation System for Smart Healthcare. It contains radar data and Kinect skeleton data for rehabilitation movements. The radar files are MATLAB files with `radar_data_cropped` arrays of shape `(8, total_points)`. Row 0 is the frame id, rows 2 to 6 are the model input features, and row 7 is timestamp-like metadata.

The model input features used here are `x`, `y`, `z`, Doppler `velocity`, and `intensity`. The dataset has ten movement classes: left upper limb extension, right upper limb extension, both upper limb extension, left front lunge, right front lunge, squad, left side lunge, right side lunge, left limb extension, and right limb extension. In this repository, the local MARS folder is 1.2 GB and contains 39 recordings with 40,022 radar frames: 29 train recordings with 28,221 frames and 10 test recordings with 11,801 frames. The original MARS description uses 5 radar features: `x`, `y`, `z`, Doppler velocity, and intensity, and Kinect labels with 19 joints, each represented by `x`, `y`, and `z`.
