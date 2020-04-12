from libreria import *
import pygame as pg
import figure as fig
import library as lib


def Cart_conv(o, p):
    ptfin = [0, 0]
    ptfin[0] = o[0] + p[0]
    ptfin[1] = o[1] - p[1]
    return ptfin


def Poligono_Lineas(win, color, list):
    pygame.draw.polygon(win, color, list, 3)


def PoligonoSolido(win, color, list):
    pygame.draw.polygon(win, color, list)


def Traslacion(pt, cuant):
    ptfin = [0, 0]
    ptfin[0] = pt[0] + cuant[0]
    ptfin[1] = pt[1] + cuant[1]
    return ptfin


def scale_figure(large):
    angle_for_scaling = 30

    # Down
    p1 = [0, 0]
    p2 = rothor(traslacion(p1, [-large * 2, 0]), angle_for_scaling)
    p3 = rothor(traslacion(p1, [-large * 6, 0]), angle_for_scaling)
    p4 = rothor(traslacion(p1, [-large * 8, 0]), angle_for_scaling)
    p5 = rotanthor(traslacion(p1, [large * 5, 0]), angle_for_scaling)
    p6 = rotanthor(traslacion(p1, [large * 3, 0]), angle_for_scaling)
    p6[1] = p6[1] + large * 2
    p7 = rothor(traslacion(p1, [-large, 0]), angle_for_scaling)
    p7[1] = p7[1] + large * 5
    p8 = rothor(traslacion(p1, [-large * 3, 0]), angle_for_scaling)
    p8[1] = p8[1] + large * 5
    p9 = traslacion(p1, [0, large * 2])
    p10 = rothor(traslacion(p1, [-large * 4, 0]), angle_for_scaling)
    p10[1] = p10[1] + large * 2

    # Middle
    p11 = [0, large * 3]
    p12 = rothor(traslacion(p1, [-large * 2, 0]), angle_for_scaling)
    p12[1] = p12[1] + large * 3
    p13 = rothor(traslacion(p1, [-large * 6, 0]), angle_for_scaling)
    p13[1] = p13[1] + large * 3
    p14 = rothor(traslacion(p1, [-large * 8, 0]), angle_for_scaling)
    p14[1] = p14[1] + large * 3
    p15 = rotanthor(traslacion(p1, [large * 5, 0]), angle_for_scaling)
    p15[1] = p15[1] + large * 3
    p16 = rotanthor(traslacion(p1, [large * 3, 0]), angle_for_scaling)
    p16[1] = p16[1] + large * 5
    p17 = rothor(traslacion(p1, [-large, 0]), angle_for_scaling)
    p17[1] = p17[1] + large * 8
    p18 = rothor(traslacion(p1, [-large * 3, 0]), angle_for_scaling)
    p18[1] = p18[1] + large * 8

    # Up
    p19 = [0, large * 8]
    p20 = rothor(traslacion(p1, [-large * 4, 0]), angle_for_scaling)
    p20[1] = p20[1] + large * 8
    p21 = rotanthor(traslacion(p1, [large * 3, 0]), angle_for_scaling)
    p21[1] = p21[1] + large * 8
    p22 = rothor(traslacion(p1, [-large, 0]), angle_for_scaling)
    p22[1] = p22[1] + large * 11

    p23 = [0, large * 5]
    p24 = rothor(traslacion(p1, [-large * 4, 0]), angle_for_scaling)
    p24[1] = p24[1] + large * 5

    # points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22]
    down = [p2, p1, p5, p6, p7, p8, p4, p3, p10, p9]

    back = [p6, p5, p15, p16, p21, p22, p17, p18, p8, p7]

    izquierda1 = [p2, p9, p23, p12]  # Small
    izquierda2 = [p4, p8, p18, p14]  # Rectangle
    izquierda3 = [p24, p17, p22, p20]  # Square

    derecha1 = [p3, p10, p24, p13]
    derecha2 = [p1, p5, p15, p11]
    derecha3 = [p23, p16, p21, p19]

    arribaa = [p11, p15, p16, p12]
    arribab = [p19, p21, p22, p20]
    arribac = [p13, p17, p18, p14]

    frentea = [p1, p11, p12, p2]
    frenteb = [p9, p19, p20, p10]
    frentec = [p3, p13, p14, p4]

    # Changing to screen
    vec_cart_pan(origin, down)

    vec_cart_pan(origin, back)

    vec_cart_pan(origin, izquierda1)
    vec_cart_pan(origin, izquierda2)
    vec_cart_pan(origin, izquierda3)

    vec_cart_pan(origin, derecha1)
    vec_cart_pan(origin, derecha2)
    vec_cart_pan(origin, derecha3)

    vec_cart_pan(origin, arribaa)
    vec_cart_pan(origin, arribab)
    vec_cart_pan(origin, arribac)

    vec_cart_pan(origin, frentea)
    vec_cart_pan(origin, frenteb)
    vec_cart_pan(origin, frentec)

    # Drawing the figure
    poligono(window, down)

    poligono(window, back, Rojo)

    poligono(window, izquierda1, Verde)
    poligono(window, izquierda2, Verde)
    poligono(window, izquierda3, Verde)

    poligono(window, derecha1, Morado)
    poligono(window, derecha2, Morado)
    poligono(window, derecha3, Morado)

    poligono(window, arribab, Azul)
    poligono(window, arribac, Azul)

    poligono(window, frentea, Amarillo)
    poligono(window, frenteb, Amarillo)
    poligono(window, frentec, Amarillo)

    poligono(window, arribaa, Azul)

    # Lines
    """
    poligonoline(ventana, down)

    poligonoline(ventana, back)

    poligonoline(ventana, izquierda1)
    poligonoline(ventana, izquierda2)
    poligonoline(ventana, izquierda3)
    """
    # Those lines are hide by the perspective

    poligonoline(window, derecha1)
    poligonoline(window, derecha2)
    poligonoline(window, derecha3)

    poligonoline(window, arribaa)
    poligonoline(window, arribab)
    # poligonoline(window,arribac)

    poligonoline(window, frentea)
    poligonoline(window, [frenteb[2], frenteb[3]])
    # poligonoline(ventana,frenteb)
    poligonoline(window, frentec)


