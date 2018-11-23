# A two player tic-tac-toe Game implemented in Python
from ForOnePlayer import main
def main():
	print('Welcome to the tic tac toe game folks!')
	P1=input("Player 1 enter your choice as 'X' or 'O' : ")    #player 1 takes input
	print()
	if P1=='X':
		P2='O'				#if player 1 takes 'X',player 2 is assigned 'O'
	else:
		P2='X' 				#else if player 1 takes 'O', player 2 is assigned 'X'

	print("Player 1 has chosen : " + P1)
	print("and Player 2 has chosen : " + P2)
	print()
	num_board()
	board_list=[' ']*10		#initialising our board_list with whitespaces 
	while flag!=1:
		pc1 = int(input("Player 1 enter your choice(1-9) : "))

		if board_list[pc1]== 'X' or board_list[pc1]=='O':					#preventing overwriting of choices !
			print("Enter another choice,this one is already filled bud !")
			continue

		if P1=='X':
			board_list[pc1]= 'X'
		else:
			board_list[pc1]='O'
		filled_board(board_list)

		res=CheckResults(board_list)
		if res == 'X':

			if P1=='X':
				print('Congratulations Player 1 ! You have won the match. ')
				break
			else:
				print('Congratulations Player 2 ! You have won the match. ')
				break
		elif res == 'O':

			if P1 == 'O':
				print('Congratulations Player 1 ! You have won the match. ')
				break
			else:
				print('Congratulations Player 2 ! You have won the match. ')
				break
		elif res == ' ':
			print("Well its a tie guys,well played ! ")
			break

		pc2=20				#initialising pc2 to an arbitrary value(>=10) so till the time the player doesnt enter the correct
		while pc2 ==20:		#value pc2 will keep on taking the input from user.
			pc2 = int(input("Player 2 enter your choice(1-9) : "))					
			if board_list[pc2]== 'X' or board_list[pc2]=='O':					#preventing overwriting of choices !
				print("Enter another choice,this one is already filled bud !")
				pc2=20

		if P2 == 'O':
			board_list[pc2]='O'		#filling the board list
		else :
			board_list[pc2]='X'
		filled_board(board_list)

		res=CheckResults(board_list)
		if res == 'X':

			if P1=='X':
				print('Congratulations Player 1 ! You have won the match. ')
				break
			else:
				print('Congratulations Player 2 ! You have won the match. ')
				break
		elif res == 'O':

			if P1 == 'O':
				print('Congratulations Player 1 ! You have won the match. ')
				break
			else:
				print('Congratulations Player 2 ! You have won the match. ')
				break
		elif res == ' ':
			print("Well its a tie guys,well played ! ")
			break

def CheckResults(board_list):		#condition checking for 'winning' and 'tie' of the match

	if board_list[1] == board_list[2] == board_list[3] and board_list[1]!=' ':
		flag=1
		return board_list[1]
	elif board_list[4] == board_list[5] == board_list[6] and board_list[4]!=' ' :
		flag=1
		return board_list[4]
	elif board_list[7] == board_list[8] == board_list[9] and board_list[7]!=' ' :
		flag=1
		return board_list[7]
	elif board_list[1] == board_list[4] == board_list[7] and board_list[1]!=' ' :
		flag=1
		return board_list[1]
	elif board_list[2] == board_list[5] == board_list[8] and board_list[2]!=' ' :
		flag=1
		return board_list[2]
	elif board_list[3] == board_list[6] == board_list[9] and board_list[3]!=' ' :
		flag=1
		return board_list[3]
	elif board_list[1] == board_list[5] == board_list[9] and board_list[1]!=' ' :
		flag=1
		return board_list[1]
	elif board_list[3] == board_list[5] == board_list[7] and board_list[3]!=' ' :
		flag=1
		return board_list[3]

	if board_list.count(' ')== 1:
		return ' '


def filled_board(board_list  ): 		#function for displaying the filled board.

	print('Current board :')
	print()
	print(' '+board_list[1] + ' | '+ board_list[2] + ' | '+board_list[3])
	print('-----------')
	print(' '+board_list[4] + ' | '+ board_list[5] + ' | '+ board_list[6])
	print('-----------')
	print(' '+board_list[7] + ' | '+ board_list[8] + ' | '+ board_list[9])

def num_board():						#function for telling the players about numbering on the board.
	print('The board looks like this :')
	print(' 1 '+' | '+ ' 2 '+' | '+' 3 ')
	print('-----------------')
	print(' 4 '+' | '+' 5 '+' | '+' 6 ')
	print('-----------------')
	print(' 7 '+' | '+' 8 '+' | '+' 9 ')
	print()
flag=0	
if __name__== "__main__":			#declaring a global varoable 'flag' 
	main() 