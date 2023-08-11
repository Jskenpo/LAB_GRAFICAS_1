
from gl import Renderer
import shaders

# El tama o del FrameBuffer
width = 960
height = 960

# Se crea el renderizador
rend = Renderer(width, height)

# Le damos los shaders que se utilizar s
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

# Cargamos los modelos que rederizaremos
rend.glLoadModel(filename = "model.obj",
                 textureName = "Textures/model.BMP",
                 translate = (width/4, height/4, 0),
                 rotate = (45, 0, 0),
                 scale = (10,10,10))


# Se renderiza la escena
rend.glRender()

# Se crea el FrameBuffer con la escena renderizada
rend.glFinish("toonshader.bmp")
