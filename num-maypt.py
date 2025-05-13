# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20230904-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':

	print ("Dime los 3 numeros y te dire cual es el mayor")
	n1 = input("introduzca el primer numero: ")
	n2 = input("introduzca el segundo numero:")
	n3 = input("introduzca el tercer numero:")
	if n1>n2 and n1>n3:
		print  (n1,  "es el numero mayor")
	else:
		if n2>n1 and n2>n3:
			print (n2, "es el numero mayor")
		else:
			if n3>n2 and n3>n1:
				print (n3, "es el numero mayor")

