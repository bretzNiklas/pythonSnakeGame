import pygame
from pygame.locals import *

import game_classes



def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    MOVE_TIME = 50
    FOOD_SPAWN_TIME = 5000
    FPS = 60


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 36)

    last_move_call = pygame.time.get_ticks()
    last_food_call = pygame.time.get_ticks()

    playing_field = game_classes.PlayingField(20)

    run = True

    i = 0

    while run:
        current_time = pygame.time.get_ticks()

        screen.fill(game_classes.Theme.DARK.value)




        for row in playing_field.fields:
            for field in row:
                pygame.draw.rect(screen, field.field_state.value, field.rect)

        score_text = font.render(f'Score: {playing_field.score}', True, (255, 255, 255))
        screen.blit(score_text, (650, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    playing_field.setDirection(game_classes.Direction.UP)
                elif event.key == K_DOWN:
                    playing_field.setDirection(game_classes.Direction.DOWN)
                elif event.key == K_LEFT:
                    playing_field.setDirection(game_classes.Direction.LEFT)
                elif event.key == K_RIGHT:
                    playing_field.setDirection(game_classes.Direction.RIGHT)


        if current_time - last_move_call >= MOVE_TIME:
            game_lost = playing_field.moveSnakeOne()
            last_move_call = current_time

            if game_lost:
                run = False

        if current_time - last_food_call >= FOOD_SPAWN_TIME:
            playing_field.spawnFood()
            last_food_call = current_time

        pygame.display.update()

        clock.tick(FPS)



if __name__ == '__main__':
    main()
