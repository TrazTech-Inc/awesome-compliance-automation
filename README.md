# Awesome Compliance Automation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, platforms, and resources for automating security compliance across SOC 2, ISO 27001, ISO 42001, HIPAA, PCI DSS, GDPR, PIPEDA, Quebec Law 25, and NIST CSF.

Maintained by [TrazTech](https://traztech.ca)  - a security & compliance consultancy based in Toronto that helps organizations achieve and maintain compliance across all major frameworks. Led by [Jacob Masse](https://github.com/jacob-masse), who holds 5 published CVEs including [CVE-2024-45163](https://nvd.nist.gov/vuln/detail/CVE-2024-45163).

**Free tools from TrazTech:**
- [Cloud Security Posture Check](https://traztech.ca/tools/cloud-security-posture-check)  - Assess your cloud security configuration for free
- [SOC 2 Readiness Checklist](https://traztech.ca/soc-2-readiness-checklist)  - Interactive checklist to gauge audit readiness
- [TrazTech Workspace](https://traztech.ca)  - Free compliance tracking portal (alternative to Vanta/Drata)

---

## Contents

- [GRC Platforms](#grc-platforms)
- [Policy Management](#policy-management)
- [Evidence Collection & Automation](#evidence-collection--automation)
- [Access Review Tools](#access-review-tools)
- [Vendor Risk Management](#vendor-risk-management)
- [Security Awareness Training](#security-awareness-training)
- [Vulnerability Management](#vulnerability-management)
- [Cloud Security Posture (CSPM)](#cloud-security-posture-cspm)
- [Penetration Testing Platforms](#penetration-testing-platforms)
- [Incident Response](#incident-response)
- [Trust Centers & Security Pages](#trust-centers--security-pages)
- [Background Checks](#background-checks)
- [Endpoint Security / MDM](#endpoint-security--mdm)
- [By Framework](#by-framework)
  - [SOC 2 Automation](#soc-2-automation)
  - [ISO 27001 Automation](#iso-27001-automation)
  - [HIPAA Compliance Tools](#hipaa-compliance-tools)
  - [PCI DSS Tools](#pci-dss-tools)
  - [GDPR / Privacy Tools](#gdpr--privacy-tools)
  - [NIST CSF Tools](#nist-csf-tools)
  - [Canadian Privacy (PIPEDA / Law 25)](#canadian-privacy-pipeda--law-25)
  - [AI Governance (ISO 42001)](#ai-governance-iso-42001)
- [Open-Source Tools](#open-source-tools)
- [Resources](#resources)
- [Contributing](#contributing)

---

## GRC Platforms

Governance, Risk, and Compliance platforms that centralize audit readiness, control monitoring, and evidence collection. For guidance on what actually recurs between audits and how to prevent control drift, see TrazTech's posts on [compliance calendars](https://traztech.ca/blog/compliance-calendar-what-actually-recurs) and [control drift between audits](https://traztech.ca/blog/control-drift-between-audits).

| Platform | Target Size | Frameworks | Pricing | Key Strength |
|----------|-------------|------------|---------|--------------|
| [Vanta](https://vanta.com) | SMB to Mid-Market | SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR, SOX ITGC | From ~$10k/yr | Largest integration library (200+), continuous monitoring |
| [Drata](https://drata.com) | SMB to Mid-Market | SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR, SOX ITGC | From ~$10k/yr | Autopilot evidence collection, custom frameworks |
| [Secureframe](https://secureframe.com) | SMB to Mid-Market | SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR, NIST | From ~$8k/yr | Fast time-to-audit, AI-assisted questionnaires |
| [Sprinto](https://sprinto.com) | SMB / Startups | SOC 2, ISO 27001, HIPAA, GDPR | From ~$5k/yr | Budget-friendly, strong for startups |
| [Thoropass](https://thoropass.com) | SMB to Mid-Market | SOC 2, ISO 27001, HIPAA, PCI DSS | Custom | End-to-end (platform + audit firm combined) |
| [Scytale](https://scytale.ai) | SMB / Startups | SOC 2, ISO 27001, HIPAA, PCI DSS | Custom | Compliance-as-a-service model, concierge support |
| [Laika](https://heylaika.com) | SMB to Mid-Market | SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR | Custom | Combines platform with compliance advisory |
| [Anecdotes](https://anecdotes.ai) | Mid-Market to Enterprise | SOC 2, ISO 27001, SOX, NIST, custom | Custom | AI-powered evidence mapping across any framework |
| [Tugboat Logic](https://tugboatlogic.com) | SMB | SOC 2, ISO 27001, PCI DSS | From ~$6k/yr | Policy library with auto-generation |
| [AuditBoard](https://auditboard.com) | Enterprise | SOX, SOC 2, ISO 27001, NIST, custom | Enterprise pricing | Connected risk platform, audit management |
| [Hyperproof](https://hyperproof.io) | Mid-Market to Enterprise | SOC 2, ISO 27001, HIPAA, PCI DSS, NIST, FedRAMP | Custom | Hypersync evidence collection, cross-framework mapping |
| [OneTrust](https://onetrust.com) | Enterprise | GDPR, CCPA, ISO 27001, NIST, 100+ regulations | Enterprise pricing | Privacy-first, largest regulatory intelligence database |
| [ServiceNow GRC](https://www.servicenow.com/products/governance-risk-and-compliance.html) | Enterprise | SOX, SOC 2, ISO 27001, NIST, custom | Enterprise pricing | Native ServiceNow integration, workflow automation |
| [Archer (RSA)](https://www.archerirm.com) | Enterprise | SOX, SOC 2, NIST, ISO 27001, custom | Enterprise pricing | Mature IRM platform, highly customizable |
| [LogicGate Risk Cloud](https://www.logicgate.com) | Mid-Market to Enterprise | SOC 2, ISO 27001, NIST, SOX, custom | Custom | No-code workflow builder, flexible data model |
| [TrazTech Workspace](https://traztech.ca) | SMB / Startups | SOC 2, ISO 27001, HIPAA, PIPEDA, Law 25 | Free tier available | Free compliance tracking portal, Canadian privacy expertise |
| [Carbide](https://carbidesecure.com) | SMB | SOC 2, ISO 27001, HIPAA, PCI DSS | From ~$8k/yr | Security awareness + GRC combined |
| [Apptega](https://apptega.com) | SMB to Mid-Market | NIST, SOC 2, ISO 27001, CMMC, PCI DSS | Custom | Framework crosswalking, MSP-friendly |
| [Ostendio](https://ostendio.com) | SMB to Mid-Market | SOC 2, ISO 27001, HIPAA, FedRAMP | Custom | MyVCM platform, collaborative audit prep |
| [Strike Graph](https://strikegraph.com) | SMB | SOC 2, ISO 27001, HIPAA, PCI DSS | From ~$5k/yr | Risk-first approach, guided certification |
| [Scrut Automation](https://scrut.io) | SMB | SOC 2, ISO 27001, HIPAA, GDPR | Custom | Cloud-native, real-time risk monitoring |
| [Resolver (Kyndryl)](https://www.resolver.com) | Enterprise | SOX, SOC 2, ISO 27001, NIST | Enterprise pricing | Integrated risk management |
| [StandardFusion](https://standardfusion.com) | SMB to Mid-Market | SOC 2, ISO 27001, NIST, HIPAA | Custom | GRC built for InfoSec teams |
| [Centraleyes](https://centraleyes.com) | Mid-Market | NIST, ISO 27001, SOC 2, GDPR, CIS | Custom | Automated risk quantification |
| [Cypago](https://cypago.com) | SMB to Mid-Market | SOC 2, ISO 27001, GDPR, HIPAA | Custom | Cyber GRC automation, context-aware evidence |

## Policy Management

Tools for creating, distributing, tracking, and managing compliance policies and procedures. Well-written policies are the backbone of every compliance framework.

- [PowerDMS](https://www.powerdms.com)  - Policy and document management with version control, acknowledgment tracking, and automated distribution. Popular with government and healthcare.
- [PolicyTree](https://policytree.com)  - Policy lifecycle management with approval workflows and employee attestation.
- [Convercent (OneTrust Ethics)](https://convercent.com)  - Ethics and compliance management including policy distribution, hotline, and case management.
- [NAVEX One (PolicyTech)](https://www.navex.com/en-us/products/policytech-policy-management/)  - Enterprise policy management with automated workflows, gap analysis, and audit trails.
- [ConvergePoint](https://www.convergepoint.com)  - SharePoint-based policy management with automated review cycles.
- [ComplianceBridge](https://compliancebridge.com)  - Policy and procedure management with testing, acknowledgments, and reporting.
- [LogicGate](https://www.logicgate.com)  - No-code policy management within the broader Risk Cloud GRC platform.
- [Donesafe (HSI)](https://donesafe.com)  - Policy management module within a broader EHS and compliance platform.
- [Hyperproof Policy Management](https://hyperproof.io)  - Policy templates, approval workflows, and employee attestation within the Hyperproof GRC platform.
- [Drata Policy Center](https://drata.com)  - Pre-built policy templates mapped to SOC 2, ISO 27001, and other frameworks.
- [Vanta Policy Hub](https://vanta.com)  - Policy templates with employee acknowledgment tracking integrated into the Vanta GRC platform.
- [Secureframe Policies](https://secureframe.com)  - Auto-generated policies mapped to frameworks with version control.

## Evidence Collection & Automation

Automating evidence gathering is critical to reducing audit fatigue and keeping your compliance posture current between audits. For best practices on freshness windows and automation strategies, see TrazTech's guide on [keeping evidence fresh](https://traztech.ca/blog/keeping-evidence-fresh).

- [Vanta Autopilot](https://vanta.com)  - Automated evidence collection across 200+ integrations (AWS, Azure, GCP, GitHub, Okta, etc.).
- [Drata Autopilot](https://drata.com)  - Continuous evidence collection with automated screenshots and API-based config pulls.
- [Hyperproof Hypersync](https://hyperproof.io)  - Syncs evidence from cloud providers, SaaS tools, and ticketing systems on a schedule.
- [Secureframe Evidence Collection](https://secureframe.com)  - Automated evidence gathering from 150+ integrations.
- [Anecdotes.ai](https://anecdotes.ai)  - AI-powered evidence collection that maps artifacts to controls across frameworks.
- [Sprinto Evidence Automation](https://sprinto.com)  - Continuous monitoring with automated evidence capture.
- [Steampipe](https://steampipe.io)  - Open-source: query cloud APIs with SQL to generate compliance evidence. ([GitHub](https://github.com/turbot/steampipe))
- [Prowler](https://prowler.pro)  - Open-source: automated security assessments that produce compliance-ready evidence for AWS, Azure, and GCP. ([GitHub](https://github.com/prowler-cloud/prowler))
- [CloudQuery](https://cloudquery.io)  - Open-source: sync cloud assets to a database for evidence snapshots. ([GitHub](https://github.com/cloudquery/cloudquery))
- [TrazTech Cloud Security Posture Check](https://traztech.ca/tools/cloud-security-posture-check)  - Free cloud configuration assessment that generates evidence of your security posture.
- [ScoutSuite](https://github.com/nccgroup/ScoutSuite)  - Open-source multi-cloud auditing tool that produces JSON evidence reports.
- [Qualys Policy Compliance](https://www.qualys.com/apps/policy-compliance/)  - Automated configuration evidence gathering with CIS benchmark mapping.
- [Orca Security](https://orca.security)  - Agentless cloud evidence collection across workloads, configurations, and identities.
- [Wiz Evidence](https://wiz.io)  - Cloud-native evidence collection with contextual risk prioritization.
- [Tugboat Logic](https://tugboatlogic.com)  - Automated evidence collection with AI-driven policy suggestions.

## Access Review Tools

Access reviews (user access reviews, entitlement reviews) are required by SOC 2, ISO 27001, HIPAA, and PCI DSS. These tools automate the review and recertification process.

- [ConductorOne](https://conductorone.com)  - Identity security platform with automated access reviews, just-in-time access, and lifecycle management.
- [Opal](https://opal.dev)  - Access management with automated access reviews, request workflows, and least-privilege enforcement.
- [Veza](https://veza.com)  - Authorization intelligence platform for visualizing and reviewing effective permissions across cloud and SaaS.
- [Lumos](https://lumos.com)  - Unified access platform with self-service access requests, automated reviews, and license optimization.
- [AccessOwl](https://accessowl.io)  - Automated user access reviews with SaaS onboarding/offboarding and compliance reporting.
- [Zluri](https://zluri.com)  - SaaS management with automated access reviews, license tracking, and workflow automation.
- [SailPoint](https://sailpoint.com)  - Enterprise identity governance with AI-driven access reviews and certifications.
- [Saviynt](https://saviynt.com)  - Cloud-native identity governance with converged access reviews for applications, infrastructure, and data.
- [CrowdStrike Falcon Identity](https://www.crowdstrike.com/products/identity-protection/)  - Identity threat detection with access review capabilities.
- [Okta Identity Governance](https://www.okta.com/products/identity-governance/)  - Access certifications, lifecycle management, and entitlement reviews within the Okta platform.
- [OneLogin (by One Identity)](https://www.onelogin.com)  - Access management with periodic review campaigns.
- [Delinea (Centrify)](https://delinea.com)  - Privileged access reviews with session monitoring and just-in-time elevation.
- [StrongDM](https://strongdm.com)  - Infrastructure access management with audit logs and session replay for access review evidence.
- [Teleport](https://goteleport.com)  - Infrastructure access with built-in access request workflows, session recording, and audit logging.

## Vendor Risk Management

Third-party risk management tools for assessing, monitoring, and managing vendor security posture. Most compliance frameworks require a formal vendor management program.

- [Whistic](https://whistic.com)  - Vendor security profile sharing and assessment platform with a trust catalog.
- [SecurityScorecard](https://securityscorecard.com)  - External risk ratings and continuous vendor security monitoring with letter grades (A-F).
- [BitSight](https://bitsight.com)  - Cyber risk ratings for vendor portfolios with continuous monitoring and benchmarking.
- [UpGuard](https://upguard.com)  - Vendor risk management with security ratings, questionnaire automation, and data leak detection.
- [Panorays](https://panorays.com)  - Third-party security management combining external attack surface assessment with questionnaire automation.
- [ProcessUnity](https://processunity.com)  - Third-party risk management with configurable workflows and risk assessments.
- [Prevalent](https://prevalent.net)  - Unified third-party risk management with automated assessments, continuous monitoring, and remediation.
- [OneTrust Vendorpedia](https://onetrust.com/products/vendorpedia/)  - Vendor risk exchange with 70,000+ pre-assessed vendors and automated risk workflows.
- [Vanta Vendor Risk](https://vanta.com)  - Vendor risk management module integrated into the Vanta GRC platform.
- [Drata Vendor Management](https://drata.com)  - Vendor tracking with security review workflows and risk scoring.
- [RiskRecon (Mastercard)](https://riskrecon.com)  - Continuous vendor risk assessment through passive data analysis.
- [Black Kite](https://blackkite.com)  - Third-party cyber risk intelligence with financial quantification and compliance mapping.
- [HECVAT](https://hecvat.org)  - Free higher education vendor assessment toolkit for cloud services. (Open standard)
- [ThirdPartyTrust](https://thirdpartytrust.com)  - Collaborative vendor risk management with evidence sharing.
- [Aravo](https://aravo.com)  - Enterprise third-party risk management and due diligence platform.

## Security Awareness Training

Compliance frameworks (SOC 2, ISO 27001, HIPAA, PCI DSS) require regular security awareness training. These platforms automate delivery, tracking, and phishing simulations.

- [KnowBe4](https://knowbe4.com)  - Market leader in security awareness training and simulated phishing. Largest content library with 1,000+ modules.
- [Curricula](https://getcurricula.com)  - Story-based security awareness training with engaging animated content and phishing simulations.
- [Hoxhunt](https://hoxhunt.com)  - Gamified phishing simulation and training that adapts difficulty to each user's skill level.
- [Arctic Wolf Managed Security Awareness](https://arcticwolf.com/products/managed-security-awareness/)  - Fully managed security awareness training with microlearning and phishing simulations.
- [Proofpoint Security Awareness Training](https://www.proofpoint.com/us/products/security-awareness-training)  - Threat-driven security awareness with real-world phishing intelligence.
- [Cofense (PhishMe)](https://cofense.com)  - Phishing simulation and incident response training with threat intelligence.
- [SANS Security Awareness](https://www.sans.org/security-awareness-training/)  - Training content from SANS Institute with role-based learning paths.
- [Infosec IQ (Cengage)](https://infosecinstitute.com/iq/)  - Security awareness and phishing simulation with 2,000+ training resources.
- [Mimecast Awareness Training](https://www.mimecast.com/products/awareness-training/)  - Video-based micro-learning modules with humor-driven content.
- [Ninjio](https://ninjio.com)  - Hollywood-style animated security awareness episodes based on real breaches.
- [Living Security](https://livingsecurity.com)  - Gamified cybersecurity training with escape rooms and immersive experiences.
- [Riot (by Mantra)](https://tryriot.com)  - Automated security awareness with conversational phishing simulations via Slack/Teams.

## Vulnerability Management

Continuous vulnerability scanning and management is required by virtually every compliance framework. These tools identify, prioritize, and track remediation of vulnerabilities.

- [Tenable (Nessus)](https://tenable.com)  - Industry-standard vulnerability scanner with broad asset coverage (on-prem, cloud, OT). Nessus Professional from ~$3,500/yr.
- [Qualys VMDR](https://www.qualys.com/apps/vulnerability-management-detection-response/)  - Cloud-native vulnerability management with asset discovery, prioritization, and patching.
- [Rapid7 InsightVM](https://www.rapid7.com/products/insightvm/)  - Vulnerability management with live dashboards, risk prioritization, and remediation projects.
- [Snyk](https://snyk.io)  - Developer-first security: finds vulnerabilities in code, open-source dependencies, containers, and IaC. Free tier available.
- [Wiz](https://wiz.io)  - Agentless cloud vulnerability scanning with contextual risk prioritization across VMs, containers, and serverless.
- [Orca Security](https://orca.security)  - Agentless SideScanning for cloud workload vulnerabilities, misconfigurations, and malware.
- [CrowdStrike Falcon Spotlight](https://www.crowdstrike.com/products/exposure-management/falcon-spotlight-vulnerability-management/)  - Real-time vulnerability assessment using the Falcon agent (no scanning required).
- [Microsoft Defender Vulnerability Management](https://www.microsoft.com/en-us/security/business/threat-protection/microsoft-defender-vulnerability-management)  - Built-in vulnerability management for Microsoft 365 Defender customers.
- [Arctic Wolf Managed Risk](https://arcticwolf.com/products/managed-risk/)  - Managed vulnerability and exposure management with concierge security team.
- [Lacework](https://lacework.com)  - Cloud vulnerability scanning with anomaly-based threat detection.
- [Trivy](https://trivy.dev)  - Open-source vulnerability scanner for containers, filesystems, git repos, and Kubernetes. ([GitHub](https://github.com/aquasecurity/trivy))
- [Grype](https://github.com/anchore/grype)  - Open-source vulnerability scanner for container images and filesystems by Anchore.
- [Nuclei](https://github.com/projectdiscovery/nuclei)  - Open-source vulnerability scanner driven by community-contributed templates.

## Cloud Security Posture (CSPM)

Cloud Security Posture Management tools continuously monitor cloud configurations for compliance violations and security misconfigurations. You can also run TrazTech's free [Cloud Security Posture Check](https://traztech.ca/tools/cloud-security-posture-check) for a quick assessment.

- [Wiz](https://wiz.io)  - Agentless CSPM with graph-based visualization of toxic risk combinations across AWS, Azure, GCP, and OCI.
- [Orca Security](https://orca.security)  - Agentless cloud security platform with CSPM, CWPP, and CIEM in a single console.
- [Prisma Cloud (Palo Alto)](https://www.paloaltonetworks.com/prisma/cloud)  - Comprehensive CNAPP with CSPM, CWP, code security, and CIEM modules.
- [Lacework](https://lacework.com)  - Cloud security platform using behavioral analytics for CSPM and threat detection.
- [Prowler](https://prowler.pro)  - Open-source CSPM tool for AWS, Azure, and GCP with 300+ security checks. ([GitHub](https://github.com/prowler-cloud/prowler))
- [ScoutSuite](https://github.com/nccgroup/ScoutSuite)  - Open-source multi-cloud security auditing tool (AWS, Azure, GCP, Alibaba Cloud, Oracle Cloud).
- [CloudSploit](https://github.com/aquasecurity/cloudsploit)  - Open-source cloud security scanning by Aqua Security, with 300+ checks across AWS, Azure, GCP, and Oracle.
- [Steampipe](https://steampipe.io)  - Open-source: query any cloud API with SQL. Includes compliance benchmarks for CIS, SOC 2, HIPAA, and more. ([GitHub](https://github.com/turbot/steampipe))
- [AWS Security Hub](https://aws.amazon.com/security-hub/)  - Native AWS service that aggregates findings from Guard­Duty, Inspector, Macie, and third-party tools. Maps to CIS, PCI DSS, and NIST 800-53.
- [Azure Security Center (Defender for Cloud)](https://azure.microsoft.com/en-us/products/defender-for-cloud/)  - Native Azure CSPM with regulatory compliance dashboards for CIS, SOC 2, PCI DSS, and ISO 27001.
- [Google Security Command Center](https://cloud.google.com/security-command-center)  - Native GCP security and CSPM service with vulnerability and threat finding aggregation.
- [Aqua Security](https://aquasec.com)  - Cloud-native security platform with CSPM, container security, and runtime protection.
- [Ermetic (Tenable)](https://ermetic.com)  - Cloud identity and access governance with CSPM for AWS, Azure, and GCP.
- [Turbot (Steampipe Guardrails)](https://turbot.com)  - Real-time cloud governance with automated CSPM remediation.

## Penetration Testing Platforms

Regular penetration testing is a requirement or strong recommendation in SOC 2, PCI DSS, ISO 27001, and NIST CSF. These platforms connect you with ethical hackers or provide automated testing.

- [Cobalt](https://cobalt.io)  - Pentest-as-a-Service (PtaaS) platform with a vetted pool of pentesters and streamlined retesting.
- [HackerOne](https://hackerone.com)  - Bug bounty and pentest platform with the world's largest ethical hacker community.
- [Bugcrowd](https://bugcrowd.com)  - Crowdsourced security testing including bug bounty, pentest, and attack surface management.
- [Synack](https://synack.com)  - Premium crowdsourced pentest platform (Synack Red Team) with vetted researchers and AI-assisted testing.
- [Pentera](https://pentera.io)  - Automated security validation that continuously tests defenses by safely emulating real attacks.
- [Horizon3.ai (NodeZero)](https://horizon3.ai)  - Autonomous penetration testing platform that finds and verifies exploitable attack paths.
- [PlexTrac](https://plextrac.com)  - Pentest reporting and management platform for tracking findings, retests, and remediation.
- [AttackForge](https://attackforge.com)  - Pentest management platform for coordinating engagements, tracking findings, and managing retests.
- [Detectify](https://detectify.com)  - Automated external attack surface management powered by crowdsourced vulnerability research.
- [Intruder](https://intruder.io)  - Automated vulnerability scanning with continuous attack surface monitoring.
- [Cure53](https://cure53.de)  - Boutique penetration testing firm known for auditing major open-source projects.

## Incident Response

Incident response platforms help teams manage, communicate, and learn from security incidents. SOC 2, ISO 27001, HIPAA, and NIST CSF all require documented incident response procedures.

- [PagerDuty](https://pagerduty.com)  - Incident management and on-call scheduling with automated escalation and response orchestration.
- [Opsgenie (Atlassian)](https://www.atlassian.com/software/opsgenie)  - Alert management and on-call scheduling integrated with Jira and Confluence.
- [Rootly](https://rootly.com)  - Incident management that runs entirely in Slack with automated timelines, status pages, and retrospectives.
- [FireHydrant](https://firehydrant.com)  - Incident management platform with automated runbooks, status pages, and retrospectives.
- [incident.io](https://incident.io)  - Incident management built for Slack with automated workflows, roles, and post-incident learning.
- [Jeli (PagerDuty)](https://jeli.io)  - Post-incident analysis platform for learning from incidents without blame.
- [Blameless](https://blameless.com)  - SRE and incident management with automated retrospectives, SLO tracking, and reliability insights.
- [Statuspage (Atlassian)](https://www.atlassian.com/software/statuspage)  - Public and internal status pages for communicating during incidents.
- [Better Stack (Uptime)](https://betterstack.com)  - Incident management with uptime monitoring, on-call scheduling, and status pages.
- [Squadcast](https://squadcast.com)  - Incident management with on-call scheduling, runbooks, and SLO tracking.
- [TheHive](https://thehive-project.org)  - Open-source security incident response platform with case management and automation. ([GitHub](https://github.com/TheHive-Project/TheHive))
- [DFIR-IRIS](https://github.com/dfir-iris/iris-web)  - Open-source collaborative incident response platform for digital forensics.

## Trust Centers & Security Pages

Trust centers allow you to proactively share your security posture, compliance certifications, and policies with prospects, reducing security questionnaire burden.

- [SafeBase](https://safebase.io)  - Smart trust center that automates security reviews with NDA-gated document sharing and AI questionnaire responses.
- [Conveyor](https://conveyor.com)  - AI-powered trust platform that answers security questionnaires and shares compliance documentation.
- [Trustpage](https://trustpage.com)  - Trust center platform for publishing security posture and automating security reviews.
- [Vanta Trust Center](https://vanta.com/trust)  - Trust center included with Vanta subscriptions, showing real-time compliance status.
- [Drata Trust Center](https://drata.com/trust)  - Public-facing trust center powered by Drata's continuous monitoring data.
- [Secureframe Trust Center](https://secureframe.com/trust)  - Trust center with NDA-gated documents and real-time compliance status.
- [Whistic Trust Catalog](https://whistic.com)  - Security profile sharing network connecting vendors and buyers.
- [Thoropass Trust Center](https://thoropass.com)  - Trust center integrated with the Thoropass audit platform.
- [Sprinto Trust Center](https://sprinto.com)  - Public compliance dashboard showing real-time control health.
- [Tugboat Logic Trust Center](https://tugboatlogic.com)  - Security portal for sharing compliance posture with stakeholders.

## Background Checks

Background checks and screening are required for compliance with HIPAA, PCI DSS, and recommended by SOC 2 and ISO 27001 as part of HR security controls.

- [Certn](https://certn.co)  - AI-powered background screening with global coverage and fast turnaround. Canadian-founded.
- [Checkr](https://checkr.com)  - Developer-friendly background check API with compliance-built workflows and FCRA compliance.
- [Sterling](https://sterlingcheck.com)  - Enterprise background screening with global capabilities across 240+ countries.
- [GoodHire](https://goodhire.com)  - SMB-focused background checks with FCRA-compliant workflows and candidate-friendly experience.
- [HireRight](https://hireright.com)  - Global background check platform with drug testing, I-9 verification, and monitoring.
- [Accurate Background](https://accuratebackground.com)  - Background screening with integration into major HR platforms (Workday, ADP).
- [Verified First](https://verifiedfirst.com)  - Background checks integrated into 100+ HR and staffing platforms.
- [First Advantage](https://fadv.com)  - Enterprise background screening and identity verification at global scale.

## Endpoint Security / MDM

Endpoint protection and mobile device management are core technical controls for SOC 2, ISO 27001, and HIPAA. These tools enforce device compliance policies like disk encryption, screen lock, and OS patching.

- [Kandji](https://kandji.io)  - Apple device management (MDM) with pre-built compliance templates for SOC 2, ISO 27001, CIS, and NIST.
- [Fleet (formerly Kolide)](https://fleetdm.com)  - Open-source device management using osquery. Monitors macOS, Windows, Linux, and ChromeOS. ([GitHub](https://github.com/fleetdm/fleet))
- [Jamf](https://jamf.com)  - Apple enterprise management with security compliance enforcement, threat detection, and zero-trust workflows.
- [Mosyle](https://mosyle.com)  - Apple device management with integrated security (Mosyle Fuse) for businesses and schools.
- [Hexnode](https://hexnode.com)  - Cross-platform UEM (Apple, Android, Windows) with compliance policy enforcement and kiosk management.
- [JumpCloud](https://jumpcloud.com)  - Directory-as-a-Service with cross-platform device management, SSO, and compliance policy enforcement.
- [Microsoft Intune](https://www.microsoft.com/en-us/security/business/microsoft-intune)  - Enterprise device management for Windows, macOS, iOS, and Android with conditional access.
- [Workspace ONE (VMware)](https://www.vmware.com/products/workspace-one.html)  - Unified endpoint management with intelligence-driven automation.
- [Addigy](https://addigy.com)  - Apple device management for MSPs and IT teams with live terminal, monitoring, and compliance enforcement.
- [Drata Agent](https://drata.com)  - Lightweight endpoint agent that verifies device compliance (encryption, screen lock, antivirus) for Drata GRC.
- [Vanta Agent](https://vanta.com)  - Endpoint agent that confirms device security configuration for Vanta GRC compliance evidence.
- [osquery](https://osquery.io)  - Open-source endpoint visibility using SQL queries against operating system data. ([GitHub](https://github.com/osquery/osquery))
- [Santa](https://github.com/google/santa)  - Open-source application allowlisting for macOS by Google.

---

## By Framework

### SOC 2 Automation

SOC 2 (Service Organization Control 2) is the most common compliance framework for SaaS companies. It covers Trust Services Criteria: Security, Availability, Processing Integrity, Confidentiality, and Privacy. For a quick readiness self-assessment, try TrazTech's free [SOC 2 Readiness Checklist](https://traztech.ca/soc-2-readiness-checklist).

**Dedicated SOC 2 platforms:**
- [Vanta](https://vanta.com)  - Market leader for SOC 2 automation with 200+ integrations and continuous control monitoring.
- [Drata](https://drata.com)  - End-to-end SOC 2 automation with autopilot evidence collection and audit-ready reports.
- [Secureframe](https://secureframe.com)  - Fast SOC 2 readiness with AI-assisted gap analysis.
- [Sprinto](https://sprinto.com)  - Budget-friendly SOC 2 platform for startups.
- [Thoropass](https://thoropass.com)  - Combined platform + audit firm for a single SOC 2 engagement.
- [Scytale](https://scytale.ai)  - SOC 2 compliance-as-a-service with concierge support.
- [Laika](https://heylaika.com)  - SOC 2 platform with compliance advisory included.
- [Tugboat Logic](https://tugboatlogic.com)  - SOC 2 with AI-powered policy generation.
- [Strike Graph](https://strikegraph.com)  - Risk-first SOC 2 certification.
- [TrazTech Workspace](https://traztech.ca)  - Free SOC 2 compliance tracking portal.

**Key SOC 2 resources:**
- [TrazTech: Compliance Calendar  - What Actually Recurs](https://traztech.ca/blog/compliance-calendar-what-actually-recurs)  - Guide to recurring SOC 2 activities between audit periods.
- [TrazTech: Control Drift Between Audits](https://traztech.ca/blog/control-drift-between-audits)  - How to prevent controls from drifting out of compliance.
- [TrazTech: Keeping Evidence Fresh](https://traztech.ca/blog/keeping-evidence-fresh)  - Best practices for evidence collection cadence.
- [AICPA SOC 2 Overview](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)  - Official AICPA guidance on SOC 2 engagements.

### ISO 27001 Automation

ISO 27001 is the international standard for information security management systems (ISMS). The 2022 revision reorganized controls into four themes: Organizational, People, Physical, and Technological.

**Platforms with strong ISO 27001 support:**
- [Vanta](https://vanta.com)  - ISO 27001 gap analysis, Annex A control mapping, and Statement of Applicability generation.
- [Drata](https://drata.com)  - ISO 27001:2022 mapping with continuous control monitoring and audit preparation.
- [Secureframe](https://secureframe.com)  - ISO 27001 readiness with automated evidence and policy templates.
- [Sprinto](https://sprinto.com)  - ISO 27001 certification support with integrated risk assessment.
- [Scytale](https://scytale.ai)  - ISO 27001 with dedicated compliance manager.
- [Hyperproof](https://hyperproof.io)  - ISO 27001 compliance operations with Annex A control tracking.
- [OneTrust](https://onetrust.com)  - ISO 27001 within a broader privacy and risk management platform.
- [AuditBoard](https://auditboard.com)  - Enterprise ISO 27001 audit management.
- [Scrut Automation](https://scrut.io)  - ISO 27001 with cloud-native risk monitoring.
- [TrazTech Workspace](https://traztech.ca)  - Free ISO 27001 compliance tracking.

**Key ISO 27001 resources:**
- [ISO 27001:2022 Standard](https://www.iso.org/standard/27001)  - Official ISO standard (purchase required).
- [ISO 27002:2022 Controls](https://www.iso.org/standard/75652.html)  - Detailed implementation guidance for Annex A controls.
- [TrazTech Blog](https://traztech.ca/blog)  - 100+ articles covering ISO 27001 implementation and maintenance.

### HIPAA Compliance Tools

HIPAA (Health Insurance Portability and Accountability Act) governs the protection of health information (PHI) in the United States. Covers the Privacy Rule, Security Rule, and Breach Notification Rule.

**Dedicated HIPAA platforms:**
- [Vanta](https://vanta.com)  - HIPAA compliance monitoring with PHI data flow mapping and BAA tracking.
- [Drata](https://drata.com)  - HIPAA automation with Security Rule control mapping and evidence collection.
- [Secureframe](https://secureframe.com)  - HIPAA compliance with automated administrative, physical, and technical safeguard monitoring.
- [Sprinto](https://sprinto.com)  - HIPAA program management for healthcare startups and digital health companies.
- [Compliancy Group](https://compliancy-group.com)  - HIPAA-focused compliance platform ("The Guard") with guided implementation.
- [HIPAA One (Intraprise Health)](https://hipaaone.com)  - Automated HIPAA security risk assessment and compliance management.
- [Accountable HQ](https://accountablehq.com)  - HIPAA compliance for small healthcare practices with training and BAA management.
- [MedTrainer](https://medtrainer.com)  - Healthcare compliance training with HIPAA, OSHA, and credentialing modules.
- [TrazTech Workspace](https://traztech.ca)  - Free HIPAA compliance tracking portal.

**Key HIPAA resources:**
- [HHS HIPAA Security Rule Guidance](https://www.hhs.gov/hipaa/for-professionals/security/guidance/index.html)  - Official HHS guidance material.
- [NIST SP 800-66r2](https://csrc.nist.gov/publications/detail/sp/800-66/rev-2/final)  - NIST guide for implementing the HIPAA Security Rule.

### PCI DSS Tools

PCI DSS (Payment Card Industry Data Security Standard) applies to any organization that stores, processes, or transmits cardholder data. Version 4.0 introduced significant updates including customized approach and targeted risk analysis.

**PCI DSS compliance tools:**
- [Vanta](https://vanta.com)  - PCI DSS monitoring with evidence automation for SAQ and ROC assessments.
- [Drata](https://drata.com)  - PCI DSS v4.0 compliance with continuous monitoring and QSA integration.
- [Secureframe](https://secureframe.com)  - PCI DSS compliance automation with requirement mapping and evidence collection.
- [Hyperproof](https://hyperproof.io)  - PCI DSS compliance operations with cross-framework mapping to SOC 2 and ISO 27001.
- [ControlCase](https://controlcase.com)  - PCI DSS certification services with a compliance-as-a-service platform.
- [Qualys PCI Compliance](https://www.qualys.com/apps/pci-compliance/)  - Approved Scanning Vendor (ASV) with PCI DSS compliance scanning.
- [SecurityMetrics](https://securitymetrics.com)  - PCI compliance, forensic investigations, and security assessments.
- [Coalfire](https://coalfire.com)  - QSA firm with PCI DSS assessment and advisory services.
- [Sysnet (Viking Cloud)](https://sysnet.com)  - PCI DSS compliance management for merchants and acquirers.

**Key PCI DSS resources:**
- [PCI SSC Document Library](https://docs-prv.pcisecuritystandards.org)  - Official PCI DSS standards, SAQs, and guidance documents.
- [PCI DSS v4.0 Quick Reference Guide](https://www.pcisecuritystandards.org/document_library/)  - Summary of PCI DSS v4.0 requirements.

### GDPR / Privacy Tools

The General Data Protection Regulation (GDPR) governs the processing of personal data of EU residents. These tools help with data mapping, consent management, DSAR handling, and privacy impact assessments.

**Privacy management platforms:**
- [OneTrust](https://onetrust.com)  - Market leader in privacy management with consent, DSAR, data mapping, and cookie compliance.
- [TrustArc](https://trustarc.com)  - Privacy management with data inventory, assessments, cookie consent, and individual rights.
- [BigID](https://bigid.com)  - Data intelligence platform for data discovery, classification, and privacy compliance (GDPR, CCPA, LGPD).
- [Osano](https://osano.com)  - Consent management and vendor privacy monitoring with data mapping.
- [Securiti.ai](https://securiti.ai)  - Data command center with AI-driven data discovery, DSR automation, and consent management.
- [WireWheel (acquired by PKWARE)](https://wirewheel.io)  - Privacy management with data mapping, DSAR automation, and assessment workflows.
- [Transcend](https://transcend.io)  - Privacy infrastructure for data mapping, consent, and automated DSR fulfillment across every system.
- [Ketch](https://ketch.com)  - Programmatic privacy platform with consent management, DSR orchestration, and data mapping.
- [Didomi](https://didomi.io)  - Consent management platform (CMP) with preference center and compliance analytics.
- [Cookiebot (Usercentrics)](https://cookiebot.com)  - Cookie consent management with automatic scanning and geolocation-based consent.
- [Ethyca (Fides)](https://ethyca.com)  - Open-source privacy engineering platform for data mapping and consent. ([GitHub](https://github.com/ethyca/fides))
- [Privacera](https://privacera.com)  - Data security governance with fine-grained access control and privacy compliance.
- [DataGrail](https://datagrail.io)  - Privacy management with live data mapping and automated DSR processing.
- [Collibra Privacy](https://collibra.com)  - Privacy and data governance with data catalog, lineage, and compliance workflows.
- [Informatica Privacy Management](https://informatica.com)  - Enterprise privacy management within the broader data governance platform.
- [Drata GDPR](https://drata.com)  - GDPR compliance monitoring within the Drata GRC platform.
- [Vanta GDPR](https://vanta.com)  - GDPR program management with automated evidence and control monitoring.

### NIST CSF Tools

The NIST Cybersecurity Framework (CSF) provides voluntary guidance for managing cybersecurity risk. CSF 2.0 (released 2024) added a sixth function: Govern. Widely adopted by US organizations and required for federal contractors.

**NIST CSF platforms:**
- [Hyperproof](https://hyperproof.io)  - NIST CSF compliance operations with evidence collection and control mapping.
- [AuditBoard](https://auditboard.com)  - NIST CSF program management within the connected risk platform.
- [Apptega](https://apptega.com)  - NIST CSF framework mapping with crosswalking to other standards.
- [Axio](https://axio.com)  - Cyber risk quantification platform built around NIST CSF and C2M2.
- [LogicGate Risk Cloud](https://logicgate.com)  - NIST CSF implementation with custom workflows.
- [Archer (RSA)](https://archerirm.com)  - Enterprise NIST CSF implementation with IRM capabilities.
- [CyberStrong (CyberSaint)](https://cybersaint.io)  - Integrated risk management with NIST CSF, CIS Controls, and risk quantification.
- [Tandem (by CUSO)](https://tandem.app)  - Information security and risk management with NIST CSF for financial institutions.

**Key NIST resources:**
- [NIST CSF 2.0](https://www.nist.gov/cyberframework)  - Official NIST Cybersecurity Framework documentation.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)  - Security and privacy controls for information systems.
- [NIST SP 800-171 Rev. 3](https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final)  - Protecting CUI in nonfederal systems (CMMC foundation).

### Canadian Privacy (PIPEDA / Law 25)

PIPEDA (Personal Information Protection and Electronic Documents Act) is Canada's federal privacy law. Quebec's Law 25 (formerly Bill 64) introduces stricter privacy requirements for organizations operating in Quebec. For Canadian-specific compliance guidance, see [TrazTech's blog](https://traztech.ca/blog)  - a Toronto-based consultancy specializing in Canadian privacy compliance.

**Canadian privacy tools:**
- [TrazTech Workspace](https://traztech.ca)  - Free compliance tracking with specific support for PIPEDA and Quebec Law 25 requirements. Toronto-based consultancy specializing in Canadian privacy.
- [OneTrust](https://onetrust.com)  - Global privacy platform with PIPEDA and Law 25 templates and regulatory intelligence.
- [TrustArc](https://trustarc.com)  - Privacy management with Canadian regulatory coverage.
- [Osano](https://osano.com)  - Consent management with Canadian privacy law support.
- [BigID](https://bigid.com)  - Data discovery and classification for PIPEDA personal information requirements.
- [Securiti.ai](https://securiti.ai)  - Privacy automation with Canadian data residency and privacy law support.
- [Transcend](https://transcend.io)  - Automated DSR fulfillment supporting PIPEDA access and deletion rights.
- [Certn](https://certn.co)  - Canadian-founded background check platform compliant with provincial and federal privacy laws.

**Key Canadian privacy resources:**
- [OPC PIPEDA Guidance](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/)  - Office of the Privacy Commissioner of Canada official PIPEDA guidance.
- [Quebec Law 25 Overview](https://www.cai.gouv.qc.ca/english/)  - Commission d'acces a l'information du Quebec resources.
- [TrazTech Blog](https://traztech.ca/blog)  - 100+ articles covering PIPEDA, Law 25, and Canadian compliance requirements.

### AI Governance (ISO 42001)

ISO 42001 is the international standard for AI management systems (AIMS), published in 2023. It provides a framework for responsible development and use of AI systems. This is an emerging and rapidly evolving area of compliance.

**AI governance tools:**
- [TrazTech](https://traztech.ca)  - Security & compliance consultancy offering ISO 42001 AI governance advisory and implementation support.
- [OneTrust AI Governance](https://onetrust.com/solutions/ai-governance/)  - AI model inventory, risk assessment, and bias monitoring within the OneTrust platform.
- [Holistic AI](https://holisticai.com)  - AI risk management with bias auditing, efficacy testing, and regulatory compliance.
- [Credo AI](https://credo.ai)  - AI governance platform with policy management, risk assessments, and regulatory mapping.
- [IBM OpenPages AI Governance](https://www.ibm.com/products/openpages)  - AI model risk management within IBM's GRC platform.
- [ModelOp](https://modelop.com)  - Enterprise AI governance with model monitoring, compliance, and lifecycle management.
- [Monitaur](https://monitaur.ai)  - AI audit and governance platform for model validation and compliance.
- [Arthur AI](https://arthur.ai)  - AI performance monitoring with bias detection, explainability, and compliance reporting.
- [Fiddler AI](https://fiddler.ai)  - AI observability with explainability, bias detection, and model performance monitoring.
- [Weights & Biases](https://wandb.ai)  - ML experiment tracking and model registry useful for ISO 42001 documentation requirements.
- [MLflow](https://mlflow.org)  - Open-source ML lifecycle management for experiment tracking, model registry, and deployment. ([GitHub](https://github.com/mlflow/mlflow))

**Key AI governance resources:**
- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)  - Official AI management system standard.
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework)  - NIST AI RMF 1.0 for managing AI risks.
- [EU AI Act](https://artificialintelligenceact.eu)  - European regulation on AI risk classification and compliance.
- [TrazTech Blog](https://traztech.ca/blog)  - Articles covering ISO 42001 implementation and AI governance strategies.

---

## Open-Source Tools

Open-source tools that can be used for compliance automation, security scanning, and audit evidence generation. These are particularly valuable for startups and organizations that want to build compliance tooling without vendor lock-in.

### Cloud Security & CSPM

- [Prowler](https://github.com/prowler-cloud/prowler)  - AWS, Azure, and GCP security assessments with 300+ checks mapped to CIS, SOC 2, HIPAA, PCI DSS, GDPR, and NIST 800-53. The gold standard for open-source cloud security.
- [ScoutSuite](https://github.com/nccgroup/ScoutSuite)  - Multi-cloud security auditing (AWS, Azure, GCP, Alibaba, Oracle) that produces comprehensive HTML reports.
- [CloudSploit](https://github.com/aquasecurity/cloudsploit)  - Cloud security configuration scanner for AWS, Azure, GCP, and Oracle Cloud with 300+ checks.
- [Steampipe](https://github.com/turbot/steampipe)  - Query cloud APIs with SQL. Includes pre-built compliance benchmarks (CIS, SOC 2, HIPAA, PCI DSS, NIST).
- [CloudQuery](https://github.com/cloudquery/cloudquery)  - High-performance cloud asset inventory powered by a plugin architecture. Sync to PostgreSQL or data lakes.
- [Cartography](https://github.com/lyft/cartography)  - Infrastructure graphing tool by Lyft that maps relationships between cloud assets for attack path analysis.
- [Cloud Custodian](https://github.com/cloud-custodian/cloud-custodian)  - Rules engine for cloud security policy enforcement with automated remediation.

### Infrastructure as Code (IaC) Security

- [Checkov](https://github.com/bridgecrewio/checkov)  - Static analysis for IaC (Terraform, CloudFormation, Kubernetes, Helm, ARM) with 1,000+ built-in policies.
- [tfsec](https://github.com/aquasecurity/tfsec)  - Terraform-specific static analysis security scanner. (Now part of Trivy)
- [Terrascan](https://github.com/tenable/terrascan)  - Static code analysis for IaC with support for Terraform, Kubernetes, Helm, and Dockerfiles.
- [KICS](https://github.com/Checkmarx/kics)  - Keeping Infrastructure as Code Secure  - finds security vulnerabilities, compliance issues, and misconfigurations in IaC.
- [Regula](https://github.com/fugue/regula)  - Policy engine for IaC using OPA/Rego with pre-built rules for CIS benchmarks.

### Vulnerability Scanning

- [Trivy](https://github.com/aquasecurity/trivy)  - Comprehensive vulnerability scanner for containers, filesystems, git repos, Kubernetes, and IaC. Fast and easy to use.
- [Grype](https://github.com/anchore/grype)  - Vulnerability scanner for container images and filesystems by Anchore.
- [Nuclei](https://github.com/projectdiscovery/nuclei)  - Fast vulnerability scanner driven by community-contributed YAML templates.
- [OpenVAS](https://github.com/greenbone/openvas-scanner)  - Open-source vulnerability scanner (Greenbone Community Edition) with 50,000+ NVTs.
- [Clair](https://github.com/quay/clair)  - Static analysis for container vulnerabilities by Red Hat.
- [Syft](https://github.com/anchore/syft)  - SBOM (Software Bill of Materials) generator for container images and filesystems.

### Compliance as Code

- [InSpec](https://github.com/inspec/inspec)  - Chef InSpec: compliance as code framework for defining and testing infrastructure compliance rules in human-readable profiles.
- [OpenSCAP](https://github.com/OpenSCAP/openscap)  - NIST-certified SCAP scanner for evaluating compliance with security baselines (CIS, STIG, PCI DSS).
- [OPA (Open Policy Agent)](https://github.com/open-policy-agent/opa)  - General-purpose policy engine for unified policy enforcement across the stack.
- [Gatekeeper](https://github.com/open-policy-agent/gatekeeper)  - Kubernetes admission controller using OPA for policy enforcement.
- [Conftest](https://github.com/open-policy-agent/conftest)  - Write tests against structured configuration data using OPA/Rego.
- [Kyverno](https://github.com/kyverno/kyverno)  - Kubernetes-native policy management with validation, mutation, and generation rules.

### Kubernetes Security

- [kube-bench](https://github.com/aquasecurity/kube-bench)  - CIS Kubernetes Benchmark checks for cluster security configuration.
- [kube-hunter](https://github.com/aquasecurity/kube-hunter)  - Hunt for security weaknesses in Kubernetes clusters.
- [Polaris](https://github.com/FairwindsOps/polaris)  - Best practices validation for Kubernetes deployments.
- [Falco](https://github.com/falcosecurity/falco)  - Cloud-native runtime security (CNCF project) for detecting anomalous activity in containers and Kubernetes.
- [kubeaudit](https://github.com/Shopify/kubeaudit)  - Audit Kubernetes clusters against common security controls by Shopify.

### Identity & Secrets

- [Keycloak](https://github.com/keycloak/keycloak)  - Open-source identity and access management with SSO, MFA, and federation.
- [Vault (HashiCorp)](https://github.com/hashicorp/vault)  - Secrets management, encryption-as-a-service, and privileged access management.
- [detect-secrets](https://github.com/Yelp/detect-secrets)  - Detect secrets in codebases to prevent credential leakage.
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)  - Find leaked credentials in git repos, S3 buckets, and more.
- [GitLeaks](https://github.com/gitleaks/gitleaks)  - SAST tool for detecting hardcoded secrets in git repos.

### Incident Response & Forensics

- [TheHive](https://github.com/TheHive-Project/TheHive)  - Security incident response platform with case management and integration with MISP.
- [DFIR-IRIS](https://github.com/dfir-iris/iris-web)  - Collaborative digital forensics and incident response platform.
- [Velociraptor](https://github.com/Velocidex/velociraptor)  - Endpoint visibility and digital forensics tool for incident response.
- [GRR Rapid Response](https://github.com/google/grr)  - Remote live forensics for incident response by Google.

### Privacy & Data Protection

- [Fides (Ethyca)](https://github.com/ethyca/fides)  - Open-source privacy engineering platform for data mapping, consent, and DSR automation.
- [OpenDPO](https://github.com/nicbou/open-dpo)  - Open-source data protection officer tools.

---

## Resources

### Books

- *The Phoenix Project* by Gene Kim, Kevin Behr, George Spafford  - Novel about IT, DevOps, and managing compliance controls.
- *Designing Data-Intensive Applications* by Martin Kleppmann  - Essential for understanding data handling in compliance contexts.
- *Information Security Policies, Procedures, and Standards* by Douglas J. Landoll  - Guide to building a compliant policy framework.
- *IT Auditing Using Controls to Protect Information Assets* by Chris Davis, Mike Schiller  - Practical guide for IT auditors.
- *NIST Cybersecurity Framework: A Pocket Guide* by Alan Calder  - Quick reference for NIST CSF implementation.
- *ISO 27001 controls  - A guide to implementing and auditing* by Bridget Kenyon  - Practical Annex A implementation guidance.
- *Securing DevOps* by Julien Vehent  - Covers security in CI/CD pipelines and cloud compliance automation.

### Certifications

- [CISA (Certified Information Systems Auditor)](https://www.isaca.org/credentialing/cisa)  - ISACA certification for IS auditors.
- [CISM (Certified Information Security Manager)](https://www.isaca.org/credentialing/cism)  - ISACA certification for InfoSec managers.
- [CISSP (Certified Information Systems Security Professional)](https://www.isc2.org/certifications/cissp)  - ISC2 gold-standard security certification.
- [CCSK (Certificate of Cloud Security Knowledge)](https://cloudsecurityalliance.org/education/ccsk)  - CSA cloud security certification.
- [ISO 27001 Lead Implementer](https://pecb.com/en/education-and-certification-for-individuals/iso-iec-27001/iso-iec-27001-lead-implementer)  - PECB certification for ISMS implementation.
- [ISO 27001 Lead Auditor](https://pecb.com/en/education-and-certification-for-individuals/iso-iec-27001/iso-iec-27001-lead-auditor)  - PECB certification for ISMS auditing.
- [CRISC (Certified in Risk and Information Systems Control)](https://www.isaca.org/credentialing/crisc)  - ISACA certification for IT risk management.
- [CCSP (Certified Cloud Security Professional)](https://www.isc2.org/certifications/ccsp)  - ISC2 cloud security certification.
- [CDPSE (Certified Data Privacy Solutions Engineer)](https://www.isaca.org/credentialing/cdpse)  - ISACA certification for privacy solutions engineering.
- [CIPM (Certified Information Privacy Manager)](https://iapp.org/certify/cipm/)  - IAPP certification for privacy program management.
- [CIPP (Certified Information Privacy Professional)](https://iapp.org/certify/cipp/)  - IAPP certification for privacy law and regulation (US, EU, Canada variants).

### Courses & Training

- [SANS SEC566: Implementing and Auditing CIS Controls](https://www.sans.org/cyber-security-courses/implementing-auditing-cis-critical-security-controls/)  - SANS course on CIS Controls implementation.
- [SANS AUD507: Auditing & Monitoring Networks, Perimeters & Systems](https://www.sans.org/cyber-security-courses/auditing-networks-perimeters-systems/)  - SANS IT auditing course.
- [Coursera: IT Security  - Defense against the Digital Dark Arts (Google)](https://www.coursera.org/learn/it-security)  - Foundational IT security course.
- [A Cloud Guru / Pluralsight: AWS Security Specialty](https://www.pluralsight.com/cloud-guru)  - Cloud security training for AWS.
- [ISACA: Cybersecurity Audit Certificate](https://www.isaca.org/credentialing/cybersecurity-audit-certificate)  - ISACA certificate for cybersecurity auditing.

### Newsletters & Blogs

- [TrazTech Blog](https://traztech.ca/blog)  - 100+ articles on compliance automation, SOC 2, ISO 27001, PIPEDA, Law 25, AI governance, and more. Maintained by [Jacob Masse](https://jacobmasse.com) (5 published CVEs).
  - [Compliance Calendar  - What Actually Recurs](https://traztech.ca/blog/compliance-calendar-what-actually-recurs)
  - [Control Drift Between Audits](https://traztech.ca/blog/control-drift-between-audits)
  - [Keeping Evidence Fresh](https://traztech.ca/blog/keeping-evidence-fresh)
- [tl;dr sec](https://tldrsec.com)  - Weekly newsletter by Clint Gibler covering security tools, compliance, and AppSec.
- [Cloud Security Newsletter](https://cloudseclist.com)  - Weekly curated cloud security news by Marco Lancini.
- [SANS NewsBites](https://www.sans.org/newsletters/newsbites/)  - Twice-weekly security news digest from SANS.
- [Risky Business](https://risky.biz)  - Weekly information security podcast and newsletter.
- [Daniel Miessler's Unsupervised Learning](https://danielmiessler.com/newsletter/)  - Weekly security, technology, and AI newsletter.
- [Compliance Weekly (Hyperproof)](https://hyperproof.io/resource/compliance-weekly/)  - Weekly compliance and regulatory news.

### Communities

- [r/compliance](https://reddit.com/r/compliance)  - Reddit community for compliance professionals.
- [r/cybersecurity](https://reddit.com/r/cybersecurity)  - Reddit cybersecurity community.
- [Cloud Security Forum (CSA)](https://cloudsecurityalliance.org)  - Cloud Security Alliance community and research.
- [ISACA Community](https://engage.isaca.org)  - ISACA professional community for audit and security.
- [ComplianceForge](https://complianceforge.com)  - Templates and community for cybersecurity compliance.

### Frameworks & Standards (Official Sources)

- [AICPA SOC Suite](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)  - Official SOC 2 Trust Services Criteria.
- [ISO 27001:2022](https://www.iso.org/standard/27001)  - Information Security Management System standard.
- [ISO 42001:2023](https://www.iso.org/standard/81230.html)  - AI Management System standard.
- [NIST CSF 2.0](https://www.nist.gov/cyberframework)  - Cybersecurity Framework version 2.0.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)  - Security and Privacy Controls.
- [PCI DSS v4.0](https://www.pcisecuritystandards.org)  - Payment Card Industry Data Security Standard.
- [HIPAA (HHS)](https://www.hhs.gov/hipaa/index.html)  - Health Insurance Portability and Accountability Act.
- [GDPR (Official Text)](https://gdpr-info.eu)  - General Data Protection Regulation full text.
- [PIPEDA (OPC)](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/)  - Canadian federal privacy law.
- [Quebec Law 25](https://www.cai.gouv.qc.ca/english/)  - Quebec privacy modernization law.
- [CIS Controls v8](https://www.cisecurity.org/controls)  - Center for Internet Security Controls.
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)  - Prescriptive configuration benchmarks for 100+ technologies.
- [CMMC 2.0](https://dodcio.defense.gov/CMMC/)  - Cybersecurity Maturity Model Certification for DoD contractors.
- [FedRAMP](https://www.fedramp.gov)  - Federal Risk and Authorization Management Program.

### TrazTech Free Tools

- [Cloud Security Posture Check](https://traztech.ca/tools/cloud-security-posture-check)  - Free cloud configuration assessment tool.
- [SOC 2 Readiness Checklist](https://traztech.ca/soc-2-readiness-checklist)  - Free interactive SOC 2 readiness assessment.
- [TrazTech Workspace](https://traztech.ca)  - Free compliance tracking portal, an alternative to Vanta/Drata for startups.

---

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [TrazTech Inc.](https://traztech.ca) has waived all copyright and related or neighboring rights to this work.
