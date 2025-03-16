from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BMICalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text="Enter Weight (kg):", font_size=20))
        self.weight_input = TextInput(hint_text="Weight in kg", input_filter="float")
        self.add_widget(self.weight_input)

        self.add_widget(Label(text="Enter Height (cm):", font_size=20))
        self.height_input = TextInput(hint_text="Height in cm", input_filter="float")
        self.add_widget(self.height_input)

        self.calc_button = Button(text="Calculate BMI", size_hint=(1, 0.2))
        self.calc_button.bind(on_press=self.calculate_bmi)
        self.add_widget(self.calc_button)

        self.result_label = Label(text="", font_size=20, color=(1,1,1,1))
        self.add_widget(self.result_label)

    def calculate_bmi(self, instance):
        try:
            weight = float(self.weight_input.text)
            height = float(self.height_input.text) / 100
            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"

            self.result_label.text = f"Your BMI: {bmi:.2f}\nCategory: {category}"
        except ValueError:
            self.result_label.text = "Enter valid numbers."

class BMIApp(App):
    def build(self):
        return BMICalculator()

if __name__ == "__main__":
    BMIApp().run()
