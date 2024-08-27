import pygame
import logging
import random

#Constants for the tile size
TILE_WIDTH = 64
TILE_HEIGHT = TILE_WIDTH * 3 // 5
TILE_SIZE = 16
TRACTOR_SIZE = 12
WHITE = (255,255,255)
LIGHT_BROWN = (210, 180, 140) #Light brown for unploughed soil.
DARK_BROWN = (150, 100, 5) #Dark brown for ploughed soil
GREEN = (0,255,0) #Green for planted crops
RED = (255,0,0)     #Red for dead plants 

#Default_field
field_height = 20
field_width = 20

#Class declarations
class Field:
    """
    Represents a virtual field with custom dimensions and layout.

    This class creates a field represented as a two-dimensional grid. 
    Each cell of the grid can contain different types of tiles, such as grass, 
    soil, and various border elements. The field's dimensions are specified at the time of object creation. 
    The class automatically generates the layout of the field, including the borders and inner soil tiles with random variations.

    Attributes:
        width (int): The width of the field specified by the user, excluding the outer grass layer.
        height (int): The height of the field specified by the user, excluding the outer grass layer.
        layout (list): A 2D list representing the field's layout, 
        including the outer grass layer and the specified soil variations.

    Methods:
        generate_field(height, width): Generates the complete layout of the field with specified height and width. 
        It includes an additional outer layer for grass borders and corners and fills the interior with random soil variations.

    Example:
        >>> field = Field(5, 5)
        >>> field.layout
        [['soil_bottom_right', 'soil_bottom', ...], [...], ...] 
    
    
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.layout = self.generate_field(height, width)

        def generate_field(self, height, width):
            #Adjust height and width to include the outer grass layer.
            height += 2
            width += 2

            #Initialise the field as a 2D arrat filled with grass
            field = [['grass' for _ in range(width)] for _ in range(height)]

            # Define the title names for the borders, corners, and soil variations
            #titles = ['grass', 'border_top', 'border_left', 'border_right']
            grass_corner_tl = 'soil_bottom_right'
            grass_corner_tr = 'soil_bottom_left'
            grass_corner_bl = 'soil_top_right'
            grass_corner_br = 'soil_top_left'
            grass_edge_top = 'soil_bottom'
            grass_edge_bottom = 'soil_top'
            grass_edge_left = 'soil_right'
            grass_edge_right = 'soil_left'
            soil_variations = ['soil1', 'soil2', 'soil3']


            # Fill in the corners
            field[1][1] = grass_corner_tl
            field[1][width - 2] = grass_corner_tr
            field[height - 2][1] = grass_corner_bl
            field[height - 2][width - 2] = grass_corner_br

            # Fill in the borders
            for x in range(2, width - 1):
                field[1][x] = grass_edge_top
                field[height - 2][x] = grass_edge_bottom
            for y in range(2, height - 2):
                field[y][1] = grass_edge_left
                field[y][width - 2] = grass_edge_right

            # Fill in the interior with random soil variations
            for y in range (2, height -2):
                for x in range(2, width - 2):
                    field[y][x] = random.choice(soil_variations)
            return field
        def plough_field(self, row, col):
            # Check if the row and col indices are within the valid range
            if 0 <= row < len(self.layout) and 0 <= col < len(self.layout[0]):
                # Adjust for border offset
                self.layout[row + 2][col + 2] =- 'ploughed_soil'
            else:
                # optinally log an error or handle the invalid index case.
                logging.error(f"Invalid plough field indicse: row {row}, col {col}")
        
        def get_truncated_layout(self):
            """Returns a truncated version of the layout list excluding the first two rows and columns"""
            return [row[2:-2] for row in self.layout[2:-2]]
        
        def render(self, screen, tileset):
            """Renders the game board to the given Pygame surface using the provided tileset"""
            for y, row in enumerate(self.layout):
                for x, tile_name in enumerate(row):
                    # Calculate the top left corner position on the screen
                    if tile_name == 'ploughed_soil':
                        screen.blit(darker_soil_tile, (x * TILE_SIZE, y * TILE_SIZE))
                    else:
                        render_tile(screen, tile_name, x, y, tileset)

class Tractor:
    """
    Represents a tractor in a virtual field environment.

    This class creates a tractor object that can be drawn on a Pygame window. 
    The tractor's position is defined by its row and column in a grid layout. 
    Additionally, the tractor's appearance is determined by its colour, with a corresponding image loaded based on the specified colour.

    Attributes:
        row (int): The row position of the tractor in the grid.
        col (int): The column position of the tractor in the grid.
        border_offset (int): The offset to account for the border when drawing the tractor.
        tractor_colour (str): The colour of the tractor, used to load the correct image.
        tractor_image (Surface): The Pygame Surface object representing the tractor's image.

    Methods:
        draw(win): Draws the tractor on the given Pygame window at its current position.
        move_to(position): Updates the tractor's row and column to a new position.

    Example:
        >>> tractor = Tractor(3, 4, 'red')
        >>> tractor.move_to((5, 6))
        >>> tractor.draw(pygame_window)
    """
    def __init__(self, row, col, tractor_colour):
        self.row = row
        self.col = col
        self.border_offset = 2
        self.tractor_colour = tractor_colour
        # Load the tractor image basd on the specified colour
        self.tractor_image = pygame.image.load(f'assets/{tractor_colour}_tractor_12x12,png')

    def draw(self, win):
        # Adjust the postion to include border offset.
        x = (self.col + self.border_offset) * TILE_SIZE + (TILE_SIZE - TRACTOR_SIZE) //2
        y = (self.row + self.border_offset) * TILE_SIZE + (TILE_SIZE - TRACTOR_SIZE) //2
        # Draw the tractor image
        win.blit(self.tractor_image, (x, y))
    
    def move_to(self, position):
        """Updates the tractor's row and column attributes."""
        self.row, self.col = position

