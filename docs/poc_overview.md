
# Vaudit – Product Overview (POC Version)

## 1. Introduction
**Vaudit** supports institutions and individuals alike in simplifying the governance, construction, and operation of crypto asset wallets by applying the concept of **"Wallet as Code"**—in much the same way that **"Infrastructure as Code"** transformed the management of **IT infrastructure**.

While designed with enterprise governance needs in mind, Vaudit provides value to **any Fireblocks user**, from large financial institutions to individual operators, by offering clear visibility and risk awareness over wallet configurations.

This document outlines the core concept, target users, key capabilities, and **limitations of the POC version** of Vaudit.

## 1.1 Purpose of the POC
The purpose of this Proof of Concept (POC) is to validate the direction and potential value of Vaudit before proceeding to full product development. Specifically, the POC aims to:

- **Verify whether Vaudit provides enough value for customers to pay for it**
- **Identify the real, underlying challenges faced by prospective users**
- **Build an initial list of interested or potential customers**

This POC will serve as a foundation for deeper product discovery, feedback collection, and potential go-to-market planning.

## 2. Problem Statement
Institutions using Fireblocks face challenges in:

- Understanding and evaluating the security implications of wallet (vault) configurations
- Maintaining governance standards across teams and roles
- Ensuring transparency and consistency in the setup of transaction policies and user permissions

There is no lightweight tool to assess the **risk level** of current settings from a corporate governance perspective.

> *Note: Staking-related activity tracking is out of scope for this POC and may be considered as a separate feature or product.*

## 3. Target Users
- Financial institutions using Fireblocks
- Compliance teams
- Internal audit departments
- Security and governance leads
- Individual users who need increased visibility into wallet setup

## 4. Scope and Key Capabilities
This POC version of Vaudit is implemented as a CLI tool with the following core capabilities:

- Retrieves wallet configuration, user information, and **policy-related settings** from the Fireblocks REST API to support **system-level auditability and governance checks**
- Applies rule-based evaluation to identify potential governance or security risks in wallet setup
- Assists with the **creation of API users** by generating configuration suggestions aligned with internal governance policies
- Outputs findings in a human-readable format, with export options in **CSV or PDF**
- Provides a **conceptual mockup** (e.g., presentation slide) illustrating the direction of a future web-based dashboard

The following items are **explicitly out of scope** for this POC:

- Real-time monitoring
- Features related to **accounting systems**, such as staking reward calculations or transaction-level financial reporting
- Web interface implementation
- Access control or user authentication
- Persistent storage or historical tracking

> Note: Topics related to accounting (e.g., staking reward tracking) may be discussed during user interviews for potential future development.

## 5. System Overview
The POC consists of:

- A Python-based CLI tool that communicates with the Fireblocks REST API
- In-memory analysis (no persistent database)
- Configuration risk rules defined as code (e.g., YAML or Python modules)
- Export of results in human-readable summaries for compliance or review purposes

## 6. Assumptions
- Fireblocks API key with appropriate read-only access is available
- All relevant vaults and policies are under a single Fireblocks workspace
- Risk rules are reviewed and agreed upon with internal stakeholders
- Timezone for reporting is consistent per organization

## 7. Next Steps After POC
Following the POC, user feedback will be analyzed to identify common needs and pain points. Development priorities will be determined based on these insights, with a focus on features that provide the highest value to early users.

Potential future capabilities include:

- Web-based dashboard with role-based access
- Scheduled assessments and automated notifications
- Historical data tracking and version comparison
- Custom rule definitions via UI
- Integration with audit, compliance, or accounting platforms
- **Functionality to modify Fireblocks settings (e.g., vault policies, user roles)**
- **Staking-related capabilities** (e.g., delegation visibility, validator exposure analysis)
- **Accounting-related features**, such as automated reward tracking and financial reporting
