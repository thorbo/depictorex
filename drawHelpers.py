import pyautogui, globals

# # Modify image to match color palette colors
# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         pix = img.getpixel((i,j))
#         img.putpixel((i,j), helpers.getColor_brute(pix))
#     print(f"converting {i} / {img.size[0]}")
# img.show()


def pixel_draw(img, color):
    """Draws all pixels matching color in img. Draws pixel by pixel.
    color is one value for "1" mode, and tuple of 3 values for "RGB" mode."""
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i, j)) == color:
                pyautogui.moveTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE * j,
                                 _pause=False)
                pyautogui.click(button="left", _pause=False)


def line_draw(img, color):
    """Draws all pixels matching color in img. Draws line by line (vertical).
    color is one value for "1" mode, and tuple of 3 values for "RGB" mode. """
    dark = False
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i, j)) == color:
                if not dark:
                    pyautogui.moveTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE * j,
                                     _pause=False)
                    dark = True
                elif j == img.size[1] - 1:
                    pyautogui.dragTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE * j,
                                     button="left", duration=0.01, _pause=False)
                    dark = False
            else:
                if dark:
                    pyautogui.dragTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE * j,
                                     button="left", duration=0.01, _pause=False)
                    dark = False
                else:
                    continue


def combo_draw(img, color):
    """Draws all pixels matching color in img. Draws line by line (vertical).
    If there is only one pixel at a time, it clicks. If multiple, it drags.
    color is one value for "1" mode, and tuple of 3 values for "RGB" mode. """
    dark = False
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i, j)) == color:
                if not dark:
                    pyautogui.moveTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE * j,
                                     _pause=False)
                    dark = True
                elif j == img.size[1] - 1:
                    pyautogui.dragTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE * j,
                                     button="left", duration=globals.DRAG_DUR, _pause=0.3)
                    dark = False
            else:
                if dark:
                    x, y = pyautogui.position()
                    if y != globals.Y_START + globals.BLOT_SIZE * (j - 1):
                        pyautogui.dragTo(globals.X_START + globals.BLOT_SIZE * i, globals.Y_START + globals.BLOT_SIZE * j,
                                         button="left", duration=globals.DRAG_DUR, _pause=False)
                    else:
                        pyautogui.click(button="left", _pause=False)
                    dark = False
                else:
                    continue
