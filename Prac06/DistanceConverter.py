from kivy.app import App
from kivy.lang import Builder

CONVERSION_RATE = 1.60934


class DistanceConverter(App):
    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('distance_converter.kv')
        return self.root

    def handle_conversion(self):
        value = self.validate_input()
        result = CONVERSION_RATE * value
        self.root.ids.output_number.text = str(result)

    def handle_increment(self, num):
        value = self.validate_input() + num
        self.root.ids.input_number.text = str(value)

    def validate_input(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

DistanceConverter().run()
