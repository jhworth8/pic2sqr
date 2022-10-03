# pic2sqr
This program takes an image file and creates a square image with the original image in the center of the square. 
This is helpful when you need a square image for img2img programs like Stable Diffusion.
Now you can also resize the image to your desired px size.
Use it in terminal.



Only prerequisite is to 'pip install pillow'.

This program takes an image file or path and creates a square image with the original image in the center of the square.

The user can enter "resize" after the input file to resize the output image.

The user can enter "-jpg" after the input file to output a jpg image with a white background.

If there is nothing after the input file, then the output will be a png image with a transparent background.

The CLI will be like this:



input: python pic2sqr.py image.jpg

output: image-sqr.png

input: python pic2sqr.py image.png -jpg

output: image-sqr.jpg

input: python pic2sqr.py resize image.jpg 500px

output: image-sqr-500.png

input: python pic2sqr.py resize image.png 500px -jpg

output: image-sqr-500.jpg
