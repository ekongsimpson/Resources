## Kiosk preparation from scratch

Change internal SSD with at least 8GB (if you're using HW Praim C9010)
ISO-Boot-USB used: ubuntu-16.10-server-amd64.iso
Connect the TC or Kiosk-HW to LAN to be able to access the internet (reservation and FW rule)
Choose thelanguage: English
Install Ubuntu Server
If you run into DHCP issues, use static IP for the initial stages
User sudoers = userxxx pw=xxx
Choose guided partitioning
Follow the installation wizard
The boot partition required by GRUB must be /dev/sda - that's the internal SSD

After the installation login as user01
Then _sudo su_ –
change root user password:
_passwd root_
... 
Move on to SSH client (putty) using user01…..

![image](https://github.com/user-attachments/assets/39f515ee-ddf5-4f7d-b524-ea39264b0ce8)

Run the following:
  - _apt-get update_
  - _apt-get upgrade_
  - _reboot_

## Install the OpenBox graphics engine
  - a_pt-get install openbox xorg_

## Install firefox
  - _apt-get install firefox_

Carry out a test on the graphical screen with:
  - _startx_

Test firefox browser (right click)
Search for the _mKiosk_ plugin and install it
Download and install _noMachine_ for linux (.deb amd64)

![image](https://github.com/user-attachments/assets/a9e3a1de-dbf9-4e95-bd6f-d3735053dd38)

_dpkg -i nomachine_5.2.11_1_amd64.deb_

N.B. thanks to noMachine we'll be able to manage the kiosk, during the setup, via LAN and we'll be able to connect remotely via reverse SSH tunnel.

noMachine daemon port assignment, differentiating it from kiosk to kiosk:
_vim /usr/NX/etc/server.cfg_
e.g.:
![image](https://github.com/user-attachments/assets/5b568d71-9aba-4297-829d-370d774729e6)

Verify noMachine is running:

![image](https://github.com/user-attachments/assets/96e8f70d-88c8-4504-9299-65ab29f2cd22)

_enable_ it if that hasn't been done yet.

Open a noMachine client you installed on the PC you're using for management (NX protocol):

![image](https://github.com/user-attachments/assets/e3b121f4-f054-4fdd-8e3d-60000d0dd3a2)


## mKiosk plugin configuration
Start the browser by right-clicking on desktop
To invoke the mKiosk config → F11 (password: xxx)

![image](https://github.com/user-attachments/assets/680d1848-2ff3-4218-b141-82a1aaebeec0)

Library catalog consultation preparation (this is already in WL)

![image](https://github.com/user-attachments/assets/5a64a001-e07d-4358-8789-48659108bc54)
![image](https://github.com/user-attachments/assets/7f06c6c1-329b-4eb6-a85f-2aab418566bf)
![image](https://github.com/user-attachments/assets/b1f2ff91-0da0-4921-9873-d798576443f6)

## Make sure Firefox starts when the kiosk boots up

![image](https://github.com/user-attachments/assets/13eeedfb-8e24-4e39-a371-5b2b855ea5a9)
![image](https://github.com/user-attachments/assets/ccc0ac21-c9ff-479c-ac5a-b3fa573219ff)

## Make sure the Graphics server also starts automatically
Let's create a service for the graphics engine (give it a name of your choice)
![image](https://github.com/user-attachments/assets/f4bfa4ea-fe84-4e58-9b20-e7228b9a68bf)
![image](https://github.com/user-attachments/assets/cc83ec8f-5f75-48d7-ad68-8fd591615f16)

After that:
  -_ systemctl daemon-reload_
  - _systemctl enable mydesktop.service_

## SSH tunnel for remote management
Create a config file for SSH tunnel:
![image](https://github.com/user-attachments/assets/3404ae1f-0b64-4ff7-856f-83db26ed5652)
![image](https://github.com/user-attachments/assets/c7893927-e411-470c-b272-d884dabba581)

#!/bin/bash
if [[ `ps -ef | grep ssh` == *"2201:localhost:2201"* ]] || [[ `ps -ef | grep ssh` == *"4001:localhost:4001"* ]]
then
        echo "GOT IT"
else
        ssh -fNR 2201:localhost:2201 kioskcdm.comune.monza.it -p 2222
        ssh -fNR 4001:localhost:4001 kioskcdm.comune.monza.it -p 2222
fi

Where:
2222 is the management server port on your cloud provider - e.g. ARUBA
2201 is the SSH port that the ARUBA server can use to control the kiosk remotely
4001 is the noMachine port used by the ARUBA server for graphic remote control 
NB: the ..01 in the ports number conventionally identifies kiosk-site01
E.g. kiosk-site03 would be:
![image](https://github.com/user-attachments/assets/b9f802d7-608a-4e79-95a9-f8e9eff1dbc9)

Let's make it executable:
  - _chmod +x tunnel-compliance.sh_

Let's update the crontab:
  - _crontab –e_

![image](https://github.com/user-attachments/assets/7c200977-2851-4a0e-a392-7600835b4e3b)

Let's add the management SSH port for the tunnel (on the kiosk host):
![image](https://github.com/user-attachments/assets/863588c6-47ce-4085-adb6-f7f115ef7d2a)

Perform key exchange for SSH tunnel:
![image](https://github.com/user-attachments/assets/4a1e9ee5-05f6-44be-92a9-1af04023b31a)

![image](https://github.com/user-attachments/assets/88e2f246-1bd9-4f8d-b4ee-96d410e5be06)

On the ARUBA management server:
![image](https://github.com/user-attachments/assets/b4b11b05-d354-4f29-bb70-7820b3093a07)

It is possible to remotely control any kiosk from the ARUBA server
![image](https://github.com/user-attachments/assets/4aa192d9-d9b7-4572-9f3f-f78834decc23)
Where port 2203 (LOCAL) redirects the tunnel to kiosk-site03 thanks to the newly defined tunnel.

## Printer configuration
Let's assume the use of a Samsung ML 5510.
Installing the CUPS service:
  - _apt-get install cups_
Retrieve drivers from the manufacturer site if absent:
![image](https://github.com/user-attachments/assets/3650f101-8c12-4308-8e8b-15ee34ad3b6c)

![image](https://github.com/user-attachments/assets/6922b5b3-ea3b-49bc-834b-e8ec09eb2acd)

  - _tar –xvzf file_driver
  - ./install-printer.sh_

Configure the new printer via CUP from the browser (root privilege needed):

## Config Wifi

Network Installation:
  - _apt install network-manager manager_

Using nmtui interface:
![image](https://github.com/user-attachments/assets/c69095f8-5503-4f9f-b823-d6f929a228bb)

If there is no hotspot with the same SSID in the location where the kiosk will be installed, this network must be 
simulated with the use of a mobile phone in HS mode.

![image](https://github.com/user-attachments/assets/42bca07d-d4e1-486e-b37d-ed14a56b8128)

  - _reboot_

## TROUBLESHOOTING
1) The browser crashes

Edit /etc/xdg/openbox/autostart
![image](https://github.com/user-attachments/assets/c7f4d0bc-bfb5-4cc1-9939-548e1555b24f)
And comment off firefox (firefox &)

2) The left and right keys of the Mouse do not work outside the browser

Edit /etc/xdg/openbox/rc.xml
Comment off the following section:
![image](https://github.com/user-attachments/assets/140dfdb5-8180-4cdd-ba96-622dc0d14f1d)
And restart the desktop:
  - _systemctl restart mydesktop.service_

3) Delayed openinfg of the browser
Fixing the issues at number 2) should also address this too

4) Issues with WIFI
Edit /etc/systemd/system/network-online.target.wants/networking.service
Change delay timeout from 5 min to 30 sec.

