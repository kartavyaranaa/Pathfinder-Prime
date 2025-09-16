# main.py

import argparse
from pathfinder.environment import GridWorld
from pathfinder.agent import Agent, manhattan_distance
import time

def run_static_search(map_file, algorithm):
    """Runs a search algorithm on a static map."""
    env = GridWorld(map_file)
    agent = Agent(env)

    print(f"--- Running {algorithm} on {map_file} ---")
    
    path = None
    if algorithm == 'UCS':
        path = agent.uniform_cost_search()
    elif algorithm == 'A*':
        path = agent.a_star_search(manhattan_distance)
    else:
        print(f"Error: Unknown algorithm '{algorithm}'")
        return

    if path:
        print(f"Path found with cost: {agent.total_cost}")
        print(f"Nodes expanded: {agent.nodes_expanded}")
        print(f"Execution time: {agent.execution_time:.6f} seconds")
        print("Path visualization:")
        env.visualize_path(path)
    else:
        print("No path found.")
    print("-" * 20 + "\n")


def run_dynamic_replanning_demo(map_file):
    """
    Demonstrates the agent's ability to replan when an obstacle appears.
    """
    print(f"--- Running Dynamic Replanning Demo on {map_file} ---")
    
    # 1. Initial state of the world
    env = GridWorld(map_file)
    agent = Agent(env)
    
    print("\nStep 1: Agent calculates initial path with A*.")
    initial_path = agent.a_star_search(manhattan_distance)
    
    if not initial_path:
        print("No initial path could be found. Aborting demo.")
        return
        
    print(f"Initial path found: {initial_path}")
    env.visualize_path(initial_path)
    print("-" * 10)

    # 2. Agent starts moving. Let's say it moves 3 steps.
    current_position_index = 3
    agent.current_pos = initial_path[current_position_index]
    print(f"\nAgent moves 3 steps to {agent.current_pos}.")

    # 3. Suddenly, an obstacle appears on its planned path!
    obstacle_pos = initial_path[current_position_index + 2]
    print(f"\nLOG: DYNAMIC OBSTACLE APPEARS at {obstacle_pos}!")
    env.grid[obstacle_pos[1]][obstacle_pos[0]] = '#'
    
    print("Proof-of-concept log: Obstacle detected, agent must replan.")

    # 4. Agent replans from its new current position
    print("\nStep 2: Agent reruns A* from its current position.")
    env.start = agent.current_pos
    new_agent = Agent(env)
    
    replanned_path = new_agent.a_star_search(manhattan_distance)
    
    if replanned_path:
        print(f"Replanned path found: {replanned_path}")
        final_path = initial_path[:current_position_index+1] + replanned_path
        print(f"Full new path of travel: {final_path}")
        print("Final path visualization:")
        env.visualize_path(final_path)
    else:
        print("Could not find a new path after obstacle appeared.")
    
    print("-" * 20 + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run Pathfinder Prime agent.")
    parser.add_argument('map', type=str, help='Path to the map file.')
    parser.add_argument('algorithm', type=str, choices=['UCS', 'A*', 'dynamic_demo'],
                        help='Algorithm to use (UCS, A*, dynamic_demo).')

    args = parser.parse_args()

    if args.algorithm == 'dynamic_demo':
        run_dynamic_replanning_demo(args.map)
    else:
        run_static_search(args.map, args.algorithm)