#!/bin/bash
folder_name='testing_folder'
echo Creating folder '->' $folder_name...
creating_folder=$(mkdir $folder_name)
sleep 2
echo Folder '->' $folder_name was created
rights_folder=$(ls -ld $folder_name)
echo Rights for the folder '->' $folder_name...
echo $rights_folder
echo

file_name='text_file'
file_expansion='.txt'
echo Creating file '->' $file_name$file_expansion
file_creating=$(touch $file_name$file_expansion)
sleep 2.5
rights_file=$(ls -l $file_name$file_expansion)
echo Rights for the file '->' $file_name$file_expansion...
echo $rights_file
echo

echo Changing rights for the file '->' $file_name$file_expansion...
chmod go-rwx $file_name$file_expansion
chmod u+rwx $file_name$file_expansion
new_rights_for_file=$(ls -l $file_name$file_expansion)
echo New rights for the file '->' $file_name$file_expansion
echo $new_rights_for_file
echo

echo Start downloading image into the folder '->' $folder_name...
sleep 2.5
cd $folder_name
wget https://bingvsdevportalprodgbl.blob.core.windows.net/demo-images/9b3b22ca-d065-40a9-b5d8-2296beb8c717.jpeg --no-check-certificate
echo
folder_file='picture.jpeg'
mv *.jpeg $folder_file
list=$(ls)
sleep 5
echo Contents of folder '->' $folder_name...
echo $list
echo

ls -l $folder_file > rights.txt
echo Displaying only $folder_file rights in folder '->' $folder_name...
image_rights=$(cut -c-12 rights.txt)
echo $image_rights
cd ..
echo

echo Removing folder '->' $folder_name and file '->' $file_name$file_expansion...
sleep 3
rm -rf $folder_name
rm $file_name$file_expansion
echo 'THE END :)'
