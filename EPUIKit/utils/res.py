from pathlib import Path

from PIL import ImageFont, Image

BASE_DIR = Path(__file__).resolve().parent.parent
RES_DIR = BASE_DIR.joinpath('res')


def font(size):
    return ImageFont.truetype(str(RES_DIR.joinpath('Font.ttc')), size)


def icon(name, size):
    im = Image.open(str(RES_DIR.joinpath(name)))
    im.thumbnail(size, Image.BICUBIC)
    return im
