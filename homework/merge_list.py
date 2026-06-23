class ListMerge:
    def merge(self,data1,data2):
        data=[]
        c1=0 #Current pointer for data1
        c2=0 #for data2

        while c1 <len(data1) and c2 <len(data2):
            if c1==len(data1):
                data.append(data2[c2])
                c2 +=1
            elif c2==len(data1):
                data.append(data2[c1])
                c1 +=1
            elif data1[c1]< data2[c2]:
                data.append(data1[c1])
                c1=c1+1
            else:
                data.append(data2[c2])
                c2=c2+1



if __name__ == "__main__":
    merger = ListMerge()
    
    data1 = [7, 19, 21, 44, 45, 54, 57]
    data2 = [16, 20, 34, 67, 89]
    
    result = merger.merge(data1,data2)
    print({result})