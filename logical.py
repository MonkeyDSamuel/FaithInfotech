#LOGICAL OPERATORS

#AND - Both conditions must be TRUE
#OR - Atleast one condition must be true
#NOT - Reverses the condition

a = 10
b = 5
c = 20

#Logical AND
print(a>b and c>a)      #TRUE

#Logical OR
print(a<b or c>a)       #TRUE

#Logical NOT
print(not(a>b))     #not(TRUE) = FALSE
