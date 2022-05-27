# File: tierlistapp.py
"""
Goal functionality:
1. Add tiers according to user
2. Save/delete tierlists made
3. Alter title/color of tiers
4. Create labels of words
5. Drag/drop labels
"""


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import (
    NumericProperty,
    ColorProperty,
    ObjectProperty
)
from kivy.graphics import Color
from kivy.uix.togglebutton import ToggleButton, Button

class TierList(Widget):
    pass


class MainWindow(Screen):
    pass

class NewWindow(Screen):
    parentGrid = ObjectProperty(None)
    color = ColorProperty(None)
    
    tierCounter = 0
    textDict = {1: "S Tier", 2: "A Tier", 3: "B Tier", 4: "C Tier", 5: "D Tier", 6: "F Tier"}
    colorDict = {
        1: ((255/255, 32/255, 32/255, .6), (255/255, 32/255, 32/255, .9)),
        2: ((219/255, 178/255, 137/255, .6), (219/255, 178/255, 137/255, 1)),
        3: ((223/255, 223/255, 133/255, .6), (223/255, 223/255, 133/255, 1)),
        4: ((104/255, 221/255, 104/22, .6), (104/255, 221/255, 104/22, 1)),
        5: ((84/255, 221/255, 221/255, .6), (84/255, 221/255, 221/255, 1)),
        6: ((147/255, 79/255, 216/255, .6), (147/255, 79/255, 216/255, 1))
    }
    buttonDict = {}


    def incrementTierCounter(self):
        if self.tierCounter <= 6:
            self.tierCounter += 1
    def addTier(self):
        if self.tierCounter > 6:
            return
        
        newTier = TierPreview(self.colorDict[self.tierCounter])
        newTier.text = self.textDict[self.tierCounter]
        self.parentGrid.add_widget(newTier)

        self.buttonDict[self.tierCounter] = newTier
        self.buttonDict[self.tierCounter].bind(on_press = self.untoggleButton)
    def untoggleButton(self, instance):
        for button in self.buttonDict:
            if self.buttonDict[button] != instance:
                self.buttonDict[button].state = "normal"

class TierPreview(ToggleButton):
    color1 = ColorProperty(None)
    color2 = ColorProperty(None)
    def __init__(self, color, **kwargs):
        self.color1 = color[0]
        self.color2 = color[1]
        super(TierPreview, self).__init__(**kwargs)

class LoadWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


w_manager = WindowManager()

class TierListApp(App):
    def build(self):
        
        screens = [MainWindow(name = "main"), NewWindow(name = "new"), LoadWindow(name = "load")]
        for screen in screens:
            w_manager.add_widget(screen)
        w_manager.current = "main"
        return w_manager


if __name__ == "__main__":
    Window.size = (320, 480)
    
    TierListApp().run()