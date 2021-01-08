def areSimilar(a, b):
    res = []
    for i in range(len(a)):
        if a[i] != b[i] :
            res.append(i)
    if len(res) != 0 and len(res) != 2:
        return False
    if len(res) == 0 : return True
    return a[res[0]] == b[res[1]] and a[res[1]] == b[res[0]]
    
 '''
 Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
 '''
