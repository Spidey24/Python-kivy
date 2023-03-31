from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp

class StackLayoutExample(StackLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.orientation = 'lr-tb'
    for i in range(0,100):
      b = Button(text=str(i+1), size_hint = (None,None) , size =(dp(100),dp(100)))
      self.add_widget(b)


# class GridLayoutExample(GridLayout):
#   pass

#Box Layout
class BoxLayoutExample(BoxLayout):
  pass
"""
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.orientation ='vertical'
    b1 = Button(text = 'A Button')
    b2 = Button(text= 'Another button')
    self.add_widget(b1)
    self.add_widget(b2)
"""
#Anchor Layout
class AnchorLayoutExample(AnchorLayout):
  pass

class MainWidget(Widget):
  pass

class TheLabApp(App):
  pass

obj = TheLabApp() # Needed to create an object
obj.run()