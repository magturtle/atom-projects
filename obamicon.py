import time
from PIL import Image

new_sequence = []

im = Image.open("grapefruit.jpg")
im.show ()
#time.sleep (5)

sequence = im.getdata() #gets pixels
for pixels in sequence:
    color = pixels[0] + pixels[1] + pixels[2]
    #darkBlue = (0, 51, 76) BLACK
    if color <400:
        new_sequence.append ((0, 0, 0))
    #red = (217, 26, 33) YELLOW
    elif color <600:
        new_sequence.append ((255, 255, 0))
    #lightBlue = (112, 150, 158)
    elif color <800:
        new_sequence.append ((204, 0, 0))
    #yellow = (252, 227, 166)
    elif color <1000:
        new_sequence.append ((252, 227, 166))
        
new_image = Image.new(im.mode, im.size)
new_image.putdata(new_sequence)
new_image.show ()
time.sleep (3)
