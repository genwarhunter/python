import time
import sys

def hungarian(graph):
    height = len(graph)
    width = len(graph[0])
   
    # Значения, вычитаемые из строк (u) и столбцов (v)
    u=[0 for i in range(height)] 
    v=[0 for i in range(width)]
   
    # Индекс помеченной клетки в каждом столбце
    markIndices=[-1 for i in range(width)]
   
    # Будем добавлять строки матрицы одну за другой
    for i in range(height): 
        links=[-1 for i in range(width)]
        mins=[1000000 for i in range(width)]
        visited=[0 for i in range(width) ]
      
        # Разрешение коллизий (создание "чередующейся цепочки" из нулевых элементов)
        markedI = i
        markedJ = -1
        while markedI != -1 :
            
            #Обновим информацию о минимумах в посещенных строках непосещенных столбцов
            #Заодно поместим в j индекс непосещенного столбца с самым маленьким из них
            j = -1
            for j1 in range(width):
                if not visited[j1]:
                    if graph[markedI][j1] - u[markedI] - v[j1] < mins[j1]: 
                        mins[j1] = graph[markedI][j1] - u[markedI] - v[j1]
                        links[j1] = markedJ
               
                    if j==-1 or mins[j1] < mins[j]:
                        j = j1

            #Теперь нас интересует элемент с индексами (markIndices[links[j]], j)
            #Произведем манипуляции со строками и столбцами так, чтобы он обнулился
            delta = mins[j]
            for j1 in range(width):
                if visited[j1]:
                    u[markIndices[j1]] += delta
                    v[j1] -= delta
                else:
                    mins[j1] -= delta 
            u[i] += delta
         
            #Если коллизия не разрешена - перейдем к следующей итерации
            visited[j] = 1
            markedJ = j
            markedI = markIndices[j]

        #Пройдем по найденной чередующейся цепочке клеток, снимем отметки с
        #отмеченных клеток и поставим отметки на неотмеченные
        while links[j] != -1:
            markIndices[j] = markIndices[links[j]]
            j = links[j]
        markIndices[j] = i
   
   
    #Вернем результат
    resultInd=[]
    result=[]
    for j in range(width):
        if markIndices[j] != -1:
            resultInd.append([markIndices[j], j, graph[markIndices[j]][j]])
            result.append(graph[markIndices[j]][j])
    return resultInd, sum(result)

def graphInit():
    if len(sys.argv)!=1:
        file=open(sys.argv[1], "r")
    else:
        filename=input("Enter Filename: ")
        file=open(filename, "r")
    leng = int(file.readline())
    graph = []
    for i in range(leng):
        graph.append([])
        line = file.readline()
        tmp = line.split()
        for j in range(leng):
            graph[i].append(int(tmp[j]))
    file.close()
    return graph

def outputGraph(answer):
    if len(sys.argv)!=1:
        file=open('output for '+sys.argv[1], 'w')
    else:
        file=open('output.txt', 'w')
    for i in range(len(answer)):
        file.write(str(answer[i])+'\n')
    file.close()
    return True

def main():
    graph=graphInit()
    start_time = time.perf_counter()
    answer, sumA=hungarian(graph)
    end_time = time.perf_counter()
    print(sumA)
    print("algorythm: "+"{:g} ms".format((end_time - start_time)*1000))
    outputGraph(answer)
    

if __name__ == "__main__":
    main()