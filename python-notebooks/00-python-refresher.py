#!/usr/bin/env python
# coding: utf-8

# # Python Refresher

# In[2]:


x = 5 


# In[3]:


def good_enough(x, guess): 
    return abs((guess * guess) - x) < 0.00000000001

def improve_guess(x, guess): 
    return (guess + x/guess)/2 

def sqrt(x, guess=0.0001): 
    if good_enough(x, guess): 
        return guess 
    else: 
        return sqrt(x, improve_guess(x, guess)) 


# In[4]:


sqrt(36)


# In[5]:


p = 0
while (p < 10): 
    print(p)
    p += 1


# In[6]:


for i in range(10): 
    print(i)


# In[7]:


l = [1, 2, 4] 


# In[8]:


for i in [1, 2, 5]: 
    print("Square root of " + str(i)  + ": ",     end="") 
    print(sqrt(i))


# In[10]:


d = {1: "one", 
     2: "two"
    }


print(d[1])
print(d.items())


# In[11]:


for k, v in d.items(): 
    print(k, v)


# In[12]:


list(d.keys())


# In[13]:


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]

merged = list(zip(a, b))


# In[14]:


merged


# In[15]:


# Real world usecase of ZIP: combining column headers with row values 
# much more, along with usecases, here: 
# https://stackoverflow.com/questions/2429692

fields = ["id", "name", "location"]
values = ["13", "bill", "redmond"]
dict(zip(fields, values))


# **Very important:** When trying to solve any problem, first see if you can do it with lists or dictionaries (dynamic arrays and maps). These will solve a majority of your problems. 

# # OOP Concepts in Python

# Creating a class with a constructor is simple with a minor difference: <code>self</code> 

# To access member variables and methods, you must always use <code>self</code>. This is not optional as in other languages. 

# In[16]:


class Point:
    # constructors are defined using a special method, which must be named __init__ 
    
    def __init__(self, x=0, y=0): 
        self.x = x
        self.y = y 
        
    def __str__(self): 
        return "[" + str(self.x) + "," + str(self.y) + "]"


# In[17]:


p1 = Point()   # p1 is a reference variable 
print("p1 = ", p1.x)
print("p1 = ", p1)


p2 = Point(2, 4)    # notice that we do NOT pass in self. That is automatically done for us! 


print("p2 = ", p2.x)
print("p2 = ", p2)


# In[ ]:


print(p1)


# ## Composition 

# Composition is simple as always. 

# In[18]:


class Shape: 
    def __init__(self, points): 
        self.points = points 
    
    def __str__(self): 
        ret = "" 
        
        for i in self.points:
            ret += str(i) + " - "
            
        return ret 


# In[19]:


p1 = Point(5, 5) 
p2 = Point(10, 5) 
p3 = Point(5, 10) 
p = [p1, p2, p3]

sh = Shape(p)


# In[20]:


print(sh)


# We can add methods to class even after it has been defined! 

# In[24]:


def print_points(self): 
    for i in self.points: 
        print(i) 
        
Shape.print_points = print_points 


# In[25]:


sh.print_points()


# ## Inheritance 

# Inhertiance syntax is also slightly different but quite easy.

# In[26]:


class Triangle(Shape):    # Triangle inhertis from Shape 
    pass     # pass means I'm not going to have anything in this block 


# In[27]:


t = Triangle(p)


# In[28]:


t.print_points()   # automatically inherited 


# In[29]:


def get_area(self): 
    vertices = self.points
    n = len(vertices) # of corners
    a = 0.0
    for i in range(n):
        j = (i + 1) % n
        a += abs(vertices[i].x * vertices[j].y - vertices[j].x * vertices[i].y)
    return a / 2.0

Triangle.get_area = get_area 


# In[30]:


t.get_area()


# ## Access Parent Class' Overridden Methods 

# In[31]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def __str__(self): 
        return "L: " + str(self.length) + " W: " + str(self.width)


# In[32]:


rect = Rectangle(2, 4) 
print(rect)


# In[ ]:


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
    def __str__(self): 
        return "Square: " + super().__str__()


# In[ ]:


square = Square(4)
square.area()


# In[ ]:


print(square)


# ## Polymorphism 
# 
# You get that for free in Python. Just call the method. If it's overridden, the child class' method will be executed. 

# ## Access Modifiers 
# 
# There are none. By convention, methods starting with <code>_</code> are considered private and shouldn't be called from the outside. If you still want to do it, the response is, "good luck!". 

# See more details about classes on https://docs.python.org/3/tutorial/classes.html

# In[ ]:




