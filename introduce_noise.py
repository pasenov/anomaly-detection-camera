# import os
# import cv2
# import numpy as np

# # Define paths
# input_folder = "anomaly_patches_small_original/dummy_class"
# output_folder = "anomaly_patches_small/dummy_class"

# # Create output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# def add_blurred_color_spots(image):
#     """Adds blurred multi-color spots to an image."""
#     modified_image = image.copy()

#     # Define number of spots
#     num_spots = np.random.randint(8, 20)  # Increased number of spots
    
#     for _ in range(num_spots):
#         x, y = np.random.randint(0, modified_image.shape[1]), np.random.randint(0, modified_image.shape[0])
#         radius = np.random.randint(200, 800)  # Large radius for visibility

#         # Sample a random color from the image near the spot location
#         sample_x, sample_y = np.clip([x + np.random.randint(-50, 50), y + np.random.randint(-50, 50)], 0, min(modified_image.shape[:2]) - 1)
#         sampled_color = modified_image[sample_y, sample_x].tolist()

#         # Create a blurred colored spot
#         overlay = modified_image.copy()
#         cv2.circle(overlay, (x, y), radius, sampled_color, -1)
#         modified_image = cv2.addWeighted(modified_image, 0.7, overlay, 0.3, 0)

#     return modified_image

# # Process only the first 1200 images
# image_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg")][:1200]

# for filename in image_files:
#     img_path = os.path.join(input_folder, filename)
#     image = cv2.imread(img_path)

#     if image is not None:
#         modified_image = add_blurred_color_spots(image)

#         # Save with new filename
#         new_filename = filename.replace(".jpg", "_spots.jpg")
#         output_path = os.path.join(output_folder, new_filename)
#         cv2.imwrite(output_path, modified_image)

# print("Processing complete! Images with multi-color spots saved in anomaly_patches_small/dummy_class.")


import os
import cv2
import numpy as np

# Define paths
input_folder = "anomaly_patches_small_original/dummy_class"
output_folder = "anomaly_patches_small/dummy_class"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def modify_color_spots(image):
    """Randomly changes the colors of adjacent pixels to create visible spots."""
    modified_image = image.copy()

    # Define number of spots
    num_spots = np.random.randint(8, 20)  # Number of clusters
    
    for _ in range(num_spots):
        # Randomly select a spot location
        x, y = np.random.randint(0, modified_image.shape[1]), np.random.randint(0, modified_image.shape[0])
        radius = np.random.randint(10, 20)  # Size of modification spots
        
        # Generate random color modification
        random_color = np.random.randint(0, 256, size=(3,), dtype=np.uint8)

        # Modify colors within the selected radius
        for dx in range(-radius, radius):
            for dy in range(-radius, radius):
                nx, ny = x + dx, y + dy
                if 0 <= nx < modified_image.shape[1] and 0 <= ny < modified_image.shape[0]:
                    modified_image[ny, nx] = random_color

    return modified_image

# Process only the first 1200 images
image_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg")][:1200]

for filename in image_files:
    img_path = os.path.join(input_folder, filename)
    image = cv2.imread(img_path)

    if image is not None:
        modified_image = modify_color_spots(image)

        # Save with new filename
        new_filename = filename.replace(".jpg", "_color_spots.jpg")
        output_path = os.path.join(output_folder, new_filename)
        cv2.imwrite(output_path, modified_image)

print("Processing complete! Images with modified color spots saved in anomaly_patches_small/dummy_class.")
