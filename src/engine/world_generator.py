import random
import noise

class WorldGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(height)] for _ in range(width)]
        self.generate_world()

    def generate_world(self):
        scale = 100.0  # Масштаб шума
        octaves = 6    # Число октав для шума
        persistence = 0.5  # Постоянная шума
        lacunarity = 2.0   # Лакунарность шума

        for x in range(self.width):
            for y in range(self.height):
                nx = x / scale
                ny = y / scale
                value = noise.pnoise2(nx, ny, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
                if value < -0.1:
                    self.tiles[x][y] = 'water'
                elif value < 0.1:
                    self.tiles[x][y] = 'grass'
                else:
                    self.tiles[x][y] = 'mountain'

    def get_tile(self, x, y):
        x = int(x) 
        y = int(y) 
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[x][y]
        return None

    def get_visible_tiles(self, camera_rect, zoom_level, tile_size):
        visible_tiles = []
        start_x = max(0, int(camera_rect.x // tile_size))
        start_y = max(0, int(camera_rect.y // tile_size))
        end_x = min(self.width, int((camera_rect.x + camera_rect.width) // tile_size) + 1)
        end_y = min(self.height, int((camera_rect.y + camera_rect.height) // tile_size) + 1)

        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                visible_tiles.append((x, y, self.get_tile(x, y)))

        return visible_tiles