print ("\tValentina Cardona Ligarreto \n Misión TIC 2022 \n Universidad El Bosque \n Elabore un algoritmo que realice las siguientes operaciones")
print ("\t1.   4*x^2-2*x+7 \n\t2.   rc(b^2)-4*a*c \n\t3.   (x+y1)/x - (3*x/5) \n\t4.   (x+y)^3/x^(1/3) - 3x/5")

x = int(input("\tDigite el valor de x: "))
y = int(input("\tDigite el valor de y: "))
a = int(input("\tDigite el valor de a: "))
b = int(input("\tDigite el valor de b: "))
c = int(input("\tDigite el valor de c: "))

#1.
f = 4 * x**2 - 2 * x + 7
#2
g = (b**2)**(1/2) - 4*a*c
#3
h = (x+y)/x - (3*x)/5
#4
i = (x+y)**3/x**(1/3) - (3*x)/5

print("\tEl resultado de la primer operación es: ", f)
print("\tEl resultado de la segunda operación es: ", g)
print("\tEl resultado de la tercer operación es: ", h)
print("\tEl resultado de la cuarta operación es: ", i)
