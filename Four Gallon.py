from typing import List, Tuple, Set

def water_bucket_solver(bucket_sizes: Tuple[int, int], target: int, max_steps: int = 15):
    def recurse(state: Tuple[int, int], path: List[Tuple[Tuple[int, int], str]], visited: Set[Tuple[int, int]]):
        if state in visited or len(path) >= max_steps:
            return None
        if target in state:
            return path + [(state, f"Reached goal: {state}")]

        visited.add(state)
        a, b = state
        max_a, max_b = bucket_sizes
        next_states = []

        # All possible operations
        next_states.extend([
            ((max_a, b), "Fill 3-gallon bucket"),
            ((a, max_b), "Fill 5-gallon bucket"),
            ((0, b), "Empty 3-gallon bucket"),
            ((a, 0), "Empty 5-gallon bucket"),
            (pour(a, b, max_b), "Pour 3-gal -> 5-gal"),
            (pour(b, a, max_a)[::-1], "Pour 5-gal -> 3-gal")
        ])

        for new_state, action in next_states:
            if new_state not in visited:
                result = recurse(new_state, path + [(state, action)], visited.copy())
                if result:
                    return result
        return None

    def pour(from_amt, to_amt, to_max):
        total = from_amt + to_amt
        return max(0, total - to_max), min(to_max, total)

    # Start recursive search
    result = recurse((0, 0), [], set())
    if result:
        print(f"Found a solution in {len(result)} steps:\n")
        for i, (state, action) in enumerate(result, 1):
            print(f"Step {i}: {action} → Buckets = {state}")
    else:
        print("No solution found within the step limit.")

# Example
if __name__ == "__main__":
    water_bucket_solver(bucket_sizes=(3, 5), target=4)
