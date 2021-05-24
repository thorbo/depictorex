import pyautogui, globals



def pixelDraw(img, color):
    """Draws all pixels matching color in img. Draws pixel by pixel. """
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i,j)) == color:
                pyautogui.moveTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE * j, _pause=False)
                pyautogui.click(button="left", _pause=False)

def lineDraw(img, color):
    """Draws all pixels matching color in img. Draws line by line (vertical)."""
    dark = False
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i,j)) == color:
                if dark == False:
                    pyautogui.moveTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE * j, _pause=False)
                    dark = True
                elif j == img.size[1] - 1:
                    pyautogui.dragTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE *j,
                                     button="left", duration=globals.DRAG_DUR, _pause=False)
                    dark = False
            else:
                if dark == True:
                    pyautogui.dragTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE *j,
                                     button="left", duration=globals.DRAG_DUR, _pause=False)
                    dark = False
                else:
                    continue
