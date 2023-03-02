from queue import Queue

def BFS(N:int, D:set):
    #Making sure D is in ascending order
    D = sorted(D)
    #initalizing our arrays and queues
    q = Queue(maxsize = 0)
    parent = [-1]*N
    label = [-1]*7
    visited = [False]*N
    # loop for setting up arrays and queues with starting state of zero
    for j in D:
        next = delta(0,j,N)
        visited[next] = True
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
        return
        # trace the string using parent pointers and
        #  concatenate the corresponding labels as you trace until
        #  start state is reached output the reverse of the string.






def delta(cur: int, Input: int, N:int):
    return (10*cur + Input) % N


def main():
    BFS(7,{3,1})

if __name__ == '__main__':
    main()


