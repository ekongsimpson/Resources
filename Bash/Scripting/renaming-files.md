## Rename all .jpg files in a folder<br />
### #Let's rename all files with .jpg extensions in myfiles directory<br />
### #Do not forget the shebang, #!/bin/bash at the start of your script.<br />
### #This simply tells the OS to use bash as an interpreter.

#!/bin/bash

DAY=$(date +%F)

cd /C/SCRIPTS/BASH/projects/myfiles

for FILE in *.jgp
 do
    mv $FILE ${DAY}-${FILE}
 done
