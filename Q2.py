def f(arr):
        k=8.99e9
        sumEi=0
        sumEj=0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j]=='o':
                    xo=j
                    yo=i
        #Ei=kq/r**2 * cos(x) ==> cos(x)=x/r
        #Ej=kq/r**2 * sin(x) ==> sin(x)=y/r
        for y in range(len(arr)):
            for x in range(len(arr[0])):
                    if arr[y][x]=='o':
                        continue
                    r=((x-xo)**2+(y-yo)**2)**0.5
                    q=int(arr[y][x])
                    if x-xo!=0:
                        sumEi+=(k*q/r**3)*(x-xo)
                    if y-yo!=0:
                        sumEj+=(k*q/r**3)*(y-yo)
        return f'E={sumEi}i+{sumEj}j'
arr=[]
x=0
print('''Enter the map then press "Enter"
use only numbers and "o"''')
while True:
    arr.append(input().split())
    if arr[x]==[]:
        break
    x+=1
arr.remove(arr[x])
print(f(arr))
arr_str='\n'.join(['\t'.join(map(str,row))for row in arr])
file=open('d:\\project\\New folder\\output.txt','w')
file.write(arr_str)
file.write(f(arr))
file.close()