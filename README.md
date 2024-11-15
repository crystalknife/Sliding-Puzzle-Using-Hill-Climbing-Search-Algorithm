# Sliding-Puzzle-Using-Hill-Climbing-Search-Algorithm
SLIDING PUZZLE USING HILL CLIMBING ALGORITHM

Overview
The code implements an interactive Sliding 8 Puzzle game with two modes:
1. Manual Mode: Players can solve the puzzle using arrow key controls.
2. Algorithm Mode: The program uses the Hill Climbing Search Algorithm with Manhattan
Distance as the heuristic to solve the puzzle.


Features
 Randomized Start: The initial state is generated randomly, ensuring solvability using an
inversion count algorithm.
 Turtle Graphics: Visual representation of the puzzle, tiles, and movements.
 Hill Climbing Algorithm: Automates puzzle-solving by attempting to minimize Manhattan
Distance.
 Key Bindings: Enables user interaction for manual solving.
 Visual Feedback: Displays the current state of the puzzle and updates the screen in realtime.

Strengths
a. Interactivity
 Manual mode provides a user-friendly way to solve the puzzle using arrow keys.
 The algorithm mode showcases a basic AI solution for the problem.
b. Robust State Management
 The state is represented as a 2D list, making it easy to work with the tile positions.
 The solvability check ensures that the initial state can always reach the goal.

Visualization
 The use of turtle graphics makes the puzzle visually appealing.
 The split display of the current puzzle and goal state helps track progress.
d. Heuristic-Based Search
 The Manhattan Distance heuristic is efficient for guiding the algorithm closer to the solution.

Limitations
a. Algorithm Limitation
 Local Minima: Hill Climbing Search can get stuck in a local minimum, meaning it stops
improving even if the puzzle isn't solved.
 No Backtracking: Once the algorithm makes a move, it cannot revert to previous states,
which may lead to deadlock situations.
b. Fixed Puzzle Size
 The implementation is hardcoded for a 3x3 puzzle. It cannot dynamically handle other puzzle
sizes (e.g., 4x4).
c. Limited Success Feedback
 When the algorithm gets stuck, the feedback ("Algorithm Stuck!") is displayed but doesn't
provide an option to retry or exit gracefully.

Performance
 The hill-climbing algorithm is not optimal for large or complex puzzles due to its limited
search capability and reliance on local decisions.


Recommendations for Improvement
a. Algorithm Enhancement
 Implement Simulated Annealing or A Search Algorithm*:
o Simulated annealing introduces a probability of making non-optimal moves, helping
avoid local minima.
o A* Search ensures optimality and completeness by exploring all paths to the solution
systematically.
b. Dynamic Puzzle Size
 Add a feature to dynamically choose the puzzle size (e.g., 3x3, 4x4).
 Update the create_random_state() function and GOAL_STATE generation to handle variable
sizes.
c. Improved User Interaction
 Add a retry option when the algorithm fails.
 Allow users to input a custom starting state or puzzle size.
d. Visualization Enhancements
 Animate tile movements during manual mode for better user experience.
 Highlight tiles moved by the algorithm to make its progress more apparent.
e. Code Structure
 Modularize the code further by separating visualization, logic, and algorithms into distinct
functions or files for better maintainability.

Summary of the Hill Climbing Algorithm Implementation
Aspect Strength Limitation
Heuristic Uses Manhattan Distance for effective
guidance.
Cannot handle ties or equal heuristics
effectively.
State
Transition
Generates all valid neighbors of the
current state.
Does not explore deeply; stops on the first
local optimum.
Performance Efficient for small puzzles due to
simplicity.
Prone to getting stuck without global
optimization.

Suggested Extensions
1. Hint System:
o Provide hints for manual mode using the heuristic function.
2. Scoring Mechanism:
o Introduce a scoring system based on the number of moves in manual mode.
3. AI Comparison:
o Implement multiple AI algorithms (e.g., BFS, DFS, A*) and allow users to compare
their performance.
4. Customization:
o Add options for customizing tile colors, font sizes, and screen dimensions.

Conclusion
This implementation is an excellent example of combining interactivity and basic AI for solving
puzzles. While the current Hill Climbing Algorithm demonstrates a good starting point for algorithmic
solving, it can be enhanced significantly by addressing its limitations. The game is both engaging and
educational, making it a great tool for learning about problem-solving techniques.
