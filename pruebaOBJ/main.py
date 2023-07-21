from gl import Renderer, V2,V3, color
import shaders

width = 2000

height = 1000

rend = Renderer(width,height)

rend.glClearColor(0, 0, 0)
rend.glClear()

figura1 = [(165, 380), (185, 360), (180, 330),
           (207, 345), (233, 330), (230, 360),
           (250, 380), (220, 385), (205, 410),
           (193, 383)]

figura2 = [(321, 335), (288, 286), (339, 251), (374, 302)]

figura3  = [(377, 249), (411, 197), (436, 249)]

figura4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
            (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
            (597, 215), (552, 214), (517, 144), (466, 180)]

figura5 = [(682, 175), (708, 120), (735, 148), (739, 170)]


rend.CrearFiguraLineas(figura1)
rend.CrearFiguraLineas(figura2)
rend.CrearFiguraLineas(figura3)
rend.CrearFiguraLineas(figura4)
rend.CrearFiguraLineas(figura5)

rend.glFinish("output.bmp")

