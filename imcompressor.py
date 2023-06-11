from PIL import Image
import os

# Set directory containing images to compress
directory = './images/'

# Set maximum dimension for compressed images
max_dim = 1024

# Loop through each file in directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Open image file
        with Image.open(directory + filename) as img:
            # Get original dimensions
            width, height = img.size
            
            # Calculate new dimensions
            if width > height:
                new_width = max_dim
                new_height = int(height * (max_dim / width))
            else:
                new_height = max_dim
                new_width = int(width * (max_dim / height))
            
            # Resize image
            img = img.resize((new_width, new_height))
            
            # Set compression level (0-100)
            img.save(directory + 'compressed_' + filename, optimize=True, quality=85)
