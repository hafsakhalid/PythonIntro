import random

def brick_tower(numlargebricks, numsmallbricks, height): 
    heightl = numlargebricks * 7
    heights = numsmallbricks * 2

    if(height <= heightl): 
        remainingheight = heightl - height 
        if(remainingheight == 0 or remainingheight % 7 == heights): 
            return True
    else: 
        remainingheight = height - heightl    
        if(remainingheight - heights == 0): 
            return True
        else: 
            return False

def get_triangle(num, letter): 
    if(num <= 0 or letter==""):
        raise ValueError ("Please do better")
    else: 
        for i in range(1, num+1): 
          print(letter*i)
        for j in range(num-1, 0, -1): 
            print(j*letter)        

#get_triangle(3, '@')

def sort_numbers(numlist):
    for i in range(len(numlist)): 
       for j in range(len(numlist)):
           if(numlist[i] % 2 == 0) and (numlist[j] % 2 != 0):
            temp = numlist[i]
            numlist[i] = numlist[j]
            numlist[j] = temp
    
    return numlist       


def select_vector(twolist, onelist): 
    answer = []
    if(len(onelist) != len(twolist)): 
        raise ValueError("Please do better")
    for i in range(len(twolist)): 
        #i = 0 
        #onelist[i] = -1
        #twolist[i] = [8, 4, 5]
        temp = twolist[i]
        if(len(temp) != (onelist[i])): 
            obj = temp[onelist[i]]
            answer.append(obj)
        else: 
            raise ValueError("Second Error")

    return answer


#print(select_vector([[8, 4], [5, 1], [9, 5]], [1, 2, 0]))

def get_coordinates(twolist, word): 
    answer = []
    for i in range(len(twolist)):
        for j in range(len(twolist[i])):
            if(word == twolist[i][j]): 
                obj = (i, j)
                answer.append(obj)

    return answer


w = [['cats', 'dogs'], ['cat'], ['', 'cats', 'CATS', 'cats'], []]
#print(get_coordinates(w, 'cats'))

def evaluate_polynomail(dictionary, x): 
    count = 0
    for key, value in dictionary.items(): 
        answer = (value*(x**key))
        count = count + answer
    return count

def anagrams(liststrings, string): 
    for i in liststrings: 
        i = i.lower()
        i = list(i)
        for j in string:
            j = j.lower()
            if j in i: 
                boolean = True
            else:
                boolean = False

    return boolean
   
#print(anagrams(['east', 'eats', 'seal'], 'seat'))

def refill_rack(rack, pool, n):
    #d1 = rack of player 
    # d2 = pool of player 
    # n = + integer 
    while(len(pool) > 1):
        key = random.choice(list(pool.keys()))
        if(key in rack.keys()): 
            rack[key] = rack[key] + pool[key]
            pool[key]=-1
        else: 
            rack[key] = pool[key]
            pool[key]=-1
    
        if(pool[key]==-1): 
            del pool[key]
        
        if(len(rack) >= n-1): 
            break

    
random.seed(5)
r1 = {'a': 2, 'k': 1}
b = {'a': 1, 'e': 2, 'h': 1, 'l': 2, 'n': 1, 'p': 2, 's': 3, 't': 2, 'z': 1}
refill_rack(r1, b, 7)
#print(r1)
#print(b)