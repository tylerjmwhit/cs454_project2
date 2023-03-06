from queue import Queue


def BFS(N: int, D: set):
    """
    Performs a Breadth-First Search (BFS) algorithm to find the shortest
    path from the initial state (0) to the final state (0) of a deterministic
    finite automaton (DFA) with a given set of input symbols and a modulus.

    Args:
        N: An integer representing the modulus of the DFA.
        D: A set of integers representing the input symbols of the DFA.

    Returns:
        None.
    """
    # Sort the input symbols in ascending order
    D = sorted(D)

    # Initialize our arrays and queues for BFS
    q = Queue(maxsize=0)
    parent = [-1] * N
    label = [-1] * N
    visited = [False] * N

    # loop for setting up arrays and queues with starting state of zero
    for j in D:
        next = delta(0, j, N)
        visited[next] = True
        if j != 0:
            q.put(next)
        parent[next] = 0
        label[next] = j

    # preforms the BFS
    while not q.empty():
        if next == 0:
            break
        cur = q.get_nowait()
        for i in D:
            next = delta(cur, i, N)
            if next == 0:
                parent[next] = cur
                label[next] = i
                break
            elif not visited[next]:
                visited[next] = True
                parent[next] = cur
                label[next] = i
                q.put(next)

    # Output the shortest path if it exists, else print "No Solution"
    if next != 0:
        print("No Soultion")
    else:
        # trace the string using parent pointers and
        #  concatenate the corresponding labels as you trace until
        #  start state is reached output the reverse of the string.
        i = 0
        output = ''
        while (parent[i] != 0):
            output += str(label[i])
            i = parent[i]
        output += str(label[i])
        print(output[:: -1])


def delta(cur: int, input: int, N: int):
    """
    Computes the delta value given the current state, input value, and modulus.

    Args:
        cur: An integer representing the current state.
        input: An integer representing the input value.
        N: An integer representing the modulus.

    Returns:
        An integer representing the delta value.
    """
    return (10 * cur + input) % N


def main():
    val = 0
    while val != -1:
        val = int(input("Enter a positive integer N between 1 and 99999, to compute for, Enter -1 to exit: "))
        if val == -1:
            break
        if 0 < val < 100000:
            # Create a list of strings split by white space to be converted to integers
            stringDigits = input(
                "Enter a list of allowed digits seperated by a space. Digits must be an integer from 0 to 9: ").split()
            intDigits = [eval(i) for i in stringDigits]
            if all(9 >= i >= 0 for i in intDigits):
                BFS(val, intDigits)
            else:
                print("List of digits must contain integers between 0 and 9")
        else:
            print("Please enter a number between 1 and 99999 ")


if __name__ == '__main__':
    main()

