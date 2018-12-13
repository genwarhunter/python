import time
import myclass as mc



def getEdgeList(graph, EdgeList):
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if int(graph[i][j])!=0:
                EdgeList.append(mc.Edge(i,j,graph[i][j]))



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
                for j,value in enumerate(gr[i]):
                    if (int(value)!=0) and (marker[j]==1):
                        marker[j]=2
                break    
    for i in marker:
        if i==1:
            print("graph is not connected")
            return False
    return True



def FindMinimumSpanningTree(EdgeList, comps):
    answer=0
    EdgeList.sort()
    for curEdge in EdgeList:
        if(comps[curEdge.a]!=comps[curEdge.b]):
            answer+=curEdge.weight
            comp=comps[curEdge.b]
            for j in range(len(comps)):
                if comps[j]==comp:
                    comps[j]=comps[curEdge.a]       
    return answer
    


def graphInit():
    filename=input( "enter filename: ")
    file=open(filename, "r")
    len=int(file.readline())
    graph=[]
    for line in file.readlines():
        graph.append(line.split())
    
    file.close()
    return len, graph



def main():
    lenGraph, graph=graphInit()
    EdgeList=[]
    if isConnected(graph):
        comps=list(range(lenGraph))
        getEdgeList(graph, EdgeList)
        print("start")
        start_time = time.perf_counter()
        answer=FindMinimumSpanningTree(EdgeList, comps)
        end_time = time.perf_counter()
        print("weight: ", answer)
        print("algorythm: "+"{:g} ms".format((end_time - start_time)*1000))



if __name__ == "__main__":
    main()