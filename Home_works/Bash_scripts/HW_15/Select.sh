#!/bin/bash
echo "Do you want to install Python?"
PS3="Make you choice 1 or 2: "
select answer in "Yes" "No"
do
echo $answer
if [ "$answer" == "Yes" ]
then
echo "You have chose to install Python"
fi
if [ "$answer" == "No" ]
then      
echo "Go away and close the door!"
fi
break
done
