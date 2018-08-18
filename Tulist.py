# n,m=[int(i) for i in  input().strip().split()]
# array=[int(i) for i in input().strip().split()]
#
# dict={}
# for i in array:
#     if i not in dict.keys():
#         dict[i]=1
#     else:
#         dict[i]+=1
# if (len(dict)!=n):
#     print(0)
# else:
#     mins = min(dict, key=dict.get)
#     print(dict[mins])

# n,k=[int(i) for i in input().strip().split()]
# nums=[int(i) for i in input().strip().split()]
# wake=[int(i) for i in input().strip().split()]
#
# sums=0
# for i in range(n):
#     if wake[i]==1:
#         sums+=nums[i]
#     i+=1
#
# maxs=0
# for i in range(n):
#     if wake[i]==0:
#         num=sums
#         for j in range(i,min(i+k,n)):
#             if wake[j]==0:
#                 num+=nums[j]
#             j+=1
#         maxs=max(maxs,num)
#     i+=1
# print(maxs)

n=int(input())
array1=[int(i) for i in input().strip().split()]
m=int(input())
array2=[int(i) for i in input().strip().split()]
print(array2)
length=len(array1)

arrays=[]
for i in array2:
    sums=0
    for j in range(length):
        sums+=array1[j]
        if sums>=i:
            arrays.append(j+1)
            break
print(','.join(str(i) for i in arrays))