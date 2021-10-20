edad = input()
try:
    if int(edad) >= 18:
        print("mayor de edad")
except:
    if edad == "veinte":
        print("fue en letras")