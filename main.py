from PIL import Image
from rich.console import Console
import shutil

terminal_width, terminal_height = shutil.get_terminal_size()


console = Console() # rich


im = Image.open('image.webp', 'r')
orig_width, orig_height = im.size

max_width = terminal_width - 4  # padding
max_height = (terminal_height - 4) * 5 

scale = min(max_width / orig_width, max_height / orig_height)
new_width = int(orig_width * scale)
new_height = int(orig_height * scale)

im = im.resize((new_width, new_height))
width, height = im.size

pixel_values = list(im.getdata())



left_padding = (terminal_width - width) // 2

for i, pixel in enumerate(pixel_values):
    r, g, b = pixel[:3]
    if i % width == 0:
        if i != 0:
            console.print()
        print(" " * left_padding, end="")
    if r == 0 and g == 0 and b == 0:
        console.print(" ", end="")
    else:
        console.print("█", style=f"rgb({r},{g},{b})", end="")

console.print()