# Payment Service (FastAPI) — DevSecOps Security Testbed

## Overview
This repository contains a **minimal FastAPI-based backend service** designed **specifically as a controlled security testbed** for DevSecOps automation experiments.

The service is **intentionally implemented with several security weaknesses** to support:
- automated security scanning,
- advisory generation,
- remediation validation,
- before–after security comparison.

⚠️ **This project is NOT intended for production use.**

---

## Purpose
The main objectives of this repository are:

1. To provide a **simple and controllable backend service** for security testing
2. To validate **multi-tool DevSecOps pipelines**, including:
   - Static Application Security Testing (SAST)
   - Software Composition Analysis (SCA)
   - Container security scanning
3. To demonstrate that **security advisories are actionable** and can be verified through remediation and re-scanning

This repository is used as part of a broader **Intelligent DevSecOps Automation Framework**.

---

## Technology Stack
- Language: **Python 3.11**
- Framework: **FastAPI**
- ASGI Server: **Uvicorn**
- Containerization: **Docker**

---

## Repository Structure
```text
payment-service/
├── app/
│   ├── main.py        # FastAPI application entry point
│   ├── routes.py      # API route definitions
│   ├── payment.py     # Dummy payment logic
│   └── config.py      # Configuration (includes intentional secrets)
│
├── requirements.txt   # Python dependencies (includes vulnerable versions)
├── Dockerfile         # Container definition (intentionally insecure)
├── .dockerignore
└── README.md
