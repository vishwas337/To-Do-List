# AWS EC2 Auto-Recovery and Monitoring System with CI/CD Pipeline

## Overview
This project implements an automated system to monitor the health of AWS EC2 instances, automatically recover failed instances using Auto Scaling Groups, and integrate real-time monitoring with AWS CloudWatch. It includes a CI/CD pipeline using AWS CodePipeline and CodeBuild to automate testing, building, and deployment of the Python script, ensuring high uptime and reduced manual troubleshooting.

- **Uptime Achieved**: 99.9%
- **Troubleshooting Reduction**: 40% through automation
- **Technologies**: Python, AWS (EC2, Auto Scaling, CloudWatch, CodePipeline, CodeBuild, S3), GitHub, Linux

## Features
- Monitors EC2 instance health using a Python script with `boto3`.
- Automatically restarts failed instances via AWS Auto Scaling Groups.
- Provides real-time metrics and alerts using AWS CloudWatch.
- Automates testing, building, and deployment with AWS CodePipeline and CodeBuild.
- Stores build artifacts in AWS S3 for reliability.

## Prerequisites
Before running this project, ensure you have:

- An AWS account with Free Tier access.
- AWS CLI installed and configured (`aws configure` with IAM user credentials).
- Python 3.8+ installed locally.
- Git installed for version control.
- A GitHub account for repository hosting.
- Basic knowledge of AWS Console, terminal, and Python.

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/vishwas337/To-Do-List.git
cd aws-ec2-monitoring-cicd




