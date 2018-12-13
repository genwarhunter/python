import time



def graphInit():
    filename=input( "enter filename: ")
    file=open(filename, "r")
    len = int(file.readline())
    graph = []
    for i in range(len):
        graph.append([])
        line = file.readline()
        tmp = line.split()
        for j in range(len):
                if tmp[j] !="0":
                        graph[i].append(j)
    file.close()
    return graph
    


def dfs(visited, index, gr):
    visited[index]=True
    for w in gr[index]:
        if not visited[w]:
            if dfs(visited, w, gr):
                return True
    return False



def CheckForEilerPatch(gr, vertex):
    oddVertex=0
    visited=[False]*len(gr)

    dfs(visited, vertex, gr)

    if not all(visited):
        print("the graph is not connected")
        return False

    for v in gr:
            if len(v) %2 == 1:
                oddVertex+=1
    if oddVertex > 2:
        print("the graph is not an Euler")
        return False
    return True
    
    

def findEulerPath(gr, vertex):
    st = []
    find = []
    v=vertex
    st.append(v)
    while len(st) > 0:
        v=st[len(st) - 1]
        if not gr[v]:
            st.pop()
            find.append(v)
        else:
            u=gr[v][0]; st.append(u)
            gr[v].remove(u); gr[u].remove(v)
    return find    
    


def main():
    graph=graphInit()

    vertex=int(input("enter Vertex: "))

    if CheckForEilerPatch(graph, vertex,):
        start_time = time.perf_counter()
        v=findEulerPath(graph, vertex)
        end_time = time.perf_counter()
        print(v)
        print ("{:g} ms".format((end_time - start_time)*1000))
    

    
if __name__ == "__main__":
    main()