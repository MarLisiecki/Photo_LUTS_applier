import glob

from PIL import Image
from pillow_lut import load_cube_file

# Create list of LUTS
def get_all_LUTS():
    luts_list = [luts_name for luts_name in glob.glob(pathname="LUTS/*.cube")]
    return luts_list

# Generate photos
def generate_photos_with_applied_filter(luts_to_use, path):
    for count, lut in enumerate(luts_to_use):
        lut_filter = load_cube_file(lut)
        output_image = Image.open(path)
        output_image.filter(lut_filter).save("name_filter" + str(count) + ".jpg")


if __name__ == "__main__":
    luts_to_use = get_all_LUTS()
    generate_photos_with_applied_filter(luts_to_use, path)
