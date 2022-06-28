
#se están importando todas las funcionalidades del módulo "modulo_clase1"
import modulo_clase1

#la funcion "input" siempre retorna una cadena de caracteres, por eso debe 
#convertirse al tipo de dato necesario. En este caso, se requiere un entero:
lim = int(input("Ingrese el límite de la serie"))

#Otras funciones de conversion a tipos primitivos:
#   float(value): convierte a real
#   bool(value): convierte a booleano
#   str(value): convierte a cadena de caracteres
#   type(variable): devuelve el tipo de dato de var como una cadena de caracteres

#código por fuera del main:
#esta variable se trata como si fuera global
lista_serie_global = modulo_clase1.serie1(lim)
print(lista_serie_global)

#el siguiente código valida que se esté en el punto de entrada del 
#módulo o "script" actual, para que funcione como el método "main"
if __name__ == "__main__":
    pass
    lista_serie_local = modulo_clase1.serie1(lim)
    print(lista_serie_local)
