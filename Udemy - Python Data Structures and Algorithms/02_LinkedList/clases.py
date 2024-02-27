#Una clase es como un cotador de galletas


class Cookie:
    def __init__(self, color) -> None:
        self.color = color
        
    
    def get_color(self):
        return self.color


    def set_color(self, color):
        self.color = color 



cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print(cookie_one.get_color())
print(cookie_two.get_color())


cookie_one.set_color('red')
cookie_two.set_color('purple')


print(cookie_one.get_color())
print(cookie_two.get_color())




num1= 'a'
num2= 'a'

print(id(num1))
print(id(num2))


num3 = num1

num3 = 'b'

print(id(num3))


