import math
def select_menu():
    print('Menu')
    print('1. Circle 2.Rectangle')
    print('3.Traingle 4.Exit')
    menu = input('Please choose : ')
    return(menu)
def cal_circle(radius):
    area = math.pi*radius*radius
    return(area)
def cal_reatangle(width, height):
    area = width * height
    return(area)
def cal_triangle(base, height):
    area = 0.5*base*height
    return(area)

def main():
    done = True
    while done:
        print('Program calculate area.')
        menu = select_menu
    if menu == '1':
        radius = int(input('Enter radius :'))
        print("Area of circle = ",cal_circle(radius))
    elif menu == '2':
        width = int(input('Enter width : '))
        height = int(input('Enter height : '))
        print("Area of rectangle = ", cal_reatangle(width,height))
    elif menu == '3':
        base = int(input('Enter base : '))
        height = int(input('Enter height : '))
        print('Area of triangle = ',cal_triangle(base,height))
    elif menu == '4':
        done = False
