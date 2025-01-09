## TROUBLESHOOTING

ERROR: <br/>
**fatal: [XXX]: FAILED! => {"msg": "Missing sudo password"}**

SOLUTION: <br/>
- Ensure that **become** is set to **True** in ansible.cfg file. You'll find that under [privilege escalation].
- If "become = True" is present in your playbook, remove it.
