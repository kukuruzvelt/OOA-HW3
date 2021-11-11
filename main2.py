from abc import ABC, abstractmethod
import json
from datetime import date
import calendar

JSON_INGREDIENTS = '{"cheese":10, "bacon":6, "olives":5}'
JSON_PIZZA_OF_THE_DAY = '{"Monday":"PizzaMargherita", "Tuesday":"PizzaPepperoni", "Wednesday":"PizzaTexas",  ' \
                        '"Thursday":"PizzaMargherita", "Friday":"PizzaPepperoni",' \
                        '"Saturday":"PizzaTexas", "Sunday":"PizzaMargherita"}'


class Pizza(ABC):
    @property
    @abstractmethod
    def price(self):
        """Price"""

    @property
    @abstractmethod
    def additionalIngredients(self):
        """Ingredients"""

    @abstractmethod
    def __str__(self):
        """Str"""


class PizzaMargherita(Pizza):
    defaultPrice = 80

    def __init__(self):
        self.price = PizzaMargherita.defaultPrice
        self.additionalIngredients = list()

    def __str__(self):
        return f"Pizza: PizzaMargherita, additionalIngredients: {self.__additionalIngredients}, price: {self.price}."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def additionalIngredients(self):
        return self.__additionalIngredients

    @additionalIngredients.setter
    def additionalIngredients(self, value):
        self.__additionalIngredients = value


class PizzaPepperoni(Pizza):
    defaultPrice = 120

    def __init__(self):
        self.price = PizzaPepperoni.defaultPrice
        self.additionalIngredients = list()

    def __str__(self):
        return f"Pizza: PizzaPepperoni, additionalIngredients: {self.__additionalIngredients}, price: {self.price}."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def additionalIngredients(self):
        return self.__additionalIngredients

    @additionalIngredients.setter
    def additionalIngredients(self, value):
        self.__additionalIngredients = value


class PizzaTexas(Pizza):
    defaultPrice = 100

    def __init__(self):
        self.price = PizzaTexas.defaultPrice
        self.additionalIngredients = list()

    def __str__(self):
        return f"Pizza: PizzaTexas, additionalIngredients: {self.__additionalIngredients}, price: {self.price}."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def additionalIngredients(self):
        return self.__additionalIngredients

    @additionalIngredients.setter
    def additionalIngredients(self, value):
        self.__additionalIngredients = value


def addIngredients(pizza, ingredients):
    if not isinstance(ingredients, list) or not all(json.loads(JSON_INGREDIENTS)[x] for x in ingredients):
        raise TypeError("argument is not a list of additional ingredients")
    for i in ingredients:
        pizza.additionalIngredients.append(i)
        pizza.price += json.loads(JSON_INGREDIENTS)[i]


def pizzaOfTheDay(weekday):
    if weekday not in json.loads(JSON_PIZZA_OF_THE_DAY):
        raise ValueError("wrong weekday")
    str_pizzaOfTheDay = json.loads(JSON_PIZZA_OF_THE_DAY)[weekday]
    if str_pizzaOfTheDay == "PizzaMargherita":
        return PizzaMargherita()
    elif str_pizzaOfTheDay == "PizzaPepperoni":
        return PizzaPepperoni()
    elif str_pizzaOfTheDay == "PizzaTexas":
        return PizzaTexas()


class Order:
    def __init__(self, pizzas):
        self.pizzas = pizzas

    def __str__(self):
        string = str()
        for pizza in self.__pizzas:
            string += str(pizza)
            string += '\n'
        return string

    @property
    def pizzas(self):
        return self.__pizzas

    @pizzas.setter
    def pizzas(self, pizzas):
        if not isinstance(pizzas, list) or not all(isinstance(x, Pizza) for x in pizzas):
            raise TypeError("argument is not a list of pizzas")
        self.__pizzas = pizzas

    def addPizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("argument is not a pizza")
        self.__pizzas.append(pizza)

    def addIngredients(self, numOfPizza, ingredients):
        if numOfPizza >= len(self.__pizzas):
            raise ValueError("wrong pizza number")
        addIngredients(self.__pizzas[numOfPizza], ingredients)

    def getPrice(self):
        totalPrice = 0.0
        for pizza in self.__pizzas:
            totalPrice += pizza.price
        return totalPrice


try:
    pz = pizzaOfTheDay(calendar.day_name[date.today().weekday()])
    addIngredients(pz, ["cheese", "bacon"])
    pm = PizzaMargherita()
    order = Order([pz, pm])
    order.addIngredients(1, ["cheese", "olives"])
    print(order)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
