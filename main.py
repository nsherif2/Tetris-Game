import pygame,sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

def main():
    while True:
        handle_events()

        # Drawing
        draw_screen()
        pygame.display.update()
        clock.tick(60)

def handle_events():
    """
    Handles all game events such as keypresses, quitting the game, and game updates.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset()
            else:
                handle_keypress(event)

        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

def handle_keypress(event):
    """
    Handles keypress events when the game is active.
    """
    if event.key == pygame.K_LEFT:
        game.move_left()
    elif event.key == pygame.K_RIGHT:
        game.move_right()
    elif event.key == pygame.K_DOWN:
        game.move_down()
        game.update_score(0, 1)  # Add points for moving down
    elif event.key == pygame.K_UP:
        game.rotate()

def draw_screen():
    """
    Draws the entire game screen, including the game grid, score, and game over screen.
    """
    screen.fill(Colors.dark_blue)

    # Draw Score and Next Labels
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    # Draw the score value
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, 
                                                                  centery=score_rect.centery))

    # Draw the next block area
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    # Draw the game grid
    game.draw(screen)

    # Display game over message if applicable
    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))

if __name__ == "__main__":
    main()
    
# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			sys.exit()
# 		if event.type == pygame.KEYDOWN:
# 			if game.game_over == True:
# 				game.game_over = False
# 				game.reset()
# 			if event.key == pygame.K_LEFT and game.game_over == False:
# 				game.move_left()
# 			if event.key == pygame.K_RIGHT and game.game_over == False:
# 				game.move_right()
# 			if event.key == pygame.K_DOWN and game.game_over == False:
# 				game.move_down()
# 				game.update_score(0, 1)
# 			if event.key == pygame.K_UP and game.game_over == False:
# 				game.rotate()
# 		if event.type == GAME_UPDATE and game.game_over == False:
# 			game.move_down()

# 	#Drawing
# 	score_value_surface = title_font.render(str(game.score), True, Colors.white)

# 	screen.fill(Colors.dark_blue)
# 	screen.blit(score_surface, (365, 20, 50, 50))
# 	screen.blit(next_surface, (375, 180, 50, 50))

# 	if game.game_over == True:
# 		screen.blit(game_over_surface, (320, 450, 50, 50))

# 	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
# 	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
# 		centery = score_rect.centery))
# 	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
# 	game.draw(screen)

# 	pygame.display.update()
# 	clock.tick(60)