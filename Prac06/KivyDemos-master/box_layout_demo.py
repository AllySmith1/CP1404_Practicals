from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        # print('greet')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def press_clear(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        # use the .children attribute to access all widgets that are "in" another widget
        for instance in self.root.ids.entriesBox.children:
            instance.state = 'normal'
        # self.status_text = ""'

BoxLayoutDemo().run()