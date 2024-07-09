#import PIL and exif tags
import PIL

from PIL import Image as PillowImage
from PIL.Exiftags import TAGS

#create empty dict for images to populate
images = []

#add function to add images to dict

PILLOW_TAGS = [

]

EXIF_TAGS = [
    
]

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
        #add code here to take exif data for input form
        print("{}: {}".format(english_tag, value))