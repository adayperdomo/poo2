### Parámetro posicional
def tipicaFuncion(unpar:int, dospar:int)->None:
#def tipicaFuncion(unpar:int, dospar:int, /)->None:         #cuidado con el caracter /
    pass

tipicaFuncion(3, 6)
#unpar = 3
#dospar = 6


### Parámetro con valor por defecto
def tipicafuncion(unpar: int, dospar = 6:int)-> None:
    pass

tipicaFuncion(3)
#unpar = 3
#dospar = 6


### Parámetro arbitrario
def tipicaFuncion(unpar:int, *dospar:int, content:int)->None:
    pass

tipicaFuncion(3, 6, 6, 6, content=3)


### Parámetro nominal
def tipicaFuncion(*,unpar:int, dospar:int)->None
    pass

tipicaFuncion(dospar = 6, unpar = 3)
#unpar = 3
#dospar = 6


### Ejercicio 3
def myDiv(id:str, *clas:str, content:str)->str:
    resultado = ''
    
    resultado += '<div id="' + id +'" '

    if len(clas) != 0:
        resultado += 'class = "'

        for e in clas:
            resultado += e + ', '

        resultado += '\b\b"'
    
    resultado += '>' + content + '</div>'

    return resultado

def main():
    print(myDiv("midiv", "bt_h1", "row", "clear", content="Lorem ipsum"))

if __name__ == "__main__":
    main()