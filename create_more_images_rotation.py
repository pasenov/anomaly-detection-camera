
import os
import random
from PIL import Image

# Increase the limit for image size
Image.MAX_IMAGE_PIXELS = None

# Create directories for training, testing, and evaluation datasets
os.makedirs('training_dataset', exist_ok=True)
os.makedirs('testing_dataset', exist_ok=True)
os.makedirs('evaluation_dataset', exist_ok=True)

# Load the original image
original_image = Image.open('PS2605iba00004.jpg')

# Function to save rotated images
def save_rotated_images(image, folder, prefix, count, small_angle_ratio=0.9):
    for i in range(count):
        if i < count * small_angle_ratio:
            angle = random.uniform(-1.5, 1.5)  # Small random angles
            image_name = f"{prefix}_small_angle_{i+1}.jpg"
        else:
            angle = random.uniform(89.5, 90.5)  # Large random angles
            image_name = f"{prefix}_big_angle_{i+1}.jpg"

        rotated_image = image.rotate(angle)
        rotated_image.save(os.path.join(folder, image_name))

# Save 180 images in the training dataset folder
save_rotated_images(original_image, 'training_dataset', 'rotated_train', 180)

# Save 120 images in the testing dataset folder
save_rotated_images(original_image, 'testing_dataset', 'rotated_test', 120)

# # Save 120 images in the evaluation dataset folder
# save_rotated_images(original_image, 'evaluation_dataset', 'rotated_eval', 120)

print("Rotated images have been successfully saved in training, testing, and evaluation dataset folders.")
