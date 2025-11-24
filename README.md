# Terminal Image Viewer

An incredibly simple Python script that renders images in your terminal using RGB colors.

## Requirements

Install required packages

```bash
pip install Pillow rich
```

## Usage
```bash
python script.py
```

Replace `'image.jpg'` in the script with your image path.

## How it works

- Loads an image with PIL
- Renders each pixel as a colored block character using Rich's RGB support
- That's it