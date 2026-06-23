
class PatternMatcher:
    def __init__(self,txt):
        self.txt=txt
        self.postions=[]


    def find(self,pattern):
        self.positions=[]
        
        for i in range(len(self.txt)- len(pattern)+1):
            match=True

            for j in range (len(pattern)):
                if self.txt[i + j] != pattern[j]:
                    match=False

            if match==True:
                self.positions.append(i)
            
        return len(self.positions), self.positions
    

pm=PatternMatcher("abaakljabaabaazyxabaauioabaaui")
times,positions=pm.find("abaa")
print(f"{times} times found")
print(f"At: {positions}")