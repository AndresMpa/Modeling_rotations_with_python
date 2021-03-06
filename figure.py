# BASIC OBJECT AS 3D FOR PRACTICE

# Front & back

Front = [[0, 0], [0, -100], [-100, -100], [-100, 0]]

Back = [[0, 0], [0, -200], [-100, -200], [-100, -100]]

side = [[0, 0], [0, -250], [-100, -300], [-100, -200]]

Model = [Front, Back, side]

########################################################################################################################
########################################################################################################################

# FIGURE AS A 3D OBJECT

Front_1 = [[0, 0], [0, 60], [-34, 79], [-34, 19]]
Right_1 = [[86, 49], [86, 109], [0, 60], [0, 0]]
Left_1 = [[51, 69], [51, 129], [-34, 79], [-34, 19]]
Up_1 = [[86, 109], [51, 129], [-34, 79], [0, 60]]
Down_1 = [[86, 49], [51, 69], [-34, 19], [0, 0]]
Back_1 = [[51, 69], [51, 129], [86, 109], [86, 49]]

Right = [Front_1, Right_1, Left_1, Up_1, Down_1, Back_1]
Right_caps = [Up_1, Down_1]

Front_2 = [[0, 40], [0, 160], [-69, 199], [-69, 79]]
Right_2 = [[51, 69], [51, 189], [0, 160], [0, 40]]
Left_2 = [[-17, 109], [-17, 229], [-69, 199], [-69, 79]]
Up_2 = [[51, 189], [-17, 229], [-69, 199], [0, 160]]
Down_2 = [[51, 69], [-17, 109], [-69, 79], [0, 40]]
Back_2 = [[51, 69], [51, 189], [-17, 229], [-17, 109]]

Center = [Front_2, Right_2, Left_2, Up_2, Down_2, Back_2]
Center_caps = [Up_2, Down_2]

Front_3 = [[-103, 59], [-103, 119], [-138, 139], [-138, 79]]
Right_3 = [[-17, 109], [-17, 169], [-103, 119], [-103, 59]]
Left_3 = [[-51, 129], [-51, 189], [-138, 139], [-138, 79]]
Up_3 = [[-17, 169], [-51, 189], [-138, 139], [-103, 119]]
Down_3 = [[-17, 109], [-51, 129], [-138, 79], [-103, 59]]
Back_3 = [[-17, 109], [-17, 169], [-51, 189], [-51, 129]]

Left = [Front_3, Right_3, Left_3, Up_3, Down_3, Back_3]
Left_caps = [Up_3, Down_3]
