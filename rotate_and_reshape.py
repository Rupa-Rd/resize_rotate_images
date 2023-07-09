import os
import PIL
from os import listdir
from PIL import Image

origin = 'images'
destination = 'edited_images'

for images in os.listdir(origin) :
   image = Image.open(origin + '/' + images)
   new_image = image.resize((250,250)).rotate(180)
   new_image.save(destination + '/' + images)

print("Successfully Done!\nThe image is resized to 250x250 , rotated to 180 and stored in the destination folder.")
