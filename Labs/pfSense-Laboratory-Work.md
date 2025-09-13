# pfSense Laboratory Work

## 🔒 Overview

pfSense is a powerful open-source firewall and router platform based on FreeBSD. It provides comprehensive network security features including firewall protection, VPN services, intrusion detection/prevention systems (IDS/IPS), and network traffic monitoring capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [pfSense Roles in Network Security](#pfsense-roles-in-network-security)
- [Use Cases](#use-cases)
- [Lab Objectives](#lab-objectives)
- [Prerequisites](#prerequisites)
- [Lab Setup](#lab-setup)
- [Lab Exercise: Configuring and Installing a Firewall](#lab-exercise-configuring-and-installing-a-firewall)
- [Configuration Steps](#configuration-steps)
- [Verification and Testing](#verification-and-testing)
- [Troubleshooting](#troubleshooting)
- [Conclusion](#conclusion)

## 🛡️ pfSense Roles in Network Security

### Firewall
- Blocks or allows different types of network traffic
- Protects the network from unauthorized access and attacks
- Implements access control policies based on rules and policies

### VPN Server
- Creates and manages Virtual Private Networks (VPN)
- Allows users to securely connect from anywhere
- Ensures data privacy and security through encrypted tunnels

### IDS/IPS (Intrusion Detection/Prevention System)
- Monitors and analyzes network traffic in real-time
- Detects threats such as DDoS attacks, malware, and suspicious activities
- Prevents malicious traffic from entering the network

### Traffic Monitoring & Analysis
- Identifies and resolves network issues
- Prevents various types of attacks through traffic analysis
- Provides detailed network statistics and reporting

### Network Management
- Configures and manages network resources
- Handles IP addresses, subnet masks, and routing policies
- Provides centralized network administration capabilities

## 🏢 Use Cases

### 1. Protection for Small and Medium Businesses
- **Firewall Protection**: Blocks unauthorized access and malicious traffic
- **VPN Server**: Provides secure remote access for employees
- **IDS/IPS**: Monitors traffic for suspicious activities and potential threats
- **Cost-Effective**: Open-source solution reduces licensing costs

### 2. Home Network Security
- **Router Replacement**: Installed on home router for enhanced protection
- **Traffic Filtering**: Blocks unwanted traffic and filters content
- **Firewall Rules**: Implements custom security policies
- **VPN Integration**: Secures Internet connections through VPN

### 3. Educational Institutions
- **Access Control**: Controls and restricts access to certain websites and resources
- **Secure Access**: Provides secure access for students and staff
- **Monitoring**: Monitors and analyzes traffic for suspicious activity
- **Content Filtering**: Implements educational content policies

### 4. Government Organizations
- **Network Protection**: Protects government networks (ministries, agencies, authorities)
- **Reliable Firewall**: Provides enterprise-grade security features
- **Secure VPN Access**: Ensures secure remote access for government employees
- **Threat Detection**: Advanced monitoring tools to detect and respond to cyber threats

## 🎯 Lab Objectives

By the end of this lab, you will be able to:

1. **Understand pfSense Architecture**: Learn about pfSense's role in network security
2. **Install pfSense**: Successfully install pfSense on a virtual machine or dedicated hardware
3. **Configure Basic Firewall Rules**: Set up initial firewall policies and rules
4. **Network Interface Setup**: Configure network interfaces and routing
5. **Security Policy Implementation**: Create and apply security policies
6. **Monitoring and Logging**: Set up traffic monitoring and log analysis
7. **Troubleshooting**: Identify and resolve common pfSense configuration issues

## 📋 Prerequisites

Before starting this lab, ensure you have:

- Basic understanding of networking concepts (IP addressing, subnets, routing)
- Familiarity with firewall concepts and security policies
- Virtual machine software (VMware, VirtualBox) or dedicated hardware
- Minimum system requirements:
  - CPU: 1GHz or faster
  - RAM: 1GB minimum (2GB recommended)
  - Storage: 8GB minimum
  - Network interfaces: At least 2 (WAN and LAN)

## 🔧 Lab Setup

### Environment Requirements
- **Virtual Machine**: VMware Workstation, VirtualBox, or Hyper-V
- **Network Configuration**: At least 2 network adapters
- **ISO Image**: pfSense CE (Community Edition) latest version
- **Host System**: Windows, Linux, or macOS with sufficient resources

### Network Topology
```
Internet (WAN) ←→ pfSense Firewall ←→ Internal Network (LAN)
```

## 🧪 Lab Exercise: Step-by-Step Implementation Guide

This section provides a detailed walkthrough of the actual lab implementation, documenting each stage with screenshots and configuration details.

---

## 📦 Stage 1: Installing VirtualBox

### Overview
VirtualBox is a powerful virtualization platform that allows us to run pfSense as a virtual machine. This stage covers the complete installation and initial configuration of VirtualBox.

### Step-by-Step Installation

#### 1.1 Download VirtualBox
- Visit [VirtualBox.org](https://www.virtualbox.org/wiki/Downloads)
- Download the latest version for your operating system
- Choose the appropriate package for Windows, macOS, or Linux

#### 1.2 Install VirtualBox
- Run the VirtualBox installer as administrator
- Follow the installation wizard
- Accept default settings unless you have specific requirements
- Install VirtualBox Extension Pack for additional features

#### 1.3 Verify Installation
- Launch VirtualBox Manager
- Confirm the interface loads properly
- Check that all virtualization features are enabled


---

## 🔧 Stage 2: Downloading and Setting up pfSense

### Overview
This stage covers downloading the pfSense ISO image and creating the virtual machine configuration in VirtualBox.

### Step-by-Step Setup

#### 2.1 Download pfSense ISO
- Visit [pfSense.org Download Page](https://www.pfsense.org/download/)
- Select "pfSense Community Edition"
- Choose the appropriate architecture (AMD64 for most systems)
- Download the latest stable release ISO image

#### 2.2 Create Virtual Machine in VirtualBox
1. **New VM Creation**
   - Click "New" in VirtualBox Manager
   - Name: "pfSense" or "fpSense"
   - Type: FreeBSD (64-bit)
   - Memory: 4096 MB (4GB) recommended
   - Hard Disk: Create new virtual hard disk (16GB minimum)

2. **System Configuration**
   - Processors: 2 CPUs
   - Boot Order: Optical, Hard Disk, Floppy
   - Acceleration: Enable VT-x/AMD-V, Nested Paging

3. **Display Settings**
   - Video Memory: 20 MB
   - Graphics Controller: VMSVGA

4. **Storage Configuration**
   - Primary IDE Controller: pfSense.vdi (16.00 GB)
   - Secondary IDE Controller: Empty optical drive


---

## 🌐 Stage 3: Configuring Network Interfaces

### Overview
Network interface configuration is crucial for pfSense functionality. This stage covers setting up the WAN and LAN interfaces to create proper network isolation and routing.

### Step-by-Step Network Configuration

#### 3.1 VirtualBox Network Adapter Setup

**Adapter 1 (WAN Interface)**
- Enable Network Adapter: ✓ Checked
- Attached to: Bridged Adapter
- Name: [Host's Physical Network Interface]
- Adapter Type: Intel PRO/1000 MT Desktop (82540EM)
- Promiscuous Mode: Allow VMs
- Cable Connected: ✓ Checked

**Adapter 2 (LAN Interface)**
- Enable Network Adapter: ✓ Checked
- Attached to: Internal Network
- Name: intnet
- Adapter Type: Intel PRO/1000 MT Desktop (82540EM)
- Promiscuous Mode: Allow VMs
- Cable Connected: ✓ Checked

#### 3.2 pfSense Network Interface Assignment
Once pfSense boots, the system will detect the network interfaces:

**Detected Interfaces:**
- **WAN (wan)**: `em0` - IP: `v4/DHCP4: 192.168.1.23/24`
- **LAN (lan)**: `em1` - IP: `v4: 192.168.1.1/24`

#### 3.3 Interface Configuration Details
- **WAN Interface**: Automatically configured via DHCP from the bridged network
- **LAN Interface**: Configured with static IP 192.168.1.1/24 for internal network management
- **Network Isolation**: Internal network (intnet) provides isolated environment for testing


### Network Topology Implementation
```
Internet (Bridged) ←→ WAN (em0: 192.168.1.23) ←→ pfSense ←→ LAN (em1: 192.168.1.1) ←→ Internal Network (intnet)
```

---

## 🚀 Stage 4: Launching and Configuring pfSense

### Overview
This stage covers the initial boot process of pfSense, network interface detection, and the first steps of configuration through the console interface. This is where we verify that our virtual machine setup is working correctly and pfSense is ready for web-based configuration.

### Step-by-Step Launch Process

#### 4.1 Initial Boot Sequence
1. **Start pfSense Virtual Machine**
   - Launch VirtualBox Manager
   - Select the pfSense virtual machine
   - Click "Start" to begin the boot process
   - Wait for the system to complete initialization

2. **System Boot Verification**
   - pfSense will display boot messages
   - System will show "Bootup complete" for "pfSense 2.7.2-RELEASE amd64"
   - Welcome message: "*** Welcome to pfSense 2.7.2-RELEASE (amd64) on pfSense ***"

#### 4.2 Network Interface Detection
The system will automatically detect and configure network interfaces:

**Detected Network Interfaces:**
- **WAN (wan)**: `em0` → `v4/DHCP4: 192.168.1.23/24`
- **LAN (lan)**: `em1` → `v4: 192.168.1.1/24`

**Interface Configuration Details:**
- **WAN Interface**: Automatically assigned via DHCP from bridged network
- **LAN Interface**: Configured with static IP 192.168.1.1/24
- **Network Isolation**: Internal network provides secure testing environment

#### 4.3 pfSense Console Menu
Once boot is complete, pfSense displays a configuration menu with 16 options:

```
0) Logout (SSH only)
1) Assign Interfaces
2) Set interface(s) IP address
3) Reset webConfigurator password
4) Reset to factory defaults
5) Reboot system
6) Halt system
7) Ping host
8) Shell
9) pfTop
10) Filter Logs
11) Restart webConfigurator
12) PHP shell + pfSense tools
13) Update from console
14) Enable Secure Shell (sshd)
15) Restore recent configuration
16) Restart PHP-FPM
```

#### 4.4 Client Network Verification
**Windows 11 Virtual Machine Configuration:**
- Connected to pfSense LAN interface via internal network
- Obtained IP address: `192.168.1.100/24` via DHCP
- Default Gateway: `192.168.1.1` (pfSense LAN interface)
- DNS Server: `192.168.1.1` (pfSense LAN interface)
- DHCP Server: `192.168.1.1` (pfSense LAN interface)

**Network Connection Details:**
- **Physical Address**: `08-00-27-6A-28-C0`
- **IPv4 Subnet Mask**: `255.255.255.0`
- **Lease Information**: DHCP lease obtained and expires as configured
- **IPv6 Configuration**: Link-local IPv6 address assigned


### Configuration Status
✅ **pfSense Successfully Launched**
- System boot completed without errors
- Network interfaces properly detected and configured
- Console menu accessible for configuration

✅ **Network Connectivity Established**
- WAN interface connected to external network via DHCP
- LAN interface configured for internal network management
- Client VM successfully obtaining IP configuration from pfSense

✅ **Ready for Web Configuration**
- pfSense web interface accessible at https://192.168.1.1
- Default credentials: admin/pfsense
- System ready for firewall rules and advanced configuration

---

## 💻 Stage 5: Deploying a Virtual Machine with Windows 10 OS

### Overview
This stage covers creating and deploying a Windows 10 virtual machine that will serve as our test client. This VM will be connected to the pfSense LAN interface to test firewall rules and network connectivity.

### Step-by-Step Windows 10 VM Deployment

#### 5.1 Create Windows 10 Virtual Machine
1. **Open VirtualBox Manager**
   - Launch Oracle VirtualBox
   - Click "New" to create a new virtual machine

2. **VM Configuration**
   - **Name**: Windows10-Client
   - **Type**: Microsoft Windows
   - **Version**: Windows 10 (64-bit)
   - **Memory**: 4096 MB (4GB) recommended
   - **Hard Disk**: Create new virtual hard disk (50GB minimum)

3. **System Settings**
   - **Processors**: 2 CPUs
   - **Boot Order**: Optical, Hard Disk
   - **Acceleration**: Enable VT-x/AMD-V, Nested Paging
   - **EFI**: Enable if using Windows 10

4. **Display Configuration**
   - **Video Memory**: 128 MB
   - **Graphics Controller**: VBoxSVGA
   - **3D Acceleration**: Enable

#### 5.2 Install Windows 10 Operating System
1. **Mount Windows 10 ISO**
   - Insert Windows 10 installation media
   - Boot from optical drive

2. **Windows Installation Process**
   - Follow Windows 10 installation wizard
   - Configure regional settings
   - Create user account
   - Complete initial setup


---

## 🌐 Stage 6: Network Configuration

### Overview
This stage configures the network settings for the newly created Windows 10 virtual machine to connect it to the pfSense LAN interface and obtain network configuration via DHCP.

### Step-by-Step Network Configuration

#### 6.1 VirtualBox Network Adapter Configuration
1. **Access VM Settings**
   - Right-click on Windows 10 VM in VirtualBox Manager
   - Select "Settings"

2. **Configure Network Adapter**
   - Go to "Network" section
   - **Adapter 1 Configuration**:
     - Enable Network Adapter: ✓ Checked
     - Attached to: **Internal Network**
     - Name: **intnet** (same as pfSense LAN interface)
     - Adapter Type: Intel PRO/1000 MT Desktop (82540EM)
     - Promiscuous Mode: Allow VMs
     - Cable Connected: ✓ Checked

#### 6.2 Start Virtual Machine
1. **Launch Windows 10 VM**
   - Select Windows 10 virtual machine
   - Click "Start" to begin boot process
   - Wait for Windows 10 to complete startup

2. **Network Interface Detection**
   - Windows will automatically detect the network adapter
   - Network adapter will be configured via DHCP from pfSense

#### 6.3 Verify Network Configuration
1. **Check Network Settings**
   - Open "Network & Internet" settings
   - Verify network adapter is connected
   - Check IP configuration

2. **Expected Network Configuration**
   - **IP Address**: 192.168.1.x (assigned by pfSense DHCP)
   - **Subnet Mask**: 255.255.255.0
   - **Default Gateway**: 192.168.1.1 (pfSense LAN interface)
   - **DNS Server**: 192.168.1.1 (pfSense LAN interface)


---

## 🔥 Stage 7: Configuring the Firewall

### Overview
This stage covers the initial configuration of the pfSense firewall through the web interface, including basic system settings, DNS configuration, and network policies.

### Step-by-Step Firewall Configuration

#### 7.1 Access pfSense Web Interface
1. **Open Web Browser**
   - Launch web browser on host machine or Windows 10 VM
   - Navigate to: `https://192.168.1.1`

2. **Initial Login**
   - **Username**: admin
   - **Password**: pfsense (default)
   - Accept security certificate warning if prompted

#### 7.2 Initial Setup Wizard
1. **Welcome Screen**
   - Click "Next" to begin setup wizard
   - Review system information

2. **General Information Configuration**
   - **Hostname**: Leave as "pfsense" (default)
   - **Domain**: Leave blank or set as needed
   - **Primary DNS Server**: Enter `8.8.8.8`
   - **Secondary DNS Server**: Enter `8.8.4.4`
   - **Override DNS**: **Uncheck** this option
   - Click "Next"

3. **Network Configuration**
   - **WAN Interface**: Verify configuration (should show DHCP)
   - **LAN Interface**: Leave IP address unchanged (192.168.1.1/24)
   - Click "Next"

#### 7.3 Security Configuration
1. **Firewall Rules**
   - Scroll down to security options
   - **Block RFC1918 Private networks**: **Uncheck**
   - **Block bogon networks**: **Uncheck**
   - These settings allow proper internal network communication

2. **Admin Password**
   - **New Password**: Enter `admin`
   - **Confirm Password**: Re-enter `admin`
   - Click "Next"

#### 7.4 Apply Configuration
1. **Save Settings**
   - Review all configuration settings
   - Click "Reload" to apply changes
   - Wait for system to restart services

2. **Configuration Complete**
   - System will redirect to login page
   - Login with new credentials: admin/admin


---

## 🧪 Stage 8: Testing Internet Access and Firewall Rules

### Overview
This stage demonstrates testing Internet connectivity through the pfSense firewall and creating firewall rules to block specific websites, showcasing the firewall's traffic control capabilities.

### Step-by-Step Testing and Rule Creation

#### 8.1 Monitor Network Traffic
1. **Access Traffic Graph**
   - Log into pfSense web interface
   - Navigate to **Status > Traffic Graph**
   - Monitor real-time network traffic

2. **Test Internet Connectivity**
   - On Windows 10 VM, open web browser
   - Navigate to various websites (Google, YouTube, etc.)
   - Verify Internet access is working
   - Observe traffic in pfSense traffic graph

#### 8.2 Create Firewall Alias
1. **Access Firewall Aliases**
   - Go to **Firewall > Aliases**
   - Click "Add" to create new alias

2. **Configure Alias**
   - **Name**: `blocked_facebook`
   - **Type**: Host(s)
   - **Description**: Block Facebook access
   - **Host(s)**: `www.facebook.com`
   - Click "Save"

#### 8.3 Create Firewall Rule
1. **Access Firewall Rules**
   - Go to **Firewall > Rules**
   - Select **LAN** tab
   - Click "Add" to create new rule

2. **Configure Blocking Rule**
   - **Action**: **Block**
   - **Protocol**: **Any**
   - **Source**: Leave as default (LAN net)
   - **Destination**: Select **Address or Alias**
   - **Destination address**: Enter `blocked_facebook`
   - **Description**: Block Facebook access
   - Click "Save"

#### 8.4 Apply and Test Firewall Rule
1. **Apply Configuration**
   - Click "Apply Changes" to activate rules
   - Wait for rules to be applied

2. **Test Blocking Rule**
   - On Windows 10 VM, attempt to access www.facebook.com
   - Verify that Facebook is blocked
   - Test other websites to ensure they still work
   - Check pfSense logs for blocked traffic


---

## ✅ Lab Completion Summary

### Completed Stages
✅ **Stage 1**: Installing VirtualBox  
✅ **Stage 2**: Downloading and setting up pfSense  
✅ **Stage 3**: Configuring network interfaces  
✅ **Stage 4**: Launching and configuring pfSense  
✅ **Stage 5**: Deploying Windows 10 virtual machine  
✅ **Stage 6**: Network configuration  
✅ **Stage 7**: Configuring the firewall  
✅ **Stage 8**: Testing Internet access and firewall rules  

### Lab Achievements
- Successfully deployed pfSense firewall in virtualized environment
- Configured proper network isolation with WAN and LAN interfaces
- Deployed Windows 10 test client connected to pfSense LAN
- Configured firewall with custom blocking rules
- Demonstrated traffic monitoring and control capabilities
- Created working network security lab environment

### Skills Demonstrated
- Virtual machine deployment and configuration
- Network interface configuration and routing
- Firewall rule creation and management
- Network traffic monitoring and analysis
- Security policy implementation
- Troubleshooting network connectivity issues

## ⚙️ Configuration Steps

### Step 1: Basic System Configuration
```bash
# Access pfSense web interface
https://[LAN_IP_ADDRESS]

# Change default admin password
System → User Manager → admin → Edit
```

### Step 2: Firewall Rules Configuration
1. **Navigate to Firewall Rules**
   - Go to Firewall → Rules → LAN
   - Review default allow rules

2. **Create Custom Firewall Rules**
   - Block specific protocols or ports
   - Allow specific services
   - Configure time-based rules

### Step 3: Network Services Setup
1. **DHCP Server Configuration**
   - Services → DHCP Server → LAN
   - Configure IP range and lease time
   - Set DNS servers

2. **DNS Configuration**
   - Services → DNS Resolver
   - Configure upstream DNS servers
   - Enable DNS over HTTPS (optional)

### Step 4: Monitoring and Logging
1. **System Logs**
   - Status → System Logs
   - Monitor firewall logs
   - Review system events

2. **Traffic Monitoring**
   - Status → Traffic Graph
   - Monitor bandwidth usage
   - Analyze traffic patterns

## ✅ Verification and Testing

### Firewall Functionality Test
1. **Test Basic Connectivity**
   ```bash
   ping 8.8.8.8  # Test internet connectivity
   ping 192.168.1.1  # Test LAN connectivity
   ```

2. **Test Firewall Rules**
   - Block specific ports and verify blocking
   - Allow specific services and verify access
   - Test time-based rules

### Network Services Test
1. **DHCP Service**
   - Connect client device to LAN
   - Verify automatic IP assignment
   - Check DNS resolution

2. **VPN Service (Optional)**
   - Configure OpenVPN or IPsec
   - Test remote connectivity
   - Verify encrypted tunnel

## 🔍 Troubleshooting

### Common Issues and Solutions

1. **Cannot Access Web Interface**
   - Check network interface assignment
   - Verify firewall rules allow HTTPS
   - Confirm IP address configuration

2. **No Internet Connectivity**
   - Check WAN interface configuration
   - Verify default gateway settings
   - Review firewall rules for WAN traffic

3. **DHCP Not Working**
   - Verify DHCP server is enabled
   - Check IP range configuration
   - Review lease time settings

4. **Performance Issues**
   - Monitor CPU and memory usage
   - Check for excessive log entries
   - Optimize firewall rules

## 📊 Lab Deliverables

Complete the following tasks and document your findings:

1. **Network Diagram**: Create a diagram showing your lab topology
2. **Configuration Screenshots**: Capture key configuration screens
3. **Firewall Rules Documentation**: List all configured firewall rules
4. **Test Results**: Document all connectivity and functionality tests
5. **Troubleshooting Log**: Record any issues encountered and solutions applied

## 🎓 Conclusion

This lab provides hands-on experience with pfSense, a powerful open-source firewall solution. Through this exercise, you have:

- Installed and configured pfSense in a lab environment
- Implemented basic firewall rules and network policies
- Set up essential network services (DHCP, DNS)
- Learned to monitor and analyze network traffic
- Developed troubleshooting skills for network security appliances

pfSense's open-source nature and comprehensive feature set make it an excellent choice for network security implementations across various environments, from home networks to enterprise deployments.

## 📚 Additional Resources

- [pfSense Documentation](https://docs.netgate.com/pfsense/)
- [pfSense Community Forum](https://forum.netgate.com/)
- [FreeBSD Documentation](https://docs.freebsd.org/)
- [Network Security Best Practices](https://www.nist.gov/cyberframework)

---

**Lab Completion Date**: [Date]
**Instructor**: [Name]
**Student**: [Name]
**Lab Environment**: [Virtual/Hardware]
