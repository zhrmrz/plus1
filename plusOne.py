class Sol:
    def plus_one(self,list):
        num=int("".join(map(str,list)))
        num+=1
        new_list=[int(d) for d in str(num)]
        return new_list

if __name__ == '__main__':
    list=[1,2,3]
    p1=Sol()
    print(p1.plus_one(list))
