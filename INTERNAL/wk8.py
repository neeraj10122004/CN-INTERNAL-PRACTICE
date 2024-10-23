class Router:
    def __init__(self,name):
        self.name=name
        self.distance_vector={name:(name,0)}
        self.neighbors = {}
    def add_neighbor(self,neighbor,cost):
        self.neighbors[neighbor]=cost
        self.distance_vector[neighbor.name]=(neighbor.name,cost)
    def update(self):
        update = False
        for neighbor,cost_to_neig in self.neighbors.items():
            for destination,(next_hop,cost) in neighbor.distance_vector.items():
                new_cost = cost_to_neig + cost
                if destination not in self.distance_vector or new_cost<self.distance_vector[destination][1] :
                    self.distance_vector[destination]=(neighbor.name,new_cost)
                    update = True
        return update
    def __str__(self):
        ret = "table for "+self.name+ " \n"
        for dest,(next_hop,cost) in self.distance_vector.items() :
            ret+=dest + next_hop + str(cost) +"\n"
        return ret
    
def sum_dvr(routers):
    converged = False
    while not converged :
        converged = True
        for router in routers :
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