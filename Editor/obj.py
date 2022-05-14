from ursina import *
from Editor.gui.input import *
from Editor.gui.vs import *
from Editor.gui.obj_keys import *

class add_obj(Button, Object, Keys):
    def __init__(self, Origin: float=0.6, Texture: str='', Position:tuple = (5, 2, 5), Model: str = 'cube', Color='red', **kwargs):
        super().__init__(
            parent=scene,
            position=Position,
            model=Model,
            origin = Origin,
            texture=Texture,
            color = Color
            )

    def input(self, key):
        if self.hovered:
            b = Text(scale=1, text=f'{self.get_position()} {self.scale}')
            b.fade_out()
            self.key = key
            self.Mov_Keys(key)
            self.GUI_Keys(key)