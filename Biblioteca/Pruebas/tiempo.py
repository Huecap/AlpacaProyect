# Utilizamos timedelta

from datetime import date, timedelta

tiempo = date.today()

# Especificamos cuanto vale el delta
delta = timedelta(days = 7)
# Podemos operar con el delta 
tiempo_de_entrega = tiempo + delta

print('Fecha: ', tiempo)
print('Delta: ', delta)
print('Fecha nueva: ', tiempo_de_entrega)
