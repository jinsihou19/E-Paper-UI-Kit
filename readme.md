# UIKit For Raspberry EPaper

Simple UIKit For Raspberry EPaper.



##Usage

```
from UIKit.utils import font
from UIKit.widget import Label
from epd import epd2in13_V2


epd = epd2in13_V2.EPD()
layout = QuadrantsLayout()
layout.add(Label(strftime('%H:%M'), font=font(48)), QuadrantsLayout.LEFT_TOP)
paper = EPaper(epd, layout, 6)
paper.show()

```

## Supported devices

* waveshare 1.54inch e-Paper HAT V2
* waveshare 2.13inch e-Paper HAT V2

##License

MIT