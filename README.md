# Camera Anomaly Detection Pipeline

This repository contains a pipeline for generating and processing image data to train an autoencoder for anomaly detection. The pipeline consists of four main steps: data augmentation, noise introduction, patching, and training.

## Files and Their Purpose

### 1. `create_more_images_rotation.py`
This script generates additional rotated versions of an initial image to augment the dataset.

- **Input**: A single image file (`PS2605iba00004.jpg`).
- **Output**: 
  - 180 rotated images saved in the `training_dataset` folder.
  - 120 rotated images saved in the `testing_dataset` folder.
- **Rotation Details**:
  - Small random angles (±1.5°) for most images.
  - Large random angles (±90°) for a smaller subset.

### 2. `introduce_noise.py`
This script introduces random noise and large black spots to the rotated images to simulate anomalies.

- **Input**: Images from the `test_folder/dummy_class` directory.
- **Output**: Noisy images with black spots saved in the `anomaly_folder/dummy_class` directory.
- **Noise Details**:
  - Random pixel noise.
  - Large black spots with radii between 200 and 800 pixels.
- **Processing Limit**: Only the first 12 images are processed.

### 3. `patch.py`
This script splits the noisy images into smaller patches of size 1024x1024 pixels.

- **Input**: Images from the `anomaly_folder/dummy_class` directory.
- **Output**: Patches saved in the `anomaly_patches/dummy_class` directory.
- **Patch Details**:
  - Each image is divided into non-overlapping patches of size 1024x1024 pixels.

### 4. `Anomaly_Detection_Camera.ipynb`
This Jupyter Notebook trains an autoencoder on the patched images to detect anomalies.

- **Steps**:
  1. Load training and testing patches from the `train_patches` and `test_patches` directories.
  2. Load anomaly patches from the `anomaly_patches` directory.
  3. Train an autoencoder using the training patches.
  4. Evaluate the autoencoder on testing and anomaly patches.
  5. Visualize the reconstructed images and compare them with the original images.
- **Model Details**:
  - The autoencoder is built using Keras with convolutional and pooling layers.
  - The loss function is Mean Squared Error (MSE).

## Workflow

1. **Data Augmentation**:
   - Run `create_more_images_rotation.py` to generate rotated images.

2. **Noise Introduction**:
   - Run `introduce_noise.py` to add noise and black spots to the rotated images.

3. **Image Patching**:
   - Run `patch.py` to split the noisy images into 1024x1024 patches.

4. **Training**:
   - Open and execute `Anomaly_Detection_Camera.ipynb` to train the autoencoder and evaluate its performance.

## Requirements

- Python 3.x
- Required Libraries:
  - `Pillow`
  - `OpenCV`
  - `NumPy`
  - `Keras`
  - `TensorFlow`
  - `Matplotlib`
  - `Dask`
  - `h5py`
  - `glob`
