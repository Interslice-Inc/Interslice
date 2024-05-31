# Interslice
![Project Logo](https://github.com/Interslice-Inc/Interslice/blob/main/Files/Company_Logo/Interslice_Logo.jpeg)

Table of Contents
=================
<!--ts-->
  * [Project Overview](#project-overview)
  * [Team Members](#team-members)
  * [Team Agreemeent](#team-agreement)
  * [System Selection](#system-selection)
  * [Employee Handbook](#employee-handbook)
  * [Standard Operating Procedure](#standard-operating-procedure)
  * [Topologies/Visuals](#topologiesvisuals)
  * [Project Management Tool](#project-management-tool)
  * [Scripts](#scripts)
  * [Presentation Link](#presentation-link)
<!--te-->

## Project Overview
Our fictional company, InterSlice, Inc., has been hired to design and protect Cromulent Innovation's cloud infrastructure (also fictitious). For Cromulent Innovations, as a small startup scaling to a larger company, cloud infrastructure provides the greatest elasticity for growth and remote talent acquisition. InterSlice's contract with Cromulent Innovations includes implementing robust cloud security measures, setting up log aggregation (SIEM) components as well as ensuring CIS compliance.  The contract also stipulates a demonstration of the performance of the system when under attack. 

## Team Members
Meet the team behind Interslice:
* Steve Cherewaty [Github](https://github.com/SCherewaty) ! [LinkedIn](https://www.linkedin.com/in/steve-cherewaty-jr-b8727135/)
* Omar Ardid [Github](https://github.com/oardid) ! [LinkedIn](https://www.linkedin.com/in/ardidomar/)
* Julian Camilo Peña [Github](https://github.com/julianp91) ! [LinkedIn](https://www.linkedin.com/in/julian-pena-bb8643267/)
* Cody Blahnik [Github](https://github.com/Cody354) ! [LinkedIn](https://www.linkedin.com/in/cody-blahnik-/)

![ICQv](/Files/Company_Logo/ICQv.gif)


## Team Agreement
You can view our Team Agreement [here](/Files/PDF's_Files/Team_Agreement.pdf). This agreement outlines guidelines for communication, collaboration, decision-making processes, and conflict resolution within the team.

## System Selection
We selected the technology stack for Interslice based on the following criteria:
- **Scalability**: Choose scalable frameworks and tools to accommodate future growth and user demands.
- **Performance**: Prioritized technologies are known for their efficiency and speed to ensure optimal system performance.
- **Ease of Use**: Selected user-friendly tools to facilitate development and maintenance processes.
- **Community Support**: Preferred technologies with active developer communities for ongoing support and updates.

View the full System Selection [here](/Files/PDF's_Files/System_selection.pdf)


## Standard Operating Procedure
We follow a set of Standard Operating Procedures (SOPs) to maintain consistency and efficiency within the project:
<details>
<summary>Documents</summary>

  * [Compliance Documentation: Cloud Compliance](/Files/PDF's_Files/Cybersecurity_Compliance.pdf) 
  * [Cloud Security Incident Response Plan for Cromulent Innovations](/Files/PDF's_Files/Incident_Response_Plan.pdf) 

</details>
  
## Topologies/Visuals
Here are some visual representations of Interslice's architecture and topology:
* [General Topology](IGeneral_TOP.drawio.png)
* [Arch Topology](Arch_TOP.drawio.png)

## Project Management Tool
We use [Trello](https://trello.com/w/interslice2) to track our progress and tasks. In Trello, we organize tasks into boards, lists, and cards, representing different stages of development. Each card contains details such as task description, assignee, due date, and checklist items.

## Scripts
We have a collection of scripts used in the project for various purposes:
* [SSH Brute Force](/Files/Scripts/bruteforce.py) : This script is a collection of security-related tools, including network scanning, brute-force attack simulation, and file encryption for educational and testing purposes.
* [Lambda Script](/Files/Scripts/lambda_script.py) : This AWS Lambda function provides automated security measures to mitigate brute-force SSH attacks by monitoring failed login attempts and dynamically blocking users whose attempts exceed a defined threshold.
* [Lambda Script #2](/Files/Scripts/lambda_2nd.py) : This AWS Lambda function tracks SSH login attempts. If the number of attempts reaches three, it invokes another Lambda function (timeout_user_function) to potentially block the user. It uses Boto3 to interact with AWS services and returns a status message confirming the processing of the SSH attempt. This helps prevent unauthorized access and brute-force attacks.

## Presentation Link
View our live project presentation [here](/Files/Presentation.pdf) for an overview of Interslice's features and functionalities.<br>
Take a view of our project presentation slideshow [here](https://docs.google.com/presentation/d/1m3m5O-sK3qk8ESkDpDag1BTY4Q_qjwiAwv-tpqjp5qM/edit?usp=sharing)
