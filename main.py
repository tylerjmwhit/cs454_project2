from queue import Queue

def BFS(N:int, D:set):
    #Making sure D is in ascending order
    D = sorted(D)
    #initalizing our arrays and queues
    q = Queue(maxsize = 0)
    parent = [-1]*N
    label = [-1]*N
    visited = [False]*N
    # loop for setting up arrays and queues with starting state of zero
    for j in D:
        next = delta(0,j,N)
        visited[next] = True
        if j != 0:
            q.put(next)
        parent[next] = 0
        label[next] = j
    # performing the BFS
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
    if next != 0:
       return print("no soultion")
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
        return print(output[: : -1])
        






def delta(cur: int, Input: int, N:int):
    return (10*cur + Input) % N


def main():
    val = 0
    while val != -1:
        val = int(input("Enter a positive integer N, to compute for, Enter -1 to exit: "))
        if val == -1:
            break
        #Create a list of strings split by white space to be converted to integers
        stringDigits = input("Enter a list of allowed digits seperated by a space. Digits must be an integer from 0 to 9: ").split()
        intDigits = [eval(i) for i in stringDigits]
        if all(i >= 9 and i <= 0  for i in intDigits):
            print("List of digits must contain integers between 0 and 9")
        elif val > 0:
            BFS(val , intDigits)
        else:
            print("Please enter a number between Greater than 0 ")

if __name__ == '__main__':
    main()


11000001001000011
11000001001000011

11011011011001001
11011011011001001