
def sumando(*args:int|float):
    if not all(isinstance(num,(int,float)) for num in args ):
        raise TypeError("Error, Debe ingresar valores numericos")
    return  sum(args)

num_1: int = 33
num_2: int = 339

try:
    resultado = sumando(num_1,num_2)
    print(resultado)
except TypeError as e:
    print(f"Se detectó un problema: {e}")