def reverseInParentheses(inputString):
    if(len(inputString) < 3): return ''
    opens = listOccurencesIndexes(inputString, '(')
    close = listOccurencesIndexes(inputString, ')')
    if len(opens) != len(close): return ''
    print(opens)
    print(close)
    i = 0
    j = 0
    while ( len(opens) > 0):
        if (opens[i] >= close[j] or i == len(opens) -1):
            if opens[i] < close[j] : inputString = reverse(inputString, opens[i], close[j])
            else: inputString = reverse(inputString, opens[i - 1], close[j])
            print(inputString)
            opens = listOccurencesIndexes(inputString, '(')
            close = listOccurencesIndexes(inputString, ')')
            print(opens)
            print(close)
            i = 0
            j = 0
        else :
            i += 1
    return inputString
    
    
            
def listOccurencesIndexes(s, c):
    indexes = []
    for i in range(len(s)):
        if s[i] == c :
            indexes.append(i)
    return indexes
    
def reverse(s, opens, close):
    temp = s[opens + 1 : close]
    temp = temp [::-1]
    s = temp.join([s[:opens], s[close + 1:]])
    return s
    

reverseInParentheses("(bar)") # Expected Output: "rab"
reverseInParentheses("foo(bar)baz") # Expected Output: "foorabbaz"
reverseInParentheses("foo(bar)baz(blim)") # Expected Output: "foorabbazmilb"
reverseInParentheses("foo(bar(baz))blim") # Expected Output: "foobazrabblim"
reverseInParentheses("(abc)d(efg)") # Expected Output: ""cbadgfe""
    
