#!/bin/bash

echo -n "Enter a number: "
read NUMBER

if [[ $NUMBER -ge 0 ]]
then
  echo "$NUMBER is positive"
else
  echo "$NUMBER is negative"
fi
