from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class WidgetCreatorApp(App):

    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        self.stringlist = ['Ally', 'Keisha', 'Wilson', 'Carl', 'Eric']

    def build(self):
        self.title = 'Widget Creator App'
        self.root = Builder.load_file('string_widget.kv')
        return self.root

    def create_widgets(self):
        for name in self.stringlist:
            temp_label = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)

    def clear_all(self):
        self.root.ids.entriesBox.clear_widgets()

WidgetCreatorApp().run()