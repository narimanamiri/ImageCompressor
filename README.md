# ImageCompressor
this script compress images using python
this Python script compresses images using the `Pillow` library:

```python
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
```

Here's how the script works:

1. The script sets the directory containing the images to compress using the `directory` variable.
2. The script sets the maximum dimension for the compressed images using the `max_dim` variable.
3. The script loops through each file in the directory using the `os.listdir` function.
4. For each file that is a JPEG or PNG image, the script opens the image file using the `Image.open` function from the `Pillow` library.
5. The script gets the original dimensions of the image using the `size` attribute of the `Image` object.
6. The script calculates the new dimensions of the compressed image based on the maximum dimension and the aspect ratio of the original image.
7. The script resizes the image using the `resize` method of the `Image` object.
8. The script sets the compression level for the compressed image using the `quality` argument of the `save` method of the `Image` object. A higher quality value means less compression and a larger file size.
9. The script saves the compressed image to a new file with the prefix `compressed_` added to the original filename.

Note that this script assumes that you have installed the `Pillow` library, which can be installed using pip, the Python package installer. You can install `Pillow` by running `pip install Pillow` in your terminal or command prompt. Additionally, note that the script may not work correctly for all images, especially those with complex content or transparency. In those cases, you may need to adjust the compression level or use additional libraries or tools to optimize the image compression.