if __name__ == '__main__':

    # Pg initialization
    pg.init()

    """
    VIEWS STAFF
    """

    AlzadaA = [-550, -200]
    AlzadaB = Traslacion(AlzadaA, [250, 0])
    AlzadaC = Traslacion(AlzadaB, [0, 150])
    AlzadaD = Traslacion(AlzadaA, [0, 150])
    AlzadaE = Traslacion(AlzadaC, [0, 150])
    AlzadaF = Traslacion(AlzadaE, [-150, 0])
    AlzadaG = Traslacion(AlzadaD, [100, 0])

    AlzadaRectInf = [Cart_conv(lib.cts.Origin, AlzadaA), Cart_conv(lib.cts.Origin, AlzadaB),
                     Cart_conv(lib.cts.Origin, AlzadaC),
                     Cart_conv(lib.cts.Origin, AlzadaD)]
    AlzadaCuaSup = [Cart_conv(lib.cts.Origin, AlzadaC), Cart_conv(lib.cts.Origin, AlzadaE),
                    Cart_conv(lib.cts.Origin, AlzadaF),
                    Cart_conv(lib.cts.Origin, AlzadaG)]

    PerfilA = [-200, -200]
    PerfilB = Traslacion(PerfilA, [100, 0])
    PerfilC = Traslacion(PerfilB, [200, 0])
    PerfilD = Traslacion(PerfilC, [100, 0])
    PerfilE = Traslacion(PerfilD, [0, 150])
    PerfilF = Traslacion(PerfilC, [0, 150])
    PerfilG = Traslacion(PerfilC, [0, 300])
    PerfilH = Traslacion(PerfilB, [0, 300])
    PerfilI = Traslacion(PerfilB, [0, 150])
    PerfilJ = Traslacion(PerfilA, [0, 150])

    PerfilRectanguloIzquierdo = [Cart_conv(lib.cts.Origin, PerfilA), Cart_conv(lib.cts.Origin, PerfilB),
                                 Cart_conv(lib.cts.Origin, PerfilI),
                                 Cart_conv(lib.cts.Origin, PerfilJ)]
    PerfilRectanguloCentral = [Cart_conv(lib.cts.Origin, PerfilB), Cart_conv(lib.cts.Origin, PerfilC),
                               Cart_conv(lib.cts.Origin, PerfilG),
                               Cart_conv(lib.cts.Origin, PerfilH)]
    PerfilRectanguloDerecho = [Cart_conv(lib.cts.Origin, PerfilC), Cart_conv(lib.cts.Origin, PerfilD),
                               Cart_conv(lib.cts.Origin, PerfilE),
                               Cart_conv(lib.cts.Origin, PerfilF)]

    PlantaA = [300, -200]
    PlantaB = Traslacion(PlantaA, [250, 0])
    PlantaC = Traslacion(PlantaB, [0, 100])
    PlantaD = Traslacion(PlantaC, [0, 200])
    PlantaE = Traslacion(PlantaD, [0, 100])
    PlantaF = Traslacion(PlantaA, [0, 400])
    PlantaG = Traslacion(PlantaA, [0, 300])
    PlantaH = Traslacion(PlantaG, [100, 0])
    PlantaI = Traslacion(PlantaC, [-150, 0])
    PlantaJ = Traslacion(PlantaA, [0, 100])

    PlantaRectInf = [Cart_conv(lib.cts.Origin, PlantaA), Cart_conv(lib.cts.Origin, PlantaB),
                     Cart_conv(lib.cts.Origin, PlantaC),
                     Cart_conv(lib.cts.Origin, PlantaJ)]
    PlantaRectCen = [Cart_conv(lib.cts.Origin, PlantaC), Cart_conv(lib.cts.Origin, PlantaD),
                     Cart_conv(lib.cts.Origin, PlantaH),
                     Cart_conv(lib.cts.Origin, PlantaI)]
    PlantaRectSup = [Cart_conv(lib.cts.Origin, PlantaD), Cart_conv(lib.cts.Origin, PlantaE),
                     Cart_conv(lib.cts.Origin, PlantaF),
                     Cart_conv(lib.cts.Origin, PlantaG)]

    """
    WINDOW STAFF
    """
    run = True
    window = lib.new_window("Figure")
    fps = lib.frames_per_second_basics()

    """
    SCALING STAFF
    """

    origin = lib.cts.Origin
    size = 20

    """
    ROTATION STAFF
    """

    # Creating the main figure & its copy
    figure_object = []
    figure_object_rotted = []

    # Appending each piece of figure
    figure_1 = fig.Left_caps
    figure_1 = lib.screen_into_cartesian_for_array(figure_1)
    figure_object.append(figure_1)
    figure_object_rotted.append(figure_1)

    figure_2 = fig.Center_caps
    figure_2 = lib.screen_into_cartesian_for_array(figure_2)
    figure_object.append(figure_2)
    figure_object_rotted.append(figure_2)

    figure_3 = fig.Right_caps
    figure_3 = lib.screen_into_cartesian_for_array(figure_3)
    figure_object.append(figure_3)
    figure_object_rotted.append(figure_3)

    lines_1 = lib.lines_in_figures(figure_object_rotted[0][0], figure_object_rotted[0][1])
    lines_2 = lib.lines_in_figures(figure_object_rotted[1][0], figure_object_rotted[1][1])
    lines_3 = lib.lines_in_figures(figure_object_rotted[2][0], figure_object_rotted[2][1])

    # Creating other var
    direction = 1
    angle = direction

    """
    STAR STAFF
    """

    star_radius = 1000
    star_direction = 2
    star_sides = 7
    star_angle = 2

    figure = lib.regular_figures([star_radius / star_sides, star_radius / star_sides], star_sides)
    rotted_figures = []
    lines = []

    for iterator, value in enumerate(figure):
        rotted_figures.append(lib.screen_into_cartesian(figure[iterator]))

    step = 0
    for iterator, value in enumerate(rotted_figures):
        if step >= len(rotted_figures):
            step = 1
        lines.append(rotted_figures[step])
        step += 2

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    star_sides += 1
                    figure = lib.regular_figures([star_radius / star_sides, star_radius / star_sides], star_sides)
                    rotted_figures = []
                    lines = []

                    for iterator, value in enumerate(figure):
                        rotted_figures.append(lib.screen_into_cartesian(figure[iterator]))

                    step = 0
                    for iterator, value in enumerate(rotted_figures):
                        if step >= len(rotted_figures):
                            step = 1
                        lines.append(rotted_figures[step])
                        step += 2
                if event.key == pg.K_x:
                    star_sides -= 1
                    figure = lib.regular_figures([star_radius / star_sides, star_radius / star_sides], star_sides)
                    rotted_figures = []
                    lines = []

                    for iterator, value in enumerate(figure):
                        rotted_figures.append(lib.screen_into_cartesian(figure[iterator]))

                    step = 0
                    for iterator, value in enumerate(rotted_figures):
                        if step >= len(rotted_figures):
                            step = 1
                        lines.append(rotted_figures[step])
                        step += 2
                if event.key == pg.K_c:
                    star_direction = 2
                if event.key == pg.K_v:
                    star_direction = -2
                if event.key == pg.K_b:
                    for iterator, value in enumerate(figure):
                        rotted_figures[iterator] = lib.cartesian_into_screen(figure[iterator])
                        rotted_figures[iterator] = lib.clockwise(figure[iterator], star_angle)
                        rotted_figures[iterator] = lib.screen_into_cartesian(rotted_figures[iterator])
                    star_angle += star_direction

                    step = 0
                    for iterator, value in enumerate(rotted_figures):
                        if step >= len(rotted_figures):
                            step = 1
                        lines[iterator] = rotted_figures[step]
                        step += 2

                    lib.fill(window)
                    lib.polygons(window, rotted_figures, lib.random_color())
                    lib.polygons(window, lines, lib.random_color())
                if event.key == pg.K_SPACE:
                    # Creating the main figure & its copy
                    figure_object = []

                    # Appending each piece of figure
                    figure_1 = fig.Left
                    figure_1 = lib.screen_into_cartesian_for_array(figure_1)
                    figure_object.append(figure_1)

                    figure_2 = fig.Center
                    figure_2 = lib.screen_into_cartesian_for_array(figure_2)
                    figure_object.append(figure_2)

                    figure_3 = fig.Right
                    figure_3 = lib.screen_into_cartesian_for_array(figure_3)
                    figure_object.append(figure_3)

                    # Drawing issues
                    lib.fill(window)

                    # Figure
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            lib.polygons_filled(window, figure_object[stage][figure_iterated], lib.cts.PALETTE_1[stage])
                if event.key == pg.K_j:
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            lib.polygons_filled(window, figure_object[stage][figure_iterated], lib.cts.PALETTE_1[stage])
                    lib.polygons_filled(window, figure_object[0][3], lib.random_color())
                if event.key == pg.K_k:
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            lib.polygons_filled(window, figure_object[stage][figure_iterated], lib.cts.PALETTE_1[stage])
                    lib.polygons_filled(window, figure_object[1][3], lib.random_color())
                if event.key == pg.K_l:
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            lib.polygons_filled(window, figure_object[stage][figure_iterated], lib.cts.PALETTE_1[stage])
                    lib.polygons_filled(window, figure_object[2][3], lib.random_color())
                if event.key == pg.K_a:
                    lib.fill(window)
                    Poligono_Lineas(window, lib.cts.RED, AlzadaRectInf)
                    Poligono_Lineas(window, lib.cts.RED, AlzadaCuaSup)
                    Poligono_Lineas(window, lib.cts.GREEN, PerfilRectanguloIzquierdo)
                    Poligono_Lineas(window, lib.cts.GREEN, PerfilRectanguloCentral)
                    Poligono_Lineas(window, lib.cts.GREEN, PerfilRectanguloDerecho)
                    Poligono_Lineas(window, lib.cts.BLUE, PlantaRectInf)
                    Poligono_Lineas(window, lib.cts.BLUE, PlantaRectCen)
                    Poligono_Lineas(window, lib.cts.BLUE, PlantaRectSup)

            if event.type == pg.MOUSEBUTTONDOWN:
                # Remaking the main figure
                figure_object = []

                # Appending each piece of figure
                figure_1 = fig.Left_caps
                figure_1 = lib.screen_into_cartesian_for_array(figure_1)
                figure_object.append(figure_1)

                figure_2 = fig.Center_caps
                figure_2 = lib.screen_into_cartesian_for_array(figure_2)
                figure_object.append(figure_2)

                figure_3 = fig.Right_caps
                figure_3 = lib.screen_into_cartesian_for_array(figure_3)
                figure_object.append(figure_3)

                if event.button == 1:
                    angle += direction
                    figure_object_rotted[2][0] = lib.rotting_with_fixed_point(
                        figure_object[2][0],
                        figure_object[2][0][3],
                        angle)
                    figure_object_rotted[2][1] = lib.rotting_with_fixed_point(
                        figure_object[2][1],
                        figure_object[2][1][3],
                        angle)

                    # It rotes each point of the superior cap

                    # Green figure

                    figure_object_rotted[1][0][0] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][0][0],
                        figure_object[1][0][3],
                        angle
                    )
                    figure_object_rotted[1][0][1] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][0][1],
                        figure_object[1][0][3],
                        angle
                    )
                    figure_object_rotted[1][0][2] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][0][2],
                        figure_object[1][0][3],
                        angle
                    )
                    figure_object_rotted[1][0][3] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][0][3],
                        figure_object[1][0][3],
                        angle
                    )

                    # White figure

                    figure_object_rotted[0][0][0] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][0][0],
                        figure_object[2][0][3],
                        angle
                    )
                    figure_object_rotted[0][0][1] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][0][1],
                        figure_object[2][0][3],
                        angle
                    )
                    figure_object_rotted[0][0][2] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][0][2],
                        figure_object[2][0][3],
                        angle
                    )
                    figure_object_rotted[0][0][3] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][0][3],
                        figure_object[2][0][3],
                        angle
                    )

                    # It rotes each point of the inferior cap

                    # Green figure

                    figure_object_rotted[1][1][0] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][1][0],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[1][1][1] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][1][1],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[1][1][2] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][1][2],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[1][1][3] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][1][3],
                        figure_object[2][1][3],
                        angle
                    )

                    # White figure

                    figure_object_rotted[0][1][0] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][1][0],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[0][1][1] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][1][1],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[0][1][2] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][1][2],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[0][1][3] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][1][3],
                        figure_object[2][1][3],
                        angle
                    )
                    lines_1 = lib.lines_in_figures(figure_object_rotted[0][0], figure_object_rotted[0][1])
                    lines_2 = lib.lines_in_figures(figure_object_rotted[1][0], figure_object_rotted[1][1])
                    lines_3 = lib.lines_in_figures(figure_object_rotted[2][0], figure_object_rotted[2][1])

                    # Drawing issues
                    lib.fill(window)
                    # Lines
                    for iterator, value in enumerate(lines_1):
                        lib.polygons(window, lines_1[iterator], lib.cts.PALETTE_1[0])
                    for iterator, value in enumerate(lines_2):
                        lib.polygons(window, lines_2[iterator], lib.cts.PALETTE_1[1])
                    for iterator, value in enumerate(lines_3):
                        lib.polygons(window, lines_3[iterator], lib.cts.PALETTE_1[2])

                    # Caps
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            lib.polygons(window, figure_object_rotted[stage][figure_iterated], lib.cts.PALETTE_1[stage])
                if event.button == 3:
                    angle -= direction
                    figure_object_rotted[2][0] = lib.rotting_with_fixed_point(
                        figure_object[2][0],
                        figure_object[2][0][3],
                        angle)
                    figure_object_rotted[2][1] = lib.rotting_with_fixed_point(
                        figure_object[2][1],
                        figure_object[2][1][3],
                        angle)

                    # It rotes each point of the superior cap

                    # Green figure

                    figure_object_rotted[1][0][0] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][0][0],
                        figure_object[1][0][3],
                        angle
                    )
                    figure_object_rotted[1][0][1] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][0][1],
                        figure_object[1][0][3],
                        angle
                    )
                    figure_object_rotted[1][0][2] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][0][2],
                        figure_object[1][0][3],
                        angle
                    )
                    figure_object_rotted[1][0][3] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][0][3],
                        figure_object[1][0][3],
                        angle
                    )

                    # White figure

                    figure_object_rotted[0][0][0] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][0][0],
                        figure_object[2][0][3],
                        angle
                    )
                    figure_object_rotted[0][0][1] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][0][1],
                        figure_object[2][0][3],
                        angle
                    )
                    figure_object_rotted[0][0][2] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][0][2],
                        figure_object[2][0][3],
                        angle
                    )
                    figure_object_rotted[0][0][3] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][0][3],
                        figure_object[2][0][3],
                        angle
                    )

                    # It rotes each point of the inferior cap

                    # Green figure

                    figure_object_rotted[1][1][0] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][1][0],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[1][1][1] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][1][1],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[1][1][2] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][1][2],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[1][1][3] = lib.rotting_with_fixed_point_single_points(
                        figure_object[1][1][3],
                        figure_object[2][1][3],
                        angle
                    )

                    # White figure

                    figure_object_rotted[0][1][0] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][1][0],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[0][1][1] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][1][1],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[0][1][2] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][1][2],
                        figure_object[2][1][3],
                        angle
                    )
                    figure_object_rotted[0][1][3] = lib.rotting_with_fixed_point_single_points(
                        figure_object[0][1][3],
                        figure_object[2][1][3],
                        angle
                    )
                    lines_1 = lib.lines_in_figures(figure_object_rotted[0][0], figure_object_rotted[0][1])
                    lines_2 = lib.lines_in_figures(figure_object_rotted[1][0], figure_object_rotted[1][1])
                    lines_3 = lib.lines_in_figures(figure_object_rotted[2][0], figure_object_rotted[2][1])
                    # Drawing issues
                    lib.fill(window)
                    # Lines
                    for iterator, value in enumerate(lines_1):
                        lib.polygons(window, lines_1[iterator], lib.cts.PALETTE_1[0])
                    for iterator, value in enumerate(lines_2):
                        lib.polygons(window, lines_2[iterator], lib.cts.PALETTE_1[1])
                    for iterator, value in enumerate(lines_3):
                        lib.polygons(window, lines_3[iterator], lib.cts.PALETTE_1[2])

                    # Caps
                    for stage, section in enumerate(figure_object):
                        for figure_iterated, values in enumerate(figure_object[stage]):
                            lib.polygons(window, figure_object_rotted[stage][figure_iterated], lib.cts.PALETTE_1[stage])
                if event.button == 4:
                    size += 1
                    lib.fill(window)
                    scale_figure(size)
                if event.button == 5:
                    size -= 1
                    lib.fill(window)
                    scale_figure(size)

        lib.frames_per_second(fps, 10)
    pg.quit()
