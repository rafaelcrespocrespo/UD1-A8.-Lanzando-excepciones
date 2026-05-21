#Rafael Crespo Crespo

# division2.py

# Ahora que sabemos que ciertos códigos pueden lanzar excepciones, veamos cómo capturarlas para que el programa no se detenga abruptamente.
# Así evitamos que el usuario vea mensajes de error confusos y
# podemos manejar los errores de manera más elegante y sin salirnos del programa.
# Las excepciones se capturan usando bloques try-except.
# Dentro del bloque try, colocamos el código que puede lanzar una excepción.

try:
    # Secuencia de 3 divisiones sin problemas
    print("Inicio del programa.---------------------")
    print("Inicio del primer bloque.")
    print(11/22, end=", ")
    print(22/33, end=", ")
    print(33/44)
    print("Fin del primer bloque.")

    # Secuencia de 3 divisiones con un error en la segunda división
    print("Inicio del segundo bloque.")
    print(44/55, end=", ")
    print(55/0, end=", ")  # ZeroDivisionError
    print(66/77)
    print("Fin del segundo bloque.")

except ZeroDivisionError as zde:
    print(f"\n>>>>>>>>>Error capturado: {zde}. No se puede dividir por cero.")

finally:
    print("En el bloque finally. SIEMPRE se ejecuta.")

print("Fin del programa.")


# -------------------------------------------------------
# PREGUNTAS Y RESPUESTAS
# -------------------------------------------------------

# ¿Se ejecuta todo el código dentro del bloque try?
# No. Se detiene cuando ocurre la excepción en 55/0.

# ¿Cuántas divisiones se realizan en total?
# Se realizan 4 correctamente antes del error:
# 11/22, 22/33, 33/44, 44/55

# ¿Cuántas lanzan un error/excepción?
# Solo 1: 55/0

# Indica en qué línea se lanza la excepción
# En la línea: print(55/0, end=", ")

# ¿Qué tipo de excepción se lanza?
# ZeroDivisionError

# ¿Qué sucede con la ejecución del programa cuando se lanza la excepción?
# Se interrumpe el try, se ejecuta except, luego finally y continúa el programa.

# ¿Cuántas sentencias se dejan de ejecutar? ¿Por qué?
# 2 sentencias (66/77 y "Fin del segundo bloque")
# porque el flujo salta directamente al except.

# ¿Se llega a la sentencia print("Fin del programa.")?
# Sí, porque la excepción está controlada.

# ¿En qué se diferencia este código del anterior division.py?
# En que ahora la excepción está capturada con try-except-finally y el programa no se detiene.


# -------------------------------------------------------
# VERDADERO / FALSO
# -------------------------------------------------------

# Una excepción se lanza y siempre detiene la ejecución del programa. Falso
# Una excepción es un error en tiempo de ejecución. Verdadero
# El bloque try se ejecuta completamente del principio hasta el final. Falso
# El bloque except se ejecuta siempre. Falso
# El bloque finally se ejecuta siempre. Verdadero
# El bloque else se ejecuta siempre. Falso
# El bloque finally se ejecuta cuando no se lanza ninguna excepción. Verdadero
# El bloque finally se ejecuta cuando se lanza una excepción. Verdadero