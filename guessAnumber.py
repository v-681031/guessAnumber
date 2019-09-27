import random
while True:
	min_input = int(input('input min guess number :'))
	max_input = int(input('input max guess number :'))
	if min_input < max_input:
		break
	else:
		print('max number must > min number')
print('guess a number between ', min_input, ' to', max_input, ' :')
answer = random.randint(min_input, max_input)
guess = int(input())
ming = min_input
maxg = max_input
count = 0
correct = False
while correct == False:
	if guess >= min_input and guess <= max_input:
		while True:
			count += 1
			print('Guess count :', count, '!')
			if answer == guess:
				print('you are right! The answer is ', answer)
				correct = True
				break
			elif answer > guess:
				print('your number is too small!')
				if ming <= guess:
					ming = guess
				print('guess a number between ', ming, 'to' ,maxg)
			else:
				print('your number is too large!')
				if maxg >= guess:
					maxg = guess
				print('guess a number between ', ming, 'to' ,maxg)
			guess = int(input('input number :'))
	else:
		print('your guess number is out of range!')
		print('guess a number between ', min_input, ' to', max_input, ':')
		guess = int(input())	

