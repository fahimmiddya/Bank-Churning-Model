from guietta import _, Gui , Quit,HSeparator
gui = Gui(
     [ '<center>A big GUI with all of Guietta''s widgets</center>'],
    ['Enter Numbers:', "__a__",' + ',"__b__",['Calculate']],
    [' Result :'     ,'result',  _  ,      _,            _],
    [_               ,_       ,_    ,_      ,         Quit]
)

with gui.Calculate:
    gui.result = float(gui.a)+float(gui.b)

gui.run()