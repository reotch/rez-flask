from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'richard'}
    return render_template('index.html', title="Richard Sandrok—Software Developer", user=user)

@app.route('/experience')
def experience():
    positions = [
        {
            'title' : 'software developer',
            'organization' : 'coding temple',
            'dates' : '2019 – present',
            'description' : 'Part of team involved in developing, designing and testing interactive and responsive websites for clients using the front-end and back-end applications.',
            'bullets' : [
                'Developed new feature requests, fixed bugs, performed trouble shooting and problem solving',
                'Utilized CSS to make the application responsive Designed and developed the UI of the website using HTML, AJAX, CSS and JavaScript',
                'Designed Wireframes for all the pages in e-commence applications, and used HTML and CSS to create the content and design of websites',
                'Worked in SQL database on simple queries and writing Stored Procedures for normalization and re-normalization',
                'Analyzing data using NumPy and Pandas',
                'Teaching assistant and tutor for eight students for Python/Flask and CSS3'
            ]
        },
        {
            'title' : 'owner & president',
            'organization' : 'unlimited reotch, inc.',
            'dates' : '2016 – present',
            'description' : '',
            'bullets' : [
                'Digital content producer for B2B clients and various Unlimited Reotch productions',
                'Design of company WordPress site and administration of business-related email & IT resources ',
                'Digital content producer for B2B clients and various Unlimited Reotch productions',
                'Developed, recorded, produced, edited, and published podcasts (e.g., Dork Therapy)',
                'Independent sales representative for Sensaphonics in-ear monitors and hearing conservation technologies'
            ]
        },
        {
            'title' : 'production manager & business development contractor',
            'organization' : 'sonata learning',
            'dates' : '2016 – 2017',
            'description' : '',
            'bullets' : [
                'Shot and edited videos for Shirley Ryan AbilityLab, Aurora Doors, and World Bank e-learning initiatives',
                'Developed SCORM-compliant e-learning module content for 10 clients',
                'Wrote and edited proposals for 8 RFPs including 2 winners and a 3rd as the alternate finalist',
                'Managed IT resources for temporary and full-time staff',
                'QA testing for 5 content clients and two software projects',
                'Sourced, auditioned, and managed outside voice-over talent'
            ]
        },
        {
            'title' : 'technical editor & online training contractor',
            'organization' : 'kaufman hall',
            'dates' : '2014 – 2016',
            'description' : '',
            'bullets' : [
                'Advised and shot 5 “talking heads” videos for a new initiative of an SVP of Marketing',
                'Produced livestreamed presentations for 2 years for the company’s marquee event, Healthcare Leadership Conference',
                'Edited and wrote single-source and multi-source technical documentation for 10 software products',
                'Managed online educational training via third-party resources (Adobe Connect, GoToTraining) and hosted over 35 online training sessions in a year',
                'Trained over 20 consultants in best practices for online training presentations'
            ]
        },
        {
            'title' : 'artist relations',
            'organization' : 'shure, inc.',
            'dates' : '2002 – 2013',
            'description' : '',
            'bullets' : [
                'Conducted and/or filmed over 33 interviews and special interest videos for social media and internal use',
                'Produced annual artist promotion reel (50-60 minutes) highlighting the artist roster to trade show attendees',
                'Managed budget and sales for 50-60 artist endorsers',
                'Published author in 10 Shure magazines',
                'Talent buyer for trade show (NAMM) events, finding and negotiating with talent and/or co-sponsors for dealer parties for 500-3000 attendees',
                'On-site support for live and televised events – Grammys, Latin Grammys, SXSW, Lollapalooza, Austin City Limits, Shure’s Give It Voice competition'
            ]
        },
        {
            'title' : 'venue security manager',
            'organization' : 'victoria operating company, LLC',
            'dates' : '1998 – 2008',
            'description' : '',
            'bullets' : [
                'Managed 10-18 direct reports',
                'Progressed to manager position after starting as stagehand'
            ]
        }

    ]

    return render_template('experience.html', title='Richard Sandrok—Work Experience', positions=positions)