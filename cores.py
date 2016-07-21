print("""
	Lista de Cores Python!
	""")
contador = 0
while contador != 108:
	print("\033["+str(contador)+"mCor, numero => \033[0;0m", contador)
	contador = contador +1
