# Cyber-Security-Attacks
# OWASP Juice Shop Simulated Attack

# Overview
This project focuses on conducting penetration testing on the **OWASP Juice Shop**, a deliberately insecure web application designed to help learners understand and exploit common web vulnerabilities. The goal is to learn, document, and present findings on web application weaknesses and provide recommendations for mitigation.

# Objectives
- Apply penetration testing techniques to identify vulnerabilities.
- Document findings in a structured report and create a video report showcasing the attack methodology and outcomes.

# Attack Scenarios

 1. **Enumeration to Find Admin Path**
- **Description**: Discover hidden paths by analyzing URL structures.
- **Outcome**: Admin functionality revealed for further exploitation.

### 2. **Brute Force on Admin Credentials**
- **Description**: Using tools like Hydra to guess the admin password (e.g., admin@juice-sh.op).
- **Outcome**: Admin access obtained, granting full control over the application.

### 3. **Cross-Site Scripting (XSS) in Product Search**
- **Description**: Injecting malicious scripts into the search bar to execute arbitrary JavaScript.
- **Outcome**: Potential for session hijacking, steal cookies

## Tools Used
- **Kali Linux**
- **Hydra**
- **Dirb**

## Resources
- [OWASP Juice Shop Website](https://owasp.org/www-project-juice-shop/)
- [Kali Linux](https://www.kali.org/)


## Conclusion
This project provides hands-on experience in identifying and exploiting web application vulnerabilities, enhancing knowledge of cybersecurity and penetration testing. The findings are structured to help stakeholders understand risks and take steps toward improving application security.

