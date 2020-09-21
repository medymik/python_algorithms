"""
    @lst 1d list
    @peek a value to find
    @l left index of the list
    @r right index of the list
    @locals
        @m medium index of a row
"""
def binsearch_iterative(lst, peek, l, r):
    while l <= r:
        m = int(l + (r - l) / 2)
        if lst[m] == peek:
            return True
        if peek < lst[m]:
            r = m - 1
        else:
            l = m + 1
    return False

def binsearch_recursive(lst, peek, l, r):
    if l > r:
        return False
    m = int(l + (r - l) / 2)
    if lst[m] == peek:
        return True
    if peek < lst[m]:
        r = m - 1
    else:
        l = m + 1
    return binsearch_recursive(lst, peek, l, r)
