# SDLC (Software Development Life Cycle)

## Interview Definition

SDLC is a structured process that defines the stages involved in developing software applications from initial planning through deployment and maintenance. It provides a systematic approach to building high-quality software that meets customer expectations within time and cost constraints.

---

## SDLC Phases

### Phase 1: Planning and Requirements Analysis

What happens:
- Stakeholders define project goals and scope
- Feasibility study conducted (technical, operational, economic)
- Risk assessment performed
- Resource allocation determined
- Project timeline established

Key deliverables:
- Project plan
- Feasibility study report
- Risk assessment document
- Resource allocation matrix

Interview tip: When asked about this phase, emphasize that poor planning is the primary cause of project failure. Requirements gathering involves all stakeholders to ensure alignment between business needs and technical implementation.

### Phase 2: Requirements Definition

What happens:
- Functional requirements documented (what the system should do)
- Non-functional requirements defined (performance, security, scalability)
- User stories or use cases created
- Requirements validated with stakeholders

Key deliverables:
- Software Requirements Specification (SRS)
- Use case diagrams
- User stories

Interview tip: Distinguish between functional requirements (features) and non-functional requirements (quality attributes like security, performance, availability).

### Phase 3: Design

What happens:
- System architecture designed
- Database schema created
- User interface mockups developed
- Security architecture defined
- Technology stack selected

Key deliverables:
- High-Level Design (HLD) document
- Low-Level Design (LLD) document
- Database design
- Interface design specifications

Interview tip: Mention that design phase includes threat modeling and security architecture review in secure SDLC practices.

### Phase 4: Development (Implementation)

What happens:
- Code written according to design specifications
- Unit tests developed
- Code reviews conducted
- Version control utilized
- Coding standards enforced

Key deliverables:
- Source code
- Unit test cases
- Code review reports

Interview tip: Reference secure coding practices, OWASP guidelines, and static code analysis integration during development.

### Phase 5: Testing

What happens:
- Various testing types executed
- Defects identified and tracked
- Test results documented
- Security testing performed

Testing types:
- Unit Testing: Individual components tested in isolation
- Integration Testing: Combined components tested together
- System Testing: Complete system tested against requirements
- User Acceptance Testing (UAT): End users validate functionality
- Security Testing: Vulnerabilities identified and addressed
- Performance Testing: System behavior under load evaluated

Key deliverables:
- Test plans
- Test cases
- Defect reports
- Test summary report

Interview tip: Emphasize the importance of security testing including SAST, DAST, and penetration testing as part of the testing phase.

### Phase 6: Deployment

What happens:
- Application deployed to production environment
- User training conducted
- Documentation finalized
- Go-live checklist executed

Deployment strategies:
- Big Bang: Full deployment at once
- Phased: Gradual rollout by feature or user group
- Parallel: Old and new systems run simultaneously
- Blue-Green: Two identical environments with traffic switching

Key deliverables:
- Deployment guide
- User manuals
- Training materials

### Phase 7: Maintenance

What happens:
- Bug fixes implemented
- Performance optimizations applied
- Security patches deployed
- Feature enhancements developed
- System monitoring conducted

Maintenance types:
- Corrective: Fixing defects
- Adaptive: Adapting to environment changes
- Perfective: Improving performance or adding features
- Preventive: Preventing future issues

Key deliverables:
- Maintenance reports
- Updated documentation
- Patch release notes

---

## SDLC Models

### Waterfall Model

Description: Linear sequential approach where each phase must be completed before the next begins.

Phases flow: Requirements -> Design -> Implementation -> Testing -> Deployment -> Maintenance

Advantages:
- Simple and easy to understand
- Well-documented process
- Clear milestones and deliverables

Disadvantages:
- No flexibility for changes
- Testing occurs late in the cycle
- Not suitable for complex projects

Best suited for: Projects with well-defined, stable requirements.

### Agile Model

Description: Iterative approach that delivers working software in short cycles called sprints (typically 2-4 weeks).

Core principles:
- Customer collaboration over contract negotiation
- Responding to change over following a plan
- Working software over comprehensive documentation
- Individuals and interactions over processes and tools

Advantages:
- Flexible and adaptive to change
- Continuous customer feedback
- Early and frequent delivery

Disadvantages:
- Requires experienced team members
- Documentation may be insufficient
- Scope creep risk

Best suited for: Projects with evolving requirements and need for rapid delivery.

### DevOps Model

Description: Combines development and operations teams to enable continuous integration, delivery, and deployment.

Key practices:
- Infrastructure as Code
- Continuous Integration/Continuous Deployment
- Automated testing
- Monitoring and logging
- Collaboration between Dev and Ops

Advantages:
- Faster time to market
- Improved collaboration
- Automated processes reduce errors

Disadvantages:
- Cultural shift required
- Initial setup complexity
- Security can be overlooked without DevSecOps

Best suited for: Organizations seeking rapid, reliable software delivery.

### Spiral Model

Description: Risk-driven model combining iterative development with systematic aspects of waterfall.

Four quadrants:
1. Planning: Requirements gathering, objective identification
2. Risk Analysis: Risk identification and mitigation strategies
3. Engineering: Development and testing
4. Evaluation: Customer review and feedback

