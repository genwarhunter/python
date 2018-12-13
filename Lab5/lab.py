import copy
import time 

def graphInit():
    filename=input( "enter filename: ")
    file=open(filename, "r")
    leng = int(file.readline())
    graph = []
    for i in range(leng):
        graph.append([])
        line = file.readline()
        tmp = line.split()
        for j in range(leng):
            graph[i].append(int(tmp[j]))
    return graph

def ctrl(x):    
    if x > 0:
        return x
    else:    
        return 10000000


def min_way (D, w, p):
    n = len(D)
    for i in range(n):
        p[i]=0
        w[i]=10000000
    a=[0 for i in range(n)]
    for i in range(n):
        w[i] = ctrl (D[0][i]) 
    a[0] = 1
    w[0] = 0
    p[0] =-1

    for i in range(n-2):
        Min = 2 * 10000000
        iMin = - 1
        for j in range(n):
            if not a[j] and w[j] < Min:
                Min = w[j]
                iMin = j
        
        if iMin < 0: return False
        a[iMin] = 1
        
        for j in range(n):        
            if (w[j] > w[iMin] + ctrl(D[iMin][j])):
                w[j] = w[iMin] + D[iMin][j]
                p[j] = iMin

    return w[n - 1] < 10000000 // 10


#inf = 10000000

def max_flow(C):
    n = len(C)
    F=[[0 for i in range(n)]for i in range(n)]
    Cf=copy.deepcopy(C)   
    w = [10000000 for i in range(n)]  # пропускная способность 
    p = [0 for i in range(n)] #индекс
    
    while min_way(Cf, w, p): #находим кратчайший путь 
        s = 10000000
        i=n-1
        while i:
            s = min(s, Cf[p[i]][i])
            i=p[i]
        i=n-1
        while i:
            u = p[i]
            v = i
            F[u][v] += s
            F[v][u] = - F[u][v]
            Cf[u][v] = C[u][v] - F[u][v]
            Cf[v][u] = C[v][u] - F[v][u]
            i=p[i]
    return F


def outputGraph(answer):
        file=open('output.txt', 'w')
        for i in range(len(answer)):
            file.write(str(answer[i])+'\n')
        file.close()
        return True



def main():
    graph=graphInit()
    start_time = time.perf_counter()
    outgraph=max_flow(graph)
    end_time = time.perf_counter()
    print(sum(outgraph[0]))
    print("algorythm: "+"{:g} ms".format((end_time - start_time)*1000))
    outputGraph(outgraph)




if __name__ == "__main__":
    main()