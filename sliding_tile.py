import turtle
import random
import time

# Constants
TILE_SIZE = 100  # Size of each tile
FONT = ("Courier", 24, "bold")  # Robotic-style font
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # The goal state of the puzzle

# Initialize the game state
def create_random_state():
    """Create a random solvable initial state."""
    state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    while True:
        random.shuffle(state)
        if is_solvable(state):
            break
    return [state[i:i + 3] for i in range(0, 9, 3)]

def is_solvable(flat_state):
    """Check if the puzzle is solvable."""
    inversions = sum(
        1 for i in range(len(flat_state)) for j in range(i + 1, len(flat_state))
        if flat_state[i] > flat_state[j] and flat_state[i] != 0 and flat_state[j] != 0
    )
    return inversions % 2 == 0

# Game State
state = create_random_state()

# Turtle Setup
screen = turtle.Screen()
screen.title("Sliding 8 Puzzle")
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.tracer(0)

# Drawing Functions
def draw_tile(x, y, number, is_goal=False):
    """Draw a tile at position (x, y) with the specified number."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    color = "lightgreen" if number != 0 else "lightgray"
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(TILE_SIZE)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    if number != 0:
        text_color = "black" if not is_goal else "blue"
        turtle.color(text_color)
        turtle.goto(x + TILE_SIZE // 2, y + TILE_SIZE // 4)
        turtle.write(str(number), align="center", font=FONT)
    turtle.color("black")

def draw_grid(state, start_x, start_y, is_goal=False):
    """Draw the puzzle grid starting from a given position."""
    for i in range(3):
        for j in range(3):
            x = start_x + j * TILE_SIZE
            y = start_y - i * TILE_SIZE
            draw_tile(x, y, state[i][j], is_goal)
    if is_goal:
        turtle.penup()
        turtle.goto(start_x + TILE_SIZE * 1.5, start_y - TILE_SIZE * 3 - 20)
        turtle.write("Goal State", align="center", font=("Courier", 18, "bold"))

def draw_puzzles():
    """Draw both the current puzzle and the goal state."""
    turtle.clear()
    # Draw the current puzzle on the left
    draw_grid(state, -300, 150)
    # Draw the goal state on the right
    draw_grid(GOAL_STATE, 100, 150, is_goal=True)
    screen.update()

# Puzzle Movement
def find_empty():
    """Find the position of the empty tile (0)."""
    for i, row in enumerate(state):
        for j, value in enumerate(row):
            if value == 0:
                return i, j

def move_tile(direction):
    """Move the tile in the specified direction if possible."""
    global state
    empty_x, empty_y = find_empty()
    dx, dy = 0, 0
    if direction == "up":
        dx, dy = -1, 0
    elif direction == "down":
        dx, dy = 1, 0
    elif direction == "left":
        dx, dy = 0, -1
    elif direction == "right":
        dx, dy = 0, 1

    new_x, new_y = empty_x + dx, empty_y + dy
    if 0 <= new_x < 3 and 0 <= new_y < 3:
        state[empty_x][empty_y], state[new_x][new_y] = state[new_x][new_y], state[empty_x][empty_y]
        draw_puzzles()
        if state == GOAL_STATE:
            turtle.penup()
            turtle.goto(-100, -300)
            turtle.color("green")
            turtle.write("Puzzle Solved!", align="center", font=("Courier", 20, "bold"))

# Hill Climb Search Algorithm for solving the puzzle
def hill_climb():
    """Hill Climb Search Algorithm to solve the puzzle."""
    global state  # Modify the global state
    visited = set()
    visited.add(tuple(map(tuple, state)))  # Add the initial state to visited

    while state != GOAL_STATE:
        neighbors = generate_neighbors(state)
        next_state = None
        min_heuristic = float('inf')

        for neighbor in neighbors:
            h = heuristic(neighbor)
            if h < min_heuristic and tuple(map(tuple, neighbor)) not in visited:
                min_heuristic = h
                next_state = neighbor

        if not next_state:
            # If no better state is found, stop (local minimum reached)
            break

        visited.add(tuple(map(tuple, next_state)))  # Mark the new state as visited
        state = next_state  # Update the global state
        draw_puzzles()  # Update the visuals
        time.sleep(0.5)  # Adding delay to make moves visible

    # Check if the goal state is reached
    if state == GOAL_STATE:
        turtle.penup()
        turtle.goto(-100, -300)
        turtle.color("green")
        turtle.write("Puzzle Solved by Algorithm!", align="center", font=("Courier", 20, "bold"))
    else:
        turtle.penup()
        turtle.goto(-100, -300)
        turtle.color("red")
        turtle.write("Algorithm Stuck!", align="center", font=("Courier", 20, "bold"))


def heuristic(state):
    """Heuristic for Hill Climb Search: Manhattan Distance."""
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = divmod(state[i][j] - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def generate_neighbors(state):
    """Generate all valid neighbors by sliding tiles."""
    neighbors = []
    empty_x, empty_y = find_empty()
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in moves:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]  # Deep copy the state
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            neighbors.append(new_state)
    
    return neighbors

# Menu to choose between manual or algorithm mode
def game_mode_choice():
    """Prompt the user to choose between manual solving or algorithm solving."""
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 100)
    turtle.write("Choose your mode:", align="center", font=("Courier", 24, "bold"))
    turtle.goto(0, 50)
    turtle.write("1: Manual Mode", align="center", font=("Courier", 24, "bold"))
    turtle.goto(0, 0)
    turtle.write("2: Algorithm Mode", align="center", font=("Courier", 24, "bold"))
    screen.update()

    screen.listen()
    screen.onkey(manual_mode, "1")
    screen.onkey(algorithm_mode, "2")

def manual_mode():
    """Start the game in manual mode."""
    draw_puzzles()
    setup_bindings()

def algorithm_mode():
    """Start the game in algorithm mode."""
    draw_puzzles()  # Show the goal state and initial state
    hill_climb()

# Key Bindings
def setup_bindings():
    """Setup key bindings for controlling the puzzle."""
    screen.listen()
    screen.onkey(lambda: move_tile("up"), "Up")
    screen.onkey(lambda: move_tile("down"), "Down")
    screen.onkey(lambda: move_tile("left"), "Left")
    screen.onkey(lambda: move_tile("right"), "Right")

# Start the game
game_mode_choice()
screen.mainloop()
