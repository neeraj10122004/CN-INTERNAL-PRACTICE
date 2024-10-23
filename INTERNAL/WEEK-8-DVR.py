
def dvr(graph,n):
    
    distance = []
    for i in range(0,n):
        distance.append([float('inf')]*n)
    for i in range(0,n):
        distance[i][i]=0
    
    for i in range(0,n):
        for j in range(0,n):
            if graph[i][j]!=0 :
                distance[i][j]=graph[i][j]
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if distance[i][j] > distance[i][k]+distance[k][j] :
                    distance[i][j] = distance[i][k]+distance[k][j]
    return distance


graph = [[0,2,0,1,0],
         [2,0,3,2,0],
         [0,3,0,0,7],
         [1,2,0,0,1],
         [0,0,7,1,0]]


n = len(graph)

graph = dvr(graph,n)
print("Distance vector routing table : ")
for i in range(0,n):
    print(f"from node {i+1} : {graph[i]} ")