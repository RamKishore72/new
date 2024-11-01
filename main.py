from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class SampleApp(App):
    
    def build(self):
        self.appKv = '''
Screen:
    Label:
        text: 'Hello, World.'
        color: 0, 0, 1, 1  # Blue in RGBA
        halign: 'center'
        valign: 'middle'
        size_hint: (1, 1)
        text_size: self.size
'''
        AppScreen = Builder.load_string(self.appKv)
        return AppScreen

if __name__ == '__main__':
    SampleApp().run()

    