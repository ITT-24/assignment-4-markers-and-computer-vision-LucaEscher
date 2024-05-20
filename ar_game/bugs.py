import os
import pyglet
from pyglet import clock
import random

IMG_SCALE = 0.6
GIF_SECONDS = 2
LABEL_COLOR_BLACK = (1, 1, 1, 255)

BUG_SPAWN_INTERVALL = 2
NORMAL_BUG_SPEED = 15

# Init paths
bee_path = os.path.normpath('img/bee.png')
brown_bug_path = os.path.normpath('img/brown_bug.png')
green_bug_path = os.path.normpath('img/green_bug.png')
fly_path = os.path.normpath('img/fly.png')
small_bee_path = os.path.normpath('img/small_bee.png')
collision_gif_path = os.path.normpath('img/smash.gif')

# chatgpt helped in the code generation but major changes were done by me (see chatgpt.md)
class Bugs:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        # load images
        self.bee_img = pyglet.image.load(bee_path)
        self.brown_bug_img = pyglet.image.load(brown_bug_path)
        self.green_bug_img = pyglet.image.load(green_bug_path)
        self.fly_img = pyglet.image.load(fly_path)
        self.small_bee_img = pyglet.image.load(small_bee_path)

        # load gifs
        self.collision_animation = pyglet.resource.animation(collision_gif_path)

        # list to keep track of active bugs
        self.active_bugs = []

    # schedule new bugs to appear every BUG_SPAWN_INTERVALL seconds
    def start_spawner(self):
        clock.schedule_interval(self.spawn_bug, BUG_SPAWN_INTERVALL)
    
    def stop_spawner(self):
        clock.unschedule(self.spawn_bug)
        self.active_bugs.clear()

    def create_sprite(self, img, name):
        sprite = pyglet.sprite.Sprite(img=img)
        sprite.scale = IMG_SCALE
        sprite.name = name
        return sprite

    def spawn_bug(self, dt):
        sprite_images = [
            (self.bee_img, "bee"),
            (self.brown_bug_img, "brown_bug"),
            (self.green_bug_img, "green_bug"),
            (self.fly_img, "fly"),
            (self.small_bee_img, "small_bee")
        ]

        selected_image, name = random.choice(sprite_images)
        selected_sprite = self.create_sprite(selected_image, name)

        # select a random edge and position
        edge = random.choice(['left', 'right', 'top', 'bottom'])
        if edge == 'left':
            selected_sprite.x = -selected_sprite.width - 10
            selected_sprite.y = random.uniform(0, self.window_height - selected_sprite.height)
            selected_sprite.rotation = 0
        elif edge == 'right':
            selected_sprite.x = self.window_width + 10
            selected_sprite.y = random.uniform(0, self.window_height - selected_sprite.height)
            selected_sprite.rotation = 180
        elif edge == 'top':
            selected_sprite.x = random.uniform(0, self.window_width - selected_sprite.width)
            selected_sprite.y = self.window_height + 10
            selected_sprite.rotation = 270
        elif edge == 'bottom':
            selected_sprite.x = random.uniform(0, self.window_width - selected_sprite.width)
            selected_sprite.y = -selected_sprite.height - 10
            selected_sprite.rotation = 90

        self.active_bugs.append((selected_sprite, edge))

    def update(self):
        for sprite, edge in self.active_bugs:
            if edge == 'left':
                sprite.x += NORMAL_BUG_SPEED
            elif edge == 'right':
                sprite.x -= NORMAL_BUG_SPEED
            elif edge == 'top':
                sprite.y -= NORMAL_BUG_SPEED
            elif edge == 'bottom':
                sprite.y += NORMAL_BUG_SPEED

        # remove bugs that have moved out of the window
        self.active_bugs = [bug for bug in self.active_bugs if not self.is_out_of_bounds(bug[0], bug[1])]

    # check if bug is outside of window
    def is_out_of_bounds(self, sprite, edge) -> bool:
        if edge == 'left' and sprite.x > self.window_width + 10:
            return True
        if edge == 'right' and sprite.x < -sprite.width - 10:
            return True
        if edge == 'top' and sprite.y < -sprite.height - 10:
            return True
        if edge == 'bottom' and sprite.y > self.window_height + 10:
            return True
        return False

    def check_collision(self, point):
        x, y = point
        for sprite, _ in self.active_bugs:
            if (sprite.x <= x <= sprite.x + sprite.width and
                    sprite.y <= y <= sprite.y + sprite.height):
                return sprite
        return None

    def destroy_bug(self, sprite):
        self.active_bugs = [bug for bug in self.active_bugs if bug[0] != sprite]

    def draw_running_bugs(self):
        self.update()
        for sprite, _ in self.active_bugs:
            sprite.draw()
