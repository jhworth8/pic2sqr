import sys
from PIL import Image
from termcolor import colored

def main():
    if len(sys.argv) == 2 and sys.argv[1] == 'help':
        print(colored('\n  ____ ___ ____     ____      ____   ___  ____  ', 'cyan'))
        print(colored(' |  _ \\_ _/ ___|   |___ \\    / ___| / _ \\|  _ \\ ', 'cyan'))
        print(colored(' | |_) | | |   _____ __) |___\\___ \\| | | | |_) |', 'cyan'))
        print(colored(' |  __/| | |__|_____/ __/_____|__) | |_| |  _ < ', 'cyan'))
        print(colored(' |_|  |___\\____|   |_____|   |____/ \\__\\_\\_| \\_\\', 'cyan'))
        print(colored('                                                ', 'cyan'))
        print(colored('\nThis program takes an image file or path and creates a square image with the original image in the center of the square.\n', 'green'))
        print(colored('The user can enter "-jpg" after the input file to output a jpg image with a white background.\n', 'green'))
        print(colored('If there is nothing after the input file, then the output will be a png image with a transparent background.\n', 'green'))
        print(colored('The CLI will be like this:\n', 'cyan'))
        print(colored('input: python pic2sqr.py image.jpg', 'white'))
        print(colored('output: image-sqr.png\n', 'green'))
        print(colored('input: python pic2sqr.py path-to-image.png', 'white'))
        print(colored('output: image-sqr.png\n', 'green'))
        print(colored('input: python pic2sqr.py image.jpg -jpg', 'white'))
        print(colored('output: image-sqr.jpg\n', 'green'))
    elif len(sys.argv) == 2:
        image = Image.open(sys.argv[1])
        width, height = image.size
        if width > height:
            new_image = Image.new('RGBA', (width, width), (0, 0, 0, 0))
            new_image.paste(image, (0, int((width - height) / 2)))
            new_image.save(sys.argv[1].split('.')[0] + '-sqr.png')
        else:
            new_image = Image.new('RGBA', (height, height), (0, 0, 0, 0))
            new_image.paste(image, (int((height - width) / 2), 0))
            new_image.save(sys.argv[1].split('.')[0] + '-sqr.png')
    elif len(sys.argv) == 3:
        image = Image.open(sys.argv[1])
        width, height = image.size
        if width > height:
            new_image = Image.new('RGB', (width, width), (255, 255, 255))
            new_image.paste(image, (0, int((width - height) / 2)))
            new_image.save(sys.argv[1].split('.')[0] + '-sqr.jpg')
        else:
            new_image = Image.new('RGB', (height, height), (255, 255, 255))
            new_image.paste(image, (int((height - width) / 2), 0))
            new_image.save(sys.argv[1].split('.')[0] + '-sqr.jpg')
    elif len(sys.argv) == 1:
        print(colored('Please enter a valid input', 'red'))
    else:
        print(colored('Please enter a valid input', 'red'))

if __name__ == '__main__':
    main()