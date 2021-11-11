import numbers
from abc import ABC, abstractmethod
import json

JSON_TEXT = '{"regularPrice":100, "advancedPrice":60, "studentPrice":50, "latePrice":110}'


def ticketNumber():
    if not hasattr(ticketNumber, "number"):
        ticketNumber.number = 0
    ticketNumber.number += 1
    return ticketNumber.number


# todo: функция получения билетов по номеру


class Ticket(ABC):
    @property
    @abstractmethod
    def price(self):
        """Returns price of a ticket"""

    @property
    @abstractmethod
    def number(self):
        """Returns number of a ticket"""


class Event:
    def __init__(self):
        self.tickets = list()

    @property
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, tickets):
        if not isinstance(tickets, list) or not all(isinstance(x, Ticket) for x in tickets):
            raise TypeError("argument is not a list of tickets")
        self.__tickets = tickets

    def addTicket(self, ticket):
        if not isinstance(ticket, Ticket):
            raise TypeError("argument is not a ticket")
        self.__tickets.append(ticket)

    def getTicketByNumber(self, num):
        for x in self.__tickets:
            if x.number == num:
                return x
        raise ValueError("no ticket with this number")


class RegularTicket(Ticket):

    def __init__(self, event):
        self.price = json.loads(JSON_TEXT)["regularPrice"]
        self.number = ticketNumber()
        event.addTicket(self)

    def __str__(self):
        return f"Ticket № {self.number}; Type: RegularTicket; Price: {self.price};"

    @property
    def price(self):
        return self.__price

    @property
    def number(self):
        return self.__number

    @price.setter
    def price(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("argument is not a number")
        if value < 0:
            raise ValueError("wrong price")
        self.__price = value

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError("argument is not a number")
        if value < 0:
            raise ValueError("wrong number of a ticket")
        self.__number = value


class AdvancedTicket(Ticket):

    def __init__(self, event):
        self.price = json.loads(JSON_TEXT)["advancedPrice"]
        self.number = ticketNumber()
        event.addTicket(self)

    def __str__(self):
        return f"Ticket № {self.number}; Type: AdvancedTicket; Price: {self.price};"

    @property
    def price(self):
        return self.__price

    @property
    def number(self):
        return self.__number

    @price.setter
    def price(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("argument is not a number")
        if value < 0:
            raise ValueError("wrong price")
        self.__price = value

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError("argument is not a number")
        if value < 0:
            raise ValueError("wrong number of a ticket")
        self.__number = value


class StudentTicket(Ticket):
    def __init__(self, event):
        self.price = json.loads(JSON_TEXT)["studentPrice"]
        self.number = ticketNumber()
        event.addTicket(self)

    def __str__(self):
        return f"Ticket № {self.number}; Type: StudentTicket; Price: {self.price};"

    @property
    def price(self):
        return self.__price

    @property
    def number(self):
        return self.__number

    @price.setter
    def price(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("argument is not a number")
        if value < 0:
            raise ValueError("wrong price")
        self.__price = value

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError("argument is not a number")
        if value < 0:
            raise ValueError("wrong number of a ticket")
        self.__number = value


class LateTicket(Ticket):
    def __init__(self, event):
        self.price = json.loads(JSON_TEXT)["latePrice"]
        self.number = ticketNumber()
        event.addTicket(self)

    def __str__(self):
        return f"Ticket № {self.number}; Type: LateTicket; Price: {self.price};"

    @property
    def price(self):
        return self.__price

    @property
    def number(self):
        return self.__number

    @price.setter
    def price(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("argument is not a number")
        if value < 0:
            raise ValueError("wrong price")
        self.__price = value

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError("argument is not a number")
        if value < 0:
            raise ValueError("wrong number of a ticket")
        self.__number = value


class Order:
    def __init__(self, tickets):
        self.tickets = tickets

    @property
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, tickets):
        if not isinstance(tickets, list) or not all(isinstance(x, Ticket) for x in tickets):
            raise TypeError("argument is not a list of tickets")
        self.__tickets = tickets

    def addTicket(self, ticket):
        if not isinstance(ticket, Ticket):
            raise TypeError("argument is not a ticket")
        self.__tickets.append(ticket)

    def getPrice(self):
        totalPrice = 0.0
        for pr in self.__tickets:
            totalPrice += pr.price
        return totalPrice


ev = Event()
t = StudentTicket(ev)
print(ev.getTicketByNumber(1))
