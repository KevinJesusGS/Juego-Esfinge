#Las preguntas que te irá haciendo la esfinge corresponden a los print de esta plantilla
#Por favor completa cada reto

#Clase 1 Proyecto: Definidendo la aventura

#Reto 1 - Pon tu respuesta después del print
print("Define el equipamiento para una aventura de trekking y su valor en trekjuls (moneda del juego):")

agua = 14.65
arco = 120.50
armadura = 160
botella = 12.5
comida_fruta = 20.45
comida_carne = 40.24
escudo = 100
espada = 150
flechas = 10
mapa = 10.85



#Reto 2 - Pon tu respuesta después de cada print
print("Lista tres objetos del equipamiento: Nombre y valor")


print("comida_fruta", comida_fruta)
print("agua", agua)
print("botella", botella)



print("¿Puedes combinar elementos de tu equipo para prepararte mejor?")

agua_en_botella = agua + botella
arco_flechas = arco + flechas


print("Agua en botella", agua_en_botella)
print("Arco cargado", arco_flechas)


print("¿El precio del agua en botella es menor al del arco cargado?")

print(agua_en_botella < arco_flechas)




print("¿Cuanto valdría comprar fruta y un mapa?")

print(comida_fruta + mapa)




print("¿Si tienes 100 puntos, te alcanza para comprar una armadura?")

print(armadura <= 100)

#Clase 2 Proyecto: Tomando decisiones

#Reto 3 - Pon tu respuesta después del print
print("La esfinge te dice: No debes colocar más de 5 objetos en tu mochila, y tampoco pasarte de 300 trekjuls: ¿Cuales elementos colocarías?")

mochila = 0

if agua_en_botella + arco_flechas + mapa + armadura + comida_fruta <= 200:
    mochila = agua_en_botella + arco_flechas + mapa + armadura + comida_fruta
    print("El valor de los elementos es menor a 200: ", mochila)

elif agua_en_botella + arco_flechas + mapa + armadura <= 200:
    mochila = agua_en_botella + arco_flechas + mapa + armadura
    print("El valor de los elementos es menor a 200", mochila)

else:
    print("Ups! Ninguna de tus intentos fue exitoso")

if agua_en_botella + escudo + comida_fruta <= 200:
    mochila = agua_en_botella + escudo + comida_fruta
    print("El valor de los elementos es menor a 200. Total compra: ", mochila)
    
#Reto 4 - Pon tu respuesta después del print
print ("Es tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")

mochila2 = 0

while mochila2 <= 200:
    mochila2 += agua_en_botella
    print("Mochila dos: ", mochila2)

mochila2 -= agua_en_botella
print("Nos pasamos, vamos a restar una botella de agua, ahora tenemos: ", mochila2)

#Clase 3 Proyecto: Almacenando equipamimento

#Reto 4 - Pon tu respuesta después del segundo print
print("Le hice una actualización a tu mochila te dice la esfinge, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")

mochila_actzd = {
	agua_en_botella: {"cantidad": 1, "valor_unitario": agua_en_botella},
	escudo: {"cantidad": 1, "valor_unitario": escudo},
	comida_fruta: {"cantidad": 1, "valor_unitario": comida_fruta}
}

mochila2_actzd = {
	"agua_en_botellada" : {"cantidad": 2, "valor_unitario": agua_en_botella}
}

#Reto 5 - Pon tu respuesta después del print
print("Ahora, en esta aventura te van a acompañar 8 integrantes más, y te voy a pedir que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")

vehiculo = [{}] * 7

for compartimiento in range(7):
    vehiculo[compartimiento] = {
        "agua_en_botella" : {"cantidad": 1, "valor_unitario": agua_en_botella},
        "escudo" : {"cantidad": 1, "valor_unitario": escudo},
        "comida_fruta" : {"cantidad": 1, "valor_unitario": comida_fruta}
    }
    print("Acabas de armar la mochila para el compartimiento: ", compartimiento + 1)


for mochila in vehiculo:
    print(mochila)

#Clase 4 Proyecto: Organizandonos un poco

#Reto 6 - Pon tu respuesta después del segundo print
print("Te pido que para cuatro integrantes recolectes 3 elementos sin importar las cantidades que quieras adicionarles, y te da las siguientes opciones: mapa, arco_flechas, comida_carne y agua_en_botella")
print("Pero necesito que calcules el total de elementos que hay en tu equipo")

#Agregamos 2 snacks, 2 brujulas y una linterna funcional para los 4 primeros integrantes


def agregarElementosAMochilas():
    for compartimiento in range(3):
        vehiculo[compartimiento] = {
            "agua_en_botella" : {"cantidad": 1, "valor_unitario": agua_en_botella},
            "arco_flechas" : {"cantidad": 2, "valor_unitario": arco_flechas},
            "mapa" : {"cantidad": 3, "valor_unitario": mapa},
            "comida_carne" : {"cantidad": 2, "valor_unitario": comida_carne},
        }
    imprimir(vehiculo)
    calcularTotalElementosEnMochilas(vehiculo)

def calcularTotalElementosEnMochilas(vehiculo):
    total_elementos_mochilas = {}
    
    print("Calculo elementos en mochila")
    for mochila in vehiculo: 
        for elemento, detalle in mochila.items(): 
            if elemento in total_elementos_mochilas:
                total_elementos_mochilas[elemento] += detalle["cantidad"]
            else:
                total_elementos_mochilas[elemento] = detalle["cantidad"]

    print(total_elementos_mochilas)


def imprimir(estructura):
    for objeto in estructura:
        print(objeto)

agregarElementosAMochilas()
