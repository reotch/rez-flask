from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    """Homepage for User/job seeker"""
    user = {"username": "richard"}
    summary = {
        "description": "Motivated full-stack developer, experienced digital content creator, and proven collaborator with team management and software development experience. I can coordinate and communicate with technical and non-technical people at all levels, from Customer Service to C-Suite. I have experience working with organizations of various sizes, from being the third person at a start-up to mid-size global companies. I have worked in many locations throughout the world for varied clientele."
    }
    # TODO: create variable and dictionary for contact info
    contact = {
        "phone": "+1-847-868-2028",
        "email": "richard@sandrok.com",
        "skype": "richard.sandrok",
        "signal": "+1-773-430-0306",
    }
    return render_template(
        "index.html",
        title="Richard Sandrok—Software Developer",
        user=user,
        summary=summary,
        contact=contact
    )


@app.route("/experience")
def experience():
    """Route for User/job seeker experience, stored in dict()"""
    positions = [
        {
            "title": "software developer",
            "organization": "coding temple",
            "dates": "2019 – present",
            "description": "Part of team involved in developing, designing and testing interactive and responsive websites for clients using the front-end and back-end applications.",
            "bullets": [
                "Developed new feature requests, fixed bugs, performed trouble shooting and problem solving",
                "Utilized CSS to make the application responsive Designed and developed the UI of the website using HTML, AJAX, CSS and JavaScript",
                "Designed Wireframes for all the pages in e-commence applications, and used HTML and CSS to create the content and design of websites",
                "Worked in SQL database on simple queries and writing Stored Procedures for normalization and re-normalization",
                "Analyzing data using NumPy and Pandas",
                "Teaching assistant and tutor for eight students for Python/Flask and CSS3",
            ],
        },
        {
            "title": "owner & president",
            "organization": "unlimited reotch, inc.",
            "dates": "2016 – present",
            "description": "",
            "bullets": [
                "Digital content producer for B2B clients and various Unlimited Reotch productions",
                "Design of company WordPress site and administration of business-related email & IT resources ",
                "Digital content producer for B2B clients and various Unlimited Reotch productions",
                "Developed, recorded, produced, edited, and published podcasts (e.g., Dork Therapy)",
                "Independent sales representative for Sensaphonics in-ear monitors and hearing conservation technologies",
            ],
        },
        {
            "title": "production manager & business development contractor",
            "organization": "sonata learning",
            "dates": "2016 – 2017",
            "description": "",
            "bullets": [
                "Shot and edited videos for Shirley Ryan AbilityLab, Aurora Doors, and World Bank e-learning initiatives",
                "Developed SCORM-compliant e-learning module content for 10 clients",
                "Wrote and edited proposals for 8 RFPs including 2 winners and a 3rd as the alternate finalist",
                "Managed IT resources for temporary and full-time staff",
                "QA testing for 5 content clients and two software projects",
                "Sourced, auditioned, and managed outside voice-over talent",
            ],
        },
        {
            "title": "technical editor & online training contractor",
            "organization": "kaufman hall",
            "dates": "2014 – 2016",
            "description": "",
            "bullets": [
                "Advised and shot 5 “talking heads” videos for a new initiative of an SVP of Marketing",
                "Produced livestreamed presentations for 2 years for the company’s marquee event, Healthcare Leadership Conference",
                "Edited and wrote single-source and multi-source technical documentation for 10 software products",
                "Managed online educational training via third-party resources (Adobe Connect, GoToTraining) and hosted over 35 online training sessions in a year",
                "Trained over 20 consultants in best practices for online training presentations",
            ],
        },
        {
            "title": "artist relations",
            "organization": "shure, inc.",
            "dates": "2002 – 2013",
            "description": "",
            "bullets": [
                "Conducted and/or filmed over 33 interviews and special interest videos for social media and internal use",
                "Produced annual artist promotion reel (50-60 minutes) highlighting the artist roster to trade show attendees",
                "Managed budget and sales for 50-60 artist endorsers",
                "Published author in 10 Shure magazines",
                "Talent buyer for trade show (NAMM) events, finding and negotiating with talent and/or co-sponsors for dealer parties for 500-3000 attendees",
                "On-site support for live and televised events – Grammys, Latin Grammys, SXSW, Lollapalooza, Austin City Limits, Shure’s Give It Voice competition",
            ],
        },
        {
            "title": "venue security manager",
            "organization": "victoria operating company, LLC",
            "dates": "1998 – 2008",
            "description": "",
            "bullets": [
                "Managed 10-18 direct reports",
                "Progressed to manager position after starting as stagehand",
            ],
        },
    ]

    return render_template(
        "experience.html", title="Richard Sandrok—Work Experience", positions=positions
    )


