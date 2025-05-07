
import os
from PIL import Image

# Increase the maximum image pixels limit
Image.MAX_IMAGE_PIXELS = None

# # Define the input and output directories
# input_dir = 'train_folder/dummy_class'
# output_dir = 'train_patches/dummy_class'

# input_dir = 'test_folder/dummy_class'
# output_dir = 'test_patches/dummy_class'

input_dir = 'anomaly_folder/dummy_class'
output_dir = 'anomaly_patches/dummy_class'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define the patch size
patch_width = 1024
patch_height = 1024

# Function to split an image into patches and save them
def split_image_into_patches(image_path, output_dir, patch_width, patch_height):
    # Open the image
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Calculate the number of patches in each dimension
    num_patches_x = img_width // patch_width
    num_patches_y = img_height // patch_height

    # Get the base name of the image file (without extension)
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    # Initialize patch number
    patch_number = 1

    # Iterate over each patch position
    for i in range(num_patches_x):
        for j in range(num_patches_y):
            # Calculate the coordinates of the current patch
            left = i * patch_width
            upper = j * patch_height
            right = left + patch_width
            lower = upper + patch_height

            # Crop the patch from the image
            patch = img.crop((left, upper, right, lower))

            # Save the patch as a new image file
            patch_filename = f"{base_name}_{patch_number}.jpg"
            patch.save(os.path.join(output_dir, patch_filename))

            # Increment the patch number
            patch_number += 1

# Iterate over all .jpg files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg'):
        image_path = os.path.join(input_dir, filename)
        split_image_into_patches(image_path, output_dir, patch_width, patch_height)

print("Image splitting and saving completed.")
