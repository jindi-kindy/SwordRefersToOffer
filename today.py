#第一题
# def dfs(i,j,maxs,arrayList1):
#     # if arrayList1[i][j]==0:
#     #     return 0
#     arraystep=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
#     for x in range(8):
#         #把走过的路标记为陆地
#         arrayList1[i][j]=0
#         i=i+arraystep[x][0]
#         j=j+arraystep[x][1]
#         if arrayList1[i][j]==1:
#             maxs+=dfs(i,j,1,arrayList1)
#             arrayList1[i][j]==0
#         else:
#             i=i-arraystep[x][0]
#             j=j-arraystep[x][1]
#
#     return maxs
#
# if __name__=='__main__':
#     m, n = [int(i) for i in input().strip().split(',')]
#
#     arrayList1 = [[0 for i in range(n + 2)] for i in range(m + 2)]
#     for i in range(1, m + 1):
#         j = 1
#         line = input().strip().split(',')
#         for a in line:
#             arrayList1[i][j] = int(a)
#             j += 1
#     count=0
#     maxs=0
#     newmaxs=0
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if arrayList1[i][j]==1:
#                 count+=1
#                 newmaxs=dfs(i,j,1,arrayList1)
#                 print(newmaxs)
#             if newmaxs>maxs:
#                 maxs=newmaxs
#     print(str(count)+','+str(maxs))

#第二题
# m=int(input())
# arraylist=[]
# for i in range(m):
#     line1=input().strip().split(';')
#     for j in line1:
#         line2=j.strip().split(',')
#         arraylist1=[]
#         for x in line2:
#             arraylist1.append(int(x))
#         arraylist.append(arraylist1)
# arraylist=sorted(arraylist, key=lambda x: x[0])
# res=[]
# i=0
# while i<len(arraylist):
#     start_index=arraylist[i][0]
#     end_index=arraylist[i][1]
#     while i<len(arraylist) and end_index>=arraylist[i][0]:
#         end_index=max(end_index,arraylist[i][1])
#         i+=1
#     res.append((start_index,end_index))
# print(';'.join(str(temp[0])+','+str(temp[1]) for temp in res))


