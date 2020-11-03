import random
From = int(input('Lowest Range;  '))
To = int(input('Highest Range;  '))
Answers = int(input('How Many Answers:  '))
Tries = int(input('How Many Tries:  '))
lol_dict = {}
num = -1
num = int(num)
for multi_variable in range(0, Answers):
    num += 1
    lol_dict["num%s" %multi_variable] = num
lol_list = list(lol_dict.values())
lol_len = len(lol_list)
print(len)
def generating_random_numbers():
		global lol_random
		for ha in range(10000):
			lol_num = random.randint(From, To)
			if lol_num not in lol_list:
				lol_list[0] = lol_num	
				random.shuffle(lol_list)
Try = Tries
generating_random_numbers()
def checking():
	global lol_len
	global Try
	for guesses in range(Tries):
		Try += 1
		if lol_len != 0:
			Guess = int(input('Guess:  '))
			if Guess in lol_list:
				print('Right', lol_len - 1, 'More')
				lol_len -= 1
			else:
				if guesses == lol_len:
					print('Wrong You still have', lol_len, 'More')
					print('NOT FINISH ANSWERING, YOU LOST')
				else:
					print('Wrong', lol_len, 'More')
		elif lol_len == 0:
			print ('ALL RIGHT, YOU WON')
checking()
	