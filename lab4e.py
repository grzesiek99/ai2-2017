def generate_triangles():
    n = 0
    total = 0
    while True:
        total += n
        n += 1
        yield total

def triangles_under(n):
    for triangle in generate_triangles():
        if triangle >= n:
            break
        print(triangle)
