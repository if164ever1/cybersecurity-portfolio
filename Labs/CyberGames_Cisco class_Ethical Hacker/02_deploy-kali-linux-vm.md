# Lab: Deploy a Pre-Built Kali Linux Virtual Machine

## Lab Overview

| Attribute | Details |
|-----------|---------|
| Course | Cisco Networking Academy - Ethical Hacker |
| Difficulty | Beginner |
| Time Required | 30-45 minutes |
| VM Credentials | Username: kali / Password: kali |

---

## Objectives

- Deploy a customized Kali Linux VM on AMD/Intel chip-based computer using VirtualBox
- Deploy a customized Kali Linux VM on ARM M1/M2 chip-based MacOS using UTM
- Explore basic Linux commands and privilege escalation concepts

---

## Required Resources

| Resource | Minimum Requirement |
|----------|---------------------|
| RAM | 4 GB |
| Free Disk Space | 50 GB |
| Internet | Required for downloads |
| Virtualization | Must be enabled in BIOS/UEFI |

---

## Part 1: Deploying Kali VM on AMD/Intel Chip-based Computer

This section applies to Windows, Linux, and Intel-based MacOS systems.

### Step 1: Download and Install VirtualBox

1. Navigate to https://www.virtualbox.org/
2. Click the download link on the main page
3. Select the appropriate installation file for your operating system
4. Run the installer and accept default installation settings

### Step 2: Download the Pre-Built Customized Kali

