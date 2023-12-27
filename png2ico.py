# convert png to ico
# Usage: python png2ico.py <png file> <ico file>
from PIL import Image
import sys

def png_to_ico(png_file, ico_file):
    img = Image.open(png_file)
    img.save(ico_file, format='ICO', sizes=[(256,256)])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python png2ico.py <png file> <ico file>")
        sys.exit(1)

    png_file = sys.argv[1]
    ico_file = sys.argv[2]

    png_to_ico(png_file, ico_file)