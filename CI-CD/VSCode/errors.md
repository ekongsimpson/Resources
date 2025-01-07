[PROBLEM]: 

**remote: TF401019** error while trying to clone a repo from Azure DevOps to VSCode on Windows.

[SOLUTION]: 
- go to **control panel**
- search for **Manage your credentials**
- then **Windows Credentials**
- search and delete any line - under **Generic Credentials** - with the same url like the one you're trying to clone.
- that should help
