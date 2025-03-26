# CV Generation API

A FastAPI-based service that generates professional CVs in PDF format from structured JSON data. This system is built with flexibility and maintainability in mind, using HTML templates for easy customization and updates.

## System Architecture

The CV generation system is built on a modern, flexible architecture that makes it easy to update and maintain:

- **HTML Template Based**: The system uses HTML templates for CV generation, making it highly customizable and easy to update. You can modify the design by simply updating the HTML and CSS without touching the core logic.
- **Asynchronous Processing**: CV generation is handled asynchronously using FastAPI's background tasks, ensuring the API remains responsive.
- **Redis Integration**: The system uses Redis for storing CV generation status and file paths, providing efficient caching and state management.
- **Modular Design**: The codebase is organized into clear modules for different functionalities (API routes, services, models).

## Features

- Modern and professional CV template
- Asynchronous PDF generation
- Background task processing with FastAPI
- Redis caching for better performance
- RESTful API endpoints
- Beautiful and responsive design
- Easy template customization through HTML/CSS
- Scalable architecture

## Prerequisites

- Docker and Docker Compose (for containerized deployment)
- OR
- Python 3.12
- Redis server

## Installation

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/Shrhawk/CV-Genration-API.git
cd CV-Genration-API
```

2. Set up environment variables:
```bash
cp .env.example .env
```

3. Build and start the containers:
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000/docs`

### Manual Installation (Skip if using Docker)

1. Clone the repository:
```bash
git clone https://github.com/Shrhawk/CV-Genration-API.git
cd CV-Genration-API
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000/docs`

## API Endpoints

The system provides three main endpoints for CV generation and management:

### 1. Generate CV
POST /api/generate-cv/
Content-Type: application/json

This endpoint initiates the CV generation process asynchronously. It accepts JSON data and returns a CV ID that can be used to check the status or download the CV later.

