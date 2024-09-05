
def funcionA(funcionB):
    def funcionC(*args, **kwargs):
        print("hola")
        resultado =funcionB(*args, **kwargs)
        print("esto sucede")
        return resultado
    return funcionC()

