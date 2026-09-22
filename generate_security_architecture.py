#!/usr/bin/env python3
"""
Insurance Portal Application - Detailed Security & Architecture Presentation
Adds detailed slides on Roles, Authentication, Authorization, and Architecture Diagrams
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_detailed_presentation():
    # Create presentation
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    # Color scheme
    PRIMARY_COLOR = RGBColor(0, 102, 204)
    SECONDARY_COLOR = RGBColor(51, 51, 51)
    ACCENT_COLOR = RGBColor(255, 102, 0)
    SUCCESS_COLOR = RGBColor(46, 184, 92)
    WARNING_COLOR = RGBColor(240, 173, 78)
    DANGER_COLOR = RGBColor(217, 83, 79)
    WHITE = RGBColor(255, 255, 255)
    DARK_GRAY = RGBColor(51, 51, 51)
    LIGHT_GRAY = RGBColor(240, 240, 240)
    
    def add_title_slide(prs, title, subtitle):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = PRIMARY_COLOR
        
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(54)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER
        
        subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(2))
        tf = subtitle_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = subtitle
        p.font.size = Pt(24)
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER
        
        return slide
    
    def add_content_slide(prs, title, content_items, bg_color=WHITE):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = bg_color
        
        title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
        title_shape.fill.solid()
        title_shape.fill.fore_color.rgb = PRIMARY_COLOR
        title_shape.line.color.rgb = PRIMARY_COLOR
        tf = title_shape.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(40)
        p.font.bold = True
        p.font.color.rgb = WHITE
        
        content_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.1), Inches(8.6), Inches(6))
        tf = content_box.text_frame
        tf.word_wrap = True
        
        for i, item in enumerate(content_items):
            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = item
            p.font.size = Pt(16)
            p.font.color.rgb = DARK_GRAY
            p.space_before = Pt(6)
            p.space_after = Pt(6)
        
        return slide
    
    # ========== SLIDE 1: Title Slide - Security & Architecture ==========
    add_title_slide(prs, "Security & Architecture Deep Dive", 
                   "Roles, Authentication, Authorization & System Architecture")
    
    # ========== SLIDE 2: Security Overview ==========
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY_COLOR
    title_shape.line.color.rgb = PRIMARY_COLOR
    tf = title_shape.text_frame
    p = tf.paragraphs[0]
    p.text = "Security Architecture Overview"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    content = [
        "🔐 Authentication - Verify user identity (WHO you are)",
        "   JWT tokens, OAuth 2.0, Session management",
        "",
        "🔑 Authorization - Control what users can do (WHAT you can access)",
        "   Role-Based Access Control (RBAC), Permission management",
        "",
        "🛡️ Encryption - Protect data in transit and at rest",
        "   SSL/TLS, AES-256 encryption, Secure key management",
        "",
        "📊 Audit Logging - Track user actions for compliance",
        "   Complete activity history, Compliance reporting"
    ]
    
    content_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.1), Inches(8.6), Inches(6))
    tf = content_box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(content):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(16)
        p.font.color.rgb = DARK_GRAY
        p.space_before = Pt(4)
        p.space_after = Pt(4)
    
    # ========== SLIDE 3: Roles & User Types ==========
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY_COLOR
    title_shape.line.color.rgb = PRIMARY_COLOR
    tf = title_shape.text_frame
    p = tf.paragraphs[0]
    p.text = "User Roles & Permissions"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    content = [
        "1️⃣ ADMIN - System administrator",
        "   • Full system access • User management • Configuration • Audit logs",
        "",
        "2️⃣ MANAGER - Department manager",
        "   • Team management • Policy approval • Report generation • Team data access",
        "",
        "3️⃣ AGENT - Insurance agent/representative",
        "   • Create policies • Process claims • Customer management • Own policy/claim data",
        "",
        "4️⃣ CUSTOMER - End customer/policyholder",
        "   • View own policies • Submit claims • Payment management • Own data only",
        "",
        "5️⃣ AUDITOR - Compliance & audit officer",
        "   • Read-only access • Audit logs • Compliance reports • No modifications"
    ]
    
    content_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.1), Inches(8.6), Inches(6))
    tf = content_box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(content):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(14)
        p.font.color.rgb = DARK_GRAY
        p.space_before = Pt(3)
        p.space_after = Pt(3)
    
    # ========== SLIDE 4: Authentication Flow ==========
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY_COLOR
    title_shape.line.color.rgb = PRIMARY_COLOR
    tf = title_shape.text_frame
    p = tf.paragraphs[0]
    p.text = "Authentication Flow (JWT-Based)"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Add visual representation
    flow_items = [
        "STEP 1: User Login",
        "   • User enters credentials (username/password)",
        "   • Credentials sent via HTTPS to backend",
        "",
        "STEP 2: Credential Verification",
        "   • Backend validates credentials against database",
        "   • Password verified using bcrypt hashing",
        "   • MFA/2FA validation (if enabled)",
        "",
        "STEP 3: JWT Token Generation",
        "   • Backend generates JWT token with payload:",
        "     - User ID, Username, Role, Permissions, Expiry (15-60 min)",
        "   • Token signed with private key (RS256 algorithm)",
        "",
        "STEP 4: Token Storage & Usage",
        "   • Client stores token in secure storage (localStorage/sessionStorage)",
        "   • Token sent in Authorization header for subsequent requests",
        "   • Backend validates token signature on each request",
        "",
        "STEP 5: Token Refresh",
        "   • Expired token triggers refresh token flow",
        "   • New JWT token issued without re-login"
    ]
    
    content_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.1), Inches(8.6), Inches(6))
    tf = content_box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(flow_items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_GRAY
        p.space_before = Pt(2)
        p.space_after = Pt(2)
    
    # ========== SLIDE 5: Authorization & RBAC ==========
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY_COLOR
    title_shape.line.color.rgb = PRIMARY_COLOR
    tf = title_shape.text_frame
    p = tf.paragraphs[0]
    p.text = "Authorization & RBAC Implementation"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    rbac_content = [
        "Role-Based Access Control (RBAC):",
        "",
        "Database Structure:",
        "  • Users Table - Stores user information",
        "  • Roles Table - Defines available roles (ADMIN, MANAGER, etc.)",
        "  • Permissions Table - Defines granular permissions",
        "  • User_Roles Junction - Maps users to roles",
        "  • Role_Permissions Junction - Maps roles to permissions",
        "",
        "Authorization Process:",
        "  1. Extract JWT token from request header",
        "  2. Decode token to get user ID and role",
        "  3. Fetch user permissions from database cache",
        "  4. Compare requested resource/action against permissions",
        "  5. Grant access if permission exists, deny otherwise",
        "",
        "Permission Examples:",
        "  • policy:create, policy:read, policy:update, policy:delete",
        "  • claim:submit, claim:approve, claim:reject",
        "  • user:manage, report:generate, audit:view"
    ]
    
    content_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.1), Inches(8.6), Inches(6))
    tf = content_box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(rbac_content):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_GRAY
        p.space_before = Pt(2)
        p.space_after = Pt(2)
    
    # ========== SLIDE 6: System Architecture Diagram (Text-Based) ==========
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY_COLOR
    title_shape.line.color.rgb = PRIMARY_COLOR
    tf = title_shape.text_frame
    p = tf.paragraphs[0]
    p.text = "High-Level System Architecture"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    arch_text = """
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                             │
├─────────────────────────────────────────────────────────────────┤
│  Web Browser (React TypeScript)  │  Mobile App  │  API Clients  │
└────────────────────┬──────────────────────────────┬─────────────┘
                     │ HTTPS/TLS                    │
     ┌───────────────▼────────────────────────────▼─────────────┐
     │              API GATEWAY / LOAD BALANCER                 │
     │  • Route requests to microservices                       │
     │  • Handle SSL/TLS termination                            │
     │  • Basic authentication                                  │
     └───────────────┬────────────────────────────┬─────────────┘
                     │                            │
     ┌───────────────▼─────┐      ┌────────────────▼─────────┐
     │  AUTH SERVICE       │      │  POLICY SERVICE          │
     ├─────────────────────┤      ├──────────────────────────┤
     │ • JWT generation    │      │ • Policy CRUD operations │
     │ • Token validation  │      │ • Policy search/filter   │
     │ • User management   │      │ • Premium calculation    │
     │ • RBAC checks       │      │ • Policy state machine   │
     └────────┬────────────┘      └────────┬──────────────────┘
              │                            │
     ┌────────▼─────────────────────────────▼──────────────┐
     │           SHARED DATABASE LAYER                     │
     ├───────────────────────────────────────────────────┤
     │  PostgreSQL / MySQL                               │
     │  • Users & Roles  • Policies  • Claims           │
     │  • Audit Logs     • Transactions                 │
     └───────────────────────────────────────────────────┘
