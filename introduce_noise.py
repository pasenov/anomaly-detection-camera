import os
import cv2
import numpy as np

# Define paths
input_folder = "test_folder/dummy_class"
output_folder = "anomaly_folder/dummy_class"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def add_noise_and_large_spots(image):
    """Adds random noise and large black spots to an image."""
    noisy_image = image.copy()

    # Add random noise
    noise = np.random.randint(0, 50, noisy_image.shape, dtype='uint8')
    noisy_image = cv2.add(noisy_image, noise)

    # Add large black spots
    num_spots = np.random.randint(8, 20)  # Increased number of spots
    for _ in range(num_spots):
        x, y = np.random.randint(0, noisy_image.shape[1]), np.random.randint(0, noisy_image.shape[0])
        radius = np.random.randint(200, 800)  # Large radius for visibility
        cv2.circle(noisy_image, (x, y), radius, (0, 0, 0), -1)

    return noisy_image

# Process only the first 12 images
image_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg")][:12]

for filename in image_files:
    img_path = os.path.join(input_folder, filename)
    image = cv2.imread(img_path)

    if image is not None:
        modified_image = add_noise_and_large_spots(image)

        # Save with new filename
        new_filename = filename.replace(".jpg", "_noise.jpg")
        output_path = os.path.join(output_folder, new_filename)
        cv2.imwrite(output_path, modified_image)

print("Processing complete! Noisy images saved in anomaly_folder/dummy_class.")