@app.route("/summary")
def summary():
            
    # summary moved to /index for "summary and contact"
    summary = {
        "description": "Motivated full-stack developer, experienced digital content creator, and proven collaborator with team management and software development experience. I can coordinate and communicate with technical and non-technical people at all levels, from Customer Service to C-Suite. I have experience working with organizations of various sizes, from being the third person at a start-up to mid-size global companies. I have worked in many locations throughout the world for varied clientele."
    }
    skills = {
        "languages": ["Python", "JavaScript", "HTML5", "XML", "CSS3"],
        "tech": [
            "RestAPI",
            "Web Form APIs",
            "Angular",
            "Flask",
            "Bootstrap UI",
            "NumPy",
            "Pandas",
            "jQuery",
        ],
        "dbs": ["SQL", "MySQL", "PostgreSQL", "SQLite", "AWS RDS"],
        "tools": [
            "Git",
            "Object-Oriented Programming",
            "Anaconda",
            "Jupyter Notebook",
            "Data Model",
            "SQL Server Management Studios",
            "Google Developer Tools",
            "Agile Development",
            "JSON",
            "Tableau",
            "Microsoft Office (Word, Excel and PowerPoint)",
            "WordPress",
            "Adobe Suite (Photoshop, Lightroom, Premiere)",
            "SharePoint",
            "Camtasia",
            "Reaper",
            "Audacity",
            "DaVinci Resolve",
            "SAP",
            "YouTube",
            "Vimeo",
            "Libsyn",
        ],
        "source": ["GitHub", "Git", "Windows" "OS X", "Linux", "iOS", "Android"],
    }
    # NOTE: summary not used here; moved to /index route
    return render_template(
        "summary.html", title="Richard Sandrok—Summary", summary=summary, skills=skills
    )


@app.route("/projects")
def projects():
    projects = [
        {
            "name": "carzone",
            "description": "Full-stack web application for selecting vehicles and leaving ratings and reviews; as part of the back-end team I worked to create a web-based API for CRUD operation",
            "environment": "Python/Flask, Angular",
        },
        {
            "name": "sensaphonics",
            "description": "Full-stack project for ordering custom in-ear monitors for professional musicians",
            "environment": "Python/Flask, HTML5/CSS3, PostgreSQL",
        },
        {
            "name": "mountains, trees, chainsaws",
            "description": "A rock, paper, scissors of epic proportions",
            "environment": "HTML5, CSS3, JavaScript",
        },
        {
            "name": "weather app",
            "description": "A simple weather application with search functionality connected to Open Weather Map via REST API",
            "environment": "JavaScript, HTML5, Bootstrap 4",
        },
    ]

    return render_template(
        "projects.html", title="Richard Sandrok—Projects", projects=projects
    )


@app.route("/education")
def education():
    school = "elmhurst college"
    degree = "bachelor of science"
    major = "music business"

    return render_template(
        "education.html",
        title="Richard Sandrok—Education",
        school=school,
        degree=degree,
        major=major,
    )


@app.route("/interests")
def interests():
    interests = [
        {
            "type": "music & performance",
            "desc": "member of symphonic, concert, and rock/electronic bands; toured nationally, performed internationally",
        },
        {"type": "photography & videography", "desc": ""},
        {
            "type": "computers, science & technology",
            "desc": "restoring old, antiquated computers to working, functioning machines; building PCs; rooting mobile devices; hydroponic & aquaponic systems",
        },
        {
            "type": "conservation & ecology",
            "desc": "Shedd Aquarium volunteer since 2009; includes WordPress site development for educators",
        },
    ]

    return render_template(
        "interests.html",
        title="Richard Sandrok—Interests & Community",
        interests=interests,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for {form.username.data}, remember me={form.remember_me.data}"
        )
        return redirect("/index")
    return render_template("login.html", title="Sign In", form=form)
