def area_triangle(base, height):
    return (base*height)/2

def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds

def month_days(month, days):
    return print(month + " has " + str(days) + " days.")

def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  print(message)

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(99, 100)
print(smaller, bigger)

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)

sum = area_a + area_b

print("The sum of both areas is: " + str(sum))

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)

result = amount_a + amount_b

print(result)

month_days("June",30)
month_days("July",31)

lucky_number("Kay")
lucky_number("Cameron")
