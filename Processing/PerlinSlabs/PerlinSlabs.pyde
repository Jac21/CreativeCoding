# Dimensions
grid_height = 70
grid_width = 70

# Block properties
block_size = 10
block_height = 5
lines = 2
sw = 2

# Perlin Noise parameters
noise_scale = .05
noise_multiplier = 100
noise_dampener = 2

image_border_buff = 5

# Center structure based on block size
w = grid_width * block_size + grid_height * block_size + image_border_buff * block_size
h = grid_height * block_size / 2 + grid_width * block_size / 2 + (int(noise(0, 0) * noise_multiplier) / noise_dampener * block_height) + image_border_buff * block_size

start_block_x = w / 2 - grid_height / 2 * block_size + grid_width / 2 * block_size
start_block_y = h / 2 - grid_height / 2 * block_size / 2 - grid_width / 2 * block_size / 2 + (int(noise(0, 0) * noise_multiplier) / noise_dampener * block_height / 2)

# Basic block
def draw_block(x, y):
    
    # Top face
    beginShape()
    vertex(x - block_size, y)
    vertex(x, y - block_size / 2)
    vertex(x + block_size, y)
    vertex(x, y + block_size / 2)
    endShape(CLOSE)
    
    # Left face
    beginShape()
    vertex(x - block_size, y)
    vertex(x, y + block_size / 2)
    vertex(x, y + block_height + block_size / 2)
    vertex(x - block_size, y + block_height)
    endShape(CLOSE)
    
    line_sep = float(block_height) / lines
    for l in range(lines):
        line(x - block_size, y + (l * line_sep), x, y + block_size / 2 + (l * line_sep))
        
    # Right face
    beginShape()
    vertex(x + block_size, y)
    vertex(x, y + block_size / 2)
    vertex(x, y + block_height + block_size / 2)
    vertex(x + block_size, y + block_height)
    endShape(CLOSE)

def setup():
    size(w, h)
    strokeWeight(sw)
    
    background(190, 194, 249)
    fill(254, 171, 227)
    
    for g in range(3):
        for x in range(grid_height):
            for y in range(grid_width):
                
                cubes = int(noise((x + g) * noise_scale, (y + g) * noise_scale) * noise_multiplier) / noise_dampener
                
                for i in range(cubes):
                    draw_block((start_block_x + x * block_size) - y * block_size, (start_block_y + x * (block_size / 2)) + y * (block_size / 2) - i * block_height)
        save('Examples/Gif/' + str(g) + '.png')
