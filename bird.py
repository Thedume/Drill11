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
RUN_SPEED_KMPH = 45.0
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed
# fill here
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 15


class Bird:
    image = None

    def __init__(self):
        self.x = random.randint(0, 1550)
        self.y = 90
        self.frame = 0
        self.action = 2
        self.dir = 1
        if (Bird.image == None):
            Bird.image = load_image('bird_animation.png')

    def update(self):
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if self.x >= 1550:
            self.dir = -1
        elif self.x <= 50:
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) % 5 * 183, 338 - (int(self.frame) // 5 * 168), 183, 168, 0, '', self.x, self.y, 80, 60)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) % 5 * 183, 338 - (int(self.frame) // 5 * 168), 183, 168, 0, 'h', self.x, self.y, 80, 60)