1. Navigate to the Resource Hub from netacad.com (https://www.netacad.com/resources/lab-downloads?courseLang=en-US)
2. Download the OVA file for the Ethical Hacker course
3. Note the download location on your computer

### Step 3: Deploy the VM in VirtualBox

1. Open VirtualBox
2. Click File > Import Appliance
3. Select the downloaded Kali.ova file
4. Click Next to continue
5. Review appliance settings (increase RAM if desired)
6. Click Finish to import
7. Click Start to power up the VM

### VM Configuration Details

| Setting | Value |
|---------|-------|
| Memory | 4 GB |
| Processors | 2 |
| Hard Disk | 39.1 GB (IDE) |
| Network Adapter | Bridged (Automatic) |
| Display | Auto detect |

Screenshot: VM configuration in VMware Workstation

![VM Configuration](../images/CyberGames_Cisco%20class_Ethical%20Hacker/deploy-kali-linux-vm/01-vm-configuration.png)

---

## Part 2: Deploying Kali VM on ARM M1/M2 Chip-based MacOS

This section applies to Apple Silicon (M1/M2/M3) Mac computers.

### Step 1: Download and Install UTM

1. Navigate to https://mac.getutm.app/
2. Click Download to get the free version
3. Install UTM after download completes

### Step 2: Download and Load the Pre-Built Customized Kali

1. Navigate to the Resource Hub from netacad.com
2. Download the Kali.utm.zip file
3. Note the download location
4. Unzip the archive
5. Double-click the unzipped file to open the VM in UTM

---

## Part 3: Exploring Linux

### Understanding Root Privileges

The root user in Linux is equivalent to the administrator user in Windows. Two commands provide access to root permissions:

| Command | Description |
|---------|-------------|
| su | Switch to root user (requires root password), use exit to return |
| sudo | Execute single command with root privileges (uses current user password) |

### Kali Linux Login Screen

Screenshot: Cisco Networking Academy Ethical Hacker Kali VM login screen

![Kali Login Screen](../images/CyberGames_Cisco%20class_Ethical%20Hacker/deploy-kali-linux-vm/02-kali-login-screen.png)

### Practical Exercises

#### Exercise 1: Demonstrating Permission Denied

Open terminal and attempt to edit sudoers file without privileges:

Command:
visudo

Output:
visudo: /etc/sudoers: Permission denied

Explanation: The /etc/sudoers file requires root privileges to view or edit.

Screenshot: Permission denied when running visudo without sudo

![Permission Denied](../images/CyberGames_Cisco%20class_Ethical%20Hacker/deploy-kali-linux-vm/03-permission-denied.png)

#### Exercise 2: Using sudo for Elevated Privileges

Execute the same command with sudo:

Command:
sudo visudo

Output: Opens the sudoers file in nano editor

Key configuration line in sudoers:
# Allow members of group sudo to execute any command
%sudo ALL=(ALL:ALL) ALL

This line grants all members of the sudo group permission to execute any command.

Exit: Press Ctrl+X (do not save changes)

Screenshot: Sudoers file opened with sudo visudo in nano editor

![Sudoers File](../images/CyberGames_Cisco%20class_Ethical%20Hacker/deploy-kali-linux-vm/04-sudoers-file.png)

#### Exercise 3: Verify Group Membership

Check if user kali belongs to sudo group:

Command:
grep sudo /etc/group

Output:
sudo:x:27:kali

Explanation: The output confirms user kali is a member of the sudo group (GID 27).

Screenshot: Verifying sudo group membership and sudoers file status

![Group Membership](../images/CyberGames_Cisco%20class_Ethical%20Hacker/deploy-kali-linux-vm/05-group-membership.png)

#### Exercise 4: Command History

View previously executed commands:

Command:
history

Sample Output:
1  visudo
2  sudo visudo
3  clear
4  sudo visudo
5  grep sudo /etc/group
6  hystory
7  clear
8  history

Screenshot: Command history output in terminal

![Command History](../images/CyberGames_Cisco%20class_Ethical%20Hacker/deploy-kali-linux-vm/06-command-history.png)

#### Exercise 5: Using History Shortcuts

Re-execute a command from history using exclamation mark:

Command:
!3

Result: Executes the command at position 3 in history

Alternative method - search by command prefix:
!gr

Result: Executes the most recent command starting with "gr"

#### Exercise 6: Tab Completion

Tab completion autocompletes commands, files, and directories:

Example:
ls /me[TAB]

Result: Completes to ls /media

---


## Key Commands Summary

| Command | Purpose | Example |
|---------|---------|---------|
| su | Switch to root user | su - |
| sudo | Execute command as root | sudo visudo |
| exit | Exit current shell/session | exit |
| visudo | Safely edit sudoers file | sudo visudo |
| grep | Search for patterns in files | grep sudo /etc/group |
| history | Display command history | history |
| !n | Execute command number n from history | !3 |
| !string | Execute most recent command starting with string | !gr |

---

## Important Files

| File | Purpose |
|------|---------|
| /etc/sudoers | Defines sudo privileges for users and groups |
| /etc/group | Contains group membership information |
| /etc/passwd | Contains user account information |

---

## Security Considerations

1. Principle of Least Privilege: Use sudo for specific commands rather than switching to root permanently
2. Sudoers Configuration: The sudoers file controls who can execute privileged commands
3. Audit Trail: Commands executed with sudo are logged for accountability
4. Password Caching: By default, sudo caches credentials for a short period (typically 15 minutes)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Virtualization not supported | Enable VT-x/AMD-V in BIOS/UEFI settings |
| VM runs slowly | Increase allocated RAM or CPU cores |
| Network not working | Check network adapter settings (NAT vs Bridged) |
| Permission denied errors | Verify sudo group membership and sudoers configuration |

---

## Lab Questions and Answers

Question: What command is displayed when you enter !3?

Answer: The command at position 3 in history is displayed and executed. Based on the history output in this lab, !3 would execute the clear command.

Question: What is the difference between su and sudo?

Answer: The su command switches the entire session to root user and requires the root password. The sudo command executes only a single command with elevated privileges using the current user's password. Sudo is preferred for security as it maintains audit logs and follows the principle of least privilege.

---

## Additional Notes

- The Kali VM was built on 2023 Aug 14
- Contains websploit content provided by Omar Santos
- Default desktop environment: XFCE
- Pre-installed with common penetration testing tools

---

## References

- VirtualBox Documentation: https://www.virtualbox.org/manual/
- UTM Documentation: https://docs.getutm.app/
- Kali Linux Documentation: https://www.kali.org/docs/

---

Tags: kali-linux, virtualization, virtualbox, utm, linux-fundamentals, privilege-escalation, ethical-hacking