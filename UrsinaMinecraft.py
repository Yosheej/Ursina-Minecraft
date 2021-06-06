from ursina import *  
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
sky_texture = load_texture('assets/sky.png')
punch_sound = Audio('assets/assets_punch_sound', loop = False, autoplay = False)

window.fps_counter.enabled = False

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(parent = scene, position = position, model = 'assets/block', origin_y = 0.5, color = color.color(0,0,random.uniform(0.8,1)), highlight_color = color.lime, scale = 0.5)
        
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                voxel = Voxel(position = self.position + mouse.normal)

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(parent = scene, model = 'sphere', texture = sky_texture, scale = 150, double_sided = True)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x, 0, z))

player = FirstPersonController()
sky = Sky()

app.run()