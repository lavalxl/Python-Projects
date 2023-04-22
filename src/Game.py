import pygame
import src.Wall as Wall
import src.constants as const
from src.Background import MovingBackground
from src.Shop import Shop
from src.Snake import Snake
import src.Food as Food


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((const.WIDTH + 10, const.HEIGHT + 10))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Snake")
        self.running = True
        self.all_sprites = None
        self.foods = None
        self.bonuses = None
        self.buffed = False
        self.walls = None
        self.snake = None
        self.shop = Shop()
        self.background = MovingBackground((1, 1))
        self.text_color = const.BLACK
        self.state = 'menu'
        self.mode = 0
        self.record = 0

    def display_text(self, message, font, color, size, x, y):
        txt_surf = pygame.font.Font(font, size).render(message, True, color)
        txt_rect = txt_surf.get_rect()
        txt_rect.center = [x, y]
        self.window.blit(txt_surf, txt_rect)

    def general_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            self.running = False

    def menu_cycle(self):
        while self.running:
            self.clock.tick(const.FPS)
            self.background.draw(self.window)
            self.display_text("Snake Game", const.ARIAL, self.text_color, 70, const.WIDTH / 2, 100)
            self.display_text("Eat the apples to grow", const.ARIAL, self.text_color, 40, const.WIDTH / 2, 150)
            self.display_text("Use arrows or WASD to move", const.ARIAL, self.text_color, 40, const.WIDTH / 2, 200)
            self.display_text("Record score:" + str(self.record), const.ARIAL, self.text_color, 30, const.WIDTH / 2,
                              300)
            self.display_text("Press SPACE to start", const.ARIAL, self.text_color, 25, const.WIDTH / 2, 390)
            self.display_text("Press S to visit shop", const.ARIAL, self.text_color, 25, const.WIDTH / 2, 420)
            pygame.display.update()

            for event in pygame.event.get():
                self.general_event(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_g:
                        self.state = 'game'
                        self.choose_mode()
                    elif event.key == pygame.K_s:
                        self.state = 'shop'
                        self.shop_cycle()

    def choose_mode(self):
        while self.running:
            self.clock.tick(const.FPS)
            self.background.draw(self.window)
            self.display_text("Press number button to choose mode:", const.ARIAL, self.text_color,
                              40, const.WIDTH / 2, 140)
            self.display_text("1. standard snake", const.ARIAL, self.text_color, 30, const.WIDTH / 2, 200)
            self.display_text("2. vertical", const.ARIAL, self.text_color, 30, const.WIDTH / 2, 240)
            self.display_text("3. horizontal", const.ARIAL, self.text_color, 30, const.WIDTH / 2, 280)
            self.display_text("4. cross", const.ARIAL, self.text_color, 30, const.WIDTH / 2, 320)
            self.display_text("5. stairs", const.ARIAL, self.text_color, 30, const.WIDTH / 2, 360)
            self.display_text("6. I", const.ARIAL, self.text_color, 30, const.WIDTH / 2, 400)
            self.display_text("Press M to go back to menu", const.ARIAL, self.text_color, 25, const.WIDTH / 2, 450)
            pygame.display.update()

            for event in pygame.event.get():
                self.general_event(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.mode = 0
                        self.game_initialization()
                    elif event.key == pygame.K_2:
                        self.mode = 1
                        self.game_initialization()
                    elif event.key == pygame.K_3:
                        self.mode = 2
                        self.game_initialization()
                    elif event.key == pygame.K_4:
                        self.mode = 3
                        self.game_initialization()
                    elif event.key == pygame.K_5:
                        self.mode = 4
                        self.game_initialization()
                    elif event.key == pygame.K_6:
                        self.mode = 5
                        self.game_initialization()
                    elif event.key == pygame.K_m:
                        self.state = 'menu'
                        self.menu_cycle()

    def shop_cycle(self):
        while self.running:
            self.clock.tick(const.FPS)
            if self.shop.current_background % 2 == 0:
                self.text_color = const.BLACK
            else:
                self.text_color = const.WHITE
            self.background.draw(self.window)
            self.display_text("Shop", const.ARIAL, self.text_color, 50, const.WIDTH / 2, 100)
            self.display_text("Press number button to change snake skin or background:", const.ARIAL, self.text_color,
                              25, const.WIDTH / 2, 140)
            self.display_text("1. green snake", const.ARIAL, self.text_color, 25, const.WIDTH / 2, 170)
            self.display_text("2. star wars snake", const.ARIAL, self.text_color, 25, const.WIDTH / 2, 200)
            self.display_text("3. blue snake", const.ARIAL, self.text_color, 25, const.WIDTH / 2, 230)
            self.display_text("4. sand background", const.ARIAL, self.text_color, 25, const.WIDTH / 2, 260)
            self.display_text("5. anime background", const.ARIAL, self.text_color, 25, const.WIDTH / 2, 290)
            self.display_text("6. ice background", const.ARIAL, self.text_color, 25, const.WIDTH / 2, 320)
            self.display_text("Press S to go back to menu", const.ARIAL, self.text_color, 25, const.WIDTH / 2, 420)
            pygame.display.update()

            for event in pygame.event.get():
                self.general_event(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.shop.current_skin = 0
                    elif event.key == pygame.K_2:
                        self.shop.current_skin = 1
                    elif event.key == pygame.K_3:
                        self.shop.current_skin = 2
                    elif event.key == pygame.K_4:
                        self.shop.current_background = 0
                        self.background.image = self.shop.backgrounds[self.shop.current_background]
                    elif event.key == pygame.K_5:
                        self.shop.current_background = 1
                        self.background.image = self.shop.backgrounds[self.shop.current_background]
                    elif event.key == pygame.K_6:
                        self.shop.current_background = 2
                        self.background.image = self.shop.backgrounds[self.shop.current_background]
                    elif event.key == pygame.K_s:
                        self.state = 'menu'
                        self.menu_cycle()

    def food_generation(self, food_type):
        if food_type == 'score_food':
            self.foods = Food.generation(food_type, self.walls)
            self.all_sprites.add(self.foods)
        else:
            self.bonuses = Food.generation(food_type, self.walls)
            self.all_sprites.add(self.bonuses)

    def game_initialization(self):
        self.all_sprites = pygame.sprite.Group()
        self.snake = Snake(self.shop.snake_skins[self.shop.current_skin][0],
                           self.shop.snake_skins[self.shop.current_skin][1])
        self.all_sprites.add(self.snake)

        self.walls = Wall.wall_generation(self.mode)
        self.all_sprites.add(self.walls)

        self.food_generation('score_food')

        self.game_cycle()

    def pause_cycle(self):
        while self.running:
            self.display_text("Paused", const.ARIAL, self.text_color, 30, const.WIDTH / 2, const.HEIGHT / 2 - 35)
            self.display_text("Press P to continue", const.ARIAL, self.text_color, 30, const.WIDTH / 2,
                              const.HEIGHT / 2 + 60)
            self.window.blit(const.pause, [const.WIDTH / 2 - 15, const.HEIGHT / 2])
            pygame.display.update()

            for event in pygame.event.get():
                self.general_event(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    return

    def game_over_cycle(self):
        while self.running:
            const.FPS = 30
            self.buffed = False
            self.clock.tick(const.FPS)
            if self.snake.score > self.record:
                self.record = self.snake.score
            self.background.draw(self.window)
            self.display_text("You Died", const.TNR, const.RED, 100, const.WIDTH / 2, 180)
            self.display_text("Press SPACE to play again", const.ARIAL, self.text_color, 30, const.WIDTH / 2, 250)
            self.display_text("Press M to go to menu", const.ARIAL, self.text_color, 30, const.WIDTH / 2, 280)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.general_event(event)
                    if event.key == pygame.K_SPACE or event.key == pygame.K_g:
                        self.state = 'game'
                        self.game_initialization()
                    elif event.key == pygame.K_m:
                        self.state = 'menu'
                        self.menu_cycle()

    def game_cycle(self):
        while self.running:
            self.clock.tick(const.FPS)

            for event in pygame.event.get():
                self.general_event(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.state = 'pause'
                    self.pause_cycle()

            self.background.draw(self.window)
            self.walls.draw(self.window)
            self.all_sprites.update()
            self.all_sprites.draw(self.window)
            self.display_text("Score: " + str(self.snake.score), const.ARIAL, self.text_color, 20, 70, 40)

            head = [self.snake.rect.x, self.snake.rect.y]
            self.snake.pieces.append(head)

            if self.snake.length < len(self.snake.pieces):
                del self.snake.pieces[0]

            for i in self.snake.pieces[:-1]:
                if i == head:
                    self.state = 'game_over'
                    self.game_over_cycle()

            if self.snake.boarder_collisions():
                self.state = 'game_over'
                self.game_over_cycle()

            self.snake.draw(self.window)

            if pygame.sprite.spritecollide(self.snake, self.walls, True):
                self.state = 'game_over'
                self.game_over_cycle()

            if pygame.sprite.spritecollide(self.snake, self.foods, True):
                self.snake.collision('score')
                self.food_generation('score_food')

            if self.snake.score % 10 == 0 and not self.buffed:
                self.food_generation('bonus')
                self.buffed = self.bonuses.sprites()[0].id

            if self.buffed and pygame.sprite.spritecollide(self.snake, self.bonuses, True):
                self.snake.collision(self.buffed)
                self.buffed = False

            for x in range(0, const.WIDTH + 6, 5):
                self.window.blit(const.brick, (x, -10))
                self.window.blit(const.brick, (x, const.HEIGHT))
            for x in range(0, const.HEIGHT + 5, 5):
                self.window.blit(const.brick, (-10, x))
                self.window.blit(const.brick, (const.WIDTH, x))

            pygame.display.update()

    def play(self):
        pygame.mixer.music.load("Images/sonic.mp3")
        pygame.mixer.music.play(-1)
        self.menu_cycle()
