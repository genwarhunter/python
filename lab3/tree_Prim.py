import time
import myclass2 as mc 

#проверяем, граф связный или нет
def isConnected(gr):
    marker=[1]*len(gr)
    hasNext=True
    marker[0]=2
    while hasNext:
        hasNext=False
        for i in range(len(gr)):
            if marker[i]==2:
                marker[i]=3
                hasNext=True
                for j in gr[i]:
                    if  (marker[j.a]==1):
                        marker[j.a]=2
                break    
    for i in marker:
        if i==1:
            print("graph is not connected")
            return False
    return True


#считаем вес минимального дерева
def FindMinimumSpanningTree(graph):
    answer=0
    max_int=2147483647
    lenGraph=len(graph)
    count=lenGraph-1
    d=[max_int for i in range(lenGraph)]
    p=[lenGraph for i in range(lenGraph)]
    visited=[False for i in range(lenGraph)]
    visited[0]=True
    for i in graph[0]:
        d[i.a]=i.weight
        p[i.a]=0
    while count:
        min=max_int
        iter=0
        for index, value in enumerate(d):
            if value<min and not visited[index]:
                iter=index
                min=value
        count-=1
        answer+=min
        visited[iter]=True
        for i in graph[iter]:
            if not visited[i.a] and d[i.a]>i.weight:
                p[i.a]=i
                d[i.a]=i.weight
    return answer
    

#считываем подаваемый файл и создаем из него список смежности
def graphInit():
    filename=input( "enter filename: ")
    file=open(filename, "r")
    len=int(file.readline())
    graph=[]
    for i in range(len):
        graph.append([])
        line=file.readline()
        tmp=line.split()
        for j in range(len):
                if tmp[j] !="0":
                    graph[i].append(mc.Edge(j, tmp[j])) 
    
    file.close()
    return graph



def main():
    answer=0
    graph=graphInit()
    if isConnected(graph):
        print("start")
        start_time = time.perf_counter()
        answer=FindMinimumSpanningTree(graph)
        end_time = time.perf_counter()
        print("weight: ", answer)
        print("algorythm: "+"{:g} ms".format((end_time - start_time)*1000))



if __name__ == "__main__":
    main()