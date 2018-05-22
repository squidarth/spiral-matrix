def spiral(n):
    counter = 0
    
    spiral_matrix = [ [0 for j in xrange(n)] for i in xrange(n)]
    loop_sizes = range(n, 0, -2)
    loop_size_start = 0
    for size_of_loop in loop_sizes:
        x = loop_size_start
        y = loop_size_start

        if size_of_loop == 1:
            counter += 1
            spiral_matrix[x][y] = counter

        for i in xrange(size_of_loop-1):
            counter += 1
            spiral_matrix[x][y] = counter
            y += 1

        for i in xrange(size_of_loop-1):
            counter += 1
            spiral_matrix[x][y] = counter
            x += 1

        for i in xrange(size_of_loop-1):
            counter += 1
            spiral_matrix[x][y] = counter
            y -= 1

        for i in xrange(size_of_loop-1):
            counter += 1
            spiral_matrix[x][y] = counter
            x -= 1

        loop_size_start += 1

    return spiral_matrix

print spiral(3)
