#!/usr/bin/env python3
"""
Insurance Portal Application - Comprehensive Presentation
Based on actual UI (Angular) and Backend (Spring Boot) repositories
Includes: Overview, Architecture, Security, Tech Stack, Deployment
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_comprehensive_presentation():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    # Color scheme
    PRIMARY = RGBColor(0, 102, 204)
    SECONDARY = RGBColor(51, 51, 51)
    WHITE = RGBColor(255, 255, 255)
    ACCENT = RGBColor(255, 102, 0)
    
    def create_title_slide(title, subtitle):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        bg = slide.background.fill
        bg.solid()
        bg.fore_color.rgb = PRIMARY
        
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(54)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER
        
        subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(2))
        tf = subtitle_box.text_frame
        p = tf.paragraphs[0]
        p.text = subtitle
        p.font.size = Pt(24)
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER
        
        return slide
    
    def create_content_slide(title, items):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        bg = slide.background.fill
        bg.solid()
        bg.fore_color.rgb = WHITE
        
        title_bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
        title_bar.fill.solid()
        title_bar.fill.fore_color.rgb = PRIMARY
        title_bar.line.color.rgb = PRIMARY
        tf = title_bar.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(38)
        p.font.bold = True
        p.font.color.rgb = WHITE
        
        content_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.1), Inches(8.6), Inches(6))
        tf = content_box.text_frame
        tf.word_wrap = True
        
        for i, item in enumerate(items):
            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = item
            p.font.size = Pt(15)
            p.font.color.rgb = SECONDARY
            p.space_before = Pt(5)
            p.space_after = Pt(5)
        
        return slide
    
    # ============ SLIDE 1: Title ============
    create_title_slide(
        "Insurance Policy Management Portal",
        "Complete Architecture & Implementation Overview\nAngular Frontend + Spring Boot Backend"
    )
    
    # ============ SLIDE 2: Project Overview ============
    create_content_slide("Project Overview", [
        "✅ Full-stack Insurance Management Portal",
        "✅ Multi-role support: ADMIN, AGENT, CLAIMS_OFFICER, CUSTOMER",
        "✅ Angular 22 TypeScript Frontend on AWS EC2",
        "✅ Spring Boot 3.2 Java Backend on AWS ECS Fargate",
        "✅ PostgreSQL Database with Flyway migrations",
        "✅ JWT-based authentication and role-based authorization",
        "✅ Infrastructure as Code using Terraform",
        "✅ CI/CD via GitHub Actions",
        "✅ Complete Swagger/OpenAPI documentation"
    ])
    
    # ============ SLIDE 3: Frontend Architecture (Angular) ============
    create_content_slide("Frontend Architecture - Angular 22", [
        "📱 Framework: Angular 22 with TypeScript (56.7%)",
        "🎨 Styling: SCSS (10.7%) with responsive design",
        "🏗️ Structure:",
        "   • core/ - Services, guards, interceptors, models (singleton)",
        "   • features/ - Feature modules (auth, dashboard, policies, claims, payments, reports, admin)",
        "   • shared/ - Reusable components (KPI cards, status badges, spinners, empty states)",
        "   • layout/shell - Sidebar + topbar navigation",
        "",
        "🔐 Security Features:",
        "   • HTTP interceptor - Attaches JWT to all requests (except login/register)",
        "   • Error interceptor - Handles 401s, logs out, redirects to login",
        "   • authGuard - Protects authenticated routes",
        "   • roleGuard - Restricts routes by role, redirects to /forbidden"
    ])
    
    # ============ SLIDE 4: Backend Architecture (Spring Boot) ============
    create_content_slide("Backend Architecture - Spring Boot 3.2", [
        "☕ Framework: Spring Boot 3.2 Java (82.3%)",
        "🗄️ Database: PostgreSQL with Flyway migrations",
        "🏗️ Project Structure:",
        "   • controller/ - REST endpoints",
        "   • service/ - Business logic layer",
        "   • repository/ - Spring Data JPA repositories",
        "   • entity/ - JPA entities and enums",
        "   • dto/ - Request/response DTOs",
        "   • security/ - JWT, UserDetails, filters",
        "   • exception/ - Global exception handling",
        "",
        "📊 Database Migrations:",
        "   • V1: Core schema (users, roles, policies, claims, payments)",
        "   • V2: Seed data (admin/agent/claims/customer users, products)",
        "   • V3: Views and PL/pgSQL functions for analytics"
    ])
    
    # ============ SLIDE 5: Database Schema ============
    create_content_slide("Database Schema - PostgreSQL", [
        "Core Entities:",
        "  • app_user - User accounts with JWT support",
        "  • role - System roles (ADMIN, AGENT, CLAIMS_OFFICER, CUSTOMER)",
        "  • user_role - Many-to-many role assignment",
        "  • customer - Extended customer profile",
        "  • product - Insurance products (Life, Health, Auto, Property)",
        "  • policy - Customer policies with status tracking",
        "  • claim - Claims filed against policies",
        "  • payment - Premium payments and receipts",
        "",
        "Advanced Features:",
        "  • Analytical Views: policy_summary_view, claim_summary_view, payment_rollup_view",
        "  • PL/pgSQL Functions: fn_generate_policy_number, fn_claims_settlement",
        "  • Indexes on common query patterns for performance"
    ])
    
    # ============ SLIDE 6: Authentication Flow ============
    create_content_slide("Authentication & JWT Flow", [
        "1️⃣ LOGIN REQUEST",
        "   POST /api/auth/login with username/password (HTTPS only)",
        "",
        "2️⃣ VALIDATION",
        "   Backend validates credentials against database",
        "   Bcrypt hash verification (never plain text comparison)",
        "",
        "3️⃣ JWT GENERATION",
        "   Payload contains: user ID, username, role, permissions",
        "   Signed with RS256 (asymmetric) private key",
        "   Expiration: 1 hour (configurable via JWT_EXPIRATION_MS)",
        "",
        "4️⃣ TOKEN STORAGE",
        "   Frontend stores JWT in localStorage (browser) + httpOnly cookie",
        "   Sent in Authorization header: 'Bearer <token>'",
        "",
        "5️⃣ REFRESH TOKEN",
        "   When expired, use refresh endpoint (POST /api/auth/refresh)",
        "   Get new token without re-login"
    ])
    
    # ============ SLIDE 7: Role-Based Access Control ============
    create_content_slide("Role-Based Access Control (RBAC)", [
        "🔑 5 Core Roles with Different Permissions:",
        "",
        "ADMIN - Full system access",
        "  ✓ Manage users, assign roles, view audit logs, system config",
        "",
        "AGENT - Customer & policy management",
        "  ✓ Create policies, assist customers, list all policies",
        "",
        "CLAIMS_OFFICER - Claims processing",
        "  ✓ Review claims queue, make settlement decisions, update status",
        "",
        "CUSTOMER - Self-service",
        "  ✓ View own policies, submit claims, pay premiums, track claims",
        "",
        "Authorization enforced at:",
        "  • API Gateway level (Spring Security)",
        "  • Service layer (permission checks)",
        "  • Database level (row-level security if needed)"
    ])
    
    # ============ SLIDE 8: API Endpoints Overview ============
    create_content_slide("RESTful API Endpoints", [
        "Authentication: POST /api/auth/login, POST /api/auth/register",
        "",
        "Products: GET/POST/PUT/DELETE /api/products (Admin only for mutations)",
        "",
        "Policies:",
        "  • GET /api/policies/my (own policies)",
        "  • POST /api/policies (purchase)",
        "  • GET /api/policies/:id/renewal-quote, POST /api/policies/:id/renew",
        "  • POST /api/policies/:id/cancellation-request (Admin approval)",
        "",
        "Claims:",
        "  • GET /api/claims/my, GET /api/claims/queue (Officer view)",
        "  • POST /api/claims (file), PATCH /api/claims/:id/status",
        "  • PUT /api/claims/:id/decision (Officer decision)",
        "",
        "Payments: GET /api/payments/history, POST /api/payments",
        "",
        "Reports: /api/reports/customer/**, /api/reports/admin/**",
        "",
        "All endpoints documented in Swagger: http://localhost:8080/swagger-ui.html"
    ])
    
    # ============ SLIDE 9: Technology Stack Detail ============
    create_content_slide("Complete Technology Stack", [
        "Frontend (UI Repository):",
        "  • Angular 22 (framework), TypeScript (language), SCSS (styling)",
        "  • RxJS (reactive programming), Zone.js (change detection)",
        "  • @angular/forms, @angular/router, @angular/http",
        "",
        "Backend (Backend Repository):",
        "  • Java 17 (language), Spring Boot 3.2 (framework)",
        "  • Spring Security (auth/authz), Spring Data JPA (ORM)",
        "  • jjwt (JWT library), springdoc-openapi (Swagger)",
        "  • Hibernate (JPA provider), Flyway (migrations)",
        "",
        "Database:",
        "  • PostgreSQL (primary), H2 (testing)",
        "",
        "Infrastructure:",
        "  • AWS ECS Fargate (backend containers)",
        "  • AWS EC2 (frontend nginx)",
        "  • AWS RDS (managed PostgreSQL)",
        "  • AWS S3 (document storage, deployment artifacts)",
        "  • Terraform (IaC), GitHub Actions (CI/CD)"
    ])
    
    # ============ SLIDE 10: Security Features ============
    create_content_slide("Security Implementation", [
        "🔐 Authentication",
        "  • JWT with RS256 algorithm (asymmetric signing)",
        "  • Bcrypt password hashing (10+ rounds with salt)",
        "  • Account lockout after 5 failed attempts",
        "  • Session timeout on inactivity",
        "",
        "🔑 Authorization",
        "  • Spring Security @PreAuthorize annotations",
        "  • Role-based endpoint access control",
        "  • Permission-level granularity (policy:create, claim:approve, etc.)",
        "",
        "🛡️ Data Protection",
        "  • HTTPS/TLS 1.3 for all communications",
        "  • SQL injection prevention (parameterized queries)",
        "  • XSS protection (input sanitization)",
        "  • CSRF tokens on state-changing operations",
        "",
        "📊 Compliance",
        "  • Audit logging of all user actions",
        "  • Data encryption at rest (AES-256)",
        "  • Read-only AUDITOR role for compliance"
    ])
    
    # ============ SLIDE 11: Deployment Architecture ============
    create_content_slide("AWS Deployment Architecture", [
        "Frontend (Angular):",
        "  • EC2 instance(s) running nginx",
        "  • Serves pre-built Angular app from S3 bucket",
        "  • CloudFront CDN for caching",
        "",
        "Backend (Spring Boot):",
        "  • ECS Fargate (container orchestration)",
        "  • Auto-scaling based on CPU/memory metrics",
        "  • Application Load Balancer (ALB) for traffic distribution",
        "  • CloudWatch logs for monitoring",
        "",
        "Database:",
        "  • RDS PostgreSQL (managed service)",
        "  • Multi-AZ deployment for high availability",
        "  • Automated backups (35-day retention)",
        "",
        "Storage:",
        "  • S3 bucket for policy/claim documents (encrypted, versioned)",
        "  • S3 bucket for Angular build artifacts",
        "",
        "Networking:",
        "  • VPC with public/private/database subnets",
        "  • Security groups with least-privilege rules",
        "  • NAT gateway for private subnet internet access"
    ])
    
    # ============ SLIDE 12: CI/CD Pipeline ============
    create_content_slide("CI/CD Pipeline - GitHub Actions", [
        "Frontend Pipeline (.github/workflows/deploy-ui.yml):",
        "  1. Trigger on push to main branch",
        "  2. Install dependencies (npm ci --legacy-peer-deps)",
        "  3. Run tests (npm test)",
        "  4. Build production bundle (npm run build)",
        "  5. Deploy to S3 (dist/insurance-portal/browser)",
        "  6. EC2 instances auto-sync from S3 every 5 minutes",
        "",
        "Backend Pipeline (.github/workflows/deploy-backend.yml):",
        "  1. Trigger on push to main branch",
        "  2. Build Maven project (mvn clean verify)",
        "  3. Run unit/integration tests (H2 database)",
        "  4. Build Docker image",
        "  5. Push to AWS ECR (Elastic Container Registry)",
        "  6. Update ECS task definition",
        "  7. Deploy to ECS Fargate (zero-downtime rolling deployment)",
        "",
        "Terraform Infrastructure:",
        "  • Store state in S3 with DynamoDB locking",
        "  • Separate state keys for dev/prod/shared environments"
    ])
    
    # ============ SLIDE 13: Feature Walkthrough ============
    create_content_slide("Key Features & Workflows", [
        "🛡️ Policy Management",
        "  • Browse products → Purchase policy → Manage coverage",
        "  • Renewal quotes → Renew policies → Cancel (with approval)",
        "",
        "📋 Claims Processing",
        "  • Submit claim with details → Upload documents",
        "  • Officer reviews → Approve/Reject → Settlement → Receipt",
        "",
        "💳 Premium Payments",
        "  • View payment history → Make payments",
        "  • Automatic invoice/receipt generation",
        "",
        "📊 Analytics & Reports",
        "  • Customer: policy summary, claims status, payment history",
        "  • Admin: top customers by premium, claims ratio, product performance",
        "  • Uses SQL views and window functions for complex aggregations",
        "",
        "👥 User Management",
        "  • Admin: create users, assign roles, activate/suspend accounts",
        "  • Role-specific dashboards and permissions"
    ])
    
    # ============ SLIDE 14: Testing Strategy ============
    create_content_slide("Testing & Quality Assurance", [
        "Frontend Testing (Angular/Vitest):",
        "  • Unit tests for auth guards, role guard, AuthService",
        "  • HTTP interceptor tests (JWT attachment, error handling)",
        "  • Login component tests",
        "  • Run: npm test",
        "",
        "Backend Testing (JUnit 5/Spring Boot Test):",
        "  • Unit tests for service layer business logic",
        "  • Integration tests against H2 in-memory database",
        "  • Repository tests for query correctness",
        "  • Controller tests for endpoint behavior",
        "  • Run: mvn clean verify",
        "",
        "API Documentation:",
        "  • Swagger UI automatically generated from Spring annotations",
        "  • Interactive endpoint testing in browser",
        "  • OpenAPI JSON schema export",
        "",
        "Load Testing:",
        "  • ECS Fargate auto-scaling based on CloudWatch metrics",
        "  • Database connection pooling for optimal performance"
    ])
    
    # ============ SLIDE 15: Known Limitations & Future Enhancements ============
    create_content_slide("Known Limitations & Future Roadmap", [
        "Current Limitations:",
        "  ⚠️ Document handling is metadata-only (file names/sizes)",
        "  ⚠️ Payment gateway is mocked (no real payment processing)",
        "  ⚠️ Receipt generation is plain-text (placeholder for PDF)",
        "  ⚠️ No real-time notifications (placeholder for WebSocket)",
        "",
        "Future Enhancements:",
        "  ✅ Integration with real S3 object storage for documents",
        "  ✅ Payment gateway integration (Stripe/PayPal)",
        "  ✅ PDF receipt generation",
        "  ✅ WebSocket for real-time claim updates",
        "  ✅ Mobile app (React Native/Flutter)",
        "  ✅ Advanced analytics with machine learning",
        "  ✅ GraphQL API for optimized data fetching",
        "  ✅ Horizontal scaling with Kubernetes (EKS)"
    ])
    
    # ============ SLIDE 16: Running & Deploying ============
    create_content_slide("Running & Deploying the Application", [
        "Development Setup:",
        "  Frontend: npm install --legacy-peer-deps && npm start",
        "            Navigate to http://localhost:4200",
        "  Backend: mvn spring-boot:run",
        "           Accessible at http://localhost:8080",
        "  Database: PostgreSQL running on localhost:5432",
        "",
        "Default Test Credentials (from seed data):",
        "  • admin / Password123! (ADMIN role)",
        "  • agent1 / Password123! (AGENT role)",
        "  • claims1 / Password123! (CLAIMS_OFFICER role)",
        "  • customer1 / Password123! (CUSTOMER role)",
        "",
        "Production Deployment:",
        "  1. Apply Terraform: terraform apply -var-file=environments/prod.tfvars",
        "  2. Configure environment variables (DB_PASSWORD, JWT_SECRET, etc.)",
        "  3. Deploy frontend: push to main → GitHub Actions builds and deploys to S3",
        "  4. Deploy backend: push to main → GitHub Actions builds Docker image, pushes to ECR, deploys to ECS",
        "",
        "Monitoring:",
        "  • CloudWatch logs, metrics, and alarms",
        "  • Backend health check: http://<alb-dns>/actuator/health"
    ])
    
    return prs

if __name__ == "__main__":
    prs = create_comprehensive_presentation()
    output_file = "Insurance_Portal_Complete_Presentation.pptx"
    prs.save(output_file)
    print(f"✅ Comprehensive presentation created: {output_file}")
    print(f"📊 16 slides covering full architecture, implementation, and deployment")
