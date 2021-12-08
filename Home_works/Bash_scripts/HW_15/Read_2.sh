#!/bin/bash
echo -n "Enter a number:"
read NUMBER 

if [ $NUMBER -lt -1 ]
then
  echo "The number $NUMBER less than -1"
fi

if [ $NUMBER -eq -1 ]
then
  echo "The number $NUMBER equals -1"
fi

if [ $NUMBER -eq 45 ]
then
  echo "The number $NUMBER equal 45"
fi

if [ $NUMBER -gt -1 ] && [ $NUMBER -lt 45 ]
then
  echo "The result is -1 < $NUMBER <= 45"
fi

if [ $NUMBER -gt 45 ]
then
  echo "The number $NUMBER more than 45"
fi
