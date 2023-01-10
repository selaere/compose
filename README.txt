this thing is a ``.XCompose`` file generator with diacritics and stuff. i originally made this for
wincompose, and later changed things to work on X11 compose as well (see keynames in data.py).

i made this for my ``es`` keyboard layout, the default settings use keys like ñ and ç and · and ¿
that won't be available on most keyboards. make sure to customize it for your own keyboard (see 
``custom_dia.py``)

how to run:

    $ python main.py