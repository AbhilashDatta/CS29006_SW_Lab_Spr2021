# In this python file, only the definations for the magic functions and the basic operations
# for the question segments are provided. There may be the need to add new functions or overload 
# existing ones as per the question requirements.

class Vector:
    
    def __init__(self, *args): 

        # if arg is an int(dimension)
        if isinstance(args[0], int): 
            self._coords = [0]*args[0]

        else:
            self._coords = []
            for i in args[0]:
                self._coords.append(i)

    def __len__(self):
        # return the dimension of the vector
        return len(self._coords)

    def __getitem__(self, j):
        # return the jth coordinate of the vector
        return self._coords[j]

    def __setitem__(self, j, val):
        # set the jth coordinate of vector to val
        self._coords[j] = val

    def __add__(self, other):
        # u + v
        try:
            if len(other) != len(self): 
                raise ValueError("Dimension mismatch -Operation not possible")
        except ValueError as ve:
            print(ve)
            return Vector(1) 

        resultant = []
        for i in range(len(other)):
            resultant.append(other[i]+self._coords[i])
        return Vector(resultant)
            
    def __eq__(self, other):
        # return True if vector has same coordinates as other
        if len(other) == len(self._coords):
            for i in range(len(other)):
                if(other[i]!=self._coords[i]): return False
            return True
        
        else: return False

    def __ne__(self, other):
        # return True if vector differs from other
        if other == self: return False
        else: return True
    
    def __str__(self):
        # return the string representation of a vector within <>
        str_rep = "<"+str(self._coords[0])
        for i in range(len(self._coords)):
            if i!=0: str_rep += ", " + str(self._coords[i])
        str_rep += ">"
        return str_rep

    def __sub__(self, other):
        # Soln for Qs. 2
        try:
            if len(other) != len(self): 
                raise ValueError("Dimension mismatch -Operation not possible")
        except ValueError as ve:
            print(ve)
            return Vector(1) 

        resultant = []
        for i in range(len(other)):
            resultant.append(self._coords[i]-other[i])
        return Vector(resultant)
    
    def __neg__(self):
        # Soln for Qs. 3
        result = []
        for i in self._coords:
            result.append(-1*i)
        return Vector(result)
    
    def __rmul__(self, value):
        return (self * value) 
    
    def __mul__(self, other):
        # Soln for Qs. 4, 5 and 6
        result = []
        
        if isinstance(other,int) or isinstance(other,float):
            for i in self._coords:
                result.append(other*i)
            return Vector(result)
        
        if isinstance(other,Vector):
            try:
                if len(other) != len(self): 
                    raise ValueError("Dimension mismatch -Operation not possible")
            except ValueError as ve:
                print(ve)
                return Vector(1) 

            for i in range(len(other)):
                result.append(self._coords[i]*other[i])
            return sum(result)

    
def main():
    # Add suitable print statements to display the results
    # of the different question segments

    #Testing Constructors
    v1 = Vector(5)  #vector of 1 zeroes
    v2 = Vector(7)  #vector of 7 zeroes
    v3 = Vector([1,2,3,4,5]) #Iterable of type list
    v4 = Vector((6,7,8,9,10)) #Iterable of type tuple
    
    #Testing len
    print('\nTesting len\n')
    print(len(v1),len(v2),len(v3))

    #Testing getitem
    print('\nTesting getitem\n')
    print(v1[4])
    print(v2[6])
    print(v3[4])

    #Testing setitem
    print('\nTesting setitem\n')
    v3[3] = 6
    v1[3] = 8
    print(v3[3],v1[3])

    #Testing add
    print('\nTesting add\n')
    v5 = v3+v4
    print(v3,v4,v5)

    #Testing eq and ne
    print('\nTesting eq ne\n')
    v6 = v1
    print(v1==v6,v5==v3,v1!=v6)
    
    #Testing str
    print('\nTesting str\n')
    print(v5)

    #Testing sub
    print('\nTesting sub\n')
    v7 = v5-v3
    print(v5,v3,v7)

    #Testing neg
    print('\nTesting neg\n')
    print(v1,-v1)

    #Testing mul rmul
    print('\nTesting mul rmul\n')
    print(v3,2*v3,v3*2)
    print(v3,2.5*v3)
    print(v1,v3,v1*v3)



if __name__ == '__main__':
    main()