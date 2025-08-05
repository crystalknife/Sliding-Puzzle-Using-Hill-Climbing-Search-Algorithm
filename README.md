# Sliding 8-Puzzle Solver with Hill Climbing

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Made-with-Turtle](https://img.shields.io/badge/Made%20with-Turtle%20Graphics-orange)]()

## 🧩 Overview

This project implements an interactive **Sliding 8-Puzzle game** using Python's Turtle graphics library. It offers two distinct modes for solving the puzzle:

1.  **Manual Mode**: Players can solve the puzzle themselves using arrow key controls.
2.  **Algorithm Mode**: The program uses the **Hill Climbing Search Algorithm** with the **Manhattan Distance** heuristic to find a solution automatically.

The initial puzzle state is always randomized and guaranteed to be solvable, which is verified using an **inversion count algorithm**. This project serves as an excellent educational tool for demonstrating heuristic-based search and basic AI problem-solving techniques in a visual and engaging way.

## ✨ Features

* **Randomized & Solvable Start**: The puzzle board is generated randomly and checked for solvability to ensure a valid starting state every time.
* **Engaging Turtle Graphics**: The entire puzzle, including tiles and movements, is rendered using Turtle graphics for a clean and visually appealing user experience.
* **Automated Hill Climbing Solver**: Implements the Hill Climbing algorithm to automatically solve the puzzle by iteratively minimizing the **Manhattan Distance** to the goal state.
* **Intuitive Key Bindings**: Enables straightforward user interaction for manual solving via the arrow keys.
* **Real-Time Visual Feedback**: The puzzle board is updated in real-time, and a side-by-side view of the current state and goal state helps users track their progress.

## 💪 Strengths & ⚠️ Limitations

### Strengths

* **Interactivity**: Provides both a hands-on manual mode and a demonstrative AI mode.
* **Robust State Management**: Uses a simple 2D list for state representation, making tile operations and solvability checks efficient.
* **Clear Visualization**: The graphical interface makes the puzzle-solving process easy to follow.
* **Heuristic-Based Search**: Effectively uses the Manhattan Distance heuristic to guide the search algorithm toward the solution.

### Limitations

* **Local Minima**: The Hill Climbing algorithm can get stuck in a local minimum, where it cannot find a better move, even if the puzzle is not yet solved. The program will display an "Algorithm Stuck!" message in this case.
* **No Backtracking**: As a greedy algorithm, it never reverts to a previous state, which can lead to dead-end paths.
* **Fixed Puzzle Size**: The implementation is hardcoded for a 3x3 puzzle and does not support other dimensions.

## 🚀 Getting Started

To run this project on your local machine, follow these steps.

### Prerequisites

You need to have Python 3 installed on your system.

### Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone [https://github.com/your-username/sliding-puzzle-solver.git](https://github.com/your-username/sliding-puzzle-solver.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd sliding-puzzle-solver
    ```
3.  Run the main Python script:
    ```bash
    python puzzle_main.py
    ```

## 🕹️ How to Play

* **Manual Mode**: Use the **Arrow Keys** (`Up`, `Down`, `Left`, `Right`) to slide the tiles into the empty space.
* **Algorithm Mode**: Press the **'S' key** to trigger the Hill Climbing algorithm. Watch as the AI attempts to solve the puzzle.

The goal is to arrange the tiles in ascending order from 1 to 8, with the empty space in the bottom-right corner.

## 🔮 Recommendations for Improvement

* **Algorithm Enhancements**:
    * Implement **Simulated Annealing** to allow the algorithm to make non-optimal moves occasionally, helping it escape local minima.
    * Add the **A\* Search Algorithm** to guarantee an optimal solution.
* **Dynamic Puzzle Size**: Refactor the code to allow users to select different puzzle sizes (e.g., 4x4 for a 15-puzzle).
* **Improved User Interaction**:
    * Add a **"Retry"** or **"Restart"** option for when the algorithm gets stuck.
    * Allow users to input a custom starting state.
* **Visualization Enhancements**:
    * Animate the tile movements for a smoother visual experience.
    * Highlight the tile that the algorithm moves in each step.
* **Code Structure**: Modularize the code by separating the visualization logic, state management, and search algorithms into different files for better maintainability.

## 💡 Suggested Extensions

* **Hint System**: Provide hints in manual mode based on the best next move calculated by the heuristic function.
* **Scoring Mechanism**: Introduce a scoring system based on the number of moves or time taken in manual mode.
* **AI Algorithm Comparison**: Implement other search algorithms like Breadth-First Search (BFS), Depth-First Search (DFS), and A\* to compare their performance visually.
* **UI Customization**: Add options for changing tile colors, font sizes, or background themes.
