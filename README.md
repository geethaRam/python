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


