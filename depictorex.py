from PIL import Image

import helpers, drawHelpers, globals
from UIHelper import depictoWindow

if __name__ == "__main__":

    depictoWindow()

    # Resize and deres' image (width, height)
    globals.PIC = globals.PIC.resize((globals.WIDTH, globals.HEIGHT))

    # Convert image to common format
    globals.PIC = globals.PIC.convert("1") # use mode "1" for black and white

    # # Modify color palette
    # for i in range(img.size[0]):
    #     for j in range(img.size[1]):
    #         pix = img.getpixel((i,j))
    #         img.putpixel((i,j), helpers.getColor_brute(pix))
    #         # img.putpixel((i,j), (int(pix[0]*0.3 + pix[1]*0.59 + pix[2]*0.11),)*3) # Black & White
    #     print(f"converting {i} / {img.size[0]}")
    # img.show()

    # Draw image
    # drawHelpers.lineDraw(globals.PIC, (0,0,0))
    drawHelpers.lineDraw(globals.PIC, 0)



