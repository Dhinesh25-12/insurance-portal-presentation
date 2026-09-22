# Insurance Portal Application - Presentation Index & Quick Start Guide

## 📋 Overview

This repository contains multiple comprehensive PowerPoint presentations documenting the **Insurance Policy Management Portal** project - a full-stack web application with Angular frontend and Spring Boot backend.

**Project Repositories:**
- 🎨 [Frontend UI Repository](https://github.com/Dhinesh25-12/ui-repo) - Angular 22 TypeScript
- ⚙️ [Backend Repository](https://github.com/Dhinesh25-12/backend-repo) - Spring Boot 3.2 Java
- 📊 [Presentation Repository](https://github.com/Dhinesh25-12/insurance-portal-presentation) (this repo)

---

## 📊 Available Presentations

### 1. **Main Project Presentation** (10 Slides)
**File:** `generate_presentation.py`  
**Output:** `Insurance_Portal_Application_Demo.pptx`

**Contents:**
- Project Overview & Objectives
- Business Modules Implemented (7 core modules)
- Application Architecture (Frontend, Backend, Infrastructure)
- Technology Stack Breakdown
- Technical Decisions & Rationale
- Deployment Approach (CI/CD, Docker, Terraform)
- Challenges Encountered & Solutions
- Lessons Learned
- Future Enhancements & Roadmap

**Best For:** Executive summaries, stakeholder demos, quick project overview

---

### 2. **Security & Architecture Deep Dive** (12 Slides)
**File:** `generate_security_architecture.py`  
**Output:** `Insurance_Portal_Security_Architecture.pptx`

**Contents:**
- Security Architecture Overview
- User Roles & Permissions (5 core roles: ADMIN, MANAGER, AGENT, CUSTOMER, AUDITOR)
- Authentication Flow (JWT-based with refresh tokens)
- Authorization & RBAC Implementation
- High-Level System Architecture Diagram
- Microservices Architecture (6 services with ports)
- Frontend Architecture (React + TypeScript layers)
- Data Flow & Security Measures
- Database Schema Overview
- Security Best Practices
- Deployment Security
- Architecture Diagrams (Text-based ASCII art)

**Best For:** Security reviews, architecture discussions, technical deep dives

---

### 3. **Comprehensive Implementation Presentation** (16 Slides)
**File:** `generate_comprehensive_presentation.py`  
**Output:** `Insurance_Portal_Complete_Presentation.pptx`

**Contents:**
- Project Overview (full-stack details)
- Frontend Architecture (Angular 22 detailed breakdown)
- Backend Architecture (Spring Boot 3.2 detailed breakdown)
- Database Schema (PostgreSQL with Flyway migrations)
- Authentication & JWT Flow
- Role-Based Access Control (RBAC)
- RESTful API Endpoints Overview
- Complete Technology Stack
- Security Implementation Details
- AWS Deployment Architecture
- CI/CD Pipeline (GitHub Actions)
- Feature Walkthrough & Workflows
- Testing & Quality Assurance Strategy
- Known Limitations & Future Roadmap
- Running & Deploying Instructions

**Best For:** Development teams, technical documentation, onboarding new team members

---

## 🚀 Quick Start - Generating Presentations

### Prerequisites
```bash
# Python 3.7+
# Install python-pptx
pip install -r requirements.txt
```

### Generate All Presentations

```bash
# Generate Main Presentation (10 slides)
python generate_presentation.py
# Creates: Insurance_Portal_Application_Demo.pptx

# Generate Security & Architecture (12 slides)
python generate_security_architecture.py
# Creates: Insurance_Portal_Security_Architecture.pptx

# Generate Comprehensive Presentation (16 slides)
python generate_comprehensive_presentation.py
# Creates: Insurance_Portal_Complete_Presentation.pptx
```

All presentations will be created in the current directory with professional formatting and color schemes.

---

## 🏗️ System Architecture Overview

### Frontend Architecture (Angular 22)
```
Client Layer (Browser)
    ↓
Authentication Interceptor (JWT attachment)
    ↓
Angular Components
  ├─ Auth Module (Login/Register)
  ├─ Dashboard Module
  ├─ Products Module
  ├─ Policies Module (Purchase, Renew, Cancel)
  ├─ Claims Module (File, Track, Approve)
  ├─ Payments Module
  ├─ Reports Module
  └─ Admin Module (User Management)
    ↓
HTTP Interceptor (Error handling, 401 logout)
    ↓
REST API Client
    ↓
Spring Boot Backend (via HTTPS/TLS)
```

### Backend Architecture (Spring Boot 3.2)
```
API Gateway (ALB on AWS)
    ↓
Spring Security (JWT validation, Role-based authorization)
    ↓
REST Controllers
    ↓
Service Layer (Business Logic)
    ↓
Repository Layer (Spring Data JPA)
    ↓
PostgreSQL Database
  ├─ Users & Roles
  ├─ Policies
  ├─ Claims
  ├─ Payments
  ├─ Products
  └─ Audit Logs
```

---

## 🔐 Security Features

### Authentication
- ✅ JWT (JSON Web Tokens) with RS256 signing
- ✅ Bcrypt password hashing (10+ rounds)
- ✅ Refresh token mechanism (7-day expiry)
- ✅ Access token short-lived (1 hour)
- ✅ HTTPS/TLS 1.3 for all communications

### Authorization
- ✅ Role-Based Access Control (RBAC)
- ✅ 5 Core Roles: ADMIN, AGENT, CLAIMS_OFFICER, CUSTOMER, AUDITOR
- ✅ Granular permission system (policy:create, claim:approve, etc.)
- ✅ Spring Security @PreAuthorize annotations
- ✅ Resource ownership verification

### Data Protection
- ✅ SQL injection prevention (parameterized queries)
- ✅ XSS protection (input sanitization)
- ✅ CSRF token protection
- ✅ AES-256 encryption at rest
- ✅ Audit logging of all user actions

---

## 📱 Key Features

### Policy Management
- Browse insurance products
- Purchase new policies
- Renew existing policies
- View policy details and coverage
- Request policy cancellations (admin approval)
- Premium payment tracking

### Claims Processing
- Submit new claims with incident details
- Upload supporting documents
- Track claim status in real-time
- Claims officer approval workflow
- Settlement decision and payment
- Digital receipt generation

### Premium Payments
- View payment history
- Make online premium payments
- Auto-generated invoices
- Downloadable receipts
- Payment tracking and reconciliation

### Analytics & Reporting
- Customer: Policy summary, claims status, payment history
- Admin: Top customers by premium, claims ratio, product performance
- Advanced SQL views and window functions
- Monthly revenue reports

### User Management
- Create and manage user accounts
- Assign/modify user roles
- Activate and suspend accounts
- Role-specific dashboards
- User activity audit logs

---

## 🛠️ Technology Stack

### Frontend
- **Framework:** Angular 22
- **Language:** TypeScript (56.7% of repo)
- **Styling:** SCSS/CSS (10.7% of repo)
- **Build Tool:** Angular CLI
- **State Management:** RxJS Observables
- **HTTP Client:** Angular HttpClient
- **Testing:** Vitest (JUnit 5 style)

### Backend
- **Framework:** Spring Boot 3.2
- **Language:** Java 17 (82.3% of repo)
- **ORM:** Hibernate / Spring Data JPA
- **Authentication:** Spring Security + JWT (jjwt)
- **API Documentation:** Springdoc-OpenAPI (Swagger UI)
- **Testing:** JUnit 5 + Spring Boot Test
- **Database Testing:** H2 in-memory

### Database
- **Primary:** PostgreSQL 14+
- **Migrations:** Flyway
- **Testing:** H2 in-memory (development)
- **Connection Pooling:** HikariCP (via Spring Boot)

### Infrastructure
- **Cloud Provider:** AWS
- **Compute (Backend):** ECS Fargate + Docker
- **Compute (Frontend):** EC2 + nginx
- **Database:** RDS PostgreSQL (managed)
- **Storage:** S3 buckets (documents, artifacts)
- **Networking:** VPC with public/private subnets
- **Load Balancing:** Application Load Balancer (ALB)
- **Logging:** CloudWatch
- **IaC:** Terraform
- **CI/CD:** GitHub Actions

---

## 🔄 API Endpoints Summary

### Authentication
```
POST /api/auth/login              - User login with credentials
POST /api/auth/register           - New user registration
POST /api/auth/refresh            - Refresh JWT token
```

### Products
```
GET  /api/products                - List all products (all roles)
POST /api/products                - Create product (ADMIN only)
PUT  /api/products/{id}           - Update product (ADMIN only)
DELETE /api/products/{id}         - Delete product (ADMIN only)
```

### Policies
```
GET  /api/policies/my             - Get own policies (CUSTOMER)
GET  /api/policies                - List all policies (AGENT, ADMIN)
POST /api/policies                - Purchase policy (CUSTOMER)
GET  /api/policies/{id}           - Get policy details
POST /api/policies/{id}/renew     - Renew policy
POST /api/policies/{id}/cancel    - Request cancellation (CUSTOMER)
POST /api/policies/{id}/cancel/approve - Approve cancellation (ADMIN)
```

### Claims
```
GET  /api/claims/my               - Get own claims (CUSTOMER)
GET  /api/claims/queue            - Claims queue (CLAIMS_OFFICER)
POST /api/claims                  - File new claim (CUSTOMER)
PATCH /api/claims/{id}/status     - Update claim status
PUT  /api/claims/{id}/decision    - Officer decision (CLAIMS_OFFICER)
```

### Payments
```
GET  /api/payments/history        - Payment history (CUSTOMER)
POST /api/payments                - Make payment (CUSTOMER)
GET  /api/payments/{id}/invoice   - Get invoice
GET  /api/payments/{id}/receipt   - Get receipt
```

### Reports
```
GET  /api/reports/customer/**     - Customer reports (CUSTOMER)
GET  /api/reports/admin/**        - Admin reports (ADMIN)
```

### Admin
```
GET  /api/admin/users             - List all users (ADMIN)
PUT  /api/admin/users/{id}/roles  - Assign roles (ADMIN)
PATCH /api/admin/users/{id}/status - Activate/suspend (ADMIN)
```

---

## 📊 Default Test Users

All users have password: **`Password123!`**

| Username | Role | Access Level |
|----------|------|--------------|
| `admin` | ADMIN | Full system access |
| `agent1` | AGENT | Policy and customer management |
| `claims1` | CLAIMS_OFFICER | Claims processing and approval |
| `customer1` | CUSTOMER | Self-service policies and claims |
| `customer2` | CUSTOMER | Self-service policies and claims |

---

## 🚀 Running the Application

### Development Environment

**Frontend:**
```bash
cd ui-repo
npm install --legacy-peer-deps
npm start
# Runs on http://localhost:4200
# Proxies API calls to http://localhost:8080/api
```

**Backend:**
```bash
cd backend-repo
mvn spring-boot:run
# Runs on http://localhost:8080
# Swagger UI: http://localhost:8080/swagger-ui.html
```

**Database:**
```bash
# PostgreSQL connection string:
# jdbc:postgresql://localhost:5432/insurance_portal
# User: insurance_user
# Password: insurance_pass
```

### Production Deployment

**Infrastructure Provisioning:**
```bash
# Backend infrastructure
cd backend-repo/terraform/environments/prod
terraform init -backend-config=backend.hcl
terraform plan -var-file=prod.tfvars
terraform apply -var-file=prod.tfvars

# Frontend infrastructure (uses backend's VPC)
cd ui-repo/terraform/environments/shared
terraform init -backend-config=backend.hcl
terraform plan -var-file=prod.tfvars
terraform apply -var-file=prod.tfvars
```

**CI/CD Deployment:**
- Push to `main` branch
- GitHub Actions automatically:
  1. Runs tests
  2. Builds Docker image (backend) / Angular bundle (frontend)
  3. Pushes to AWS ECR (backend) / S3 (frontend)
  4. Updates AWS ECS (backend) / EC2 instances (frontend)

---

## 📈 Database Schema

### Core Tables
```sql
-- User Management
app_user           -- Users with authentication
role               -- System roles (ADMIN, AGENT, etc.)
user_role          -- Many-to-many role assignment

-- Insurance Domain
customer           -- Customer profiles and KYC data
product            -- Insurance products (Life, Health, Auto, etc.)
policy             -- Customer policies with status
claim              -- Claims filed against policies
payment            -- Premium payments and receipts

-- Audit & Compliance
audit_log          -- All user actions logged
```

### Advanced Features
```sql
-- Analytical Views
policy_summary_view    -- Aggregated policy data
claim_summary_view     -- Aggregated claim data
payment_rollup_view    -- Payment analytics

-- PL/pgSQL Functions
fn_generate_policy_number()    -- Auto-generate policy IDs
fn_claims_settlement()          -- Claim settlement logic
```

---

## ✅ Testing

### Frontend Testing
```bash
cd ui-repo
npm test                    # Run all tests
npm test -- --watch        # Watch mode
npm test -- --coverage     # Coverage report
```

**Coverage Areas:**
- Authentication guards and role guards
- HTTP interceptors (JWT attachment, error handling)
- Services (API communication)
- Components (UI behavior)

### Backend Testing
```bash
cd backend-repo
mvn test                    # Unit tests
mvn verify                  # Unit + Integration tests
mvn test -Dgroups=integration  # Integration only
```

**Coverage Areas:**
- Service layer business logic
- Repository layer queries
- Controller endpoints
- Exception handling
- Security filters

---

## 📚 Documentation

### Generated Documentation
- **Swagger UI:** `http://localhost:8080/swagger-ui.html`
- **OpenAPI JSON:** `http://localhost:8080/v3/api-docs`
- **Health Check:** `http://localhost:8080/actuator/health`

### In Repository
- [Backend README](https://github.com/Dhinesh25-12/backend-repo/blob/main/README.md)
- [Frontend README](https://github.com/Dhinesh25-12/ui-repo/blob/main/README.md)
- [Backend Deployment Guide](https://github.com/Dhinesh25-12/backend-repo/blob/main/DEPLOYMENT.md)
- [Terraform README](https://github.com/Dhinesh25-12/backend-repo/blob/main/terraform/README.md)

---

## 🎯 Project Statistics

| Metric | Value |
|--------|-------|
| **Total Slides** | 38 slides across 3 presentations |
| **Frontend Language** | TypeScript 56.7% |
| **Backend Language** | Java 82.3% |
| **Database** | PostgreSQL |
| **API Endpoints** | 25+ endpoints |
| **User Roles** | 5 core roles |
| **Business Modules** | 7 core modules |
| **Test Coverage** | Frontend: Unit tests, Backend: Unit + Integration |
| **Infrastructure** | AWS (ECS, EC2, RDS, S3) |
| **Deployment** | Terraform + GitHub Actions |

---

## 🔄 Development Workflow

1. **Feature Development**
   - Create feature branch from `main`
   - Write code (frontend + backend)
   - Write tests
   - Commit and push

2. **Continuous Integration (GitHub Actions)**
   - Run tests automatically
   - Build Docker image / Angular bundle
   - Code quality checks
   - Security scanning

3. **Deployment**
   - Merge PR to `main` (requires approval)
   - GitHub Actions deploys to production
   - Zero-downtime rolling deployment
   - Automated database migrations

---

## 🐛 Troubleshooting

### Frontend Issues

**Port 4200 already in use:**
```bash
ng serve --port 4300
```

**Peer dependency errors:**
```bash
npm install --legacy-peer-deps
```

**API connection issues:**
```bash
# Check backend is running on http://localhost:8080
# Update src/environments/environment.development.ts
apiBaseUrl: 'http://localhost:8080/api'
```

### Backend Issues

**Database connection failed:**
```bash
# Verify PostgreSQL is running
# Check connection string in application.yml
# Verify DB_USERNAME and DB_PASSWORD environment variables
```

**JWT token errors:**
```bash
# Check JWT_SECRET environment variable is set
# Override in application.yml: jwt.secret
```

### AWS Deployment Issues

**ECS task fails to start:**
```bash
# Check CloudWatch logs for error messages
# Verify environment variables are set in task definition
# Check security group allows necessary ports
```

**Frontend not updating after deployment:**
```bash
# Clear S3 bucket and re-deploy
# Clear CloudFront cache (if using CDN)
# Verify nginx is syncing from S3
```

---

## 📞 Support & Contact

For issues, questions, or contributions:
- 📧 Create an issue in the respective repository
- 🔗 See individual repository READMEs for detailed information
- 📊 Review presentations for architecture and design decisions

---

## 📄 Presentation Metadata

| Presentation | Slides | Size | Focus | Audience |
|--------------|--------|------|-------|----------|
| Main Demo | 10 | ~5 MB | Overview & Features | Stakeholders, Managers |
| Security & Architecture | 12 | ~6 MB | Security, Roles, Architecture Diagrams | Security Team, Architects |
| Comprehensive | 16 | ~8 MB | Full Implementation Details | Development Team, Onboarding |

---

## 📋 File Structure

```
insurance-portal-presentation/
├── generate_presentation.py                    # Main presentation (10 slides)
├── generate_security_architecture.py           # Security deep dive (12 slides)
├── generate_comprehensive_presentation.py      # Full implementation (16 slides)
├── requirements.txt                            # Python dependencies
├── README.md                                   # Main documentation (this file)
├── SECURITY_ARCHITECTURE.md                    # Detailed security documentation
├── Insurance_Portal_Application_Demo.pptx      # Generated: Main presentation
├── Insurance_Portal_Security_Architecture.pptx # Generated: Security presentation
└── Insurance_Portal_Complete_Presentation.pptx # Generated: Comprehensive presentation
```

---

## 🎓 Learning Path

**For New Team Members:**
1. Start with `Insurance_Portal_Application_Demo.pptx` (overview)
2. Read `README.md` (this file) for quick reference
3. Review `Insurance_Portal_Complete_Presentation.pptx` for technical details
4. Study `SECURITY_ARCHITECTURE.md` for security implementation
5. Clone and run the application locally
6. Review source code in ui-repo and backend-repo

**For Stakeholders:**
1. View `Insurance_Portal_Application_Demo.pptx`
2. Review project statistics and timeline
3. Check feature walkthroughs
4. View deployment architecture

**For Security Team:**
1. Review `Insurance_Portal_Security_Architecture.pptx`
2. Study `SECURITY_ARCHITECTURE.md`
3. Review authentication & authorization implementation
4. Check compliance features

---

**Document Version:** 1.0  
**Last Updated:** September 2026  
**Project Status:** Complete & Production-Ready
