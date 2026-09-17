"""
numero=int(input(" ingese un numero: "))

if numero>0: 
    print("el numero es positivo ")
else:
    print("el numero es negativo")
"""


"""
edad= int (input("infrese su nombre "))


if edad>= 18:
    print("eres mayor de edad ")
else:
    print("eres menor de edad ")
    """
"""
numero=float(input("ingrese un numero "))

if numero%2==0:
    print("el numero es par")

else:
    print("el numero es inpar ")
"""
"""
contraseña =(input ("ingrese su contraseña= ")) 
contra="python"
if contraseña==contra:
    print(" la contraseña es correcta")
else:
    print("la contraseña es incorrecta ")
"""

"""
numero1=int(input("ingrese un numero "))
numero2=int(input("ingrse otro numero "))
if numero1>numero2:
    print("el numero  es mayor ")
elif numero1==numero2:
    print("el numero es igual ")
else:
    print("el numero ""es menor ")
"""
"""
nota1= float(input("ingrse la nota de matematicas: "))
nota2=float(input("ingrese la nota de ingles: "))
nota3=float(input("ingrese la nota de biologia: "))
nota4=float(input("ingrese la nota de quimica: "))
final= (nota1+nota2+nota3+nota4)/4
if 90<=final<=100: 
    print("excelente:" ,final)
elif 70<=final<=89:
    print("bueno: ",final)
elif 60<= final<=69:
      print("abrobado: ",final)  
elif 0<= final<=59:           
    print("reprobo: ",final)
else: 
     print("esa nota esta mal: ",final)

"""
"""
temperatura1=float(input("ingrse la temperatura: "))
if temperatura1>25:
    print(" hace calor")
elif  10<=temperatura1<=25:
    print("temperatura agradable")
elif temperatura1< 10:
    print(" hace frio")
else:
    print("la temperatura esta mal")
"""
"""
existemayor = False
print("escribe 3 numeros para saber cual es el mayor de los 3 ")
a=float(input("escribe el 1 numero "))
b=float(input("escribe el 2 numero "))
c=float(input("escribe el 3 numero "))
if a>b:
    if a>c:
        print(" el numero ",a,("es mayor"))
if b>a:
    if b>c:
        print("el numero ",b,("es el mayor "))
if c>a:
    if c>b:
        print("el numero",c,("es el mayor"))
if existemayor== False:
    print("no hay valor que fuera mayor que todos ")

"""
"""
print("convertir de numero a letras ")
x=int(input("cual es el numnero que desea convertir: " ))
if x==1:
    print("el numerom es uno ")
elif x == 2:
    print("el numero es dos ")
elif x == 3:
    print("el numero es tres ")   
elif x == 4:
    print("el numero es cuatro ") 
elif x == 5:
    print("el numero es cinco ")
else:
    print(" el numero llega asta 5")
"""
"""
### vacaciones de  de los empleados 
print("inicio\n")
nombre=(input("diga su nombre: "))
clave=int(input(nombre+" diga la clave que le coresponde: "))
if clave==1:
    print(nombre+" diga los años que lleba con la empresa: ")
    años=float(input())
    if años<2:
        print("los dias de vacaciones son `6`")
    elif años>=2 and años<=6:
        print("los dias de vacaciones son `14`")
    elif años>=7:
        print("los dias de vacaciones son ´20´")
if clave==2:
    print(nombre+" diga los años que lleba con la empresa: ")
    años=float(input())
    if años==1:
        print("los dias de vacaciones son `7`")
    elif años>=2 and años<=6:
        print("los dias de vacaciones son `15`")
    elif años>=7:
        print("los dias de vacaciones son ´22´")   
if clave==3:
    print(nombre+" diga los años que lleba con la empresa: ")
    años=float(input())
    if años==1:
        print("los dias de vacaciones son `10`")
    elif años>=2 and años<=6:
        print("los dias de vacaciones son `20`")
    elif años>=7:
        print("los dias de vacaciones son ´30´") 
    else:
        print("la clave no esta registrada verifique de nuevo\n  ")
"""
""" 
print("\nescribe 3 numeros para saber cual es el mayor de los 3\n ")
a=int(input("escribe el 1 numero "))
b=int(input("escribe el 2 numero "))
c=int(input("escribe el 3 numero "))
if a>b and a>c:
    print (f"el numero uno es mayor: {a}")
elif b>a and b>c:
    print(f"el numero dos es mayor:{b} ")
elif c>a and c>b:
      print(f"el numero tres es mayor:{c} ")
else :
    print(f"no hay numero mayor:{a,b,c}")
"""
x=0
while x<10:
    print(x)
    x+=1
print("fin del programa")

for i in range(11):
    print(i)

y = 'Python'
for x in y:
    print(x)

print("hola desde github")