"""
    
    arch_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(5.8))
    tf = arch_box.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.text = arch_text
    p.font.name = 'Courier New'
    p.font.size = Pt(9)
    p.font.color.rgb = DARK_GRAY
    
    # ========== SLIDE 7: Microservices Architecture ==========
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY_COLOR
    title_shape.line.color.rgb = PRIMARY_COLOR
    tf = title_shape.text_frame
    p = tf.paragraphs[0]
    p.text = "Microservices Architecture"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    micro_content = [
        "Core Microservices:",
        "",
        "1. Authentication Service (Port 8001)",
        "   • User login/logout • Token generation • Token refresh • MFA handling",
        "",
        "2. Policy Service (Port 8002)",
        "   • Policy creation/update/deletion • Premium calculation • Policy search",
        "",
        "3. Claims Service (Port 8003)",
        "   • Claim submission • Claim processing • Claim settlement • Claim history",
        "",
        "4. Customer Service (Port 8004)",
        "   • Customer profiles • Contact information • KYC data • Customer preferences",
        "",
        "5. Payment Service (Port 8005)",
        "   • Payment processing • Invoice generation • Payment tracking • Refunds",
        "",
        "6. Notification Service (Port 8006)",
        "   • Email notifications • SMS alerts • Push notifications • Audit logs"
    ]
    
    content_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.1), Inches(8.6), Inches(6))
    tf = content_box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(micro_content):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_GRAY
        p.space_before = Pt(2)
        p.space_after = Pt(2)
    
    # ========== SLIDE 8: Frontend Architecture ==========
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY_COLOR
    title_shape.line.color.rgb = PRIMARY_COLOR
    tf = title_shape.text_frame
    p = tf.paragraphs[0]
    p.text = "Frontend Architecture (React + TypeScript)"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    frontend_text = """
