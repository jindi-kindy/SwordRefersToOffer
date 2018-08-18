def RenderGrid(m,n,cell):
    disArray=[[0 for i in range(m*2+1)] for i in range(n*2+1)]
    for i in cell:
        line=i.strip().split(' ')
        disArray[int(line[0][0])*2+1][int(line[0][2])*2+1]=1
        disArray[int(line[1][0])*2+1][int(line[1][2])*2+1]=1
        if((int(line[1][2])-int(line[0][2]))==1):
            disArray[int(line[0][0]) * 2 + 1][int(line[0][2]) * 2 + 1+1]=1
        elif((int(line[1][0])-int(line[0][0]))==1):
            disArray[int(line[0][0]) * 2 + 1+1][int(line[0][2]) * 2 + 1]=1
    for i in disArray:
        for j in i:
            if(j==0):
                print('[W] ',end='')
            else:
                print('[R] ',end='')
        print()

if __name__=="__main__":
    m,n=[int(i) for i in input().strip().split()]
    cell=[i for i in input().strip().split(';')]
    RenderGrid(m,n,cell)