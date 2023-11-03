import lucky_numbers

def isHappy(n):
	# запоминаем, с чего мы начали
	start = n
	# сумма на старте равна нулю
	result = 0
	# пока не получим единицу — выполняем цикл
	while result != 1:
		# получаем сумму квадратов цифр
		result = lucky_numbers.sum_of_square_digits(n)
		# делаем её новым стартовым числом
		n = result
		# если сумма совпала с тем, что было — мы зациклились
		if result == start:
			print('Всё зациклилось')
			# выходим из функции
			return False
	# если дошли сюда — число счастливое
	return True

isHappy(7)