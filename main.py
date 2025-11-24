from PIL import Image
from rich import print
from rich.console import Console

#PIL
im = Image.open('image.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())

#rich
console = Console()

for i, pixel in enumerate(pixel_values):
    r, g, b = pixel
    if i % width == 0:
        print("\n")
    console.print("█   ", style=f"rgb({r},{g},{b})", end="")