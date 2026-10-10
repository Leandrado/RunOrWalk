import pygame as py
import random

py.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
window = py.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
py.display.set_caption("Run or walk in 'Rain?'")

AWNING_WIDTH = 120
AWNING_HEIGHT = 40
SPAWN_MIN_X = AWNING_WIDTH + 9
SPAWN_MAX_X = WINDOW_WIDTH - AWNING_WIDTH + 9

font = py.font.SysFont("Arial", 24)

class Drop:
    def __init__(self, pos_x):
        self.size = 3
        self.y = 0
        self.x = pos_x

    def get_down(self):
        self.y += self.size
        return self.y
    
    def draw(self, surface):
        py.draw.rect(surface, (0, 0, 255), (self.x, self.y, self.size, self.size * 2))

    def get_rect(self):
        return py.Rect(self.x, self.y, self.size, self.size * 2)

class Person:
    def __init__(self):
        self.width = 30
        self.height = 60
        self.color = (255, 0, 0)
        
        # Cria a superfície base do personagem para podermos rotacionar
        self.surface = py.Surface((self.width, self.height), py.SRCALPHA)
        self.surface.fill(self.color)
        
        self.reset()

    def reset(self):
        self.x = 10
        self.y = WINDOW_HEIGHT - self.height - 10
        self.vel_x = 0

    def move(self):
        self.x += self.vel_x
        if self.x > WINDOW_WIDTH - self.width:
            self.x = WINDOW_WIDTH - self.width
            self.vel_x = 0

    def draw(self, surface):
        if self.vel_x == 6:
            # Inclina o personagem para a frente (sentido horário = ângulo negativo)
            rotated_surface = py.transform.rotate(self.surface, -15)
            # Ajusta a posição para não dar trancos devido à mudança de tamanho da superfície rotacionada
            new_rect = rotated_surface.get_rect(bottomleft=(self.x, self.y + self.height))
            surface.blit(rotated_surface, new_rect.topleft)
        else:
            # Desenha normalmente em pé se estiver andando ou parado
            surface.blit(self.surface, (self.x, self.y))

    def get_rect(self):
        return py.Rect(self.x, self.y, self.width, self.height)


person = Person()
drop_list = []
drop_count = 0
clock = py.time.Clock()
end = False

spawn_gap = 12
variations = [-9, -6, -3, 0, 3, 6, 9]

while not end:
    clock.tick(60)
    
    for event in py.event.get():
        if event.type == py.QUIT:
            end = True

        if event.type == py.KEYDOWN:
            if event.key == py.K_1:
                person.vel_x = 3
            if event.key == py.K_2:
                person.vel_x = 6
            if event.key == py.K_SPACE:
                person.reset()
                drop_count = 0

    row_shift = random.choice(variations)
    for x in range(SPAWN_MIN_X, SPAWN_MAX_X - spawn_gap, spawn_gap):
        drop_list.append(Drop(x + row_shift))

    person.move()

    for drop in drop_list[:]:
        current_height = drop.get_down()
        
        if drop.get_rect().colliderect(person.get_rect()):
            drop_count += 1
            drop_list.remove(drop)
        elif current_height > WINDOW_HEIGHT:
            drop_list.remove(drop)

    window.fill((255, 255, 255))
    
    py.draw.rect(window, (150, 150, 150), (0, 0, AWNING_WIDTH, AWNING_HEIGHT))
    py.draw.rect(window, (150, 150, 150), (WINDOW_WIDTH - AWNING_WIDTH, 0, AWNING_WIDTH, AWNING_HEIGHT))
    
    person.draw(window)
    for drop in drop_list:
        drop.draw(window)

    count_text = font.render(f"Drops: {drop_count}", True, (0, 0, 0))
    window.blit(count_text, (10, AWNING_HEIGHT + 10))

    py.display.flip()

py.quit()
