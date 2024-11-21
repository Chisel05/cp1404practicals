"""
Dynamic labels app according to practical 8 instructions.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ['Bob', 'Gary', 'Katie', 'Steven', 'Sally']

    def build(self):
        """Build main app."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.handle_labels()
        return self.root

    def handle_labels(self):
        """Handle creation of labels from list."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
