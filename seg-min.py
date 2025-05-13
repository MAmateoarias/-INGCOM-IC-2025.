# Este codigo ha sido generado por el modulo psexport 20230904-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print("Dime la cantidad de segundos y la pasare a minutos: ")
	sg = float(input())
	m = 0
	if sg>=60:
		m = sg/60
	else:
		print("Introduce una cantida de segundos mayor a 60 para que los minutos sean mayores a 1")
	print("La cantidad de minutos es: ",m)

