import pyautogui

xstart = 510
ystart = 125
blotSize = 5
dragDuration=0.050

def pixelDraw(img, color):
    """Draws all pixels matching color in img. Draws pixel by pixel. """
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i,j)) == color:
                pyautogui.moveTo(xstart + blotSize * i, ystart + blotSize * j, _pause=False)
                pyautogui.click(button="left", _pause=False)

def lineDraw(img, color):
    """Draws all pixels matching color in img. Draws line by line (vertical)."""
    dark = False
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i,j)) == color:
                if dark == False:
                    pyautogui.moveTo(xstart + blotSize * i, ystart + blotSize * j, _pause=False)
                    dark = True
                elif j == img.size[1] - 1:
                    pyautogui.dragTo(xstart + blotSize * i, ystart + blotSize *j,
                                     button="left", duration=dragDuration, _pause=False)
                    dark = False
            else:
                if dark == True:
                    pyautogui.dragTo(xstart + blotSize * i, ystart + blotSize *j,
                                     button="left", duration=dragDuration, _pause=False)
                    dark = False
                else:
                    continue
