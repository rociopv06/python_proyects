from cgitb import text

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout



def show_popup(output):
    popupWindow = Popup(background_color=(0.0,0.63,0.76,1),title="Output", content=TextInput(text=output,  size_hint=(None,None),size=(4000,20)), size_hint=(None,None),size=(400,200))

    popupWindow.open()

class MyFloat(FloatLayout):
    key = ObjectProperty(None)
    input = ObjectProperty(text)
    output = ObjectProperty(text)
    def __init__(self, **kwargs):
        super(MyFloat, self).__init__(**kwargs)

    def pressed(self):

        keyList = list(self.key.text)

        final = ""
        i = 0

        for x in self.input.text: #loop through each char in input

            if(x == " "):
                final = final + " "
                continue
            else:
                if i <= len(keyList):
                    num = ord(keyList[i])
                final = final + chr(((ord(x)-97 + num-96) % 26)+97)
            i += 1
            if bool(i == len(keyList)): #once its bigger than the numbers of chars in the key it starts all over again
                i = 0 #serves to count which char we're using in the key
        show_popup(final)


    def pressedd(self):

        keyList = list(self.key.text)


        final = ""
        i = 0

        for x in self.input.text: #loop through each char in input

            if(x == " "):
                final = final + " "
                continue
            else:
                if i <= len(keyList):
                    num = ord(keyList[i])
                final = final + chr(((ord(x) - num-1) % 26)+97)
            i += 1 #serves to count which char we're using in the key
            if bool(i == len(keyList)): #once its bigger than the numbers of chars in the key it starts all over again
                i = 0
        show_popup(final)


class MyApp(App):
    def build(self):
        return MyFloat()


if __name__ == "__main__":
    MyApp().run()
