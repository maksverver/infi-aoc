def FloodFill(start, neighbors):
    '''Returns the set of vertices reachable from `start`, calculated using
       a flood fill algorithm. `neighbors` should be a callable object which,
       given a vertex, returns an iterable of adjacent vertices.'''
    todo = [start]
    seen = {start}
    for v in todo:
        for w in neighbors(v):
            if w not in seen:
                seen.add(w)
                todo.append(w)
    return seen
