def traducao():  #aprendendo conceito de matriz
	animails={
		'gato': {
			'ingles': 'cat',
			'espanhol': 'gato',
			'frances': 'chat'
		},
		'cao': {
			'ingles': 'dog',
			'espanhol': 'perro',
			'frances': 'auauau'
		},
		'peixe': {
			'ingles': 'fish',
			'espanhol': 'pesce',
			'frances': 'fishing'
		},
	}
	animal = input('Entre com o animal ? ')
	idioma = input('Entre com o idioma ? ')
	#animal_dict = animails[animal]
	#print(animal_dict)
	print(animails[animal][idioma])
traducao()