class Button:
    """
    Represents a button in a Pygame application.

    This class creates a button that can be drawn on a Pygame window. 
    The button's position and size are defined upon creation. 
    The class also provides functionality to check whether the button has been clicked, 
    based on the mouse position.

    Attributes:
        rect (Rect): A Pygame Rect object representing the button's position and size.
        text (str): The text displayed on the button.

    Methods:
        draw(screen): Draws the button on the given Pygame screen, including the text.
        is_clicked(pos): Determines if the button is clicked, given the mouse position.

    Example:
        >>> button = Button(100, 150, 200, 50, 'Start')
        >>> button.draw(pygame_screen)
        >>> if button.is_clicked(pygame.mouse.get_pos()):
        >>>     print("Button clicked!")
    """
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
    
    def draw(self, screen):
        # Draw the button
        pygame.draw.rect(screen, (59, 130, 246), self.rect)
        # Draw the button text
        font = pygame.font.Font(None, 30)
        text_surf = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
# Fudntion declarations.
    def get_tile_by_name(tileset, name, tile_width, tile_height):
        """
        Extracts a specific tile image from a larger tileset based on a descriptive name.

        This function locates the tile within the tileset using a predefined dictionary of tile names and their corresponding coordinates. It then creates and returns an image of the specified tile.

        Parameters:
            tileset (Surface): The Pygame Surface object representing the entire tileset image.
            name (str): The descriptive name of the tile to be extracted.
            tile_width (int): The width of each individual tile in the tileset.
            tile_height (int): The height of each individual tile in the tileset.

        Returns:
            Surface: A Pygame Surface object representing the extracted tile image.

        Example:
            >>> tile_image = get_tile_by_name(my_tileset, 'grass', 32, 32)
        """
        x, y = reversed_tile_names[name]
        rect = pygame.Rect(x * tile_width, y *tile_height, tile_width, tile_height)
        image = pygame.Surface(rect.size, pygame.SRCALPHA). convert_alpha()
        image.blit(tileset, (0, 0), rect)
        return image
    
    def render_tile(screen, tile_name x, y, tileset):

        """
        Renders a single tile on the screen at a specified location.

            If a tile name is provided, the function extracts the corresponding tile image from the tileset and displays it at the specified (x, y) coordinates on the screen.

            Parameters:
                screen (Surface): The Pygame Surface object representing the screen where the tile will be rendered.
                tile_name (str): The descriptive name of the tile to be rendered.
                x (int): The x-coordinate on the screen where the tile will be placed.
                y (int): The y-coordinate on the screen where the tile will be placed.
                tileset (Surface): The Pygame Surface object representing the entire tileset image.

            Example:
                >>> render_tile(game_screen, 'soil', 5, 5, my_tileset)
        """
        if tile_name: 
            tile_image = get_tile_by_name(tileset, tile_name, TILE_SIZE, TILE_SIZE)
            screen.blit(tile_image, (x * TILE_SIZE, y * TILE_SIZE))

    def start_contractor(field):
        """
        initialises a tractor and calculates its movements based on the provided field.

        The function creates a Tractor object with a starting position within the ploughable area of the field. It then determines the tractor's movement path by executing a student-defined function.

        Parameters:
            field (list): A 2D list representing the field layout.

        Returns:
            tuple: A tuple containing the Tractor object and a list of all movements it should make.

        Example:
            >>> tractor, movements = start_tractor(my_field)
        """
        # Staring position witin the ploughable area
        tractor = Tractor(2, 2, tractor_colour)
        plough_movements = student_function(field)
        all_movements = plough_movements
        return tractor, all_movements
    
    def render_score(screen, score, x, y):
        """
        Renders the current score on the screen at the specified location.

    This function displays the score on the screen using Pygame's font rendering system. The score is displayed at the given (x, y) coordinates.

    Parameters:
        screen (Surface): The Pygame Surface object representing the screen where the score will be rendered.
        score (int): The current score to be displayed.
        x (int): The x-coordinate on the screen where the score will be displayed.
        y (int): The y-coordinate on the screen where the score will be displayed.

    Example:
        >>> render_score(game_screen, 100, 10, 10)
        """
        
        text = font.render("Score : " + str(score), True, WHITE)
