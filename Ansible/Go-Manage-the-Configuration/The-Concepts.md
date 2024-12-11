## Control node<br/>
The node from which we run the Ansible CLI tools like $${{Red}ansible, \space ansible-vault, \space ansible-playbook \space etc}

## Managed nodes<br/>
These are the target devices, the hosts your configurations will be aiming at.

## Inventory<br/>
A list target devices which may contain info specific to each host like IP addresses. Inventory is also useful for assigning groups - e.g. a webserver group.

## Playbooks<br/>
A list of tasks that automatically runs for a specific inventory.<br/>
You'll need some knowledge of YAML to write or read a playbook.

## Plays<br/>
A Play is a playbook object.<br/>
It maps target devices to tasks. It's made up of implicit loop over mapped hosts and tasks.

## Role
To use any Role resource, it must first be imported into Play.
Roles could contain tasks, handlers, variables, plugins, templates and files for use in a Play.

## Tasks
The definition of an ‘action’ to be applied to the managed host. 
This could be an ad hoc command that makes use of ansible or ansible-console

## Handlers
This is a special Task that could be triggered by a previous Task
