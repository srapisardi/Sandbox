from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# --- Window Config ---
window.title = 'Ursina FPS Starter'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = True
window.fps_counter.enabled = True

# --- Environment / Terrain ---
ground = Entity(
    model='plane',
    texture='white_cube',
    texture_scale=(20, 20),
    collider='box',
    scale=(40, 1, 40),
    color=color.gray
)

# --- Sky ---
sky = Sky()

# --- Player ---
player = FirstPersonController()
player.gravity = 1
player.jump_height = 1.5
player.speed = 5
player.cursor.visible = True

# --- Gun (Fake UI-only) ---
gun = Entity(
    parent=camera.ui,
    model='cube',
    color=color.azure,
    scale=(0.2, 0.1, 1),
    position=(0.2, -0.1),
    rotation=(0, -5, 0)
)

# --- Shoot Logic ---
def input(key):
    if key == 'left mouse down':
        shoot()

def shoot():
    bullet = Entity(
        model='sphere',
        color=color.yellow,
        scale=0.1,
        position=player.position + camera.forward * 1.5,
        collider='sphere'
    )
    bullet.direction = camera.forward
    bullet.speed = 20

    def update_bullet():
        bullet.position += bullet.direction * bullet.speed * time.dt
        if distance(bullet.position, player.position) > 50:
            destroy(bullet)

    bullet.update = update_bullet

# --- Run Game ---
app.run()