```json
{
  "full_name": "John Doe",
  "job_title": "Senior Software Engineer",
  "contact": {
    "email": "john.doe@example.com",
    "phone": "+1 (555) 123-4567"
  },
  "social_links": [
    {
      "platform": "GitHub",
      "url": "https://github.com/johndoe"
    },
    {
      "platform": "LinkedIn",
      "url": "https://linkedin.com/in/johndoe"
    }
  ],
  "summary": "Passionate software engineer with 8+ years of experience in full-stack development. Specialized in building scalable web applications using modern technologies. Strong focus on clean code and best practices.",
  "experience": [
    {
      "company": "Tech Solutions Inc.",
      "role": "Senior Software Engineer",
      "start_date": "Jan 2020",
      "end_date": "Present",
      "responsibilities": [
        "Led a team of 5 developers in developing a cloud-based SaaS platform",
        "Implemented microservices architecture using Python and FastAPI",
        "Reduced system response time by 40% through optimization",
        "Mentored junior developers and conducted code reviews"
      ]
    },
    {
      "company": "Digital Innovations Ltd",
      "role": "Software Engineer",
      "start_date": "Jun 2017",
      "end_date": "Dec 2019",
      "responsibilities": [
        "Developed RESTful APIs using Django and PostgreSQL",
        "Implemented automated testing, achieving 90% code coverage",
        "Collaborated with UX team to improve user interface design"
      ]
    },
    {
      "company": "Digital Innovations Ltd",
      "role": "Software Engineer",
      "start_date": "Jun 2017",
      "end_date": "Dec 2019",
      "responsibilities": [
        "Developed RESTful APIs using Django and PostgreSQL",
        "Implemented automated testing, achieving 90% code coverage",
        "Collaborated with UX team to improve user interface design"
      ]
    }
  ],
  "education": [
    {
      "institution": "University of Technology",
      "degree": "Master of Science",
      "major": "Computer Science",
      "cgpa": 3.92,
      "year": "2017",
      "achievements": [
        "Specialized in Distributed Systems and Cloud Computing",
        "Research Assistant in Cloud Computing Lab",
        "Published paper on 'Scalable Microservices Architecture' in IEEE Conference",
        "Recipient of Academic Excellence Scholarship"
      ]
    },
    {
      "institution": "State University",
      "degree": "Bachelor of Science",
      "major": "Software Engineering",
      "cgpa": 3.85,
      "year": "2015",
      "achievements": [
        "Graduated with High Honors (Summa Cum Laude)",
        "Led university's competitive programming team",
        "Developed an automated course registration system as capstone project",
        "Dean's List for all semesters"
      ]
    }
  ],
  "projects": [
    {
      "name": "Cloud-Native E-commerce Platform",
      "description": "Designed and developed a scalable e-commerce platform using microservices architecture",
      "technologies": ["Python", "FastAPI", "React", "Docker", "Kubernetes", "AWS", "MongoDB"],
      "link": "https://github.com/johndoe/ecommerce-platform",
      "highlights": [
        "Implemented event-driven architecture using Apache Kafka",
        "Designed CI/CD pipeline using GitHub Actions and ArgoCD",
        "Achieved 99.9% uptime with auto-scaling and fault tolerance",
        "Integrated multiple payment gateways and shipping providers"
      ]
    },
    {
      "name": "AI-Powered Code Review Assistant",
      "description": "Built an AI-powered tool that automates code review process by analyzing code patterns and suggesting improvements",
      "technologies": ["Python", "TensorFlow", "FastAPI", "Docker", "PostgreSQL"],
      "link": "https://github.com/johndoe/code-review-ai",
      "highlights": [
        "Trained ML model on 1M+ code reviews achieving 85% accuracy",
        "Reduced average code review time by 60%",
        "Integrated with GitHub and GitLab through webhooks",
        "Built real-time code analysis pipeline"
      ]
    },
    {
      "name": "Distributed Task Scheduler",
      "description": "Created a distributed task scheduling system for handling millions of concurrent jobs",
      "technologies": ["Go", "Redis", "gRPC", "Docker", "Prometheus", "Grafana"],
      "link": "https://github.com/johndoe/task-scheduler",
      "highlights": [
        "Implemented distributed locking using Redis",
        "Built comprehensive monitoring and alerting system",
        "Handled 100K+ concurrent tasks with sub-second latency",
        "Achieved 99.99% task completion reliability"
      ]
    }
  ],
  "skills": [
    "Python",
    "JavaScript",
    "React",
    "Node.js",
    "FastAPI",
    "Docker",
    "Kubernetes",
    "AWS",
    "MongoDB",
    "PostgreSQL"
  ],
  "languages": [
    {
      "language": "English",
      "level": "Native"
    },
    {
      "language": "Spanish",
      "level": "Professional"
    },
    {
      "language": "French",
      "level": "Intermediate"
    }
  ],
  "certifications": [
    {
      "name": "AWS Certified Solutions Architect",
      "year": "2022"
    },
    {
      "name": "Google Cloud Professional Developer",
      "year": "2021"
    },
    {
      "name": "Docker Certified Associate",
      "year": "2020"
    }
  ],
  "config": {
    "font_family": "Open Sans",
    "theme": "default",
    "company_logo": "https://dummyimage.com/200x60/007bff/ffffff.png&text=Company+Logo",
    "sections": [
      {
        "id": "summary",
        "title": "Professional Summary",
        "order": 1,
        "visible": true
      },
      {
        "id": "experience",
        "title": "Professional Experience",
        "order": 2,
        "visible": true
      },
      {
        "id": "projects",
        "title": "Featured Projects",
        "order": 3,
        "visible": true
      },
      {
        "id": "skills",
        "title": "Technical Skills",
        "order": 4,
        "visible": true
      },
      {
        "id": "education",
        "title": "Education",
        "order": 5,
        "visible": true
      },
      {
        "id": "certifications",
        "title": "Professional Certifications",
        "order": 6,
        "visible": true
      },
      {
        "id": "languages",
        "title": "Languages",
        "order": 7,
        "visible": true
      }
    ]
  }
}
```

Response:
```json
{
  "status": "processing",
  "cv_id": "20240315_123456_john_doe",
  "message": "CV generation started"
}
```

### 2. Check CV Status
GET /api/cv-status/{cv_id}

This endpoint allows you to check the status of your CV generation process. The status can be:
- "processing": CV is being generated
- "completed": CV is ready for download
- "failed": An error occurred during generation

Response:
```json
{
  "status": "completed"
}
```

### 3. Download CV
GET /api/download-cv/{cv_id}

This endpoint allows you to download the generated CV once it's ready. It returns the PDF file directly.

## Template Customization

The system uses HTML templates for CV generation, making it easy to customize the design:

1. Navigate to the templates directory
2. Modify the HTML and CSS files to update the design
3. The changes will be reflected in all newly generated CVs

The template system supports:
- Custom styling through CSS
- Dynamic content injection
- Responsive design
- Modern layout options
