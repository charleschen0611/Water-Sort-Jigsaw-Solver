from collections import deque

def is_solved(state):
    
    return all(len(set(tube)) == 1 and len(tube) == 4 for tube in state if tube)

def possible_moves(state):
    moves = []
    num_tubes = len(state)
    for i in range(num_tubes):
        src = state[i]
        if src and src[-1]:  # Ensure there's something to move.
            for j in range(num_tubes):
                if i != j:
                    dst = state[j]
                    if not dst or (dst[-1] == src[-1] and len(dst) < 4):  # Ensuring destination can receive the color.
                        # Perform the move
                        new_state = list(map(list, state))  # Deep copy of the state
                        new_state[j].append(new_state[i].pop())  # Move the color
                        if not new_state[i]:  # If source tube is empty after move, maintain structure
                            new_state[i] = []
                        new_state = tuple(tuple(tube) for tube in new_state)  # Convert back to tuple of tuples for immutability
                        moves.append(new_state)
                        # print(f"Move from Tube {i+1} to Tube {j+1}: {new_state}")  # Debugging output
    return moves

def solve(initial_state):
    visited = set()
    queue = deque([(tuple(map(tuple, initial_state)), [])])  # Store state as tuple of tuples

    while queue:
        current_state, path = queue.popleft()
        if is_solved(current_state):
            return path + [current_state]
        for next_state in possible_moves(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

def print_state(state):
    for tube in state:
        print(tube)
    print()

# Initial state as provided
initial_state = [
    ['Green','Green', 'Grey', 'Grey'],
    ['Green', 'Blue', 'Blue', 'Red'],
    ['Light Blue', 'Light Blue', 'Grey', 'Light Blue'],
    ['Brown', 'Brown', 'Grey', 'Brown'],
    ['Green', 'Blue', 'Red', 'Brown'],
    ['Light Blue', 'Blue', 'Red', 'Red'],
    [],
    []

]

solution = solve(initial_state)
if solution:
    print("Solution found:")
    for step in solution:
        print_state(step)
else:
    print("No solution found.")
