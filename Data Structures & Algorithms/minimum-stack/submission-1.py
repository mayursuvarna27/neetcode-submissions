class MinStack:

    def __init__(self):
        # Stores tuples: (value, minimum_at_this_point)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            current_min = val
        else:
            # Look at the second element [1] of the top tuple to find the previous min
            current_min = min(val, self.stack[-1][1])
            
        # Crucial: You MUST append a tuple here
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        # Returns just the value (index 0 of the tuple)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Returns just the minimum (index 1 of the tuple)
        return self.stack[-1][1]
