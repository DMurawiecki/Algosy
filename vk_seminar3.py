from collections import deque

def copyTime(n, x, y):
    l = 0
    r = (n - 1) * max(x, y)
    while l + 1 < r:
        mid = (r + l) // 2
        if mid // x + mid // y < n - 1:
            l = mid
        else:
            r = mid
    return r + min(x, y)

# print(copyTime(n=5, x=2, y=3))

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, val):
        self.queue.append(val)
    
    def pop(self):
        return self.queue.popleft()
    
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
    
    def getSize(self):
        return len(self.queue)

def isSubsequence(a, b):
    q = Queue()
    for el in a:
        q.push(el)
    
    for el in b:
        if q.peek() == el:
            q.pop()
    
    return q.getSize() == 0

# print(isSubsequence([2, 4, 6], [1, 2, 3, 4, 5, 6, 7]))

def binarySearchSqrt(target):
    l = 0
    r = target
    while l <= r:
        middle = (l + r) // 2
        middle_squared = middle ** 2
        if middle_squared > target:
            r = middle - 1
            continue
        if middle_squared < target:
            l = middle + 1
            continue
        return middle
    return r

# print(binarySearchSqrt(target =16))

def isPalindrome(s):
    l = 0
    r = len(s) - 1
    
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    
    return True

# print(isPalindrome("madam"))

def isSubsequence(s, t):
    ptr_s = 0  # Указатель для строки s
    ptr_t = 0  # Указатель для строки t

    while ptr_s < len(s) and ptr_t < len(t):
        if s[ptr_s] == t[ptr_t]:
            ptr_s += 1
        
        ptr_t += 1

    return ptr_s == len(s)


# print(isSubsequence(s= "abc", t= "ahbgdc"))

def removeAdjacentDuplicates(s):
    stack = []
    
    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)


# print(removeAdjacentDuplicates("cdffd"))  
# print(removeAdjacentDuplicates("uioouiouuo")) 