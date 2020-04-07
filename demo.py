# -*- coding:utf-8 -*-
from PIL import ImageFont

from EPUIKit import QuadrantsLayout, VirtualPaper
from EPUIKit.widget import Label


def font():
    return ImageFont.load_default()


layout = QuadrantsLayout(border=1)
layout.add(Label('LEFT_BOTTOM', font=font()), QuadrantsLayout.LEFT_TOP)
layout.add(Label('LEFT_BOTTOM', font=font()), QuadrantsLayout.LEFT_BOTTOM)
layout.add(Label('RIGHT_TOP', font=font()), QuadrantsLayout.RIGHT_TOP)
layout.add(Label('RIGHT_BOTTOM', font=font()), QuadrantsLayout.RIGHT_BOTTOM)
paper = VirtualPaper(layout, 144, 500)
paper.show()
