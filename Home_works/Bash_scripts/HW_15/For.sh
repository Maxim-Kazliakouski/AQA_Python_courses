#!/bin/bash

echo "The list from 10 to 1"
for i in {10..1}
do
echo "$i"
done

echo

echo "The list of even numbers:"
for n in {11..1}
do
      even=$(( $n % 2 ))
   if [ $even -eq 0 ]
   then
    echo "$n"
   fi
done
