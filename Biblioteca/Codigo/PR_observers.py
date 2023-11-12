from abc import ABC, abstractmethod


class Observer(ABC):
    
    @abstractmethod
    def update(self):
        """"Responsabilidad de las clases derivadas de definir el método"""
        pass

class Sujeto(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer : Observer) -> None:
        self._observers.append(observer)
    
    def detach(self, observer : Observer) -> None:
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()
