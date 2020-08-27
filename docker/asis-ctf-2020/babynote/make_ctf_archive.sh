#!/bin/bash
# In the name of Allah


scoreboard_server='69.172.212.23'
year=`date +%Y`
tasks_path="/opt/tasks/"
echo $tasks_path
ctf_user='asisctf'

if [ -z "$1" ]; then
    echo "No argument supplied, please pass a file or folder :)"
else
	fname=`echo $1 | cut -d'/' -f1`
	archive_name=$fname.txz

	echo 'Cleaning target...'
	find . -name .DS_Store | xargs -I file rm file


	echo 'Creating archive...'
	tar --owner="$ctf_user" -cJvf $archive_name $fname

	echo 'Calculate sh1sum checksum...'
	csum=`sha1sum $archive_name | cut -d' ' -f1`
	final_name=$fname"_$csum"".txz"
	echo $final_name
	mv $archive_name $final_name
	echo 'https://asisctf.com/tasks/'$final_name
	
	# Copy files to scoreboard server
	scp $final_name root@$scoreboard_server:$tasks_path
	ssh -t root@$scoreboard_server "chown -R www-data:www-data $tasks_path"
	
	echo '[Done]'
fi

