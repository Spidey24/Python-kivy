from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # create text input for displaying calculator output
        self.output = TextInput(multiline=False, readonly=True, font_size='30sp', size_hint_y=None, height=80)
        self.add_widget(self.output)

        # create grid layout for calculator buttons
        self.grid = BoxLayout(orientation='vertical', spacing=10)

        row1 = BoxLayout(spacing=10)
        row1.add_widget(Button(text='7', on_press=self.add_text))
        row1.add_widget(Button(text='8', on_press=self.add_text))
        row1.add_widget(Button(text='9', on_press=self.add_text))
        row1.add_widget(Button(text='+', on_press=self.add_text))
        self.grid.add_widget(row1)

        row2 = BoxLayout(spacing=10)
        row2.add_widget(Button(text='4', on_press=self.add_text))
        row2.add_widget(Button(text='5', on_press=self.add_text))
        row2.add_widget(Button(text='6', on_press=self.add_text))
        row2.add_widget(Button(text='-', on_press=self.add_text))
        self.grid.add_widget(row2)

        row3 = BoxLayout(spacing=10)
        row3.add_widget(Button(text='1', on_press=self.add_text))
        row3.add_widget(Button(text='2', on_press=self.add_text))
        row3.add_widget(Button(text='3', on_press=self.add_text))
        row3.add_widget(Button(text='*', on_press=self.add_text))
        self.grid.add_widget(row3)

        row4 = BoxLayout(spacing=10)
        row4.add_widget(Button(text='0', on_press=self.add_text))
        row4.add_widget(Button(text='=', on_press=self.add_text))
        row4.add_widget(Button(text='C', on_press=self.clear_output))
        row4.add_widget(Button(text='/', on_press=self.add_text))
        self.grid.add_widget(row4)

        # add grid layout to main layout
        self.add_widget(self.grid)

    # function to add text to output
    def add_text(self, button):
        if button.text == '=':
            try:
                result = str(eval(self.output.text))
            except:
                result = 'Error'
            self.output.text = result
        else:
            self.output.text += button.text

    # function to clear output
    def clear_output(self, button):
        self.output.text = ''

class CalculatorApp(App):

    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()
