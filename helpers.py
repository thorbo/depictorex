from scipy.spatial import KDTree
from timeit import timeit
import random
import math

tree = None
Palette1 = [
    # Format - list of ints, used in PIL
    [0,0,0],
    [87,87,87],
    [160,160,160],
    [156,39,176],
    [157,175,255],
    [42,75,215],
    [41,208,208],
    [76,175,80],
    [198,255,0],
    [255,238,51],
    [255,146,51],
    [233,222,187],
    [129,74,25],
    [248,187,208],
    [244,67,54],
    [173,35,35],
    [255,255,255]
]


def buildTree():
    """Build KDTree from palette when first called"""
    global tree
    tree = KDTree(Palette1)


def colorDist(c1, c2):
    """Return 3D distance between two colors"""
    rdist = c1[0] - c2[0]
    gdist = c1[1] - c2[1]
    bdist = c1[2] - c2[2]
    return math.sqrt(rdist * rdist + gdist * gdist + bdist * bdist)


def getColor_KDT(color):
    """Return closest color available in color palette"""
    if not tree:
        buildTree()
    d, i = tree.query(color)
    return tuple(Palette1[i])


def getColor_brute(color):
    """Return closest color available in color palette"""
    dist = colorDist(color, Palette1[0])
    for p in Palette1:
        check = colorDist(p, color)
        if check <= dist:
            dist = check
            newColor = p
    return tuple(newColor)


def randcolor():
    """Return random RGB value"""
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def checkPaletteFuncs():
    wrapped = wrapper(getColor_brute, randcolor())
    print(f"Brute Force Palette Location Time: {timeit(wrapped, number=20000)}")

    wrapped = wrapper(getColor_KDT, randcolor())
    print(f"KD Tree Palette Location Time: {timeit(wrapped, number=20000)}")

