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


class Mat:
    def suma (self):#para definir un metodo (: para definir el metodo)
        self.n1 = int (input ("dime el primer valor "))
        self.n2 = int (input ("dime el segundo valor "))
        #self se usa para definir las variables del metodo

s = Mat()
s.suma ()
print (s.n1 + s.n2)




import tkinter as tk

calculation = ""

def add_to_calculation (symbol):
    pass

def aevaluete_calculation ():
    pass

def clear_fiel ():
    pass

root = tk.TK()
root.geometry ("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)
root.mainloop ()
