"""
    @mat 2d list
    @nc number or rows
    @nr number of columns
    @peek value to find
    @locals
        @r right index of a row
        @l left index of a row
        @t top index of a column
        @b bottom index of a column
        @mc medium index of column
        @mr medium index of a row
"""
def binsearch_without_indexes(mat, nc, nr, peek):
    r = nc - 1
    l = 0
    t = 0
    b = nr - 1

    mc = -1
    while t <= b:
        count += 1
        mc = int(t + (b - t) / 2)
        if peek >= mat[mc][0] and peek <= mat[mc][r]:
            break;
        if peek < mat[mc][r]:
            b = mc - 1
        else:
            t = mc + 1
    if mc < -1:
        return False
    while l <= r:
        count += 1
        mr = int(l + (r - l) / 2)
        if mat[mc][mr] == peek:
            return True
        if peek < mat[mc][mr]:
            r = mr - 1
        else:
            l = mr + 1
    return False

def binsearch_with_indexes(mat, nc, nr, peek):
    l = 0
    r = (nc * nr) - 1
    print(r)
    while l <= r:
        m = int(l + (r - l) / 2)
        col = int(m % nc)
        row = int(m / nc)
        print(row)
        print(col)
        if peek == mat[row][col]:
            return [row, col]
        if peek < mat[row][col]:
            r = m - 1
        else:
            l = m + 1
    return False
