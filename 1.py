def convert_from_decimal(number, base):
	result = ''

	while number > 0:
		result = str(number % base) + result
		number //= base
	return result


enteredNumber = int(input("Введите число: "))

while True:	
	enteredBase = int(input("Введите основание целевой системы счисления (2 или 8, например): "))
	if (2 <= enteredBase <= 9):
		break
	print("!!! Основание системы счисления должно быть от 2 до 9 !!!")


print("Вывод:", enteredNumber, "->", convert_from_decimal(enteredNumber, enteredBase))
