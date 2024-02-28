# Resize Image

import cv2


def calculate_size(scale_percentage, width, height):
  new_width = int(width * scale_percentage / 100)
  new_height = int(height * scale_percentage / 100)
  print("New Dim:", new_width, new_height)
  return (new_width, new_height)


def resize(image_path, scale_percentage, resized_path):
  image = cv2.imread(image_path)
  new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
  resized_image = cv2.resize(image, new_dim)
  cv2.imwrite(resized_path, resized_image)

resize('galaxy.jpeg', 10, 'resized-galaxy.jpeg')




# This code is a Python script that utilizes the OpenCV library (cv2) to resize an image by a certain scale percentage. 
# Let me explain each part of the code:

# import cv2: This line imports the OpenCV library, which is a popular library for computer vision tasks in Python.

# calculate_size(scale_percentage, width, height): This function calculates the new dimensions (width and height) of the image after 
# resizing by a certain scale percentage.

# scale_percentage: The percentage by which the image will be resized.
# width: The original width of the image.
# height: The original height of the image.
# new_width: The new width calculated after resizing.
# new_height: The new height calculated after resizing.
# This function returns a tuple (new_width, new_height).
# resize(image_path, scale_percentage, resized_path): This function performs the actual resizing of the image.

# image_path: The path to the original image file.
# scale_percentage: The percentage by which the image will be resized.
# resized_path: The path where the resized image will be saved.
# image = cv2.imread(image_path): This line reads the image from the specified path using OpenCV.
# new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0]): This line calculates the new dimensions using the calculate_size function.
# resized_image = cv2.resize(image, new_dim): This line resizes the image using the calculated new dimensions.
# cv2.imwrite(resized_path, resized_image): This line writes the resized image to the specified path.
# resize('galaxy.jpeg', 10, 'resized-galaxy.jpeg'): This line calls the resize function with the parameters: original image path ('galaxy.jpeg'), 
# scale percentage (10%), and the path where the resized image will be saved ('resized-galaxy.jpeg').

# So, the script reads an image file named 'galaxy.jpeg', resizes it by 10% of its original size, and saves the resized image as 'resized-galaxy.jpeg'.