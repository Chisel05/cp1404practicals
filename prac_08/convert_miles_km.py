"""
'Do-from-scratch' exercise from the week 8 practical.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesKmApp(App):
    km = StringProperty()

    def build(self):
        """Build main app."""
        self.title = 'Miles and Km'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """Handle conversion from miles to km."""
        try:
            miles = float(self.root.ids.miles.text)
            self.km = str(miles * MILES_TO_KM)
        except ValueError:
            self.km = str(0.0)

    def handle_increment(self, increment):
        """Handle increment of miles."""
        try:
            miles = int(self.root.ids.miles.text) + increment
            self.root.ids.miles.text = str(miles)
        except ValueError:
            miles = 0 + increment
            self.root.ids.miles.text = str(miles)


MilesKmApp().run()
