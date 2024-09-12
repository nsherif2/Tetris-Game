import random
import pygame
from grid import Grid
from blocks import *

class Game:
    def __init__(self):
        """
        Initializes the Game with a grid, a list of blocks, current and next blocks, 
        and game state variables like score and game over status.
        """
        self.grid = Grid()
        self.blocks = [IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

        # Load sounds
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")
        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared: int, move_down_points: int) -> None:
        """
        Updates the score based on lines cleared and points for moving the block down.
        """
        score_table = {1: 100, 2: 300, 3: 500}
        self.score += score_table.get(lines_cleared, 0) + move_down_points

    def get_random_block(self) -> Block:
        """
        Returns a random block object from the list of available blocks.
        """
        return random.choice(self.blocks)()

    def move_left(self) -> None:
        self._try_move(0, -1)

    def move_right(self) -> None:
        self._try_move(0, 1)

    def move_down(self) -> None:
        if not self._try_move(1, 0):
            self.lock_block()

    def _try_move(self, row_change: int, col_change: int) -> bool:
        """
        Attempts to move the current block by the specified row and column changes.
        If the move is not valid, the block returns to its original position.

        Args:
            row_change (int): Change in row position.
            col_change (int): Change in column position.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        self.current_block.move(row_change, col_change)
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(-row_change, -col_change)
            return False
        return True

    def lock_block(self) -> None:
        """
        Locks the current block in place on the grid and spawns the next block.
        """
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        
        self.current_block = self.next_block
        self.next_block = self.get_random_block()

        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)

        if not self.block_fits():
            self.game_over = True

    def reset(self) -> None:
        """
        Resets the game to its initial state.
        """
        self.grid.reset()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.game_over = False

    def block_fits(self) -> bool:
        """
        Checks if the current block fits in the grid without overlapping other blocks.

        Returns:
            bool: True if the block fits, False otherwise.
        """
        tiles = self.current_block.get_cell_positions()
        return all(self.grid.is_empty(tile.row, tile.column) for tile in tiles)

    def rotate(self) -> None:
        """
        Attempts to rotate the current block. If the rotation is invalid, it is undone.
        """
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def block_inside(self) -> bool:
        """
        Checks if the current block is within the grid boundaries.

        Returns:
            bool: True if the block is inside the grid, False otherwise.
        """
        tiles = self.current_block.get_cell_positions()
        return all(self.grid.is_inside(tile.row, tile.column) for tile in tiles)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the current game state, including the grid, the current block, and the next block preview.

        Args:
            screen (pygame.Surface): The screen surface to draw on.
        """
        # Draw the main grid and current block
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        # Draw the next block in the preview area
        next_block_offset_x, next_block_offset_y = self._get_next_block_position()
        self.next_block.draw(screen, next_block_offset_x, next_block_offset_y)

    def _get_next_block_position(self) -> tuple:
        """
        Determines the (x, y) position for drawing the next block preview based on the block type.

        Returns:
            tuple: A tuple containing the x and y coordinates.
        """
        if self.next_block.id == 3:  # IBlock
            return 255, 290
        elif self.next_block.id == 4:  # OBlock
            return 255, 280
        else:
            return 270, 270


# from grid import Grid
# from blocks import *
# import random
# import pygame

# class Game:
# 	def __init__(self):
# 		self.grid = Grid()
# 		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
# 		self.current_block = self.get_random_block()
# 		self.next_block = self.get_random_block()
# 		self.game_over = False
# 		self.score = 0
# 		self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
# 		self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")

# 		pygame.mixer.music.load("Sounds/music.ogg")
# 		pygame.mixer.music.play(-1)

# 	def update_score(self, lines_cleared, move_down_points):
# 		if lines_cleared == 1:
# 			self.score += 100
# 		elif lines_cleared == 2:
# 			self.score += 300
# 		elif lines_cleared == 3:
# 			self.score += 500
# 		self.score += move_down_points

# 	def get_random_block(self):
# 		if len(self.blocks) == 0:
# 			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
# 		block = random.choice(self.blocks)
# 		self.blocks.remove(block)
# 		return block

# 	def move_left(self):
# 		self.current_block.move(0, -1)
# 		if self.block_inside() == False or self.block_fits() == False:
# 			self.current_block.move(0, 1)

# 	def move_right(self):
# 		self.current_block.move(0, 1)
# 		if self.block_inside() == False or self.block_fits() == False:
# 			self.current_block.move(0, -1)

# 	def move_down(self):
# 		self.current_block.move(1, 0)
# 		if self.block_inside() == False or self.block_fits() == False:
# 			self.current_block.move(-1, 0)
# 			self.lock_block()

# 	def lock_block(self):
# 		tiles = self.current_block.get_cell_positions()
# 		for position in tiles:
# 			self.grid.grid[position.row][position.column] = self.current_block.id
# 		self.current_block = self.next_block
# 		self.next_block = self.get_random_block()
# 		rows_cleared = self.grid.clear_full_rows()
# 		if rows_cleared > 0:
# 			self.clear_sound.play()
# 			self.update_score(rows_cleared, 0)
# 		if self.block_fits() == False:
# 			self.game_over = True

# 	def reset(self):
# 		self.grid.reset()
# 		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
# 		self.current_block = self.get_random_block()
# 		self.next_block = self.get_random_block()
# 		self.score = 0

# 	def block_fits(self):
# 		tiles = self.current_block.get_cell_positions()
# 		for tile in tiles:
# 			if self.grid.is_empty(tile.row, tile.column) == False:
# 				return False
# 		return True

# 	def rotate(self):
# 		self.current_block.rotate()
# 		if self.block_inside() == False or self.block_fits() == False:
# 			self.current_block.undo_rotation()
# 		else:
# 			self.rotate_sound.play()

# 	def block_inside(self):
# 		tiles = self.current_block.get_cell_positions()
# 		for tile in tiles:
# 			if self.grid.is_inside(tile.row, tile.column) == False:
# 				return False
# 		return True

# 	def draw(self, screen):
# 		self.grid.draw(screen)
# 		self.current_block.draw(screen, 11, 11)

# 		if self.next_block.id == 3:
# 			self.next_block.draw(screen, 255, 290)
# 		elif self.next_block.id == 4:
# 			self.next_block.draw(screen, 255, 280)
# 		else:
# 			self.next_block.draw(screen, 270, 270)