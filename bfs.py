gra={
    '1':['8','5','2'],
    '2':['9'],
    '8':['6','4','3'],
    '6':['10','7']
}
start=input('Enter the starting node: ')
desired=input('Enter the desired node: ')
queue=[]
queue.append(start)
visited=[]
while queue:
    node=queue[0]
    queue.pop(0)
    if node not in visited:
        visited.append(node)
        if node in gra:
            queue.extend(gra[node])
        if node==desired:
            print('Found')
            break
print("Visited ",visited)
path=[]
path.append(desired)
while path[-1]!=start:
    for keys in gra:
        if path[-1] in gra[keys]:
            path.append(keys)
print("Path ",path[::-1])