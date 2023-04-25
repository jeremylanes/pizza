from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior  # pour le background image

from models import Pizza


class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()


class MainWidget(FloatLayout):
    recycleview = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza(name="4fromage", ingredients='fromage, tomate', price=19, vegetarian=True),
            Pizza(name="chorizo", ingredients='tomate, chorizo, tomate, viande', price=19, vegetarian=False),
            Pizza(name="calzone", ingredients='fromage, jambon, champigon', price=19, vegetarian=False),

        ]

    def on_parent(self, widget, parent):
        self.recycleview.data = [pizzas.get_dictionary() for pizzas in self.pizzas]


with open('pizzasrc.kv', encoding='utf8') as f:
    Builder.load_string(f.read())


class PizzaApp(App):
    def build(self):
        return MainWidget()


PizzaApp().run()
