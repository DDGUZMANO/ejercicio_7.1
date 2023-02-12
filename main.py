# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
import operaciones_matematicas as op

print("Este programa está diseñado para hacer calculosmatemáticos simples entre dos números enteros")
print("\n1 = Suman.\n2 = Resta.\n3 = Multiplicación.\n4 = Division.")
consulta = input("Indique que operación matemática desea hacer: ")
valor_1 = int(input("Ingrese el valor del primer número: "))
valor_2 = int(input("Ingrese el valor del segundo número: "))
def main():
    
    if consulta == 1:
        print(op.suma(valor_1,valor_2))        
    elif consulta == 2:
        print(op.resta(valor_1,valor_2))
    elif consulta == 3:
        print(op.multiplica(valor_1,valor_2))
    elif consulta == 4:
        print(op.divide(valor_1,valor_2))
        

if __name__ == '__main__':
    main() 