import time

def graphInit():
    filename=input( "enter filename: ")
    file=open(filename, "r")
    file.readline()
    graph=[]
    for line in file.readlines():
        graph.append(line.split())
    return graph



def bron_kerbosch_max_by_inclusion(graph):

    results = []

    def check(candidates, wrong):
        for i in wrong:
            q = True
            for j in candidates:
                if graph[i][j]:
                    q = False
                    break
            if q: return False
        return True

    def extend(compsub, candidates, wrong):

        while candidates and check(candidates, wrong):

            v = candidates[0]
            compsub.append(v)

            new_candidates = [ i for i in candidates if not int(graph[i][v]) and i != v ]
            new_wrong = [ i for i in wrong if not int(graph[i][v]) and i != v ]

            if not new_candidates and not new_wrong:
                results.append(list(compsub))
            else:
                extend(compsub, new_candidates, new_wrong)

            candidates.remove(v)
            compsub.remove(v)
            wrong.append(v)

    extend([], list(range(len(graph))), [])

    return results



def wrFile(answer):
        file=open('output.txt', 'w')
        for i in range(len(answer)):
            file.write(str(answer[i])+'\n')
        file.close()
        return True

    


def main():
    graph=graphInit()
    print("start")
    start_time = time.perf_counter()
    result=bron_kerbosch_max_by_inclusion(graph)
    end_time = time.perf_counter()
    print(len(result))
    wrFile(result)
    print("algorythm: "+"{:g} ms".format((end_time - start_time)*1000))



if __name__ == "__main__":
    main()