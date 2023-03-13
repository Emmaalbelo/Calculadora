#calculadora \n
#\n

print ("***************")
print ("* Calculadora *")
print ("*************** \n")

print ('\n __________________\n')
print ('\n| Menu de opciones|\n')
print ('\n ------------------\n')

print ('1. Suma')
print ('2. Resta')
print ('3. Multiplicacion')
print ('4. Division')
print ('5. Division entera')
print ('6. exponente')
print ('7. Modulo o resto \n')

numero = int (input ('introduce la opcion deseada:'))

if numero == 1:
    print ("Elegiste suma\n")
    numero = int (input ("Dime el primer valor: "))
    numero += int (input ("Dime el segundo valor: "))
elif numero == 2:
    print ("Elegiste resta\n")
    numero = int (input ("Dime el primer valor: "))
    numero -= int (input ("Dime el segundo valor: "))
elif numero == 3:
    print ("Elegiste Multiplicacion\n")
    numero = int (input ("Dime el primer valor: "))
    numero *= int (input ("Dime el segundo valor: "))
elif numero == 4:
    print ("Elegiste Division\n")
    numero = int (input ("Dime el primer valor: "))
    numero /= int (input ("Dime el segundo valor: "))
elif numero == 5:
    print ("Elegiste Division entera\n")
    numero = int (input ("Dime el primer valor: "))
    numero //= int (input ("Dime el segundo valor: "))
elif numero == 6:
    print ("Elegiste exponente\n")
    numero = int (input ("Dime el primer valor: "))
    numero **= int (input ("Dime el segundo valor: "))
elif numero == 7:
    print ("Elegiste Modulo o resto\n")
    numero = int (input ("Dime el primer valor: "))
    numero %= int (input ("Dime el segundo valor :"))
else:
    print ("La opcion no es valida")

print (("\nEl resultado es: " ), numero)