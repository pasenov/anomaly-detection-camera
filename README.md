# Camera Anomaly Detection

This project provides a workflow and tools for anomaly detection in camera images using deep learning. It includes scripts for patch extraction, noise introduction, data augmentation, and a Jupyter notebook for training and evaluating an autoencoder-based anomaly detector.

---

## Contents

- `Anomaly_Detection_Camera.ipynb`: Main Jupyter notebook for loading data, training an autoencoder, and visualizing anomaly detection results.
- `patch.py`: Script to extract patches from large images and save them for training/testing.
- `introduce_noise.py`: Script to add synthetic noise to images for data augmentation or anomaly simulation.
- `create_more_images_rotation.py`: Script to augment your dataset by generating rotated versions of images.

---

## Scripts Overview

### 1. `patch.py`
Extracts smaller patches from large images, which are then used for model training and testing.


### 2. `introduce_noise.py`
Adds synthetic noise (e.g., Gaussian, salt-and-pepper) to images or patches, simulating anomalies for robust model training.


### 3. `create_more_images_rotation.py`
Performs data augmentation by rotating images at various angles (e.g., 90°, 180°, 270°) and saving the results. This increases dataset diversity and helps prevent overfitting.

---

## Main Notebook: `Anomaly_Detection_Camera.ipynb`

This notebook is the core of the workflow. It covers:

- **Data Loading:** Loads image patches for training, testing, and anomaly evaluation using Keras `ImageDataGenerator`.
- **Visualization:** Displays random samples from the training and anomaly datasets.
- **Model Definition:** Builds a convolutional autoencoder using Keras for unsupervised anomaly detection.
- **Training:** Trains the autoencoder on normal image patches.
- **Evaluation:** Computes reconstruction loss on normal and anomalous data, visualizes original vs. reconstructed images, and generates anomaly maps.
- **Visualization:** Plots training/validation loss curves and visualizes anomaly detection results.

---

## Directory Structure

- `train_patches_small/` — Training image patches (normal)
- `test_patches_small/` — Testing image patches (normal)
- `anomaly_patches_small/` — Anomalous image patches

---

## Requirements

- Python 3.7+
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib
- PIL
- Dask (for parallel image loading)
- h5py

Install dependencies with:
```sh
pip install -r requirements.txt
```

---

## Example Results

The notebook visualizes original, reconstructed, and anomaly map images for both normal and anomalous samples, helping you assess model performance.

---

## Authors

- Patrick Asenov & the CMS Pisa Anomaly Detection Team
