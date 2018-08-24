# Python!

## Python datatypes:
int
float
str
bool

`height=12.34`

>Find a datatype of a variable
`type(variable)`

>String concatenation:
`str1+str2 = str1 *2` 

>Lists:
`students=[1,2,3,45,9]`
or 
>lists of list
`students=[["abc",1]
["def",2],
["xyz",3]]`

>Zero based index
Positive index and negative index
Positive goes from lowest index ti higheest
Negative index goes from backwards - last element in the list to first element
`list_eg =[1,2,3,4,5]`
`list_eg[2]=list_eg[-3]`

### List slicing:
> Can fetch a range of values.
`list_eg[2:4]`
this gets values from index 2 and 3
start index: inclusive
end index: exclusive
So, in this case it will only get values from index 2 to 4 while 2 is inclusive but 4 is not

`list_eg[2:]`
this means it will get all elements from index 2 upto the end of the list

`list_eg[:3]`
this will get all the elements starting from beginning upto the 3rd index

### List manipulation:
Adding elements to list:
`list_eg=list_eg+[4]`
now,element 4 is added to the list
to remove an element from the list:
`del(list_eg[2])`
deletes the second index in the list

### List assignment
`list1=list_eg`
what this does is it adds a reference of list1 to the same memory of list_Eg.
So, this means that both the variables are pointing to the same block of memory. Hence any changes to the elements in the list for variable list1 will also impact the other variable.
To create another memory block with a different variable but same values of the list_eg
`list1=list(list_eg)`
or
`list1=list_eg[:]`

### List Comprehension
If you used to do it like this:
new_list = []
for i in old_list:
        new_list.append(expressions(i))
#You can obtain the same thing using list comprehension:
new_list = [expression(i) for i in old_list]

## Functions & Methods

### Builtin Functions
1.max() - Input: List, Output: one element
2.round() - Input: number, number of digits (optional  arg, default=0)
3.sorted () -  sorting a list
4.len()
5.help(function name) - documentation of the function
6. Type casting methods : str(),int(),float(),bool()

### Builtin Methods
** In python, everything is an object. Every object has methods associated with it. Depending on the type of the object: the available methods are different **

Examples of methods:
For String : `replace(), capitalize(), index(), etc`
For List : `index(), count(), etc`

### Packages
> Directory of python scripts
  Each script = module
  Specify functions, methods and types

> How to install packages in local
  Download get-pip.py
  Terminal : `python get-pip.py`
  pip install numpy

> Importing package
   import numpy
   `test_array = numpy.array()`
   
### Numpy 

Numeric Python
 > This is alternative to Python list
 Calculations over entire array
 Fast operations
 > Installing 
 `pip install numpy`
 
Numpy arrays can contain only one type. If your regular Python list has multiple types in it - str, int. When you create a numpy array from that list - then it will make all the elements in one type 

Numpy can perform operations at the element-wise without having to go over the items in the list in an explicit for loop
`array1 + array2` -  will add individual elements from the arrays
rather the same will append both the arrays if they are regular python arrays

>Type of Numpy arrays
They are N-Dimensional array
You can create 2D arrays in numpy like this : 
`np.array([[1,2,3],[4,5,6],[7,8,9]])`
You can access the elements like this : `array[0][2]` or `array[0,2]`
You can get the dimensions of the numpy arrays by using the shape: `array.shape`

> numpy can automatically convert Python List of Lists into multi-dimensional arrays
If your 2D numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.

`# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]`

### Accessing elements in numpy Arrays
`import numpy as np
np_x = np.array(x)
np_x[:,0]`
For regular Python lists, this is a real pain. For 2D numpy arrays, however, it's pretty intuitive! The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.

`# Print out the 50th row of np_baseball
print(np_baseball[49:])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]
print(np_weight)

# Print out height of 124th player
print(np_baseball[123,0])`
