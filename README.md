#  Active Directory Automation with Python, PowerShell, and Ansible            
#  This capstone project automates the health check of all Domain controllers in the domain 

# Objectives 
 - Automate 'Dcdiag' and 'repadmin' report ,collect and store it in the Centralized repository(server)
 - Schedule the health and check and deliver this to the stakeholders via email

# Technologies Used
 - Ansible
 - Powershell
 - Python(modules: 'os' , 'datetime' ,'yagmail')
 - Windows Task Scheduler
 - Active Directory
 - Linux(Ansible Control)

# What we have in Repository
- AnsibleCode.txt
- PowerShellCode.txt
- PythonCode.txt

   AnsibleCode.txt
   - Objective of Ansible is to push out the dcdiag scripts to all Domain controllers(dcdiag-report.yml)
   - It is also used in pushing out a script to all DCs ,that schedule the task on all dcs so that the dcdiag script will runn evryday(schtask.yml)

   PowershellCode.txt
   - It has dcdiag and repadmin health check script.
   - also has some required scripts for this project(Pre-requisites for Ansible)

   PythonCode.txt
   - Contains actual python code that check the result of the report and looks for any failures and deliver the report to stakeholders via email

# Sample Output 
![image](https://github.com/user-attachments/assets/250ccef9-59cc-436e-b70c-006f9c513f3c)
