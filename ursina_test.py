from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

window.fps_counter.enabled = True
window.exit_button.visible = True
window.fullscreen = True


# Create a simple terrain ##
class Terrain(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'plane'
        self.texture = 'grass'
        self.scale = 10
        self.collider = 'mesh'
        self.shader = lit_with_shadows_shader
        self.color = color.green


# Create a player controller
class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 5
        self.jump_height = 2
        self.gravity = 1.5
        self.collider = 'box'
        self.model = 'cube'
        self.color = color.orange


# Create a simple enemy
class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'cube'
        self.color = color.red
        self.scale = 0.5
        self.collider = 'box'
        self.position = (2, 0, 2)
        self.speed = 2

    def update(self):
        # Simple AI to move towards the player
        if distance(self.position, player.position) < 5:
            direction = (player.position - self.position).normalized()
            self.position += direction * self.speed * time.dt
            



# Create the game world
terrain = Terrain()
player = Player()
enemy = Enemy()