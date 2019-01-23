from PIL import Image
import random
import time

def open_image(path):
  image = Image.open(path)
  return image

# Save Image
def save_image(image, path):
  image.save('hello.png', "PNG")

# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

def change_color(path):
    image= Image.open(path)
    width, height = image.size

    new = create_image(width,height)
    pixels = new.load()

    mred = random.randint(0,255)
    mgreen = random.randint(0,255)
    mblue = random.randint(0,255)
    for i in range (width):
        for j in range (height):
            pixel = get_pixel(image, i, j)

            red =   pixel[0]
            green = pixel[1] #if you want to run it on a computer that isn't $10000+ you can comment this out
            blue =  pixel[2] #comment this out

            print(str(red)+" "+str(green)+" "+str(blue))

            if (red>10 and green>10 and blue>10): #and change this to if (red>10):
                pixels[i, j] = (mred,mgreen,mblue)

            else:
                pixels[i, j] = (255,255,255) #makes it white


    save_image(new, "hello")
    return new

change_color("/Users/pasta/Desktop/twitter_logo.png")
