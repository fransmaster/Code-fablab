from random import randint
op = ['piedra','papel','tijera']
computer = op[randint (0,2)]
x = True
while x == True:
	player = input ('piedra,papel o tijera? :')
	if player ==computer:
		print('empate')
	elif player =='piedra':
		if computer == 'papel':
			print ('perdiste:', computer,'>',player)
		else:
			print('ganaste;', player, '<', computer)
	elif player == 'papel':
		if computer == 'tijera':
			print('perdiste',computer, '>', player)
		else:
			print ('ganaste',player, '<', computer)
	elif player == 'tijera':
		if computer == 'piedra':
			print('perdiste', computer, '>' ,player)
		else:
			print('ganaste', player, '<', computer)
	elif player == 'salir':
		break
	else:
		print('error')




