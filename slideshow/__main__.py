import pptx
import whatimage
import pyheif
from PIL import Image
import os

def is_photo(filename: str):
    # photo_types = ["jpg", "png", "heic"]
    photo_types = ["jpg", "png"]
    def decodeImage(bytesIo):
        fmt = whatimage.identify_image(bytesIo)
        if fmt in ['heic', 'avif']:
            i = pyheif.read_heif(bytesIo.read())
            # Extract metadata etc

            #for metadata in i.metadata or []:
            #    if metadata['type']=='Exif':
            #        # do whatever

            # Convert to other file format like jpeg
            s = io.BytesIO()
            pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
            pi.save(s, format="jpeg")
    for typ in photo_types:
        if filename.startswith("."):
            return False
        elif filename.lower().endswith("." + typ):
            return True
    return False

def get_photos_list():
    print("Please input the location of your photos you would like to use")
    photos_dir = input(">> ")
    while not os.path.exists(photos_dir):
        print("Directory not found.  Please try again.")
        photos_dir = input(">> ")
    print("Directory Found.")
    onlyfiles = [os.path.join(photos_dir, f) for f in os.listdir(photos_dir) if is_photo(f)]
    print("Found {} files.".format(len(onlyfiles)))
    return onlyfiles

def get_output_filename():
    print("Please output the location and filename for the final slideshow")
    slideshow_dir = input("(Leave blank for slideshow.pptx in the current directory) >> ")
    return "slideshow.pptx" if slideshow_dir == "" or slideshow_dir is None else slideshow_dir

def get_slide_layout(prs):
    SLD_LAYOUT_TITLE = 0
    SLD_LAYOUT_TITLE_AND_CONTENT = 1
    SLD_LAYOUT_SECTION_HEADER = 2
    SLD_TWO_CONTENT = 3
    SLD_COMPARISON = 4
    SLD_TITLE_ONLY = 5
    SLD_LAYOUT_BLANK = 6
    SLD_CONTENT_WITH_CAPTION = 7
    SLD_PICTURE_WITH_CAPTION = 8
    slide_layout = prs.slide_layouts[SLD_LAYOUT_BLANK]
    return slide_layout

def create_slideshow(photos_list, output_filename):
    prs = pptx.Presentation()
    for photo in photos_list:
        print(photo)
        slide = prs.slides.add_slide(get_slide_layout(prs))
        left = top = pptx.util.Inches(1)
        with Image.open(photo) as pht:
            from io import BytesIO
            s = BytesIO()
            s.write(pht.tobytes())
            pic = slide.shapes.add_picture(s, left, top)

    prs.save(output_filename)

if __name__ == "__main__":
    photos_list = get_photos_list()
    output_filename = get_output_filename()
    create_slideshow(photos_list, output_filename)
