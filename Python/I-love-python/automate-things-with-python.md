## List
The list methods make it very easy to use a list as a stack<br />
We can do this:<br />
>>> stack = [3, 4, 5]<br />
>>> stack.append(6)<br />
>>> stack.append(7)<br />
>>> stack<br />
[3, 4, 5, 6, 7]<br />
>>> stack.pop()<br />
7<br />
>>> stack<br />
[3, 4, 5, 6]<br />
>>> stack.pop()<br />
6<br />
>>> stack.pop()<br />
5<br />
>>> stack<br />
[3, 4]<br />


## SELF-SIGNED CERTIFICATE

To create a self-signed certificate on the fly follow these steps:

1. INSTALL PIP3:
   - _sudo apt install python-pip3_
2. INSTALL CRYPTOGRAPHY
   - _pip3 install cryptography_
3. GRAB [THIS](https://github.com/ekongsimpson/Resources/blob/main/Python/I-love-python/self-signed-certificate.py) PYTHON SCRIPT AND RUN IT
   - _python3 ./self-signed-certificate.py_
