from pico2d import get_time, load_image, load_font, clamp,  SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from ball import Ball, BigBall
import random
import game_world
import game_framework

# state event check
# ( state event type, event value )

# Boy Run Speed
# fill here
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed
# fill here
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:
    image = None

    def __init__(self):
        self.x = random.randint(0, 1550)
        self.y = 90
        self.frame = 0
        self.action = 3
        self.dir = 1
        if (Bird.image == None):
            Bird.image = load_image('bird_animation.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, self.action * 100, 100, 100, self.x, self.y)
