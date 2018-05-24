
# coding: utf-8

# In[3]:


total=int(input())
coins=list(map(int,input().split()))
def getWays(n, c):
    if len(c)==1:
        return 1
    elif len(c)>1:
        if n<c[-1]:
            return 1
        else:
            return getWays(n,c[0:-1])+getWays(n-c[-1],c)


        
ways=getWays(total,coins)
print(ways)


# In[ ]:




