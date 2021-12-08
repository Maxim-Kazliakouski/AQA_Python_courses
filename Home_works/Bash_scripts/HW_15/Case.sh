#!/bin/bash

echo -n "Enter symbol, number or letter:"
read VAR

symbols='! @ # $ % ^ & * ( ) . , / \ | { } [ ] ~ '
letters={a..z}

for item in {-9999..9999}
do
if [ "$VAR" == "$item" ]
then
echo $VAR - is a number
fi
done

for item in {A..Z}
do
if [ "$VAR" == "$item" ]
then
echo $VAR - is a letter in upper register
fi
done

for item in {a..z}
do
if [ "$VAR" == "$item" ]
then
echo $VAR - is a letter in lower register
fi
done

for item in $symbols
do
if [ "$VAR" == "$item" ]
then
echo $VAR - is a specsymbol
fi
done
