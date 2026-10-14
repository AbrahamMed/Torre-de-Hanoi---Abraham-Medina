import time

def torre_de_hanoi(n, origen, destino, auxiliar):
    # Caso base
    if n == 1:
        print(f"Mueve el disco 1 de la torre {origen} a la torre {destino}")
        return
    
    torre_de_hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mueve el disco {n} de la torre {origen} a la torre {destino}")
    torre_de_hanoi(n - 1, auxiliar, destino, origen)

def main():
    try:
        discos = int(input("¿Cuántos discos quieres usar?: "))
        
        if discos <= 0:
            print("Ingresa un número mayor a 0")
            return
            
        print("\nTorre de Hanoi")
        
        tiempo_inicio = time.time()
        torre_de_hanoi(discos, 'A', 'C', 'B')
        tiempo_fin = time.time()
        
        # Cálculo del tiempo de ejecución
        tiempo_total = tiempo_fin - tiempo_inicio
        
        print("--- Terminado ---\n")
        print(f"Discos: {discos}")
        print(f"Tiempo de ejecución: {tiempo_total:.5f} segundos")
        
    except ValueError:
        print("Error: Ingresa un número entero")

if __name__ == "__main__":
    main()