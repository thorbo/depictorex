from PIL import Image
import urllib.request
from io import BytesIO
import numpy as np

Palette = [
    (0,0,0),
    (87,87,87),
    (160,160,160),
    (156,39,176),
    (157,175,255),
    (42,75,215),

    (41,208,208),
    (76,175,80),
    (198,255,0),
    (255,238,51),
    (255,146,51),

    (233,222,187),
    (129,74,25),
    (248,187,208),
    (244,67,54),
    (173,35,35),
    (255,255,255)
]


url = "https://ctl.s6img.com/society6/img/UPB_Z6mA6neMT-KwPmKnXY1EvcU/w_700/prints/~artwork/s6-0024/a/9774180_2379400/~~/edgar-allan-poe-5fv-prints.jpg"
response = urllib.request.urlopen(url).read()
img = Image.open(BytesIO(response))
ary = np.array(img)
print(ary[20][20])
img = Image.fromarray(ary)
img.show()
