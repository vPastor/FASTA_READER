import sys
if (len(sys.argv)>2 or len(sys.argv)<2):
	print ('Numero de argumentos invalidos')
else:
	e = 0
	for  linea  in  open(sys.argv[1]):
		if (('>') == (linea[0])):
			if e!=0:
				print ("Longitud de restos " + str(e))
				e = 0
				break
			print (linea + len(linea))
		else:
			e += len(linea)
