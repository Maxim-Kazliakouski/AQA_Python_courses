#!/bin/bash

file='1.txt'
folder='test_folder'
file_creating=$(touch $file)
folder_creating=$(mkdir $folder)
echo "Folder $folder and file $file are creating..."
sleep 2
echo
echo "Enter rout to the file or folder:"
read ROUT
echo "Checking file..."

if [[ -f $ROUT/$file ]]
then
echo "File $file is existed"
else
echo "File $file doesn't exist"
fi
echo
echo "Checking folder..."

if [[ -d $ROUT/$folder ]]
then
echo "Folder $folder is existed"
else
echo "Folder $folder doesn't exist"
fi

echo
echo "Deleting folder -> $folder and file -> $file..."
sleep 3
rmdir $folder
rm $file
echo "The end :)"

