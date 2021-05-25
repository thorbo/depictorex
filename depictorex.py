import drawHelpers, globals
from UIHelper import depicto_window

if __name__ == "__main__":

    # Launch Tkinter UI window. Loads selected image into globals.PIC
    depicto_window()

    # Resize and deres' image (width, height)
    globals.PIC = globals.PIC.resize((globals.WIDTH, globals.HEIGHT))

    # Convert image to common format
    # use mode "1" for black and white, "RGB" for color.
    globals.PIC = globals.PIC.convert("1")

    # Draw image. 0 draws black pixels in black & white mode, (0, 0, 0) draws black pixels in color mode.
    drawHelpers.combo_draw(globals.PIC, 0)
