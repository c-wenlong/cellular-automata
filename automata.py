# Set up map dimensions and colors
width=100
height=100
wolf=lightgray
sheep=white
grass=green
empty=black
conserve_energy=False

# Initialize counts
num_wolves=0
num_sheep=0

# Set up probabilities
wolf_reproduction_prob=x  # Probability of wolf reproduction
sheep_reproduction_prob=x  # Probability of sheep reproduction
wolf_starvation_chance=a  # Chance of wolf dying if not eating
sheep_starvation_chance=b  # Chance of sheep dying if not eating

# Initialize map
canvas(0, 0, width, height)
resolution(width, height)

# Populate the map randomly with wolves, sheep, and grass
noupdate()
for x in range(width):
    for y in range(height):
        entity = randrange(4)  # Randomly choose what to place: empty, wolf, sheep, or grass
        if entity == 1:
            pixset(x, y, wolf)
            num_wolves += 1
        elif entity == 2:
            pixset(x, y, sheep)
            num_sheep += 1
        elif entity == 3:
            pixset(x, y, grass)
        else:
            pixset(x, y, empty)
update()

# Helper function to move an animal
def move_animal(x, y, target):
    # Retrieve the adjacent cells
    adjacent:list[list[int]] = []
    for i in range(-1,2):
        for j in range(-1,2):
            if (i == 0) and (j == 0):
                continue  # Skip the cell itself
            nx =(x + i)
            ny =(y + j)
            if (0 <= nx) and (nx < width) and (0 <= ny) and (ny < height):
                adjacent.append([nx, ny])
    # Check for the target in the adjacent cells
    for nx, ny in adjacent_cells:
        if pixcol(nx, ny) == target:
            return nx, ny  # Move towards the target
    if(conserve_energy):
        return x, y
    else:
        return choice(adjacent) # Move randomly
    
# Function to move wolves and sheep
def move_animals():
    for x in range(width):
        for y in range(height):
            if pixcol(x, y) == wolf:
                # Wolf behavior
                new_x, new_y = move_animal(x, y, sheep)
                if (new_x, new_y) != (x, y) and pixcol(new_x, new_y) == sheep:
                    # Eat the sheep
                    num_sheep -= 1
                else:
                    # Check for starvation
                    if randrange(100) < wolf_starvation_chance:
                        pixset(x, y, empty)  # Wolf dies
                        num_wolves -= 1
                        continue
                # Check for reproduction
                if randrange(100) < wolf_reproduction_prob:
                    reproduce(x, y, wolf)
            elif pixcol(x, y) == sheep:
                # Sheep behavior
                new_x, new_y = move_animal(x, y, grass)
                if (new_x, new_y) != (x, y) and pixcol(new_x, new_y) == grass:
                    # Eat the grass
                    pass  # Implement grass consumption logic
                else:
                    # Check for starvation
                    if randrange(100) < sheep_starvation_chance:
                        pixset(x, y, empty)  # Sheep dies
                        num_sheep -= 1
                        continue
                # Check for reproduction
                if randrange(100) < sheep_reproduction_prob:
                    reproduce(x, y, sheep)

# Helper function for reproduction
def reproduce(x, y, animal_type):
    adjacent_cells:list[list[int]] = get_adjacent_cells(x, y)
    for nx, ny in adjacent_cells:
        if pixcol(nx, ny) == empty:
            pixset(nx, ny, animal_type)  # Spawn new animal
            if animal_type == wolf:
                num_wolves += 1
            else:
                num_sheep += 1
            break  # Only one offspring per turn
# Function to regrow grass
def regrow_grass():
    # Implement logic for grass to regrow in empty spaces
    pass

# Main simulation loop
while (num_wolves > 0) and (num_sheep > 0):
    move_animals()
    regrow_grass()
    # Add any additional simulation logic here
    update()
    # Pause or wait for a certain time if necessary

# End of simulation
print('Simulation has ended.')
