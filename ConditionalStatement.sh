#This progarm will ask a user a Yes or No question and then print the answer

#!/bin/bash

#Print the prompt on the screen
echo "Do you like the color blue?"
echo -n "Enter \"y\" for yes, \"n\" for no: "

#Wait for the user input and then store the answer in ans
read ans

#Conditional statement will print out the answer
if [ "$ans" = "y" ]
then
    echo "You answered yes."
elif [ "$ans" = "n" ]
then
    echo "You answered no."
else
    echo "Your answer must be y or n."
    echo "Please start over."
fi
