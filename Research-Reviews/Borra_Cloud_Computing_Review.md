# Review: An Overview of Cloud Computing and Leading Cloud Service Providers

**Author of the paper:** Praveen Borra
**Review Date:** 2026-02-21
**Topic:** Cloud Computing, AWS, Azure, GCP

## 1. Introduction

This review summarizes the article **"An Overview of Cloud Computing and Leading Cloud Service Providers"** by Praveen Borra, published in the *International Journal of Computer Engineering and Technology (IJCET)* in 2024.

The primary goal of this paper is to provide a comprehensive overview of cloud computing concepts, architecture, and the current market landscape. The author focuses on the "Big Three" hyperscalers: Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP), aiming to compare their services, global infrastructure, and market positions.

## 2. Methodology

The study is conducted as a literature and analytical review. The author employs a comparative analysis method, gathering data from:
- Official provider documentation (AWS, Azure, GCP).
- Industry analyst reports (specifically citing the Gartner Magic Quadrant for Strategic Cloud Platform Services).
- Existing academic literature on the subject.

The findings are structured using comparative tables and diagrams, making the large volume of information accessible for readers new to the field.

## 3. Key Findings

The article confirms the dominant position of the three major cloud providers:
- **Market Share:** AWS leads with approximately 32%, followed by Azure (23%) and GCP (10%).
- **Global Infrastructure:** AWS operates 105 Availability Zones, Azure has over 60 regions, and GCP has data centers in over 200 countries.
- **Service Comparison:** The paper provides a detailed breakdown of how these providers map services across categories like computing, databases, analytics, and networking (e.g., AWS S3 vs. Azure Blob Storage vs. GCP Cloud Storage).
- **Architecture:** It explains the core components of cloud architecture, including frontend/backend platforms, virtualization, and the three service models (IaaS, PaaS, SaaS).

## 4. Key Insights

While reading this publication, I identified two key insights that are valuable for my work in cloud security and architecture:

**1. The "Mapping" Strategy is Essential for Multi-Cloud Understanding**
The extensive comparison table (Table 2 in the original paper) is incredibly useful. It shows that while the "Big Three" offer similar services, they use different names and have unique implementations (e.g., AWS DynamoDB vs. Azure Cosmos DB). For my cybersecurity portfolio, this insight is practical because security configurations are service-specific. Knowing that "Cloud Front" (AWS) equals "Cloud CDN" (GCP) allows me to apply security best practices (like WAF policies or DDoS protection) consistently across different clouds by first identifying the correct corresponding service.

**2. Security is Embedded in the Shared Responsibility Model**
The paper mentions "Robust Security" as a benefit, noting that providers handle security patching. This reinforces the **Shared Responsibility Model**, a core concept in cloud security. The article reminds me that while the provider secures *of* the cloud (hardware, software, facilities), the customer is responsible for security *in* the cloud (data, access management, OS patches on IaaS). This distinction is critical when designing secure architectures and will be a key point I emphasize in my own projects.

## 5. Conclusion

Borra's article serves as an excellent primer for anyone entering the field of cloud computing. Its main contribution is the structured comparison of the leading providers and the clear explanation of cloud architecture basics. For future work, the author suggests a deeper technical comparison between providers and expanding the analysis to include other players like Alibaba and IBM. This paper provides a solid foundation for more advanced study into cloud security, compliance, and specific service implementations.