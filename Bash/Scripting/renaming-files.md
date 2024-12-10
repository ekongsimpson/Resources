## $${\color{red}Rename \space all \space .jpg \space files \space in \space a \space folder \space Red}$$<br />
#### #Let's rename all files with .jpg extensions in myfiles directory<br />
#### #Do not forget the shebang, #!/bin/bash at the start of your script.<br />
#### #This simply tells the OS to use bash as an interpreter.<br /><br />

#!/bin/bash

DAY=$(date +%F)

cd /C/SCRIPTS/BASH/projects/myfiles

for FILE in *.jgp<br /><br />
$\hspace{5pt}$  do<br /><br />
    $\hspace{5pt}$ mv $FILE ${DAY}-${FILE}<br /><br />
 $\hspace{5pt}$ done<br /><br />
