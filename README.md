# Django Project Setup Guide

This document explains how to set up and run this Django project on your local machine.

## Prerequisites

Ensure that the following software is installed on your system:

- Python (3.10 or higher)
- pip (Python package manager)
- Virtualenv (optional but recommended)
- Git (for cloning the repository)

## Getting Started

Follow the steps below to set up and run the project.

### 1. Clone the Repository

First, clone the repository to your local machine using Git.

```bash
git clone <your-repository-url>
cd <your-project-directory>
```

### 2.  Create a Virtual Environment

```bash
python -m venv env
```


### 3.  Download all requirements required

```bash
pip install -r requirements.txt
```

### 4.  Migrate the database then createsuperuser

```bash
python manage.py migrate

python manage.py createsuperuser
```

### 5.  Run the code 
```bash
python manage.py runserver
```

