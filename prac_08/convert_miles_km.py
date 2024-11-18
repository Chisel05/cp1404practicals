"""
'Do-from-scratch' exercise from the week 8 practical.
"""
from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder


class MilesKmApp(App):
    def build(self):
        self.title = 'Miles and Km'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesKmApp().run()
