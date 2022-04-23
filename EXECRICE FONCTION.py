#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Question 1

def max_trois(a,b):
     if a > b :
            return a
        else :   
        return b
def maximum (a,b,c) :
        return max_trois (a,max_trois(b,c))
print(maximum(int(input("Saisir le nombre premier ")),
              int(input("Saisir le nombre second ")),
              int(input("Saisir le nombre dernier "))))


# In[5]:


#Question 2

def calculation(x,y):
    return x+y ,x-y
x = int(input())
y = int(input())

calculation(x,y)


# In[17]:


#Question 4

myList = "vert-rouge-jaune-noir-blanc"

def joindre(mylist):
     L = mylist.split("-")
     L.sort()
     print("-".join(L))
joindre(myList)


# In[24]:


#Question 3

#########################################################

def somme(liste):
    total = 0
    for nombre in liste:
        total = total + nombre
    return total

liste = [1,5,3,9,3,5,5,7,1,2,8]

#########################################################

def listMultiply(L):
    n = 1  
    for x in L:
        n = n*x   
    return n
L = [1,5,3,9,3,5,5,7,1,2,8]

#########################################################
pair = []
impair = []
for i in range(0,len(L)):
        if i%2 == 0:
            pair.append(L[i])
        else:
            impair.append(L[i])
        
#########################################################

print("la somme des nombres d'indices paire :", somme(pair))
print("le produit des nombres d'indices impair :", listMultiply(impair))


# In[ ]:





# In[ ]:




