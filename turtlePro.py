# import turtle library
import turtle

my_wn = turtle.Screen()
my_wn.bgcolor("black")
my_wn.title("Turtle")
turtle.shape("turtle")
my_pen = turtle.Turtle()
my_pen.color("red")


def my_sqrfunction(size):
    for i in range(5):
        my_pen.fd(size)
        my_pen.right(45)
        size = size - 5


my_sqrfunction(146)
my_sqrfunction(126)
my_sqrfunction(106)
my_sqrfunction(86)
my_sqrfunction(66)
my_sqrfunction(46)
my_sqrfunction(26)

turtle.done()
