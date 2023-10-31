#This program will run a basic math problem and then see whether the product is 
#greater than, less than, or equal to the sum
#!/bin/bash

#Print the prompt on the screen
echo -n "Please enter your first integer: "

#Wait for the response and then store the variable in int1 
read int1

#Print the prompt on the screen
echo -n "Please enter your second integer: "

#Wait for the response and then store the variable in int2
read int2

#Math Operations as variables
sum=$(($int1 + $int2))
prod=$(($int1 * $int2))

#Print both the sum and the product
echo "The sum of $int1 and $int2 is $sum"
echo "The product of $int1 and $int2 is $prod"

#Logic to test whether the product is greater than, less than, or equal to the sum
if [[ "$prod" > "$sum" ]] #Alternatively I could have used [ $prod -gt $sum ]
then
    echo "The product is greater than the sum"
elif [[ "$prod" < "$sum" ]] #Alternatively I could have used [ $prod -lt $sum ]
then
    echo "The product is less than the sum"
elif [[ "$prod" == "$sum" ]]
then
    echo "The product and sum are equal"
fi