┌──────────────────────────────────────────────────┐
│         REACT APPLICATION STRUCTURE              │
├──────────────────────────────────────────────────┤
│                                                  │
│  ┌─────────────────────────────────────┐        │
│  │     Login & Authentication Layer    │        │
│  │  • Credential validation            │        │
│  │  • JWT token storage                │        │
│  │  • Protected routes                 │        │
│  └─────────────┬───────────────────────┘        │
│                │                                │
│  ┌─────────────▼───────────────────────┐        │
│  │     State Management (Redux/Context)│        │
│  │  • User state (role, permissions)   │        │
│  │  • Application state                │        │
│  │  • API response caching             │        │
│  └─────────────┬─��─────────────────────┘        │
│                │                                │
│  ┌─────────────▼───────────────────────┐        │
│  │     API Client Layer (Axios)        │        │
│  │  • Intercepts requests              │        │
│  │  • Adds JWT to headers              │        │
│  │  • Handles token refresh            │        │
│  │  • Error handling                   │        │
│  └─────────────┬───────────────────────┘        │
│                │                                │
│  ┌─────────────▼───────────────────────┐        │
│  │     Component Layer                 │        │
│  │  • Dashboard   • Policy Management  │        │
│  │  • Claims      • User Profile       │        │
│  │  • Payments    • Admin Panel        │        │
│  │  • Reports     • Settings           │        │
│  └────────────────────────────────────���┘        │
│                                                  │
└──────────────────────────────────────────────────┘
"""
    
    frontend_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.1), Inches(8.6), Inches(6))
    tf = frontend_box.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.text = frontend_text
    p.font.name = 'Courier New'
    p.font.size = Pt(10)
    p.font.color.rgb = DARK_GRAY
    
    # ========== SLIDE 9: Data Flow & Security ==========
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY_COLOR
    title_shape.line.color.rgb = PRIMARY_COLOR
    tf = title_shape.text_frame
    p = tf.paragraphs[0]
    p.text = "Data Flow & Security Measures"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    dataflow_content = [
        "Typical API Request Flow:",
        "",
        "1. Client Request",
        "   • HTTPS encrypted channel (TLS 1.3)",
        "   • JWT token in Authorization header: 'Bearer <token>'",
        "   • Request body contains data payload",
        "",
        "2. API Gateway",
        "   • Rate limiting (prevent DDoS)",
        "   • Basic validation (format, size)",
        "   • CORS policy enforcement",
        "",
        "3. Authentication Middleware",
        "   • Extract and validate JWT token",
        "   • Verify signature using public key",
        "   • Check token expiration",
        "",
        "4. Authorization Middleware",
        "   • Extract user role from token",
        "   • Check user permissions for endpoint",
        "   • Validate resource ownership (if applicable)",
        "",
        "5. Business Logic",
        "   • Execute service logic",
        "   • Database queries with parameterized statements (prevent SQL injection)",
        "",
        "6. Response",
        "   • Serialize data to JSON",
        "   • Add security headers (X-Content-Type-Options, etc.)",
        "   • HTTPS encryption for response transmission"
    ]
    
    content_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.1), Inches(8.6), Inches(6))
    tf = content_box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(dataflow_content):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_GRAY
        p.space_before = Pt(2)
        p.space_after = Pt(2)
    
    # ========== SLIDE 10: Database Schema Overview ==========
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    title_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY_COLOR
    title_shape.line.color.rgb = PRIMARY_COLOR
    tf = title_shape.text_frame
    p = tf.paragraphs[0]
    p.text = "Database Schema Overview"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    db_text = """
