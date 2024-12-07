'''
ITCS 1140 Group Project for Turtle #4
Raymond Connor Zachary Almedin
'''
import turtle as t
import random as r

## RAYMOND'S PORTION START (12/7/2024) ##

# Creating the turtle
t.shape("turtle")
t.color("green")
t.pensize(5)
t.speed(0)
t.home()

# Setting up the screen
s = t.Screen()
s.title("Random Shapes")
s.setup(width = 800, height = 600)
s.bgcolor("blue")

## RAYMOND'S PORTION END ##

## ALS PORTION START ##

#selects a random shape and adds () to the end, made it a seperate function to be able to call it in a randomized loop
def random_shape():
    r.choice(shapes)()

#Zachary (12/6/24)
#All of the shape functions, plus random angle for the other shapes, random color functions, and the random coord function
#Random shape size function
def random_size():
    size = int()
    size = r.randint(25,150)
    return size
    
#Random pen color setter function
def random_pen_color():
    rand = int()
    rand = r.randint(0,4)
    lis = ["red", "orange", "green", "purple", "yellow"]
    color = lis[rand]
    return color
    
#Random fill color function    
def random_fill_color():
    rand = int()
    rand = r.randint(0,4)
    lis = ["pink", "black", "wheat", "seagreen", "gray"]
    fill_color = lis[rand]
    return fill_color
    
#Sets a random angle for the shapes to be drawn in
def t_direct():
    direction = r.randint(0,180)
    t.setheading(direction)
    
#Sets turtle cursor to a random coord
def random_coord():
    t.penup()
    t.goto(r.randint(-200,200),r.randint(-200,200))
    t.pendown()
    
#Star shape
def star():
    fill_col = random_fill_color()
    size = random_size()
    t_direct()
    random_coord()
    t.pencolor(random_pen_color())
    t.fillcolor(fill_col)
    t.begin_fill()
    #Executing loop 5 times for a star
    for i in range(5):
        t.fd(size)
        t.right(144)
    t.end_fill()
    
#Hexagon shape
def hexagon():
    fill_col = random_fill_color()
    size = random_size()
    t_direct()
    random_coord()
    t.pencolor(random_pen_color())
    t.fillcolor(fill_col)
    t.begin_fill()
    #Executing loop 6 times for a hexagon
    for i in range(6):
        t.fd(size)
        t.left(300)
    t.end_fill()
    
#Diamond shape
def diamond():
    fill_col = random_fill_color()
    size = random_size()
    t_direct()
    random_coord()
    t.pencolor(random_pen_color())
    t.fillcolor(fill_col)
    t.begin_fill()
    t.left(45)
    #Executing loop 4 times for a rhombus
    for i in range(4):
        t.fd(size)
        t.left(90)
    t.end_fill()
    
#Cross shape
def cross():
    fill_col = random_fill_color()
    size = random_size()
    t_direct()
    random_coord()
    t.pencolor(random_pen_color())
    t.fillcolor(fill_col)
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.right(90)
        t.fd(size)
        t.left(90)
        t.fd(size)
        t.left(90)  
    t.end_fill()
    
#Semicircle shape (The best I could get)
def semicircle():
    fill_col = random_fill_color()
    t_direct()
    random_coord()
    t.fillcolor(fill_col)
    t.begin_fill()
    #Drawing out half of the circle's circ
    for i in range(180):
        t.forward(1)
        t.right(1)
    #Turn to draw the line, 90 to the right because we are exactly flipped from the start
    t.right(90)
    #Drawing to fit the line to the dia. Circumference(360)/pi(half of the circle) ~= 115
    t.forward(115)
    t.end_fill()
    
#End Zachary

# list to store shape functions for decision
shapes = [square, circle, triangle, star, hexagon, diamond, cross, semicircle]
shape_names = ["square", "circle", "triangle", "star", "hexagon", "diamond", "cross", "semicircle"] #corresponding names

# If structure for user's choice if they want random shapes (Y/N)
def user_decision(user_choice): # takes the users inputs as param for if structure
    if user_choice.upper() == "Y": # random shapes
         for i in range(r.randint(1, 6)): # generate 1 to 5 random shapes
            random_shape()
             #i put more in here later - AL (11/18/24)
    elif user_choice.upper() == "N": # user selected shapes
        user_shapes = ""
        while user_shapes.upper() != "Q": #loop until user quits
            print("Available Shapes: \n square \n circle \n triangle \n star \n hexagon \n diamond \n cross \n semicircle")
            user_shapes = input("Enter the shape ( or Q to quit): ").lower()
            if user_shapes in shape_names: # check if the input matches
                globals()[user_shapes]()
                #i put more in here later - AL (11/18/24)
            elif user_shapes == "q":
                print("Goodbye")
            else:
                print("Invalid shape. Please choose a shape from the list or enter Q to quit")
    elif user_choice.upper() == "Q":
        print("Goodbye")
            
## ALS PORTION END ##




def main():
    user_choice = input("Do you wish to use random shapes to draw your art piece? Enter Y, N, or Q to quit: ")
    user_decision(user_choice)

main()
