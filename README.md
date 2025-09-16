
# Pathfinder Prime: An Autonomous Delivery Agent

**Course:** CSA2001 - Fundamentals of AI and ML  
**Author:** Kartavya Rana  
**Registration Number:** 24MIM10081

## 📖 Overview

Pathfinder Prime is an AI agent designed to autonomously navigate a complex 2D grid-based city to deliver packages. It models the environment, finds the optimal path to minimize cost (simulating time and fuel efficiency), and can dynamically replan its route when encountering unexpected obstacles.

This project implements and compares fundamental AI search algorithms, demonstrating the power of informed search and basic reactive strategies in a simulated environment.

## ✨ Features

- **Environment Modeling:** Parses grid worlds from text files, featuring:
  - Static obstacles (`#`)
  - Variable terrain costs: Normal Road (`.`), Tough Terrain (`T`), Water (`W`)
  - Start (`S`) and Goal (`G`) positions
- **Optimal Pathfinding:** Implements two search algorithms to find the lowest-cost path:
  - **Uniform-Cost Search (UCS):** An uninformed, optimal search algorithm.
  - **A* Search:** An informed, optimal search algorithm using the Manhattan Distance heuristic for guided exploration.
- **Dynamic Replanning:** Demonstrates the ability to react to changes in the environment. If an obstacle blocks the pre-computed path, the agent will stop and compute a new optimal path from its current location.
- **Performance Analysis:** Compares algorithms based on path cost, number of nodes expanded, and execution time.

## 🛠️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone <your-repo-url>
    cd pathfinder-prime
    ```

2.  **Create a Virtual Environment (Recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    *(This project uses only the Python Standard Library. No external packages are required.)*

## 🚀 Usage

The project is run via the command line using the `main.py` script.

### Command Syntax

```bash
python main.py <path_to_map_file> <algorithm>
```

- `<path_to_map_file>`: The path to a `.txt` file containing the grid map.
- `<algorithm>`: The algorithm to use. Choose from `UCS`, `A*`, or `dynamic_demo`.

### Example Commands

1.  **Run Uniform-Cost Search on a map:**
    ```bash
    python main.py maps/small_map.txt UCS
    ```

2.  **Run A* Search on a map:**
    ```bash
    python main.py maps/medium_map.txt A*
    ```

3.  **Run the Dynamic Replanning Demo:**
    ```bash
    python main.py maps/large_map.txt dynamic_demo
    ```
    *This demo will show the agent calculating an initial path, moving along it, and then recalculating a new route when a dynamic obstacle is introduced.*

### Map File Format

Create a `.txt` file where each character represents a cell in the grid:

- `S`: Start position
- `G`: Goal position
- `.`: Normal road (Cost = 1)
- `T`: Tough terrain (Cost = 3)
- `W`: Water (Cost = 5)
- `#`: Wall (Impassable obstacle)

**Example Map (`sample_map.txt`):**
```
S . . # . .
. T # . . .
. . W W . .
. # # . G .
```

## 📊 Results and Analysis

The project experimentally compares the performance of UCS and A* algorithms.

| Metric | UCS | A* |
| :--- | :--- | :--- |
| **Optimality** | Guaranteed | Guaranteed (with admissible heuristic) |
| **Efficiency** | Explores more nodes | Explores fewer, more promising nodes |
| **Best For** | Small maps or no heuristic | Larger, complex maps |

**Key Finding:** While both algorithms always find the optimal path, **A* is significantly more efficient**, expanding far fewer nodes thanks to the guidance provided by the Manhattan Distance heuristic. This efficiency gap widens as map complexity increases.

## 🗂️ Project Structure

```
pathfinder-prime/
│
├── main.py                 # Main script to run the agent and demos
├── README.md              # This file
├── .gitignore            # Git ignore rules
├── report.pdf            # Detailed project report
│
├── pathfinder/           # Main package directory
│   ├── __init__.py      # Makes 'pathfinder' a Python package
│   ├── environment.py   # Defines the GridWorld class
│   └── agent.py         # Defines the Agent class and search algorithms
│
└── maps/                 # Directory for grid map files (create your own)
    ├── small_map.txt
    ├── medium_map.txt
    └── large_map.txt
```

## 🧠 Algorithms Implemented

- **Uniform-Cost Search (UCS):** An optimal uninformed search algorithm that expands the node with the lowest path cost first.
- **A* Search:** An optimal informed search algorithm that uses the sum of the path cost (`g(n)`) and a heuristic estimate (`h(n)`) to prioritize node expansion. Uses the **Manhattan Distance** heuristic.
- **Dynamic Replanning:** A strategy where the agent reacts to a changing environment by re-running the A* algorithm from its current position when its planned path is blocked.

## 👨‍💻 Author

**Kartavya Rana**  
- Registration Number: 24MIM10081

---
