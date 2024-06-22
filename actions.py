#import PIL and Pillow Libraries
#import human-readable exif tags
import PIL

from PIL import Image as PillowImage
from PIL import ExifTags

#create empty dict for images to populate
images = []

#add function to add images to dict

#function to iterate through photos and pull metadata
for img in images:
    print(img)
    image_path = "unaltered/{}".format(img)
    pillow_img = PillowImage.open(image_path)
    img_exif = pillow_img.getexif()
    
    for tag in PILLOW_TAGS:
        try:
            english_tag = ExifTags.TAGS[tag]
            value = img_exif[tag]
        except:
            continue
        print("{}: {}".format(english_tag, value))