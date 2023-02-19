import pickle

class vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Mi cronos es de color {self.color}, y tiene {self.ruedas} ruedas'

cronos = vehiculo('rojo', 4)
print(cronos)

f = open('miauto.bin','wb')
pickle.dump(cronos, f)
f.close()

f = open('miauto','rb')
mi_cronos = pickle.load(f)

print(mi_cronos)
f.close()
