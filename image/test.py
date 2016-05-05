from PIL import Image

img = Image.open('captcha.jpg')
img = img.convert("RGBA")

pixdata = img.load()

# Make the letters bolder for easier recognition

for y in range(img.size[1]):
	for x in range(img.size[0]):
		if pixdata[x, y][0] < 90:
			pixdata[x, y] = (0, 0, 0, 255)

for y in range(img.size[1]):
	for x in range(img.size[0]):
		if pixdata[x, y][1] < 136:
			pixdata[x, y] = (0, 0, 0, 255)

for y in range(img.size[1]):
	for x in range(img.size[0]):
		if pixdata[x, y][2] > 0:
			pixdata[x, y] = (255, 255, 255, 255)

img.save("input-black.gif")

#   Make the image bigger (needed for OCR)
im_orig = Image.open('input-black.gif')
big = im_orig.resize((1000, 500), Image.NEAREST)
ext = ".tif"
big.save("input-NEAREST" + ext)

#   Perform OCR using tesseract-ocr library
from pytesseract import image_to_string
image = Image.open('input-NEAREST.tif')
print(image_to_string(image))