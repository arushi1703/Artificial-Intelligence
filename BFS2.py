def create_graph(node, children):
    if node not in graph:
        graph[node]=children

def bfs(graph, node, destination):
    visited.append(node)
    queue.append(node)

    while queue:
        n= queue.pop(0)
        print(n, end=' ')

        for neighbour in graph[n]:
            if neighbour not in visited:
                visited.append(neighbour)
                if destination in visited:
                    break
                queue.append(neighbour)                

'''def find_path(l, destination):
    if destination in l:
        idx=l.index(destination)
        print(l[:idx+1])
    else:
        print('No path')'''

#graph = {'1':['2','3'], '2':['4','5'], '3':[], '4':[], '5':[]}
graph={}
visited=[]
queue=[]

create_graph('0',['2','1'])
create_graph('2',['1','4'])
create_graph('1',['2','3'])
create_graph('4',['2','3'])
create_graph('3',['1','4'])
print(graph)

source=input('Enter source:')
dest=input('Enter destination:')

print('\n Visited nodes:', end=' ')
bfs(graph, source, dest)
#find_path(bfs_list, dest)