from bugs import Bugs
import pyglet
from pyglet import clock

LABEL_COLOR_BLACK = (1, 1, 1, 255)

GAME_TIME = 60

NORMAL_BUG_PTS = 10
SMALL_BEE_PTS = 10
BEE_PTS = 20


class BugSmasher:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        self.bugs = Bugs(window_width, window_height)

        self.score = 0
        self.game_state = 0
        self.game_time = GAME_TIME

        clock.schedule_interval(self.update_game_time, 1)

    def update(self):
        match(self.game_state):
            case 0:
                start_label = pyglet.text.Label(text='Press SPACE to smash Bugs!',
                                                font_name='ARIAL',
                                                font_size=18,
                                                bold=True,
                                                x=self.window_width//2, y=self.window_height//2,
                                                anchor_x='center', anchor_y='center',
                                                )
                start_label.color = LABEL_COLOR_BLACK
                start_label.draw()

                description_label = pyglet.text.Label(text='Kill bugs but don\'t kill the bees (minus points)',
                                                      font_name='ARIAL',
                                                      font_size=14,
                                                      bold=True,
                                                      x=self.window_width//2, y=self.window_height//3,
                                                      anchor_x='center', anchor_y='center',
                                                      )
                description_label.color = LABEL_COLOR_BLACK
                description_label.draw()

                small_bee_sprite = self.bugs.create_sprite(self.bugs.small_bee_img, 'bee')
                small_bee_sprite.x = self.window_width / 2 - small_bee_sprite.width / 2
                small_bee_sprite.y = self.window_height // 1.8
                small_bee_sprite.draw()

            case 1:
                score_label = pyglet.text.Label(text=f'Score: {self.score}',
                                                font_name='ARIAL',
                                                font_size=16,
                                                bold=True,
                                                x=self.window_width//2, y=self.window_height//1.05,
                                                anchor_x='center', anchor_y='center',
                                                )
                score_label.color = LABEL_COLOR_BLACK
                score_label.draw()

                time_label = pyglet.text.Label(text=f'Remaining Time: {self.game_time}',
                                               font_name='ARIAL',
                                               font_size=16,
                                               bold=True,
                                               x=self.window_width // 1.25, y=self.window_height//1.05,
                                               anchor_x='center', anchor_y='center',
                                               )
                time_label.color = LABEL_COLOR_BLACK
                time_label.draw()

                self.bugs.draw_running_bugs()

            case 2:
                small_bee_sprite = self.bugs.create_sprite(self.bugs.green_bug_img, 'green_bug')
                small_bee_sprite.x = self.window_width / 2 - small_bee_sprite.width / 2
                small_bee_sprite.y = self.window_height // 1.8
                small_bee_sprite.draw()
                
                end_label = pyglet.text.Label(text=f'Final Score: {self.score}',
                                              font_name='ARIAL',
                                              font_size=24,
                                              bold=True,
                                              x=self.window_width//2, y=self.window_height//2,
                                              anchor_x='center', anchor_y='center',
                                              )
                end_label.color = LABEL_COLOR_BLACK
                end_label.draw()
                
                restart_label = pyglet.text.Label(text=f'Press R to restart!',
                                              font_name='ARIAL',
                                              font_size=16,
                                              bold=True,
                                              x=self.window_width//2, y=self.window_height//3,
                                              anchor_x='center', anchor_y='center',
                                              )
                restart_label.color = LABEL_COLOR_BLACK
                restart_label.draw()

    def adjust_score(self, sprite):
        match(sprite.name):
            case 'bee':
                self.score -= BEE_PTS
            case 'small_bee':
                self.score -= SMALL_BEE_PTS
            case 'brown_bug' | 'green_bug' | 'fly':
                self.score += NORMAL_BUG_PTS

    def update_game_time(self, dt):
        if self.game_state == 1:
            self.game_time -= 1
            if self.game_time <= 0:
                self.game_state = 2
                self.bugs.stop_spawner()
                clock.unschedule(self.update_game_time)

    def restart(self):
        self.bugs.active_bugs = []
        self.game_time = GAME_TIME
        self.score = 0
        self.game_state = 0
        self.bugs.start_spawner()
        clock.schedule_interval(self.update_game_time, 1)
    
    def run(self):
        pyglet.app.run()
