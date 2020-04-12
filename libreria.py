
import pygame
import math

Ancho = 1200
Alto = 600
Blanco = [255, 255, 255]
Verde = [0, 255, 0]
Rojo = [255, 0, 0]
Negro = [0, 0, 0]
Azul = [0, 0, 255]
Amarillo = [255, 255, 0]
Morado = [128, 0, 128]


def punto(v, p, color=Blanco):
    pygame.draw.circle(v, color, p, 2)


def poligono(v, ls, c=Blanco):
    pygame.draw.polygon(v, c, ls)


def poligonoline(v, ls, c=Negro):
    pygame.draw.polygon(v, c, ls, 3)


def Plano(v, o):
    # v:ventana
    # o:origen
    ox = o[0]
    oy = o[1]
    pygame.draw.line(v, Blanco, [ox, 0], [ox, Alto], 10)
    pygame.draw.line(v, Blanco, [0, oy], [Ancho, oy], 10)


def cart_plano(o, p):  # Cartesianas a pantalla
    xp = p[0] + o[0]
    yp = -p[1] + o[1]
    return [xp, yp]


def vector(v, pos, l):
    pygame.draw.circle(v, [255, 255, 255], l, 2)
    pygame.draw.line(v, [0, 255, 0], l, pos, 10)
    pygame.display.flip()


def pan_cart(o, p):  # o es el origen
    xp = p[0] - o[0]
    yp = -p[1] + o[1]
    return [xp, yp]


def escalamiento(p, s):  # s es el escalamiento
    xp = p[0] * s[0]
    yp = p[1] * s[1]
    return [xp, yp]


def rothor(p, angulo):  # angulo de rotacion
    a = math.radians(angulo)
    xp = p[0] * math.cos(a) + p[1] * math.sin(a)
    yp = -p[0] * math.sin(a) + p[1] * math.cos(a)
    return [int(xp), int(yp)]


def rotanthor(p, angulo):
    a = math.radians(angulo)
    xp = p[0] * math.cos(a) - p[1] * math.sin(a)
    yp = p[0] * math.sin(a) + p[1] * math.cos(a)
    return [int(xp), int(yp)]


def traslacion(punto, traslacion):
    xt = punto[0] + traslacion[0]
    yt = punto[1] + traslacion[1]
    return [xt, yt]


def traslacion_origen(punto, traslacion):  # traslacion en punto que quiero que quede en el origen
    xt = punto[0] - traslacion[0]
    yt = punto[1] - traslacion[1]
    return [xt, yt]


def pitagoricas(v, p, l, r):  # l es la cantidad de lados, r es el radio.
    pygame.draw.circle(v, Blanco, p, r)


def vec_cart_pan(o, vec):
    i = 0
    while i < len(vec):
        vec[i] = cart_plano(o, vec[i])
        i += 1
