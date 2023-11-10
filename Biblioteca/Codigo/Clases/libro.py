
class Libro():
    def __init__(self, titulo : str, estado : str, precio : int) -> None:
            self._codigo = None # El código lo genera la base de datos 
            self._titulo = titulo 
            self._estado = estado 
            self._precio = precio 
        
    # Getters 
    
    @property
    def codigo(self) -> int: 
        return self._codigo
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def estado(self) -> str:
        return self._estado
    
    @property
    def precio(self) -> float:
        return self._precio 

    @codigo.setter
    def codigo(self):
        pass
    
    @titulo.setter
    def titulo(self):
        pass
    
    @estado.setter
    def estado(self, estado):
        self._estado = estado
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio
    
    
    
    def __str__(self) -> str:
        pass