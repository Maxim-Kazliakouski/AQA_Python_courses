#!/bin/bash

echo -n "Enter a number: "
read NUMBER

if [ $NUMBER -gt 15 ] && [ $NUMBER -lt 45 ]
then
  echo "15 <= $NUMBER <= 45" 
fi

if [ $NUMBER -lt 15 ]
then
  echo "$NUMBER less then 15"
fi

if [ $NUMBER -gt 45 ]
then
  echo "$NUMBER more than 45"
fi
if [ $NUMBER -eq 15 ]
then
  echo "You choose $NUMBER"
fi
if [ $NUMBER -eq 45 ]                
then
  echo "You choose $NUMBER"
fi
