class Router :

    def __init__(self,name):
        self.name = name
        self.distance_vector = {name : (name,0)}
        self.neighbors = {}
    
    def add_neighbor(self,neighbor,cost):
        self.neighbors[neighbor]=cost
        self.distance_vector[neighbor.name] = (neighbor.name,cost)
    
    def update(self):
        updated = False
        for neighbors,cost_to_next in self.neighbors.items():
            for destination , (next_hop,cost_from_next) in neighbors.distance_vector.items():
                new_Cost= cost_from_next+cost_to_next
                if destination not in self.distance_vector or new_Cost < self.distance_vector[destination][1] :
                    self.distance_vector[destination]=(neighbors.name,new_Cost)
                    updated=True
        return updated
    def __str__(self):
        result = f"for node {self.name} table \n"
        for dest , (next_hop,cost) in self.distance_vector.items(): 
            result += f"{dest}  {next_hop}  {cost} \n"
        return result

def sum_dvr(Routers):
    converged=False
    while not converged :
        converged=True
        for router in Routers :
            if router.update() :
                converged = False


A = Router("A")
B = Router("B")
C = Router("C")
D = Router("D")


A.add_neighbor(B, 1)
A.add_neighbor(C, 4)

B.add_neighbor(A, 1)
B.add_neighbor(C, 2)
B.add_neighbor(D, 5)

C.add_neighbor(A, 4)
C.add_neighbor(B, 2)
C.add_neighbor(D, 1)

D.add_neighbor(B, 5)
D.add_neighbor(C, 1)


routers = [A, B, C, D]

sum_dvr(routers)

for router in routers :
    print(router)