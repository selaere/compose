this thing is a ``.XCompose`` file generator with diacritics and stuff. i originally made this for
wincompose, and later changed things to work on X11 compose as well (see keynames in data.py).

i made this for my ``es`` keyboard layout, the default settings use keys like ñ and ç and · and ¿
that won't be available on most keyboards. make sure to customize it for your own keyboard (see 
``data.py``)

how to run:

    $ python main.py

THINGS

greek starts with `1`. based on Beta code

 ⎕ a b c d e f g h i j k l m n o p q r s t u v w x y z
1⎕ α β ξ δ ε φ γ η ι ς κ λ μ ν ο π θ ρ σ τ υ ϝ ω χ ψ ζ

cyrillic starts with `2`

  ⎕ a b c d e f g h i j k l m n o p q*r s t u v w x y z ' "
 2⎕ а б ц д э ф г   и · к л м н о п щ р с т у в ў х ы з ь ъ
2j⎕ я   ч ђ е є џ   і ј   љ   њ ё ӏ ѕ   ш ћ ю       й ж ь ъ

ARROWS

arrows by default use numpad keys. 5 ends an arrow sequence.
7 8 9   ↖ ↑ ↗
4 5 6   ← ↲ →
1 2 3   ↙ ↓ ↘

opposite arrows are combined in the obvious way:
    ↔  ←→↲      ↕  ↑↓↲  
more than one arrow results in more than one arrowhead:
    ↠  →→↲
other arrows create more complex paths:
    ↱  ↑→↲      ↶  ↑←↓↵
there are also other arrowforms:
    ↺  cw↲      ↻  ccw↲     ↯  zigzag
and also:
    ↝  ~→↲      ↣  >→↲      ↪  '→↵      ↬  %→↲
    ⇥  |→↲      ↦  ||→↲     ⇒  =→↲      ⇛  ==→↵
    ↾  r↑↵      ↿  l↑↵      ⇀  *→↵      ⇁  _→↵   
    ⇸  -→↲      ⇻  --→↲     ⇢  .→↵      ⤑  ..→↵
    ⇨  W→↲      ⭢  @→↲      ⇾  t→↵      ⟶  l→↵
    ⤞  v→↵      ⮕  b→↲      ⮊  O→↵      ⮎  U→↵
    ⮞  h→↵     ⮚  H→↵       ⯈  p←↵      ⮑  ret→↵

    ⇆  ←+→↵     ⥃  ←_→↵     ⥄  ←*→↵  

BOX DRAWING

─ is ←→x
┼ is ↑↓←→
╬ is ↑↑↓↓←←→→x
(they always have to go in this order)