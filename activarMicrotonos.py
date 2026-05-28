import winsound
import time









opcion= int(input("Elige una opcion(1-5):"))
if opcion == 1:
    print("")
elif opcion == 2:
    print()
    if microtonos_libres == 0:
        print(Ya no se pueden emitir mas microtonos, )
    else:
        try:
            cantidad = int(input(""))
            if cantidad <= 0
                print("Tienes que activar al menos 1 microtono")
            elif cantidad > microtonos_libres:
                print(f"Solo puedes activar hasta {microtonos_libres} microtonos")
            else:
                microtonos_libres -= cantidad
                microtonos_activos += cantidad
                print("Reproduciendo microtonos")
                #for i in range (1, cantidad +1):
                #    print(f"Microtono {i} activado...")
                #    winsound.Beep(440,300) # 440 hz por 300 milesimas de segundo
                #    time.sleep(0.05)
                frecuencias = [440,440,440,587,880,784,740,659]
                duraciones = [300,300,300,700,700,200,200,200]
                for i in range (1, cantidad +1):
                    nota_actual = frecuencias[(i -1) % len (frecuencias)]
                    duracion_actual = duraciones[(i -1) % len (duraciones)]
                    winsound.Beep(nota_actual, duracion_actual)
                    time.sleep(0.05)
        except ValueError:
            print("Error")
elif opcion == 3:
    try:
        print(f"\n Recuperar microtonos, actualmente hay {microtonos_activos} microtonos activos")
        cantidad = int(input("¿Cuantos microtonos quieres recuperar?: "))
        if cantidad <= 0:
            print("Error, la cantidad de microtonos a recuperar debe ser mayor a 0")
        elif microtonos_libres + cantidad > maximo_microtonos:
            print(f"Error: no puedes apagar tantos microtonos por que el maximo es {maximo_microtonos}")
        else:
            microtonos_libres += cantidad
            microtonos_activos -= cantidad
            print(f"Recuperaste {cantidad} de microtonos para ser usados en otro momento")
    except ValueError:
        print("Error, debes colocar un número entero")
else:
    ("Error")