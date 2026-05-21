#Rafael Crespo Crespo

# division.py

# Terminología de las excepciones:
# - Excepción: un evento que interrumpe el flujo normal de un programa.
# - Excepción es un error en tiempo de ejecución.
# - Las excepciones se LANZAN (RAISE) cuando ocurre un error.
# - Las excepciones se CAPTURAN (CATCH) usando bloques try-except.
# - Si una excepción no se captura, el programa se detiene y muestra un mensaje de error.
# - Tipos comunes de excepciones: ZeroDivisionError, ValueError, TypeError, IndexError, KeyError.
# - try-except: estructura para manejar/capturar excepciones.
# - try: bloque de código donde se intenta ejecutar una operación que puede fallar.
# - Cuando una excepción es capturada, el programa puede continuar su ejecución.


# Ejecuta el siguiente código para observar el comportamiento de las excepciones en divisiones
# Responde a las preguntas planteadas en los comentarios
# No modifiques el código, solo ejecútalo y observa los resultados
# El código consiste en mostrar varias divisiones, divididas en dos bloques.

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
print(55/0, end=", ") # ZeroDivisionError: division by zero
print(66/77)
print("Fin del segundo bloque.")
print("Fin del programa.")


# ¿cuántas divisiones se realizan en total?
# 5 divisiones

# ¿cuántas lanzan un error/excepción?
# 1 división

# Indica en qué línea se lanza la excepción
# En la línea: print(55/0, end=", ")

# ¿Qué tipo de excepción se lanza?
# ZeroDivisionError

# ¿Qué sucede con la ejecución del programa cuando se lanza la excepción?
# El programa se detiene inmediatamente.

# Se llega a la sentencia print("Fin del programa.")?
# No

# ¿Cuántas sentencias se dejan de ejecutar? ¿Por qué?
# 3 sentencias, porque la excepción no es capturada.



# Responde verdadero/falso:
# Una excepción se lanza y detiene la ejecución del programa si no es capturada. V/F
# Verdadero

# Una excepción es un error en tiempo de ejecución. V/F
# Verdadero

# Una excepción se lanza cuando ocurre un error. V/F
# Verdadero

# El nombre del tipo de excepción indica el tipo de error que ocurrió. V/F
# Verdadero

# Las excepciones tienen la palabra "Error" en su nombre. V/F
# Verdadero