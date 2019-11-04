import time
import pygame

SPACE_PER_LEVEL = 200

class Hanoi:
    def __init__(self, n_levels, base_width, level_height, interval):
        self.n_levels = n_levels
        self.base_width = base_width
        self.level_height = level_height
        self.interval = interval

    def hanoi(self, levels, start, target, n):
        if n == 1:
            levels[target].append(levels[start].pop())
            yield levels
        else:
            aux = 3 - start - target 
            for i in self.hanoi(levels, start, aux, n-1): yield i
            for i in self.hanoi(levels, start, target, 1): yield i
            for i in self.hanoi(levels, aux, target, n-1): yield i

    def pyramid(self, levels, start_x, start_y, level_height, screen):
        for i, levelwidth in enumerate(levels):
            pygame.draw.rect(screen, (255-levelwidth, 255-levelwidth, 255-levelwidth), (start_x + (SPACE_PER_LEVEL - levelwidth)/2 , start_y - level_height * i, levelwidth, level_height))

    def hanoi_display(self):
        levels = [[i * self.base_width for i in reversed(range(1, self.n_levels+1))], [], []]
        positions = self.hanoi(levels, 0, 2, self.n_levels)

        pygame.init()
        screen = pygame.display.set_mode( (650, 650) )
        pygame.display.set_caption('Towers of Hanoi')

        for position in positions:
            screen.fill((0, 0, 0)) 
            for i, pile in enumerate(position):
                self.pyramid(pile, 50 + SPACE_PER_LEVEL*i, 500, self.level_height, screen)
            pygame.display.update()
            time.sleep(self.interval)
        pygame.quit()

if __name__ == "__main__":
    n = int(input("Choose the number of pieces: "))
    hanoi = Hanoi(n, 120//n, 160//n, 0.35)
    hanoi.hanoi_display()    