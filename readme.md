# Install Requirements
```
pip install -r requirements.txt
```

# Image Extraction

## Run Code
To run the code do the following:

```
python3 image_extractor.py sample_image.jpg ../new_file.jpg 1000 780
```

The pattern is the following:

``'<file> -image_path -ouput_path -width -height\n'``


## Shortcuts

- press ESC to restart setting points. **This can only be done if 4 points are already set.**
- press S to save the warped image at the specified ouput_path with the correspoding width and height



### Input Parameters
- image_path: the path from your current dir to the image you want to warp. For example **sample_image.jpg**.
- ouput_path: the path + the name + the file type to the photo you want to save (which is edited in perspective). For example **./edited_file.jpg**.
- width: the final width in pixels that your saved and edited photo will have. For example **1000**.
- height: the final height in pixels that your saved and edited photo will have. For example **780**.


Notice: The file type should be jpg or png.


# AR-Game
The distance from the camera to the paper should not be too far, so the marker can be tracked reliable.
Be aware that the distance to the markers does matter. If it is flickering try to get the camera closer to the markers.


## Game
- destroy all bugs (brown/green bugs and flys) but do not destroy any kind of bee
- small bees give less minus points than big bees
- You have 60 seconds to smash as many bugs as possible


## Start The Gamae
Set up a camera that sees all 4 aruco markers of your paper. **Your markers have to have the id 0, 1, 2 and 3. Anything else than these ids will be ignored**. This is due to some random marker detection in your environment. For example id 130 and 127 were randomly detected in my environment.

```
python3 AR_game.py 0 True
```

- press SPACE to start the game
- press Q to quit the game
- press R to restart the game

### Input Parameters

python3 AR_game.py 

- your camera id (in most cases it is 0)
- choose your resolution! If you enter **True** the resolution of your game window will be the same as from your camera. If you enter **False** the window size is fixed (see ./ar_game/config.py).
    - be aware that if your camera resolution is very high, the window size might be bigger than your screen.

The pattern is the following:

``'<file> -camera_id (as int) -resolution (as boolean)``

## Controller

Your controller is your hand! You can use your finger or your whole hand but be careful to not smash any bees.


## Image Sources

| Image name | Source |
|------------|--------|
|Fly | https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6fKcUp7IBg75UpxBggB9ruY_sVUIAKMhbMUgFQ0XjGsQq4Fasr_vns7lHueOn2jP3B6M&usqp=CAU|
|BEE | https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9xjJRdfRr0Yd9W3l7dqr8Wt9_wxmELFTagA&s|
|  Green Bug | https://www.shutterstock.com/image-vector/beetle-pixel-art-potato-bug-260nw-1912842055.jpg|
|Small Bee | https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQq5CXy5tbn2MK6c0YgRtF1bVRMSfZ7_Lay3wgt51mG_m47JXwXkHA6GSO3CITnBWmou1E&usqp=CAU |
|Brown Bug | https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9yqBiQ4weSweGsQ7gfj056DkAPQCRaKJWYrKPSLTZkL1lIL5S5uyUuyERJEf81fqDrYE&usqp=CAU|
