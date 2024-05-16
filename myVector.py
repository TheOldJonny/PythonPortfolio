import math

class Vector():
    def __init__(self, array: list):

        self._array = array
      
    def norm(self):
        """It returns the norm of the vector"""
        
        norm = 0
        for el in self._array:
            norm += el * el
            
        return math.sqrt(norm)
    
    def sum(self):
        """It sums all the elements inside the vector """
        return sum(self._array)
    
    def __getitem__(self, i):
        """ It returns the i-th element of the vector"""
        try:
            return self._array[i]
        except:
            print("ERROR: Index outside the boundaries")
            
    def __eq__(self, vector):
        """Comparison between two vectors"""
        if len(self._array) != len(vector._array):
            print("Error: the two vectors have different sizes")
            return None
        
        return self._array == vector._array
    
    def __mul__(self, vector):
        """Dot product between two vectors"""
        if len(self._array) != len(vector._array):
            print("Error: the two vectors have different sizes")
            return None
        
        dot=0
        for i in range(len(self._array)):
            dot+=self._array[i] * vector._array[i]
        
        return dot
    
    def __add__(self, vector):
        """Sum between two vectors"""
        if len(self._array) != len(vector._array):
            print("Error: the two vectors have different sizes")
            return None
        
        sumList = []
        for i in range(len(self._array)):
            sumList.append(self._array[i] + vector._array[i])
        
        sumVector = Vector(sumList)
        return sumVector
        
    def __sub__(self, vector):
        """Subtraction between two vectors"""
        if len(self._array) != len(vector._array):
            print("Error: the two vectors have different sizes")
            return None
        
        difList = []
        for i in range(len(self._array)):
            difList.append(self._array[i] - vector._array[i])
        
        difVector = Vector(difList)
        return difVector
    
    def __len__(self):
        """Implementation of the len method"""
        return len(self._array)
    
    def __repr__(self):
        """String representation of the object"""
        myStr = "Object vector ["
        for i, el in enumerate(self._array):
            myStr += str(el)
            if i != len(self) -1:
                myStr += " "
        myStr+="]"
        return myStr
