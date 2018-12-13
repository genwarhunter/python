import time



def nComps(gr):
    cnt=0
    visited=[False]*len(gr)
    for i in range(len(gr)):
        if(not visited[i]):
            dfs(visited, i, gr)
            cnt+=1
    return cnt



def isBridge(gr, a, b):
    gr[a].remove(b); gr[b].remove(a)
    if not nComps(gr):
        gr.insert(a, b); gr.insert(b, a)
        return True
    return False



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
    find = []
    num=0
    v=vertex
    find.append(v)
    for i in gr:
        num+=len(i)
    num/=2
    while num:
        changed=False
        for i in gr[v]:
            if (not isBridge(gr, v, i)) or (len(gr[v])==1):
                find.append(i)
                v=i; num-=1; changed=True
                break
        if (len(gr[v])==0) and (num>0):
            i=v
            find.pop()
            v=find[len(find)-1]
            gr[v].append(i); gr[i].append(v)
            num+=1
            continue
        if(not changed):
            i=gr[0]
            gr[v].remove(i); gr[i].remove(v)
            find.append(i)
            v=i
            num-=1   
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