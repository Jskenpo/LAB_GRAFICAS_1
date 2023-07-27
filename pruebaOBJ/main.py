from gl import Renderer, V2,V3, color
import shaders

width = 1000

height = 700

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


rend.CrearFiguraRelleno(figura1, color(1, 0, 0))   # Colorea la figura 1 de rojo
rend.CrearFiguraRelleno(figura2, color(0, 1, 0))   # Colorea la figura 2 de verde
rend.CrearFiguraRelleno(figura3, color(0, 0, 1))   # Colorea la figura 3 de azul
rend.CrearFiguraRelleno(figura4, color(1, 1, 0))   # Colorea la figura 4 de amarillo
rend.CrearFiguraRelleno(figura5, color(1, 0, 1))   # Colorea la figura 5 de magenta


rend.glFinish("output.bmp")

