#!/bin/bash

#If you had log files with .log extensions, you could rename them with the following code:

one=.1
declare -a NEWLOG=()
for i in *.log;
do 
        string-cutter=`echo $i | rev | cut -d. -f2 | rev`
        after-the-cutter=$(echo $i | sed "s/$string-cutter/$string-cutter$one/g")
        NEWLOG+=($after-the-cutter)
done
echo "${NEWLOG[@]}"