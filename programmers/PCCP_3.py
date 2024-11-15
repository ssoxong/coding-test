def solution(points, routes):
    visited = set()
    dup = set()
    for r in routes:
        time = 0
        for i in range(len(r)-1):
            sx, sy = points[r[i]-1][0]-1, points[r[i]-1][1]-1 
            ex, ey = points[r[i+1]-1][0]-1, points[r[i+1]-1][1]-1
            
            # If we've already visited this point at this time, add it to the duplicates
            if (sx, sy, time) in visited:
                dup.add((sx, sy, time))
            else:
                visited.add((sx, sy, time))

            # Move from start to end point, incrementing time
            while (sx, sy) != (ex, ey):
                if sx < ex: sx += 1
                elif sx > ex: sx -= 1
                elif sy < ey: sy += 1 
                elif sy > ey: sy -= 1
                time += 1
                
                # If we've already visited this point at this time, add it to the duplicates
                if (sx, sy, time) in visited:
                    dup.add((sx, sy, time))
                else:
                    visited.add((sx, sy, time))

    return len(dup)

# Test case
points, routes = [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]
print(solution(points, routes)) # Output: 0