import datetime

from .cogs import *
from .utils import *


def year():
    return str(datetime.datetime.now().year)

def creator():
    if year() == "2021":
        return "© 2021 MirthfulFox"
    else:
        return f"© 2021-{year()} MirthfulFox"