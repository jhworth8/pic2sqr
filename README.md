# pic2sqr
This program takes an image file and creates a square image with the original image in the center of the square. 
This is helpful when you need a square image for img2img programs like Stable Diffusion.
Use it in terminal.

Only prerequisite is to 'pip install pillow'.

  ____ ___ ____     ____      ____   ___  ____  
 |  _ \_ _/ ___|   |___ \    / ___| / _ \|  _ \ 
 | |_) | | |   _____ __) |___\___ \| | | | |_) |
 |  __/| | |__|_____/ __/_____|__) | |_| |  _ < 
 |_|  |___\____|   |_____|   |____/ \__\_\_| \_\
                                                


This program takes an image file or path and creates a square image with the original image in the center of the square.

The user can enter "-jpg" after the input file to output a jpg image with a white background.

If there is nothing after the input file, then the output will be a png image with a transparent background.

The CLI will be like this:

input: python pic2sqr.py image.jpg
output: image-sqr.png

input: python pic2sqr.py path-to-image.png
output: image-sqr.png

input: python pic2sqr.py image.jpg -jpg
output: image-sqr.jpg
