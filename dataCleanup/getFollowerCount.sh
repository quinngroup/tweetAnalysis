#! /bin/bash

while read line
do
	
	url="https://twitter.com/users/username_available?username="
	req="$url$line"
	IP=$(curl -s $req)
	if [[ $IP =~ .false.* ]]; then
		echo $line
	fi
done < part5.txt
