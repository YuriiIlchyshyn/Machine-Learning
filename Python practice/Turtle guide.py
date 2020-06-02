import turtle # імпортуємо бібліотеку
screen = turtle.getscreen() # створюємо вікно для відображення
turtle.title("Черепашка гайд")
my_turtle = turtle.Turtle() # створюємо об'єкт
my_turtle.shape("turtle") # можемо міняти форму , міняємо на черепашку
my_turtle.color("green") # міняємо колір об'єкта
#Є 4 напрямки в яких може рухатись черепашка:

#    Forward вперед
#    Backward назад
#    Left вліво
#    Right вправо

# використання циклів
for i in range(0,180):
    my_turtle.forward(1)
    my_turtle.right(1)

# готові фігури
my_turtle.circle(90)

# Можна використовувати скорочений синтаксис
#    t.rt() instead of t.right()
#    t.fd() instead of t.forward()
#    t.lt() instead of t.left()
#    t.bk() instead of t.backward()

# Згадуємо осі x y

my_turtle.goto(0,0) # goto(x,y) рухає в координати

my_turtle.goto(100,50)
my_turtle.setposition(100,100)
print(my_turtle.pos()) # виводить координати черепашки

my_turtle.shapesize(1,5,10)
