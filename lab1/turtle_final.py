from turtle import * 
import time


speed(10.5)
penup()
#lt(90)
def flower1(x,y,size_flower,size_Kan,pen,color,kan_color):   
   
    penup()
    goto(x,y)
    pendown()
    size_flower = int(size_flower)
    #a = size_Kan
    b = 0
    lt(90)
    for i in range (size_Kan):
        pencolor(kan_color)
        pensize(size_Kan)
        forward(26)
        #x = size_Kan//10
        size_Kan -= 1
        rt(b)
        b += 0.3
    
    
    for i in range (12):
        pencolor("black")
        begin_fill()
        fillcolor(color)
        pensize(pen)
        penup()
        #forward(size_flower)
        pendown()
        forward(size_flower*4)
        lt(15)
        circle(size_flower,180)
        lt(15)
        forward(size_flower*4)
        penup()
        #forward(size_flower)
        pendown()
        lt(180)
        end_fill()

    forward(size_flower)
    lt(90)
    begin_fill()
    fillcolor("yellow")
    circle(size_flower)
    lt(90)
    penup()
    forward(size_flower)
    rt(180)
    end_fill()

def flower2(x,y,size_flower,size_Kan,pen,color,kan_color):   
   
    penup()
    goto(x,y)
    pendown()
    size_flower = int(size_flower)
    #a = size_Kan
    b = 0
    lt(90)
    for i in range (size_Kan):
        pencolor(kan_color)
        pensize(size_Kan)
        forward(26)
        #x = size_Kan//10
        size_Kan -= 1
        rt(b)
        b -= 0.3
    
    
    for i in range (12):
        pencolor("black")
        begin_fill()
        fillcolor(color)
        pensize(pen)
        penup()
        #forward(size_flower)
        pendown()
        forward(size_flower*4)
        lt(15)
        circle(size_flower,180)
        lt(15)
        forward(size_flower*4)
        penup()
        #forward(size_flower)
        pendown()
        lt(180)
        end_fill()

    forward(size_flower)
    lt(90)
    begin_fill()
    fillcolor("yellow")
    circle(size_flower)
    lt(90)
    penup()
    forward(size_flower)
    rt(180)
    end_fill()
      


#x,y,size_flower,size_Kan,pen,color,kan_color 
penup()

flower1(50,-270,30,20,2,"pink","#613333")
lt(3)
flower1(00,-220,22,14,2,"#4CC6CF","#864E4E")
rt(80)
flower1(-30,-230,27,22,2,"#179FA9","#613333")
rt(40)
flower2(20,-260,24,21,2,"#F15DBA","#7D3939")
rt(163)
flower2(70,-290,20,18,3,"#8F65F6","#6C2A2A")


time.sleep(10)