USERS TABLE
├─ user_id (PK)
├─ username (UNIQUE)
├─ email (UNIQUE, ENCRYPTED)
├─ password_hash (bcrypt)
├─ created_at
└─ updated_at

ROLES TABLE
├─ role_id (PK)
├─ role_name (ADMIN, MANAGER, AGENT, CUSTOMER, AUDITOR)
├─ description
└─ created_at

USER_ROLES TABLE (Many-to-Many)
├─ user_id (FK)
├─ role_id (FK)
└─ assigned_at

PERMISSIONS TABLE
├─ permission_id (PK)
├─ permission_name (policy:create, claim:approve, etc.)
├─ resource_type
└─ action

ROLE_PERMISSIONS TABLE (Many-to-Many)
├─ role_id (FK)
├─ permission_id (FK)
└─ assigned_at

AUDIT_LOGS TABLE
├─ log_id (PK)
├─ user_id (FK)
├─ action_type (CREATE, UPDATE, DELETE, VIEW)
├─ resource_type (POLICY, CLAIM, USER)
├─ resource_id
├─ timestamp
└─ ip_address
"""
    
    db_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.1), Inches(8.6), Inches(6))
    tf = db_box.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.text = db_text
    p.font.name = 'Courier New'
    p.font.size = Pt(10)
    p.font.color.rgb = DARK_GRAY
    
    # ========== SLIDE 11: Security Best Practices ==========
    add_content_slide(prs, "Security Best Practices", [
        "✓ Password Security",
        "  • Minimum 12 characters with complexity requirements",
        "  • Hashed using bcrypt with salt (10+ rounds)",
        "  • Password reset via secure token email",
        "",
        "✓ Token Management",
        "  • Short-lived access tokens (15-60 minutes)",
        "  • Refresh tokens stored securely (httpOnly cookie)",
        "  • Token revocation on logout",
        "",
        "✓ Data Encryption",
        "  • All data encrypted in transit (TLS 1.3)",
        "  • Sensitive data encrypted at rest (AES-256)",
        "  • Secure key management with HSM/KMS",
        "",
        "✓ API Security",
        "  • Rate limiting to prevent brute force",
        "  • Input validation & sanitization (prevent injection attacks)",
        "  • CORS policy enforcement",
        "  • Security headers (CSP, X-Frame-Options, etc.)"
    ])
    
    # ========== SLIDE 12: Deployment Security ==========
    add_content_slide(prs, "Deployment Security", [
        "🐳 Container Security",
        "  • Minimal base images (Alpine Linux)",
        "  • No hardcoded credentials (use environment variables)",
        "  • Image scanning for vulnerabilities",
        "  • Registry access control",
        "",
        "☁️ Infrastructure Security",
        "  • VPC/Private network isolation",
        "  • Security groups with minimal required ports",
        "  • SSL certificates for all endpoints",
        "  • DDoS protection (AWS Shield, CloudFlare)",
        "",
        "📊 Monitoring & Logging",
        "  • Centralized logging (ELK Stack)",
        "  • Real-time security alerts",
        "  • Failed login attempt tracking",
        "  • Anomaly detection",
        "",
        "🔄 CI/CD Security",
        "  • Automated security scanning",
        "  • Dependency vulnerability checks",
        "  • Code review requirements",
        "  • Secrets management (HashiCorp Vault)"
    ])
    
    return prs

if __name__ == "__main__":
    prs = create_detailed_presentation()
    output_file = "Insurance_Portal_Security_Architecture.pptx"
    prs.save(output_file)
    print(f"✅ Security & Architecture presentation created successfully!")
    print(f"📁 File: {output_file}")
    print(f"📊 Slides: 12 comprehensive slides on Security & Architecture")
    print(f"✨ Includes: Roles, Authentication, Authorization, Architecture Diagrams")
