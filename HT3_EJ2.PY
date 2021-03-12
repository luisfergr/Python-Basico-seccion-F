nombre = input("Cual es su nombre?")
genero = input("Cual es su sexo es? (Ingrese F si es femenino o M si es masculino)")

N = nombre
G = genero

if (G == "F" and N.lower() < 'm') or (G == "F" and N.lower() > 'n'):
    grupo = 'A'
else:
    grupo = 'B'

print(N + " tu grupo es: " + grupo)