Advantages:
- Risk management focused
- Suitable for large, complex projects
- Flexibility for changes

Disadvantages:
- Expensive and time-consuming
- Requires risk assessment expertise
- Complex to manage

Best suited for: Large, high-risk projects with significant budget.

### V-Model (Verification and Validation)

Description: Extension of waterfall where testing phases correspond to each development phase.

Structure:
- Requirements Analysis <-> Acceptance Testing
- System Design <-> System Testing
- Architecture Design <-> Integration Testing
- Module Design <-> Unit Testing
- Coding (at the bottom of the V)

Advantages:
- Testing planned early
- Clear deliverables at each stage
- Higher quality through verification

Disadvantages:
- Rigid like waterfall
- No early prototypes
- Difficult to accommodate changes

Best suited for: Projects requiring high reliability (medical, aerospace).

---

## SDLC Models Comparison

| Model | Flexibility | Risk Management | Documentation | Speed |
|-------|-------------|-----------------|---------------|-------|
| Waterfall | Low | Low | High | Slow |
| Agile | High | Medium | Low | Fast |
| DevOps | High | Medium | Medium | Fast |
| Spiral | Medium | High | High | Slow |
| V-Model | Low | Medium | High | Slow |

---

## Secure SDLC (SSDLC)

Definition: Integration of security practices at every phase of the SDLC rather than treating security as an afterthought.

Security activities by phase:

| Phase | Security Activities |
|-------|---------------------|
| Planning | Security requirements, compliance requirements, risk assessment |
| Requirements | Security user stories, abuse cases, security acceptance criteria |
| Design | Threat modeling, security architecture review, secure design patterns |
| Development | Secure coding practices, SAST, code review, dependency scanning |
| Testing | DAST, penetration testing, security regression testing |
| Deployment | Security configuration review, hardening, vulnerability scanning |
| Maintenance | Patch management, security monitoring, incident response |

Key frameworks:
- Microsoft SDL (Security Development Lifecycle)
- OWASP SAMM (Software Assurance Maturity Model)
- NIST Secure Software Development Framework
- BSIMM (Building Security In Maturity Model)

Interview tip: When discussing SSDLC, emphasize "shift left" approach - integrating security early in the development process reduces cost and time to fix vulnerabilities.

---

## Common Interview Questions and Answers

Question: What is SDLC and why is it important?

Answer: SDLC is a systematic process for planning, creating, testing, and deploying software. It is important because it provides a structured framework that ensures quality, reduces risks, controls costs, and delivers software that meets user requirements. Without SDLC, projects often face scope creep, budget overruns, and quality issues.

Question: What is the difference between Waterfall and Agile?

Answer: Waterfall is a linear, sequential approach where each phase must be completed before moving to the next. It works well for projects with stable, well-defined requirements. Agile is an iterative approach that delivers working software in short cycles, allowing for continuous feedback and adaptation to changing requirements. Agile is preferred when requirements are expected to evolve or when rapid delivery is needed.

Question: How does security fit into SDLC?

Answer: Security should be integrated throughout the entire SDLC, not just at the testing phase. This is called Secure SDLC or "shifting left." It includes security requirements gathering during planning, threat modeling during design, secure coding practices and SAST during development, DAST and penetration testing during testing, and security monitoring during maintenance. This approach reduces the cost of fixing vulnerabilities and improves overall security posture.

Question: When would you choose Spiral model over Agile?

Answer: Spiral model is preferred for large, complex projects with significant risks and substantial budgets, such as aerospace or defense systems. It emphasizes risk analysis at each iteration. Agile is better suited for projects requiring rapid delivery and frequent customer feedback, typically in commercial software development where time-to-market is critical.

Question: What is the role of testing in SDLC?

Answer: Testing validates that software meets requirements and functions correctly. It includes multiple levels: unit testing verifies individual components, integration testing checks component interactions, system testing validates the complete system, and acceptance testing confirms the software meets user needs. In secure SDLC, testing also includes security testing such as SAST, DAST, and penetration testing to identify vulnerabilities before deployment.

Question: Explain the maintenance phase and its importance.

Answer: Maintenance is the longest and often most expensive phase of SDLC. It includes corrective maintenance (bug fixes), adaptive maintenance (environment changes), perfective maintenance (enhancements), and preventive maintenance (preventing future issues). From a security perspective, maintenance includes patch management, vulnerability remediation, and security monitoring. Neglecting maintenance leads to technical debt, security vulnerabilities, and system degradation.

---

## Key Terms

| Term | Definition |
|------|------------|
| SRS | Software Requirements Specification - documents what the system should do |
| HLD | High-Level Design - overall system architecture |
| LLD | Low-Level Design - detailed component design |
| UAT | User Acceptance Testing - validation by end users |
| SAST | Static Application Security Testing - code analysis without execution |
| DAST | Dynamic Application Security Testing - testing running application |
| Threat Modeling | Systematic identification of potential security threats |
| Shift Left | Moving security practices earlier in the development process |

---

## Additional Resources

- NIST SP 800-64: Security Considerations in the SDLC
- OWASP Software Assurance Maturity Model (SAMM)
- Microsoft Security Development Lifecycle
- ISO/IEC 12207: Software Life Cycle Processes

---

Tags: sdlc, software-development, security, interview-prep, devsecops