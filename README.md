# Developing a Persistent Monitoring Script

The goal of this exercise is to develop a Python script that simulates monitoring a user with enhanced persistence capabilities. This script will include functionalities for capturing keystrokes (keylogging), taking screenshots, system monitoring, and directory checking. Moreover, the script will encrypt all captured data before transmitting it to a server, ensuring secure storage and analysis of the data. This exercise is crucial for understanding how digital monitoring and espionage tools work and their relevance in the context of cybersecurity, especially for threat detection and data leakage prevention.

## Part 1: Advanced Capture and Monitoring

### Task 1: Keystroke and Screenshot Capture

> Implement a Keylogger: Develop a Python-based keylogger to capture all keystrokes made by the user and save this data in a log file. This keylogger will operate covertly in the background and will automatically initialize when the system starts. This exercise will help understand how user actions can be monitored without their knowledge.

> Capture Screenshots: Set up a mechanism to periodically capture and save screenshots of the user's screen in a specified directory. This is useful for understanding how visual information can be collected for analysis or evidence without alerting the user.

### Task 2: System Activity Monitoring

> Collect System Information: Write a function to collect critical system information, such as CPU usage, memory usage, and a list of currently running processes. This simulates surveillance over the user's computing environment, which is vital for identifying anomalous or malicious behavior.

### Task 3: Script Persistence

> Ensure Script Continuity: Design the script to ensure it remains active and continues executing even after the system restarts. This demonstrates how malicious programs can maintain persistence in an infected system, a common technique in malware and rootkits.

### Task 4: Directory Checking and ZIP File Creation

> Routine Check: Implement a routine that checks the contents of the TARGETDIR directory daily, compresses its content into a ZIP file, and prepares it for transmission to the server. This step is crucial for understanding how data can be periodically collected and prepared for exfiltration.

## Part 2: Data Encryption and Transmission

### Task 5: Data Encryption

> Encrypt Captured Data: Ensure that all captured data, including keystrokes, screenshots, and ZIP files, are encrypted before being sent to the server. This teaches the importance of encryption for data security during transmission, protecting sensitive information from interception.

### Task 6: Sending Encrypted Data

>Configure Data Transmission: Set up the script to securely transmit the encrypted data to a server. Here, you will learn how to ensure that data transfer between the client and server is conducted securely, using safe communication protocols.

## Part 3: Decoding and Notification Server

### Task 7: Python Server

> Server Development: Develop a server-side script that receives, decrypts, and processes the encrypted data sent by the monitoring script. This allows understanding the process of data reception and analysis in a server context, which is essential for cybersecurity operations and digital forensic analysis.

### Task 8: Integration with Telegram

> Notifications via Telegram Bot: Create a Telegram bot to receive and display notifications and alerts from the server about the captured data and other significant events. This shows how alert and notification systems can be integrated into cybersecurity operations to provide real-time monitoring and response.

## Wrap-Up

This exercise not only strengthens the technical understanding of how monitoring tools operate but also contextualizes the importance of these skills in protecting information and detecting malicious activities. It is an excellent opportunity to apply cybersecurity concepts in a practical and realistic scenario.

## Disclaimer: Educational Use Only

This material is provided exclusively for educational and learning purposes. The goal is to teach cybersecurity concepts, monitoring practices, and the importance of data protection in a controlled and ethical context.
