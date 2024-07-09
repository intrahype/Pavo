#import PIL and exif tags
import PIL

from PIL import Image as PillowImage
from PIL.Exiftags import TAGS

#create empty dict for images to populate
unmodified = [

 ]

for file in unmodified:
    #open image
    image = image.open()

    #get exif data
    exifdata = image.getexif()

    #loop to make tags human readable
    for tagid in exifdata:
        #get tagid
        tagname = TAGS.get(tagid, tagid)
        #get tag value
        value = exifdata.get(tagid)
        #print final result
        print(f"{tagname:30}: {value}")