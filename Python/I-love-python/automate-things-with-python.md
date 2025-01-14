## List
The list methods make it very easy to use a list as a stack<br />
We can do this:<br />
```
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
```
[3, 4, 5, 6, 7]
```
stack.pop()
stack
```
[3, 4, 5, 6]
```
stack.pop()
```
6
```
stack.pop()
```
5
```
stack
```
[3, 4]

<br />
<br />
<br />


## SELF-SIGNED CERTIFICATE

To create a self-signed certificate on the fly follow these steps:

1. INSTALL PIP3:
   ```
   sudo apt install python3-pip
   ```
3. INSTALL CRYPTOGRAPHY
   ```
   pip3 install cryptography
   ```
5. GRAB [THIS](https://github.com/ekongsimpson/Resources/blob/main/Python/I-love-python/self-signed-certificate.py) PYTHON SCRIPT AND RUN IT
   ```
   python3 ./self-signed-certificate.py
   ```

<br />
<br />
<br />


## REMOVE SPACES FROM FILENAMES

RUN THE FOLLOWING IN THE FOLDER WHERE THE FILENAMES WITH SPACE ARE FOUND:
```
import os
for f in os.listdir("."):
   r = f.replace(" ","")
   if( r != f):
       os.rename(f,r)
```


