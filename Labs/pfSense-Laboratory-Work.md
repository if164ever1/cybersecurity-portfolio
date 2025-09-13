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

### Screenshots
*Screenshots of VirtualBox installation process will be added here*

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

### Screenshots
*Screenshots of pfSense VM creation and configuration will be added here*

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

### Screenshots
*Screenshots of VirtualBox network configuration and pfSense interface detection will be added here*

### Network Topology Implementation
```
Internet (Bridged) ←→ WAN (em0: 192.168.1.23) ←→ pfSense ←→ LAN (em1: 192.168.1.1) ←→ Internal Network (intnet)
```

---

## 🎯 Next Steps: pfSense Configuration

After completing the three stages above, the following configuration phases will be covered:

### Phase 4: Initial pfSense Setup
1. **Network Interface Assignment**
   - Assign WAN and LAN interfaces during pfSense setup
   - Configure interface IP addresses
   - Set up routing tables

2. **Web Interface Access**
   - Access pfSense web interface via LAN IP (192.168.1.1)
   - Default credentials: admin/pfsense
   - Initial setup wizard configuration

### Phase 5: Firewall Configuration
1. **Basic Firewall Rules**
2. **Service Configuration**
3. **Security Policies**

### Phase 6: Testing and Verification
1. **Connectivity Tests**
2. **Firewall Rule Testing**
3. **Performance Monitoring**

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
