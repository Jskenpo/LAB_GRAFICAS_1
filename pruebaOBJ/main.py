from gl import Renderer, V2,V3, color
import shaders

width = 3000

height = 1500

rend = Renderer(width,height)

rend.glClearColor(0, 0, 0)
rend.glClear()


rend.glLine(V2(165, 380), V2(185, 360))
rend.glLine(V2(185, 360), V2(180, 330))
rend.glLine(V2(180, 330), V2(207, 345))
rend.glLine(V2(207, 345), V2(233, 330))
rend.glLine(V2(233, 330), V2(230, 360))
rend.glLine(V2(230, 360), V2(250, 380))
rend.glLine(V2(250, 380), V2(220, 385))
rend.glLine(V2(220, 385), V2(205, 410))
rend.glLine(V2(205, 410), V2(193, 383))
rend.glLine(V2(193, 383), V2(165, 380))

rend.glFinish("output.bmp")