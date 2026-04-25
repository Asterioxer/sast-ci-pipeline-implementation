from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import inch

def create_sast_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    
    styles = getSampleStyleSheet()
    story = []

    # Custom Styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        fontSize=24,
        spaceAfter=20,
        alignment=1, # Center
        textColor=colors.darkblue
    )
    
    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Heading1'],
        fontSize=16,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.darkblue,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Header2',
        parent=styles['Heading2'],
        fontSize=13,
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.black,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        leftIndent=20,
        bulletIndent=10,
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=9,
        leading=11,
        fontName='Courier',
        backColor=colors.whitesmoke,
        borderPadding=5,
        spaceBefore=5,
        spaceAfter=10,
        leftIndent=20,
        rightIndent=20
    )

    # --- Title Page ---
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("Infrastructure-Wide SAST Implementation and Standardization", title_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("<b>Submission Type:</b> Technical Research Report", body_style))
    story.append(Paragraph("<b>Subject:</b> Application Security & DevSecOps", body_style))
    story.append(Paragraph("<b>Submitted by:</b> Soham Mukherjee", body_style))
    story.append(PageBreak())

    # --- Section 1: Introduction ---
    story.append(Paragraph("1. Introduction to SAST", h1_style))
    story.append(Paragraph("Static Application Security Testing (SAST), often referred to as 'white-box testing,' is a methodology for analyzing source code to identify security vulnerabilities, coding errors, and non-compliance with standards without executing the program. Unlike dynamic testing, which interacts with a running application, SAST scans the codebase at rest (source code, bytecode, or binaries).", body_style))
    story.append(Paragraph("In modern software development, SAST acts as the first line of defense, enabling developers to identify critical flaws—such as SQL Injection, Cross-Site Scripting (XSS), and buffer overflows—before the code leaves the development environment.", body_style))

    # --- Section 2: Purpose and Use ---
    story.append(Paragraph("2. Purpose and Use of SAST", h1_style))
    story.append(Paragraph("Organizations implement SAST primarily to achieve a 'Shift-Left' security posture. By moving security testing earlier in the Software Development Life Cycle (SDLC), organizations derive several key benefits:", body_style))
    
    bullets = [
        "<b>Early Vulnerability Detection:</b> Fixing a bug during the coding phase is significantly cheaper and faster than fixing it in production.",
        "<b>Cost Reduction:</b> Reduces the technical debt associated with security patches and emergency hotfixes.",
        "<b>Secure Coding Culture:</b> Provides immediate feedback to developers, acting as an educational tool for secure coding practices.",
        "<b>Compliance Assurance:</b> Helps meet regulatory requirements (PCI-DSS, HIPAA, GDPR) by strictly enforcing security policies in code."
    ]
    for b in bullets:
        story.append(Paragraph(f"• {b}", bullet_style))

    # --- Section 3: Infrastructure-Wide vs Traditional ---
    story.append(Paragraph("3. Infrastructure-Wide SAST vs Traditional SAST", h1_style))
    story.append(Paragraph("Traditionally, SAST was implemented in silos—individual teams selected their own tools and ran scans ad-hoc. This leads to fragmented visibility and inconsistent security postures. Infrastructure-wide SAST, conversely, treats security scanning as a standardized, scalable service available to the entire organization.", body_style))
    
    # Comparison Table
    data = [
        ["Feature", "Traditional / Project-Level SAST", "Infrastructure-Wide SAST"],
        ["Governance", "Decentralized; team-specific rules", "Centralized; organization-wide policy"],
        ["Consistency", "Varies by project", "Uniform quality gates across all repos"],
        ["Scalability", "Manual setup per project", "Automated onboarding via templates/IaC"],
        ["Reporting", "Isolated reports", "Aggregated dashboards for CISO/AppSec"]
    ]
    t = Table(data, colWidths=[1.2*inch, 2.3*inch, 2.3*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('FONTSIZE', (0,0), (-1,-1), 9),
    ]))
    story.append(t)

    # --- Section 4: Domains ---
    story.append(Paragraph("4. Domains Where SAST is Used", h1_style))
    story.append(Paragraph("SAST is implementation-agnostic and is critical across various technology domains:", body_style))
    domains = [
        "<b>Web Applications:</b> Detecting injection flaws (OWASP Top 10) in Java, Python, .NET, etc.",
        "<b>Mobile Apps:</b> Identifying insecure data storage and permissions in iOS (Swift/Obj-C) and Android (Kotlin/Java) code.",
        "<b>Cloud-Native Systems:</b> Scanning Infrastructure as Code (Terraform, Kubernetes manifests) for misconfigurations.",
        "<b>Fintech:</b> Ensuring strict data handling logic to prevent financial fraud and leaks.",
        "<b>Healthcare:</b> Protecting PII/PHI by enforcing encryption standards in source code.",
        "<b>DevOps Pipelines:</b> Automated gating of builds based on security severity."
    ]
    for d in domains:
        story.append(Paragraph(f"• {d}", bullet_style))

    # --- Section 5: Tools ---
    story.append(Paragraph("5. SAST Tools Used in Industry", h1_style))
    story.append(Paragraph("The market includes both open-source and commercial enterprise tools:", body_style))
    tools = [
        "<b>SonarQube:</b> The industry standard for code quality and basic security. Excellent for measuring technical debt.",
        "<b>Checkmarx:</b> An enterprise-grade tool known for deep scanning capabilities and robust support for legacy languages.",
        "<b>Fortify (OpenText):</b> A veteran tool in the space, offering comprehensive coverage and deep integration with enterprise workflows.",
        "<b>Veracode:</b> A cloud-based platform offering binary static analysis (SAST) alongside other testing methods.",
        "<b>Snyk Code:</b> Developer-first tool focusing on speed and open-source library vulnerabilities (SCA) alongside SAST.",
        "<b>Semgrep:</b> A modern, fast, and customizable tool that treats code search like grep. Highly popular in DevSecOps.",
        "<b>CodeQL (GitHub):</b> Treats code as data, allowing security teams to write queries to find complex vulnerability patterns."
    ]
    for tool in tools:
        story.append(Paragraph(f"• {tool}", bullet_style))

    # --- Section 6: Internals ---
    story.append(Paragraph("6. How SAST Tools Work Internally", h1_style))
    story.append(Paragraph("SAST tools operate much like a compiler but focus on logic rather than execution. The process generally involves:", body_style))
    
    story.append(Paragraph("<b>1. Lexical Analysis & Parsing:</b>", h2_style))
    story.append(Paragraph("The tool reads the source code and converts it into an Abstract Syntax Tree (AST). This tree represents the syntactic structure of the code.", body_style))

    story.append(Paragraph("<b>2. Control Flow Analysis (CFA):</b>", h2_style))
    story.append(Paragraph("The tool builds a Control Flow Graph (CFG) to understand the order in which statements are executed, including loops, branches, and function calls.", body_style))

    story.append(Paragraph("<b>3. Data Flow & Taint Analysis:</b>", h2_style))
    story.append(Paragraph("This is the core of vulnerability detection. The tool tracks data from 'Sources' (user input) to 'Sinks' (sensitive functions like SQL execution). If data moves from a source to a sink without being 'sanitized' or validated, a vulnerability is flagged.", body_style))

    story.append(Paragraph("<b>4. Pattern Matching & Heuristics:</b>", h2_style))
    story.append(Paragraph("Simple scanners use regular expressions or structural pattern matching to find known bad practices (e.g., hardcoded passwords or usage of `strcpy` in C).", body_style))

    # --- Section 7: Commands ---
    story.append(Paragraph("7. Common Commands Used (Examples)", h1_style))
    
    story.append(Paragraph("<b>Semgrep (CLI):</b>", h2_style))
    story.append(Paragraph("Semgrep is known for its simplicity and speed in CI environments.", body_style))
    story.append(Paragraph("semgrep scan --config=auto", code_style))
    
    story.append(Paragraph("<b>SonarQube Scanner:</b>", h2_style))
    story.append(Paragraph("The standard CLI invocation for a generic project.", body_style))
    story.append(Paragraph("sonar-scanner \\\n  -Dsonar.projectKey=my_project_key \\\n  -Dsonar.sources=. \\\n  -Dsonar.host.url=http://localhost:9000 \\\n  -Dsonar.login=my_auth_token", code_style))

    # --- Section 8: CI/CD Integration ---
    story.append(Paragraph("8. CI/CD Integration", h1_style))
    story.append(Paragraph("In an infrastructure-wide implementation, SAST is integrated into CI/CD platforms (Jenkins, GitHub Actions, GitLab CI, Azure DevOps). The workflow typically follows these steps:", body_style))
    steps = [
        "<b>Trigger:</b> A developer pushes code or opens a Pull Request (PR).",
        "<b>Scan Execution:</b> The CI pipeline spins up a containerized SAST scanner.",
        "<b>Analysis:</b> The code is analyzed against the centralized quality profile.",
        "<b>Gate Check:</b> The pipeline checks the results against defined thresholds (e.g., 'Block build if > 0 Critical Vulnerabilities').",
        "<b>Feedback:</b> Results are posted back to the PR as comments, allowing the developer to fix issues immediately."
    ]
    for s in steps:
        story.append(Paragraph(f"• {s}", bullet_style))

    # --- Section 9: Standardization ---
    story.append(Paragraph("9. Standardization Components", h1_style))
    story.append(Paragraph("To ensure the system works at scale, the following components must be standardized:", body_style))
    standard_points = [
        "<b>Tool Standardization:</b> Mandating specific tools for specific languages (e.g., Checkmarx for Legacy .NET, Semgrep for modern Python/JS) to ensure consistent results.",
        "<b>Rule Consistency:</b> Using a 'Quality Profile' that is centrally managed. Individual teams should not be able to disable critical security rules without approval.",
        "<b>Severity Thresholds:</b> Defining clearly what constitutes a 'Critical', 'High', or 'Medium' issue across the organization to prevent alarm fatigue.",
        "<b>Ownership:</b> Every identified vulnerability must have an assigned owner (usually the developer who committed the code) and a Service Level Agreement (SLA) for remediation.",
        "<b>Centralized Reporting:</b> A single pane of glass (dashboard) where security leadership can view the risk posture of the entire infrastructure."
    ]
    for p in standard_points:
        story.append(Paragraph(f"• {p}", bullet_style))

    # --- Section 10: Challenges ---
    story.append(Paragraph("10. Challenges and Mitigation Strategies", h1_style))
    
    story.append(Paragraph("<b>False Positives:</b>", h2_style))
    story.append(Paragraph("<i>Challenge:</i> Tools flagging secure code as vulnerable, causing developer frustration.\n<i>Mitigation:</i> Regular rule tuning, using context-aware scanners, and allowing a 'mark as false positive' workflow with security review.", body_style))

    story.append(Paragraph("<b>Scan Performance:</b>", h2_style))
    story.append(Paragraph("<i>Challenge:</i> Scans taking too long, slowing down deployments.\n<i>Mitigation:</i> Implement incremental scanning (scanning only changed files) and set timeouts for PR checks.", body_style))

    story.append(Paragraph("<b>Developer Resistance:</b>", h2_style))
    story.append(Paragraph("<i>Challenge:</i> Developers viewing security as a blocker.\n<i>Mitigation:</i> Integrate deeply into the IDE so they see issues while typing, and focus on education over punishment.", body_style))

    # --- Section 11: Business Impact ---
    story.append(Paragraph("11. Business Impact", h1_style))
    story.append(Paragraph("Standardized SAST directly impacts the bottom line and risk profile:", body_style))
    impacts = [
        "<b>Reduced Breach Risk:</b> Significantly lowers the probability of exploitable vulnerabilities reaching production.",
        "<b>Operational Efficiency:</b> Automating security reviews frees up senior engineers from manual code review tasks.",
        "<b>Trust & Reputation:</b> Demonstrating robust security practices builds trust with clients and partners, which is a competitive advantage."
    ]
    for i in impacts:
        story.append(Paragraph(f"• {i}", bullet_style))

    # --- Section 12: Conclusion ---
    story.append(Paragraph("12. Conclusion", h1_style))
    story.append(Paragraph("Infrastructure-wide SAST implementation is not merely about installing a tool; it is about establishing a culture of security. By standardizing tools, rules, and workflows, organizations can achieve a scalable, consistent, and effective security posture. While challenges like false positives exist, a well-tuned and integrated SAST pipeline is the cornerstone of modern, secure software delivery.", body_style))

    # Build PDF
    doc.build(story)
    print(f"PDF generated: {filename}")

if __name__ == "__main__":
    create_sast_pdf("Infrastructure_Wide_SAST_Implementation.pdf")