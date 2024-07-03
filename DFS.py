def create_graph(node, children):
    if node not in graph:
        graph[node]=children

def dfs(visited, node, destination):
    if node not in visited and destination not in visited:
        print(node, end=' ')
        visited.append(node)
        for children in graph[node]:
            dfs(visited, children, destination)

graph={}
visited=[]
queue=[]

create_graph('10',['20','30'])
create_graph('20',['40','50'])
create_graph('30',['60'])
create_graph('40',[])
create_graph('50',['60'])
create_graph('60',[])
print(graph)

source=input('Enter source:')
dest=input('Enter destination:')

print('\n Visited nodes:', end=' ')
dfs(visited, source, dest)