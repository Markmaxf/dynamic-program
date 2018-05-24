
# coding: utf-8

# In[14]:



nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().split()))
c.sort()
def getWays(n, c):
    if len(c)==1:
        return (1 if n%c[0]==0 else 0)
    elif len(c)>1:
        if n<c[-1]:
            return getWays(n,c[0:-1])
        else:
            return getWays(n,c[0:-1])+getWays(n-c[-1],c)


        
ways=getWays(n,c)
print(ways)


# In[ ]:





# In[ ]:





# In[ ]:




