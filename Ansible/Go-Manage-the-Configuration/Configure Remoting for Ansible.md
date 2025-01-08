## SETTING UP WINDOWS FOR ANSIBLE MANAGEMENT

**PowerShell remoting with Active Directory**
- Download and run [this](https://github.com/ekongsimpson/Resources/blob/main/Ansible/Go-Manage-the-Configuration/ConfigureRemotingForAnsible.ps1)

**PowerShell remoting without Active Directory**
- To use PowerShell remoting without Active Directory, we need a few extra steps.

The command below adds your local subnet (the 192.168/16 subnet in this case) to your trusted hosts to allow other systems on your network to execute scripts.

_Set-Item -Path WSMan:\localhost\Client\TrustedHosts -Value 192.168.* -Force_<br/>

To apply the changes, you have to restart the WSMan service:

_Restart-Service WSMan_<br/>

If both machines are in the same Active Directory domain, you should have credentials that PowerShell remoting can use. However, this is different with standalone machines; you must create the credentials.

The command below prompts the user to enter a password for the remote admin user. It stores the resulting credentials object in the $creds variable and displays Remote Credentials as the prompt message.

_$creds = Get-Credential -UserName remote_admin -Message "Remote Credentials"_<br/>

![image](https://github.com/user-attachments/assets/2f061c8f-08e1-4af4-8859-cbd67f2c19fd)


Now connect to the remote host:

_$httpsOptions = New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck_<br/>
_Enter-PsSession -UseSSL -ComputerName "remote.local" -Credential $creds -SessionOption $httpsOptions_<br/>

The remote computer's hostname is remote.local on a local subnet. Because we are on a local system, and the TLS certificates are self-signed and not trusted, we must add session options to the connection.

Thanks to [**Evi Vanoost** - the Assistant Director for the Office of Research at the University of Rochester](https://4sysops.com/archives/enable-windows-remote-management-winrm-for-ansible/) for providing this invaluable guide.
