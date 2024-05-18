# Image Extraction

## Install Requirements
```
pip install -r requirements.txt
```

## Run Code
To run the code do the following:

```
python3 image_extractor.py sample_image.jpg ../new_file.jpg 1000 780
```

The pattern is the following:

``'<file> -image_path -ouput_path -width -height\n'``

### Input Parameters
- image_path: the path from your current dir to the image you want to warp. For example **sample_image.jpg**.
- ouput_path: the path + the name + the file type to the photo you want to save (which is edited in perspective). For example **./edited_file.jpg**.
- width: the final width in pixels that your saved and edited photo will have. For example **1000**.
- height: the final height in pixels that your saved and edited photo will have. For example **780**.


Notice: The file type should be jpg or png.