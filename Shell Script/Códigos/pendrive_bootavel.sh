#!/bin/bash

confirmation=""
while [[ $confirmation != "done" ]]
do
	line_counter=$(ls ~/Downloads | grep .iso | wc -l)
	if [[ $line_counter -eq 1 ]]; then
		iso=$(ls ~/Downloads | grep .iso)
		echo "ISO: $iso"
	else
		files=$(ls ~/Downloads | grep .iso)
		while true; do
			counter=1
			array=()
			echo 
			for file in $files
			do
				echo "$counter - $file"
				array+=( "$file" )
				((counter++))
			done

			read -p 'Select an image (number): ' number
			if [[ $number -gt $line_counter || $number -le 0 ]]; then
				echo 'Invalid number. Try again.'
			else
				iso=${array[$number - 1]}
				echo "ISO: $iso"
				break
			fi
		done
	fi

	path_to_iso=~/Downloads/$iso
	confirmation="done"
done

while true; do
	echo
	lsblk
	read -p 'Device: ' device
	if [[ $device =~ ^sda.* || $device =~ ^sdb.* ]]; then
		echo 'Invalid device.'
	else
		echo "Device: $device"
		break
	fi
done

echo
echo "ISO...: $iso"
echo "Device: $device"
echo
read -p 'Continue? (y/n) ' permission
echo
if [[ $permission == "n" ]]; then
	echo 'Canceled!!!'
elif [[ $permission == "y" ]]; then
	sudo dd if=$path_to_iso of=/dev/$device bs=4M status=progress && sync
else
	echo 'Invalid character'
fi
