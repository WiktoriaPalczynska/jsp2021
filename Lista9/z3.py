import matplotlib.pyplot as plt
import numpy as np
import math

v0 = float(input("Podaj predkosc poczatkowa: "))
alpha = float(input("Podaj kat rzutu: "))
alpha = math.radians(alpha)
g = 9.81  #przyspieszenie ziemskie
v0x = v0 * math.cos(alpha)
v0y = v0 * math.sin(alpha)


h_max = (v0y**2)/(2*g) #max wysokosc
print("Maksymalna wysokosc na jaka wzniesie sie cialo: ", h_max)

x_max = ((v0**2)*math.sin(2*alpha))/g #zasieg rzutu
print("Zasieg rzutu: ", x_max)

czas_calkowity = (2*v0*math.sin(alpha))/g #czas lotu
print("Czas całkowity: ", czas_calkowity)


time = list(np.arange(0, czas_calkowity+0.01, 0.01))
vx_t = [v0x for t in time]
vy_t = [v0y-g*t for t in time]
x_t = [v0x*t for t in time]
y_t = [v0y*t-(g*(t**2)/2) for t in time]
y_x = [(X*math.tan(alpha))-(g*(X**2)/(2*(v0x**2))) for X in x_t]


fig, (px0, px2, p3) = plt.subplots(3) #trzy wykresy

px0.plot(time, vx_t, time, vy_t) #stwórz wykres
px0.set(xlabel="t [s]", ylabel="v [m/s]") #opisy osi
px0.legend(["vx(t)", "vy(t)"])  #legenda
color = 'tab:orange'
px0.set_xlabel('t [s]') 
color1 = 'tab:blue'
px0.set_ylabel('vx [m/s]', color=color1)
px1 = px0.twinx()
px1.set_ylabel('vy [m/s]', color=color)
px1.title.set_text("Predkosc chwilowa w kierunku pionowym i poziomym po czasie t") #tytuł wykresu
px1.grid() #siatka

px2.plot(time, x_t, time, y_t) 
px2.legend(["x(t)", "y(t)"])
color = 'tab:orange'
px2.set_xlabel('t [s]') 
color1 = 'tab:blue'
px2.set_ylabel('x [m]', color=color1)
px3 = px2.twinx()
px3.set_ylabel('y [m]', color=color)
px3.title.set_text("Polozenie od czasu") 
px3.grid() 

p3.plot(x_t, y_x) 
p3.set(ylabel="y [m]", xlabel="x [m]") 
p3.title.set_text("Tor rzutu ukosnego") 
p3.grid() 

plt.tight_layout() #dostosuj dopełnienie między wykresami podrzędnymi i wokół nich
plt.show()