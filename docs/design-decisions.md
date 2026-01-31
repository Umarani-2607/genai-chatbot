# Design Decisions

This document explains the key technical decisions made in this project.

---

## Why Amazon Bedrock?

- Fully managed LLM service
- No need to manage model infrastructure
- Integrates naturally with AWS IAM
- Suitable for enterprise-grade applications

---

## Why Mock Responses in CI?

- CI pipelines should be deterministic
- Avoids cloud cost during automated builds
- Prevents pipeline failures due to missing credentials
- Enables safe local development

---

## Why Docker?

- Ensures consistent runtime across environments
- Simplifies deployment and CI/CD integration
- Eliminates "works on my machine" issues

---

## Why GitHub Actions?

- Native integration with GitHub repositories
- Easy to automate Docker builds
- Industry-standard CI/CD tool
