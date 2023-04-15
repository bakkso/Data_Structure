class ArrayList:		  
    def __init__( self ):
        self.items = []
    """
    def __str__(self): #테스트 코드에서 print를 사용하기 위해서 꼭 선언해줘야됨
    
        return str(self.items)
    """
    def insert(self, pos, elem) :
        self.items.insert(pos, elem)
    def delete(self, pos) :
        self.items.pop(pos)
    def isEmpty( self ):
        return self.size() == 0
    def getEntry(self, pos) :
        return self.items[pos]
    def size( self ):
        return len(self.items)
    def clear( self ) :
        self.items = []	
    def find(self, item) :
        return self.items.index(item)
    def replace(self, pos, elem) :
        self.items[pos] = elem
    def sort(self) :
        self.items.sort()
    def merge(self, lst) :
        print("lst: ", lst)
        print("self.items: ", self.items)
        self.items.extend(lst)
        print("extend:", self.items)
    def display(self, msg='ArrayList:' ):
        print(msg, self.size(), self.items)
        
        
    def findLargestNumber(self):
        if self.isEmpty():
            print("x")
            return None
        else:
            Largest = 0
            for i in range(1,self.size()):
                if self.items[i] > self.items[Largest]:
                    Largest = i
            #print("items", self.items)
            return self.items[Largest]  
        
    def findSmallestLargestNumber(self):
        if self.isEmpty():
            return None
        else :
            Largest = 0
            Smallest = 0
            for i in range(1,self.size()):
                if self.items[i] >self.items[Largest]:
                    Largest = i
                elif self.items[i] < self.items[Smallest]:
                    Smallest = i
            return (self.items[Largest], self.items[Smallest])
    
    def findsameIndex(self,B):
        for i in self.items: #s1으로 사용한 same 이니까 s1을 self로 쓰는것임. 자료구조 교재 77쪽 참고
            
            if i in B.items:
                return True
        return False
    
    def Merge2List (self,B):
        self.items.sort() # 첫번째 배열을 정렬
        B.items.sort()  # self사용하지 않는 이유 : n.data와 같은 이유 - s1.Merge2List(s2)에서 s1의 메소드만 사용하고 s2의 메소드는 사용하지 않았기때문에 s2에 해당되는 B에는 self를 안 써도 되는것이다.
        self.merge(B.items) # 원래는 FinalList라는 곳에 로 저장해놨는데 extend는 self.items 그 자체에 extend 되는건데 생뚱맞은 FinalList에 할당을 해줬으니 None이 나오는 것은 당연한 것
        # FinalList = self.merge(B.items) -> 'merge'메소드 호출 결과를 잘못된 변수(FinalList)에 할당하여 값이 나오지 않음.
        self.items.sort()
        a = self.items
        return a
s1 = ArrayList()    
s2 = ArrayList()

for i in range(1, 4):
    s1.insert(i-1, i)
for i in range(3, 7):
    s2.insert(i-3, i)

#print()을 사용하기 위해선 __str__ 필수
print(" max: ", s1.findLargestNumber())

print(" max : ",s2.findLargestNumber())

print(" max & min : ", s1.findSmallestLargestNumber())

print(" max & min : ", s2.findSmallestLargestNumber())

print(" same : ", s1.findsameIndex(s2))

print(s1.Merge2List(s2)) # s1의 items에 s2를 extend , 메소드만 사용한 것. Merge2List의 return값이 없으니까 출력되는 것이 없는 것이 당연.
print(" merge : " , s1.items) # s1의 리스트 출력 
