from abc import ABC, abstractmethod


class Sujeto:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class Observer(ABC):
    @abstractmethod
    def update(self):
        "Responsabilidad de las clases derivadas de definir el método"
