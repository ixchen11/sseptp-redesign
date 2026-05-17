from pathlib import Path
from html import escape
import os
import json

ROOT = Path('/root/.openclaw/workspace/sseptp-redesign')

SITE = {
    'title': 'Sanskrithi School of Engineering',
    'email': 'info@sseptp.org',
    'enquiry_email': 'enquiry@sseptp.org',
    'hr_email': 'hr@sseptp.org',
    'phone': '+91 9100064545 / 74545',
    'address': 'Puttaparthi, Sri Sathya Sai District, AP - 515134',
    'domain': 'https://sseptp.org',
    'tagline': 'Autonomous engineering education with strong placements, quality systems, and global pathways',
    'logo': 'https://sseptp.org/assets/sse-logo-D5ZBduKC.svg',
}

NAV = [
    ('Home', '/index.html'),
    ('About', '/about/index.html'),
    ('Admissions', '/admissions/index.html'),
    ('Academics', '/academics/index.html'),
    ('Campus Life', '/campus/index.html'),
    ('Placements', '/placements/index.html'),
    ('Contact', '/contact.html'),
]

MEGA = {
    'About': [
        ('Overview', '/about/index.html', 'Institutional story and identity'),
        ('Vision & Mission', '/about/vision-mission.html', 'Purpose, values, and direction'),
        ('Leadership', '/about/leadership.html', 'Messages, roles, and guidance'),
        ('Quality & Recognition', '/about/quality.html', 'NAAC, IQAC, and governance'),
        ('Industry Interface', '/about/industry-interface.html', 'Academic relevance in practice'),
    ],
    'Admissions': [
        ('Overview', '/admissions/index.html', 'Your admissions starting point'),
        ('Admission Process', '/admissions/process.html', 'Step-by-step student journey'),
        ('Fees & Scholarships', '/admissions/fees.html', 'Financial clarity and support'),
        ('Enquiry', '/admissions/enquiry.html', 'Talk to admissions quickly'),
    ],
    'Academics': [
        ('Overview', '/academics/index.html', 'Academic pathways and depth'),
        ('Programs', '/academics/programs.html', 'Undergraduate and advanced routes'),
        ('Labs', '/academics/labs.html', 'Applied learning environments'),
        ('Sai Prudent Scholarship', '/academics/scholarships.html', 'Merit and need-based support'),
        ('RIT Pathway', '/academics/rit.html', 'Europe-facing differentiator'),
    ],
    'Campus Life': [
        ('Overview', '/campus/index.html', 'Student experience across campus'),
        ('Facilities', '/campus/facilities.html', 'Academic and support spaces'),
        ('Hostel Life', '/campus/hostel.html', 'Comfort, community, and security'),
        ('Health & Safety', '/campus/health-safety.html', 'Wellbeing and trust'),
        ('Sports', '/campus/sports.html', 'Energy, teamwork, and participation'),
    ],
    'Placements': [
        ('Overview', '/placements/index.html', 'Outcomes and readiness'),
        ('Success Stories', '/placements/success-stories.html', 'Student results and proof'),
        ('Placement Contact', '/placements/contact.html', 'Career cell and recruiter route'),
    ],
}

PAGES = {
    'index.html': {
        'section': 'Home',
        'title': 'Admissions Open 2026 | Autonomous Engineering Education',
        'description': 'Sanskrithi School of Engineering in Puttaparthi presents admissions, academics, placements, hostel life, RIT pathway, and institutional quality credentials in one clear experience.',
        'hero_kicker': 'Admissions Open 2026',
        'hero_title': 'Autonomous engineering education with visible outcomes, quality systems, and global exposure.',
        'hero_text': 'SSETP presents a strong institutional story through autonomous status, NAAC quality credentials, visible placement outcomes, campus life, and the RIT pathway in partnership with European mentors.',
        'hero_badges': ['Autonomous Institute', 'NAAC A Grade (3.17/4)', 'RIT Pathway', 'Placement-focused'],
        'hero_stats': [('1675', 'Total offers highlighted on the site'), ('150', 'Recruiting companies'), ('95%', 'Placement rate shown for 2024-25'), ('36 LPA', 'Highest package highlighted')],
        'highlights': [('Puttaparthi identity', 'The school is rooted in Sri Sathya Sai District and that context is presented clearly and prominently.'), ('Real differentiators', 'RIT, placements, hostel life, and quality credentials are presented as core reasons to explore further.'), ('Clear contact routes', 'Admissions, general enquiries, and placement contact paths are easy to find and use.')],
        'hero_image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg',
        'service_cards': [('Admissions & Enquiry', 'Admissions overview, process, fees, scholarship support, and direct enquiry routes in one guided flow.', '/admissions/index.html'), ('Academics & Global Pathways', 'Departments, laboratory infrastructure, curriculum governance, and the RIT program with RISE / INSO.', '/academics/index.html'), ('Placements & Campus Life', 'Placement evidence, recruiter trust, hostel life, facilities, and student experience built from the live SSETP content.', '/placements/index.html')],
        'news_items': [('Placements 2024-25', 'The live placement story is now easier to scan: total offers, recruiters, placement rate, and internship visibility.', '/placements/index.html', 'https://sseptp.org/assets/placement-D9x0hLK2.jpg'), ('RIT Program', 'SSE’s Europe-facing software-engineering pathway is treated as a real differentiator instead of a buried secondary page.', '/academics/rit.html', 'https://sseptp.org/assets/ritprogram-Bc3C0C6e.jpg')],
        'content': [
            {'type': 'feature_grid', 'kicker': 'Explore SSE', 'title': 'The key journeys now reflect the real structure of the institution.', 'text': 'Instead of abstract marketing buckets, the homepage routes visitors into the concrete topics already present on the existing website.', 'cards': [
                ('About SSE', 'Vision, mission, leadership, NAAC / IQAC context, recognition, and the industry advisory story.', '/about/index.html'),
                ('Admissions', 'Overview, admission process, fee clarity, Sai Prudent Scholarship, and enquiry options.', '/admissions/index.html'),
                ('Academics', 'Departments, curriculum process, laboratories, and the RIT pathway with European mentors.', '/academics/index.html'),
                ('Campus & Placements', 'Facilities, hostel life, recruiters, CDC team, and placement outcomes.', '/campus/index.html'),
            ]},
            {'type': 'metrics_band', 'items': [('24', 'structured information pages'), ('6', 'core academic departments surfaced'), ('1', 'clear admissions-first navigation'), ('3', 'direct contact routes: general, admissions, placements')]},
            {'type': 'split', 'kicker': 'Why this structure fits SSE', 'title': 'The content reflects the institution’s actual proof points.', 'text': 'SSETP already contains strong material across quality, academics, placements, and campus life. This structure helps students, parents, and recruiters reach the right trust signals faster.', 'bullets': ['NAAC, IQAC, affiliation, and autonomous positioning are easier to verify', 'Placement statistics and recruiter proof sit closer to the top-level journey', 'RIT and international academic differentiation are more visible', 'Contact routes use the real SSETP office, admissions, and HR mailboxes']},
            {'type': 'quote_panel', 'kicker': 'Positioning', 'title': 'SSE does not need invented positioning — it already has one.', 'text': 'Autonomous status, quality systems, placement visibility, hostel life, department depth, and the RIT program are enough to tell a stronger story when the architecture is disciplined.'},
        ],
    },
    'about/index.html': {
        'section': 'About',
        'title': 'About the School',
        'description': 'Learn about Sanskrithi School of Engineering in Puttaparthi: its mission, heritage, leadership, recognition, and industry-facing academic direction.',
        'hero_kicker': 'About SSE',
        'hero_title': 'An engineering institution shaped by place, purpose, and quality systems.',
        'hero_text': 'SSE is located in Puttaparthi in Sri Sathya Sai District and presents itself as a premier autonomous engineering institution with a visible NAAC quality story, leadership voice, and industry-linked academic intent.',
        'hero_stats': [('Puttaparthi', 'Institutional home and identity'), ('A Grade', 'NAAC accreditation highlighted by the institution'), ('3.17/4', 'NAAC score referenced on the current site'), ('5', 'core About journeys brought into one structure')],
        'hero_image': 'https://sseptp.org/assets/girlsnearsteps-DxC0q7RC.jpg',
        'content': [
            {'type': 'spotlight', 'kicker': 'Institutional profile', 'title': 'A stronger institutional picture should emerge within a few seconds.', 'text': 'The About section should immediately connect SSETP’s place, leadership tone, quality credentials, and academic seriousness instead of treating them as isolated pages.', 'image': 'https://sseptp.org/assets/principal-Cgd9y_bj.jpg', 'image_alt': 'SSETP leadership and academic identity', 'bullets': ['Puttaparthi identity with a clear educational purpose', 'Autonomous positioning supported by visible quality signals', 'Leadership, NAAC, IQAC, and industry relevance in one narrative'], 'actions': [('View Vision & Mission', '/about/vision-mission.html', 'primary'), ('Quality & Recognition', '/about/quality.html', 'secondary')]},
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Inside About', 'title': 'The institutional story is grouped the way visitors actually look for it.', 'text': 'The live site spans heritage, mission, leadership, recognition, advisory structures, and quality cells. These parts should feel curated, not scattered.', 'cards': [
                ('Vision & Mission', 'The school’s published vision, mission, and student-development intent.', '/about/vision-mission.html'),
                ('Leadership', 'Chairman, Principal, and Secretary messages collected into one coherent section.', '/about/leadership.html'),
                ('Quality & Recognition', 'Autonomous status, AICTE / UGC recognition, NAAC, and IQAC context.', '/about/quality.html'),
                ('Industry Advisory', 'Board members and the industry-academia bridge described on the current site.', '/about/industry-interface.html'),
            ]},
            {'type': 'story_cards', 'variant': 'editorial', 'kicker': 'Institutional reading', 'title': 'What this section should communicate clearly.', 'items': [('Heritage', 'Puttaparthi is not filler context; it helps explain the school’s values, location, and identity.'), ('Credibility', 'Recognition, NAAC, IQAC, and leadership are visible trust signals and should be easy to find.'), ('Direction', 'Industry relevance, global exposure, and student development belong in the same institutional narrative.')]},
        ],
    },
    'about/vision-mission.html': {
        'section': 'About',
        'title': 'Vision & Mission',
        'description': 'The published vision and mission of Sanskrithi School of Engineering, focused on dynamic, socially responsible engineers with wisdom, initiative, and character.',
        'hero_kicker': 'Vision & Mission',
        'hero_title': 'To develop dynamic and socially responsible engineers.',
        'hero_text': 'The existing SSETP site already articulates a specific educational intention: wisdom, positive attitude, character, innovation, initiative, teamwork, and the ability to respond to change.',
        'hero_image': 'https://sseptp.org/assets/principal-Cgd9y_bj.jpg',
        'content': [
            {'type': 'split', 'kicker': 'Vision', 'title': 'The school’s published vision is already strong and specific.', 'text': 'SSE describes its aim as developing dynamic and socially responsible engineers possessing wisdom, positive attitude, and impeccable character, with innovation, initiative, teamwork, and responsiveness to change as hallmarks.', 'bullets': ['Dynamic and socially responsible engineers', 'Wisdom, positive attitude, and impeccable character', 'Innovation, initiative, and teamwork', 'Ability to anticipate change and create opportunity']},
            {'type': 'story_cards', 'kicker': 'Mission', 'title': 'The mission statement centers on quality, skills, and service.', 'items': [('Quality education', 'The college states that it serves society and the nation through quality education and skill development.'), ('Research and innovation', 'It commits to new benchmarks in engineering education through research, development, and innovation.'), ('Service orientation', 'The mission explicitly references service to society, industry, and the wider world.')]},
        ],
    },
    'about/leadership.html': {
        'section': 'About',
        'title': 'Leadership',
        'description': 'Leadership messages and institutional voice from Sanskrithi School of Engineering.',
        'hero_kicker': 'Leadership',
        'hero_title': 'Leadership pages should feel personal, not ceremonial.',
        'hero_text': 'The existing website already publishes Chairman, Principal, and Secretary-facing content. This section makes those voices easier to reach and easier to understand in context.',
        'hero_image': 'https://sseptp.org/assets/principal-Cgd9y_bj.jpg',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Leadership voices', 'title': 'Three message pages now read as one coherent leadership layer.', 'text': 'Families want to know how the institution speaks for itself. These pages support that trust decision.', 'cards': [('Chairman Message', 'Institutional vision and educational direction.', '#'), ('Principal Message', 'Academic environment, standards, and student growth.', '#'), ('Secretary Message', 'Continuity, administration, and institutional support.', '#'), ('Shared purpose', 'Together these pages reinforce values, seriousness, and accountability.', '#')]},
            {'type': 'split', 'kicker': 'Why it helps', 'title': 'Leadership copy works best when it strengthens admissions confidence.', 'text': 'Well-placed leadership pages can reassure students and parents that the institution is led deliberately and communicates with clarity.', 'bullets': ['Shows who leads the institution', 'Connects values to the student experience', 'Supports trust for parents and stakeholders', 'Adds substance beyond pure marketing copy']},
        ],
    },
    'about/quality.html': {
        'section': 'About',
        'title': 'Quality & Recognition',
        'description': 'Autonomous status, affiliation and recognition, NAAC accreditation, IQAC, and institutional quality signals at Sanskrithi School of Engineering.',
        'hero_kicker': 'Quality & Recognition',
        'hero_title': 'Recognition matters more when it is easy to verify.',
        'hero_text': 'SSE already shows a real quality framework: autonomous positioning, AICTE and UGC recognition, NAAC A Grade accreditation, and an IQAC structure aimed at continuous improvement.',
        'hero_image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Core credentials', 'title': 'The quality story is clearer when the signals are grouped together.', 'text': 'These are not decorative badges; they are central proof points for institutional trust.', 'cards': [('Autonomous Institute', 'Academic independence is a major part of the current SSE positioning.', '#'), ('AICTE Approved', 'Engineering programs are presented within the expected national approval framework.', '#'), ('UGC Recognized', 'Recognition signals are part of the institution’s credibility layer.', '#'), ('NAAC A Grade', 'The current site highlights an A Grade with a score of 3.17 out of 4.', '#')]},
            {'type': 'story_cards', 'kicker': 'Quality systems', 'title': 'What the current site says about improvement culture.', 'items': [('IQAC', 'The Internal Quality Assurance Cell is described as a catalyst for academic and administrative enhancement.'), ('Continuous improvement', 'The institution frames quality as a recurring process, not a one-time badge.'), ('Stakeholder confidence', 'Recognition is used to strengthen trust for students, parents, and industry partners.')]},
        ],
    },
    'about/industry-interface.html': {
        'section': 'About',
        'title': 'Industry Interface',
        'description': 'Industry advisory and collaboration context at Sanskrithi School of Engineering.',
        'hero_kicker': 'Industry Interface',
        'hero_title': 'Industry linkage should be treated as academic proof, not decoration.',
        'hero_text': 'The current site already names an Industry Advisory Board with members from RISE, TCS, CGI, HCLTech, Brillio, HP, Mphasis, and Capgemini. That deserves a direct, concrete presentation.',
        'hero_image': 'https://sseptp.org/assets/recruiters-B_A9F7qO.png',
        'content': [
            {'type': 'story_cards', 'kicker': 'What the page already proves', 'title': 'The board signals range and seriousness.', 'items': [('International connection', 'RISE-linked members strengthen the school’s global academic positioning.'), ('Employer relevance', 'Indian industry leaders help connect curriculum with market expectations.'), ('Academic bridge', 'The industry page supports the placement story and should sit close to it conceptually.')]},
            {'type': 'split', 'kicker': 'Functional role', 'title': 'This page should explain why industry input matters.', 'text': 'The industry interface is valuable because it ties curriculum relevance, mentorship, guest talks, internships, and employability into one visible academic-support story.', 'bullets': ['Curriculum relevance', 'Internships and guest sessions', 'Board-level external guidance', 'Stronger placement credibility']},
        ],
    },
    'admissions/index.html': {
        'section': 'Admissions',
        'title': 'Admissions Overview',
        'description': 'Admissions guidance for Sanskrithi School of Engineering with overview, process, fees, scholarship information, and direct enquiry routes.',
        'hero_kicker': 'Admissions',
        'hero_title': 'A clearer front door for students and families.',
        'hero_text': 'Admissions should not be scattered between footer links and disconnected subpages. This section brings together overview, process, fees, scholarship support, and the real enquiry contacts already published by SSETP.',
        'hero_stats': [('2026', 'Admissions cycle surfaced prominently'), ('3', 'core enquiry mailboxes available'), ('1', 'clear admissions journey'), ('Puttaparthi', 'Campus destination now visible')],
        'hero_image': 'https://sseptp.org/assets/girlsnearsteps-DxC0q7RC.jpg',
        'content': [
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Admissions routes', 'title': 'The admissions section answers the first four practical questions clearly.', 'text': 'Visitors usually need orientation, process, money clarity, and a way to ask a real person. Those routes should feel immediate.', 'cards': [('Admissions Overview', 'What SSE is, where it is, and why a student might shortlist it.', '/admissions/index.html'), ('Admission Process', 'A simplified step-by-step view for prospective students and families.', '/admissions/process.html'), ('Fees & Scholarship Support', 'Fee clarity plus Sai Prudent Scholarship visibility.', '/admissions/fees.html'), ('Enquiry', 'Direct access to enquiry@sseptp.org and institutional contact points.', '/admissions/enquiry.html')]},
            {'type': 'quote_panel', 'kicker': 'Why this matters', 'title': 'Good admissions UX reduces hesitation.', 'text': 'Parents and students do not want to hunt for process, support, or contact information. This structure brings those decisions into one focused path.'},
        ],
    },
    'admissions/process.html': {
        'section': 'Admissions',
        'title': 'Admission Process',
        'description': 'Step-by-step admission journey for prospective students at Sanskrithi School of Engineering.',
        'hero_kicker': 'Admission Process',
        'hero_title': 'A simple process view removes unnecessary uncertainty.',
        'hero_text': 'This page turns admissions intent into a clean sequence so students and families know what to do next instead of guessing across multiple pages.',
        'hero_image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg',
        'content': [
            {'type': 'timeline', 'kicker': 'How to move forward', 'title': 'A practical admissions sequence', 'text': 'The operational details can expand later, but the information architecture should already reflect the real applicant journey.', 'steps': ['Start with an enquiry or admissions conversation to identify the right program and route.', 'Review eligibility, required documents, and any counselling or admission guidance shared by the institution.', 'Submit documents and complete the formal admission steps for the selected program.', 'Confirm fees, onboarding instructions, and campus reporting before joining.']},
            {'type': 'cta_strip', 'title': 'Need help before applying?', 'text': 'For many students, the right next step is still a conversation.', 'primary': ('Send an enquiry', '/admissions/enquiry.html'), 'secondary': ('View fees', '/admissions/fees.html')},
        ],
    },
    'admissions/fees.html': {
        'section': 'Admissions',
        'title': 'Fees & Scholarships',
        'description': 'Admissions fee clarity and Sai Prudent Scholarship information at Sanskrithi School of Engineering.',
        'hero_kicker': 'Fees & Scholarships',
        'hero_title': 'Financial clarity should sit beside student support.',
        'hero_text': 'SSE already publishes the Sai Prudent Scholarship story. This page brings cost conversations and support visibility into the same admissions decision flow.',
        'hero_image': 'https://sseptp.org/assets/girlsnearsteps-DxC0q7RC.jpg',
        'content': [
            {'type': 'story_cards', 'kicker': 'Sai Prudent Scholarship', 'title': 'The existing scholarship story is already concrete.', 'items': [('Established in 2010', 'The scholarship is presented as a long-running support initiative.'), ('Supported by partners', 'The current site references Anahata Stiftung and RISE, Austria.'), ('Merit + need', 'The program is described for deserving students from economically disadvantaged backgrounds.')]},
            {'type': 'split', 'kicker': 'What this page should do', 'title': 'Students need both cost clarity and confidence that support exists.', 'text': 'The page should clearly connect fees, scholarship logic, and enquiry support so students and families can make decisions with more confidence.', 'bullets': ['Explain fee structure clearly', 'Show scholarship support prominently', 'Link questions to admissions contact', 'Reduce early uncertainty for families']},
        ],
    },
    'admissions/enquiry.html': {
        'section': 'Admissions',
        'title': 'Admissions Enquiry',
        'description': 'Admissions enquiry routes for Sanskrithi School of Engineering.',
        'hero_kicker': 'Admissions Enquiry',
        'hero_title': 'Admissions contact should feel direct and human.',
        'hero_text': 'The page uses the institution’s real enquiry routes instead of treating contact as an afterthought.',
        'hero_image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Contact routes', 'title': 'Use the right route for the right question.', 'text': 'This page should prioritize response paths over decoration.', 'cards': [('Admissions Enquiry', 'enquiry@sseptp.org for student and parent admissions questions.', '#'), ('General Office', 'info@sseptp.org for broader institutional questions.', '#'), ('Phone Contact', '+91 9100064545 / 74545 for direct office contact.', '#'), ('Visit / Reach Campus', 'Puttaparthi, Sri Sathya Sai District, AP - 515134.', '#')]},
            {'type': 'quote_panel', 'kicker': 'Live contact data', 'title': 'enquiry@sseptp.org | info@sseptp.org | +91 9100064545 / 74545', 'text': 'The admissions contact layer should use the same real data consistently across hero, body, and footer.'},
        ],
    },
    'academics/index.html': {
        'section': 'Academics',
        'title': 'Academics Overview',
        'description': 'Academics at Sanskrithi School of Engineering: departments, curriculum process, laboratories, scholarship support, and the RIT pathway.',
        'hero_kicker': 'Academics',
        'hero_title': 'Academic depth, practical learning, and curriculum governance in one place.',
        'hero_text': 'The live site already explains that SSE continuously revises curriculum through departmental committees, Boards of Studies, and the Academic Council while strengthening labs, research, and industry readiness.',
        'hero_image': 'https://sseptp.org/assets/ritprogram-Bc3C0C6e.jpg',
        'hero_stats': [('6', 'engineering departments surfaced'), ('BoS', 'Board of Studies layer present in current copy'), ('DAC', 'Department Academic Committees referenced'), ('RIT', 'international academic differentiator')],
        'content': [
            {'type': 'spotlight', 'kicker': 'Featured pathway', 'title': 'Academics should foreground the differentiators, not hide them in navigation.', 'text': 'SSETP already has strong academic proof points: curriculum governance, practical labs, student support, and the RIT pathway. The overview page should stage those elements with more intent.', 'image': 'https://sseptp.org/assets/ritprogram-Bc3C0C6e.jpg', 'image_alt': 'RIT pathway and academic experience at SSETP', 'bullets': ['RIT pathway as a visible international software-engineering differentiator', 'Laboratories and curriculum review as practical academic proof', 'Scholarship support and departmental depth kept within the same academic journey'], 'actions': [('Explore RIT Pathway', '/academics/rit.html', 'primary'), ('View Programs', '/academics/programs.html', 'secondary')]},
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Academic structure', 'title': 'The key academic journeys are clearer when treated as one system.', 'text': 'Programs, labs, support, and international pathways should reinforce each other instead of living on unrelated pages.', 'cards': [('Programs', 'Core departments and engineering pathways currently highlighted by SSE.', '/academics/programs.html'), ('Laboratories', 'Practical infrastructure across computing, electronics, civil, electrical, and mechanical domains.', '/academics/labs.html'), ('Sai Prudent Scholarship', 'Student support tied to progression and access.', '/academics/scholarships.html'), ('RIT Pathway', 'Software-engineering learning in cooperation with RISE and INSO.', '/academics/rit.html')]},
            {'type': 'split', 'kicker': 'Published academic process', 'title': 'Curriculum revision is part of the academic story.', 'text': 'The current SSETP copy explicitly references DACs, Boards of Studies, and the Academic Council. That governance detail is useful because it signals seriousness and structured academic review.', 'bullets': ['Departments review and discuss syllabus content', 'Board of Studies finalizes course structure and syllabus', 'Academic Council approves broader academic matters', 'Infrastructure and research are framed as part of academic quality']},
        ],
    },
    'academics/programs.html': {
        'section': 'Academics',
        'title': 'Programs',
        'description': 'Engineering departments and program areas at Sanskrithi School of Engineering.',
        'hero_kicker': 'Programs',
        'hero_title': 'Six engineering departments deserve a cleaner overview.',
        'hero_text': 'The academic structure highlighted on the current site spans Computer Science, ECE, EEE, Civil, Mechanical, and Information Technology.',
        'hero_image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Departments', 'title': 'A simpler department overview.', 'text': 'Instead of forcing users through one long undifferentiated academic page, the programs view can establish the range immediately.', 'cards': [('Computer Science & Engineering', 'Programming, software, AI/ML, databases, networks, and strong alignment with the RIT pathway.', '#'), ('Electronics & Communication', 'Communication systems, embedded systems, VLSI, and signal-oriented engineering.', '#'), ('Electrical & Electronics / Civil', 'Power, control, infrastructure, and core engineering disciplines with practical lab support.', '#'), ('Mechanical / Information Technology', 'Mechanical systems, manufacturing, and IT-focused software and systems pathways.', '#')]},
            {'type': 'quote_panel', 'kicker': 'Academic intent', 'title': 'Programs should be explained through outcomes, facilities, and relevance.', 'text': 'Program pages work best when they move away from abstract brochure language and toward department-specific clarity.'},
        ],
    },
    'academics/labs.html': {
        'section': 'Academics',
        'title': 'Laboratory Facilities',
        'description': 'Laboratory infrastructure and practical learning environments at Sanskrithi School of Engineering.',
        'hero_kicker': 'Laboratory Facilities',
        'hero_title': 'Hands-on learning is one of the easiest academic strengths to show.',
        'hero_text': 'The live site already presents a deep laboratory story across departments, from programming and networking labs to VLSI, manufacturing, structures, and power systems.',
        'hero_image': 'https://sseptp.org/assets/ritprogram-Bc3C0C6e.jpg',
        'content': [
            {'type': 'story_cards', 'kicker': 'Examples from the live site', 'title': 'Laboratory content should stay concrete.', 'items': [('CSE labs', 'Programming, databases, computer networks, and AI / machine learning are explicitly called out.'), ('ECE / EEE labs', 'Digital electronics, communication systems, VLSI, electrical machines, power systems, and control labs are part of the published story.'), ('Core engineering labs', 'Mechanical, civil, manufacturing, structural, geotechnical, and environmental labs broaden the practical picture.')]},
            {'type': 'split', 'kicker': 'Why this page works', 'title': 'Practical infrastructure makes academic claims believable.', 'text': 'Lab pages are strongest when they show how theory becomes practice.', 'bullets': ['Department-specific facilities', 'Equipment and experimentation context', 'Practical relevance to curriculum', 'Research and project-readiness signals']},
        ],
    },
    'academics/scholarships.html': {
        'section': 'Academics',
        'title': 'Sai Prudent Scholarship',
        'description': 'Sai Prudent Scholarship support at Sanskrithi School of Engineering.',
        'hero_kicker': 'Student Support',
        'hero_title': 'Scholarship content should be part of student confidence, not a side note.',
        'hero_text': 'The Sai Prudent Scholarship is already one of the more concrete support stories on the current site and should remain visible from both academics and admissions.',
        'hero_image': 'https://sseptp.org/assets/girlsnearsteps-DxC0q7RC.jpg',
        'content': [
            {'type': 'story_cards', 'kicker': 'Key facts', 'title': 'What the current site already states clearly.', 'items': [('Purpose', 'Support deserving students from economically disadvantaged backgrounds.'), ('Partners', 'Supported by Anahata Stiftung and RISE, Austria according to the current site.'), ('Selection logic', 'Academic merit, need, attendance, conduct, and participation are part of the eligibility story.')]},
            {'type': 'cta_strip', 'title': 'Need support or clarification?', 'text': 'Scholarship questions should connect directly back to admissions and enquiry routes.', 'primary': ('Admissions enquiry', '/admissions/enquiry.html'), 'secondary': ('Contact SSE', '/contact.html')},
        ],
    },
    'academics/rit.html': {
        'section': 'Academics',
        'title': 'RIT Pathway',
        'description': 'RISE Institute of Higher Technologies (RIT) pathway at Sanskrithi School of Engineering in cooperation with European mentors.',
        'hero_kicker': 'RIT Pathway',
        'hero_title': 'A real academic differentiator with international visibility.',
        'hero_text': 'The RIT Program is one of the most distinctive parts of the current SSETP site: a software-engineering learning pathway with RISE / INSO and mentors linked to Vienna and Graz.',
        'hero_image': 'https://sseptp.org/assets/ritprogram-Bc3C0C6e.jpg',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Program structure', 'title': 'The current RIT page already has a usable four-module logic.', 'text': 'That structure should be preserved and made easier to understand through a clearer academic presentation.', 'cards': [('Module 1', 'Foundation setup: tools, communication habits, typing, and programming mindset.', '#'), ('Module 2', 'Programming basics with introductory Java problem solving.', '#'), ('Module 3', 'Advanced Java assignments with more depth and longer timelines.', '#'), ('Module 4', 'Software architecture, OOP, design patterns, SQLite, Git, and GitHub.', '#')]},
            {'type': 'story_cards', 'kicker': 'Why it matters', 'title': 'RIT strengthens SSE’s software-engineering identity.', 'items': [('International mentors', 'The live page names mentors connected to RISE and European universities.'), ('Practical focus', 'The program is assignment-heavy and problem-solving oriented.'), ('Career relevance', 'It gives CSE students a visible pathway beyond generic department copy.')]},
        ],
    },
    'campus/index.html': {
        'section': 'Campus Life',
        'title': 'Campus Life Overview',
        'description': 'Campus life, facilities, hostel, wellbeing, and student experience at Sanskrithi School of Engineering.',
        'hero_kicker': 'Campus Life',
        'hero_title': 'Campus pages should help families picture daily life, not just buildings.',
        'hero_text': 'The current SSETP material already covers accommodation, dining, facilities, student activities, and sports. This section reorganizes that material into clearer trust-building pages.',
        'hero_image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg',
        'content': [
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Student experience', 'title': 'Campus life is structured around the questions families actually ask.', 'text': 'Where will students live, what facilities exist, how is wellbeing handled, and what does student life look like beyond class?', 'cards': [('Facilities', 'Academic and support spaces that shape the day-to-day experience.', '/campus/facilities.html'), ('Hostel Life', 'Accommodation, dining, safety, and student community.', '/campus/hostel.html'), ('Health & Safety', 'Wellbeing, support, and trust signals for parents and students.', '/campus/health-safety.html'), ('Sports', 'Participation, energy, and campus-life balance.', '/campus/sports.html')]},
            {'type': 'quote_panel', 'kicker': 'Campus reading', 'title': 'A good campus section reduces emotional uncertainty.', 'text': 'Students do not choose only on academics. Families also want to see where a student will live, move, eat, and feel supported.'},
        ],
    },
    'campus/facilities.html': {
        'section': 'Campus Life',
        'title': 'Facilities',
        'description': 'Campus facilities at Sanskrithi School of Engineering.',
        'hero_kicker': 'Facilities',
        'hero_title': 'Facilities pages should show practical support, not generic pride.',
        'hero_text': 'The campus content already points to academic spaces, accommodation support, common areas, dining, and connectivity. This page groups those facility stories in one clear layer.',
        'hero_image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg',
        'content': [
            {'type': 'story_cards', 'kicker': 'Facility themes', 'title': 'What the current SSETP content already emphasizes.', 'items': [('Academic environment', 'Laboratories, classrooms, and department spaces support the academic promise.'), ('Residential support', 'Hostel blocks, common rooms, dining, and Wi-Fi shape the lived student experience.'), ('Daily usability', 'Families want to know the campus is functional and student-ready, not just visually attractive.')]},
            {'type': 'cta_strip', 'title': 'Want the residential view too?', 'text': 'Facilities and hostel life work best when linked tightly in the navigation.', 'primary': ('View hostel life', '/campus/hostel.html'), 'secondary': ('Contact SSE', '/contact.html')},
        ],
    },
    'campus/hostel.html': {
        'section': 'Campus Life',
        'title': 'Hostel Life',
        'description': 'Hostel accommodations and student living experience at Sanskrithi School of Engineering.',
        'hero_kicker': 'Hostel Life',
        'hero_title': 'Hostel content should answer the parental trust question directly.',
        'hero_text': 'The live site already gives hostel-specific detail on boys and girls blocks, common rooms, Wi-Fi, dining, security, activities, and rules.',
        'hero_image': 'https://sseptp.org/assets/girlsnearsteps-DxC0q7RC.jpg',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Residential life', 'title': 'The current hostel story already has useful structure.', 'text': 'This content should stay specific, because specificity builds trust.', 'cards': [('Accommodation', 'Separate hostel blocks, furnished rooms, and supervised residential arrangements.', '#'), ('Dining & Mess', 'Meal support, kitchen facilities, and dining-hall context are already part of the live copy.', '#'), ('Student Activities', 'Cultural events, sports, and hostel committees contribute to community life.', '#'), ('Safety & Rules', 'Security, timings, conduct, and support expectations matter to families.', '#')]},
            {'type': 'story_cards', 'kicker': 'Concrete points from the live content', 'title': 'The page already has trust-building detail.', 'items': [('24×7 security', 'Security is explicitly part of the current hostel presentation.'), ('Common spaces', 'Common rooms and shared facilities make the residential environment feel more real.'), ('Dining support', 'Mess and meal arrangements are already described, so they should remain prominent.')]},
        ],
    },
    'campus/health-safety.html': {
        'section': 'Campus Life',
        'title': 'Health & Safety',
        'description': 'Health, safety, and student wellbeing information at Sanskrithi School of Engineering.',
        'hero_kicker': 'Health & Safety',
        'hero_title': 'Wellbeing pages need calm clarity, not promotional noise.',
        'hero_text': 'The broader campus and hostel material already references medical support, first aid, security, and student rules. This page gives those concerns a dedicated place in the navigation.',
        'hero_image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg',
        'content': [
            {'type': 'split', 'kicker': 'What families care about', 'title': 'Safety information is one of the highest-trust parts of a school website.', 'text': 'It helps when health and safety are treated as a service page with concrete reassurance instead of vague adjectives.', 'bullets': ['Campus and hostel security visibility', 'Medical / first-aid support context', 'Student support expectations', 'Clear contact routes when help is needed']},
            {'type': 'cta_strip', 'title': 'Need a direct answer?', 'text': 'For many safety questions, direct contact is still the right interaction.', 'primary': ('Contact SSE', '/contact.html'), 'secondary': ('Hostel life', '/campus/hostel.html')},
        ],
    },
    'campus/sports.html': {
        'section': 'Campus Life',
        'title': 'Sports',
        'description': 'Sports and student participation at Sanskrithi School of Engineering.',
        'hero_kicker': 'Sports & Participation',
        'hero_title': 'Sports pages should support the idea of a balanced student life.',
        'hero_text': 'Campus-life content is stronger when it shows that SSE is not only about classrooms and placements, but also about teamwork, participation, and student energy.',
        'hero_image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg',
        'content': [
            {'type': 'story_cards', 'kicker': 'Role of sports', 'title': 'Why this page belongs in the structure.', 'items': [('Balance', 'Sports helps round out the academic and residential story.'), ('Teamwork', 'It reinforces the collaborative values described elsewhere across the site.'), ('Campus energy', 'It makes student life feel active and lived-in rather than static.')]},
        ],
    },
    'placements/index.html': {
        'section': 'Placements',
        'title': 'Placements Overview',
        'description': 'Placement outcomes, recruiter relationships, training, and CDC team information at Sanskrithi School of Engineering.',
        'hero_kicker': 'Placements',
        'hero_title': 'Placements are one of SSE’s strongest public proof points.',
        'hero_text': 'The current site already publishes strong placement evidence: 1675 total offers, 800 students placed, 150 recruiting companies, 36 LPA highest package, and 95% placement rate for 2024-25. This placement story deserves strong visibility.',
        'hero_stats': [('1675', 'Total offers'), ('800', 'Students placed'), ('150', 'Recruiting companies'), ('36 LPA', 'Highest package')],
        'hero_image': 'https://sseptp.org/assets/placement-D9x0hLK2.jpg',
        'content': [
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Placement section', 'title': 'This content should feel evidence-led, not vague.', 'text': 'SSE already has enough material to present placements as a major strength.', 'cards': [('Placement Highlights', 'Published numbers, recruiter relationships, and internship visibility.', '/placements/index.html'), ('Success Stories', 'Outcome-led examples framed without unnecessary filler.', '/placements/success-stories.html'), ('Placement Contact', 'CDC team, coordinators, and recruiter-facing routes.', '/placements/contact.html'), ('Training Readiness', 'Aptitude, technical, communication, and interview-prep support described on the current site.', '#')]},
            {'type': 'split', 'kicker': 'Placement narrative', 'title': 'The live copy already explains the student-readiness model.', 'text': 'SSE frames its placement cell as more than a recruitment desk: it starts early, shapes readiness, and connects training with market expectations.', 'bullets': ['Training starts from the second year', 'Technical, aptitude, and communication preparation are all emphasized', 'Recruiter trust is reinforced visually through company visibility', 'The CDC team is visible and should stay reachable']},
        ],
    },
    'placements/success-stories.html': {
        'section': 'Placements',
        'title': 'Success Stories',
        'description': 'Placement outcome snapshots at Sanskrithi School of Engineering.',
        'hero_kicker': 'Success Stories',
        'hero_title': 'Outcome pages work best when they stay close to evidence.',
        'hero_text': 'Rather than inventing polished student profiles, the success-stories layer works best as a structured extension of the published placement performance and recruiter ecosystem.',
        'hero_image': 'https://sseptp.org/assets/recruiters-B_A9F7qO.png',
        'content': [
            {'type': 'story_cards', 'kicker': 'Outcome lens', 'title': 'What this page should show clearly.', 'items': [('High-value offers', 'The current site already highlights strong top-end packages.'), ('Broad recruiter base', 'The number of recruiting companies matters because it signals scale, not just a few standout cases.'), ('Training-to-offer logic', 'Success stories should connect back to the placement training model rather than reading like isolated testimonials.')]},
            {'type': 'metrics_band', 'items': [('95%', 'placement rate'), ('1500', 'internship offers'), ('2', 'international offers'), ('7.5 LPA', 'average package highlighted')]},
        ],
    },
    'placements/contact.html': {
        'section': 'Placements',
        'title': 'Placement Contact',
        'description': 'Training & Placement / CDC contact routes at Sanskrithi School of Engineering.',
        'hero_kicker': 'Placement Contact',
        'hero_title': 'Recruiter and placement contact should be easy to find.',
        'hero_text': 'The current site already names members of the CDC / Training & Placement team including Kiran Ravi Srivastava, Dr. Bala Koteswari, and Rakesh Yadav Kodari.',
        'hero_image': 'https://sseptp.org/assets/placement-D9x0hLK2.jpg',
        'content': [
            {'type': 'story_cards', 'kicker': 'Published team visibility', 'title': 'The live site already gives this page strong raw material.', 'items': [('CDC Head', 'Ms. Kiran Ravi Srivastava is named as CDC – Head.'), ('Coordinators', 'Dr. Bala Koteswari and Mr. Rakesh Yadav Kodari are visible as coordinators.'), ('Training layer', 'The team structure supports the broader placement-readiness narrative.')]},
            {'type': 'cta_strip', 'title': 'Need the placements mailbox?', 'text': 'Recruiters and career-related queries should be routed clearly to the team.', 'primary': ('Contact page', '/contact.html'), 'secondary': ('Placement overview', '/placements/index.html')},
        ],
    },
    'contact.html': {
        'section': 'Contact',
        'title': 'Contact & Enquiry',
        'description': 'Contact Sanskrithi School of Engineering for admissions, academics, placements, and institutional enquiries.',
        'hero_kicker': 'Contact SSE',
        'hero_title': 'Real contact routes deserve a proper page.',
        'hero_text': 'This page is built around the published SSETP contact details: Puttaparthi campus address, office phone numbers, and dedicated mailboxes for general, admissions, and placement / HR conversations.',
        'hero_badges': ['info@sseptp.org', 'enquiry@sseptp.org', 'hr@sseptp.org', '+91 9100064545 / 74545'],
        'hero_stats': [('Puttaparthi', 'Sri Sathya Sai District campus'), ('3', 'email routes'), ('2', 'published phone numbers'), ('1', 'clear contact hub')],
        'hero_image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg',
        'content': [
            {'type': 'spotlight', 'kicker': 'Start here', 'title': 'The Contact page should guide the next action immediately.', 'text': 'Students, parents, recruiters, and institutional visitors should reach the right route without scanning through generic information blocks.', 'image': 'https://sseptp.org/assets/ssecampus-tJIhAnGN.jpg', 'image_alt': 'SSETP campus and enquiry routes', 'bullets': ['Admissions: enquiry@sseptp.org for prospective students and parents', 'General: info@sseptp.org for institutional questions', 'Placements / HR: hr@sseptp.org for recruiter and career-related contact'], 'actions': [('Send Admissions Enquiry', '/admissions/enquiry.html', 'primary'), ('View Placements', '/placements/index.html', 'secondary')]},
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Contact paths', 'title': 'Choose the right route quickly.', 'text': 'The page should make the next action obvious, especially on mobile.', 'cards': [('Admissions', 'enquiry@sseptp.org for prospective-student and parent conversations.', '#'), ('General Office', 'info@sseptp.org for institutional and broad enquiries.', '#'), ('Placements / HR', 'hr@sseptp.org for recruiter and placement-related questions.', '#'), ('Call or Visit', '+91 9100064545 / 74545 | Puttaparthi, Sri Sathya Sai District, AP - 515134', '#')]},
            {'type': 'split', 'kicker': 'Social presence', 'title': 'The institution already publishes its main public channels.', 'text': 'Alongside social channels, the primary user need remains fast, trustworthy institutional contact.', 'bullets': ['Facebook: sseptp', 'X: SanskrithiGroup', 'Instagram: sanskrithigroup_ptp', 'Address and phone remain the primary trust anchors']},
        ],
    },

}

STYLE = r'''
:root{--navy:#001A3D;--navy-2:#0d2d61;--navy-3:#173d7d;--orange:#f26522;--orange-2:#ff8c42;--orange-3:#ffd2ad;--ink:#162230;--muted:#64748b;--line:rgba(0,26,61,.1);--surface:#ffffff;--surface-2:#f8fbff;--surface-3:#fff7ef;--shadow-xl:0 28px 80px rgba(0,26,61,.16);--shadow-lg:0 18px 42px rgba(0,26,61,.10);--radius-xl:30px;--radius-lg:22px;--radius-md:16px;--container:1180px}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,system-ui,sans-serif;color:var(--ink);background:linear-gradient(180deg,#fffaf6 0%,#fff 16%,#f8fbff 100%);line-height:1.68;overflow-x:hidden}img{display:block;max-width:100%}a{-webkit-tap-highlight-color:transparent}.container{width:min(calc(100% - 2rem),var(--container));margin:0 auto}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.site-header{position:sticky;top:0;z-index:80;background:var(--navy);color:#fff;box-shadow:0 10px 24px rgba(0,0,0,.08)}.nav-wrap,.footer-wrap,.section-head,.hero-actions,.button-row,.cta-box,.breadcrumb{display:flex;gap:1rem}.nav-wrap,.footer-wrap,.cta-box{align-items:center;justify-content:space-between}.nav-wrap{min-height:80px}.brand{display:inline-flex;align-items:center;gap:.9rem;color:#fff;text-decoration:none;font-weight:800;letter-spacing:-.04em}.brand span:last-child{max-width:20rem}.brand-mark{display:block;width:3rem;height:3rem;object-fit:contain;filter:drop-shadow(0 10px 24px rgba(242,101,34,.18))}.nav{display:flex;align-items:stretch;gap:0;flex-wrap:wrap}.nav a{text-decoration:none;color:rgba(255,255,255,.9);font-weight:700;padding:1.45rem 1.25rem;position:relative;display:inline-flex;align-items:center}.nav a.active,.nav a:hover{color:#fff;background:rgba(255,255,255,.08)}.nav a.active{background:var(--orange)}.nav a.active:after{display:none}.nav-cta{margin-left:.5rem;padding:1rem 1rem !important;border-radius:12px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12)}.nav-cta:hover{background:rgba(255,255,255,.16) !important}.nav-toggle{display:none;flex-direction:column;justify-content:center;gap:.26rem;width:2.9rem;height:2.9rem;border:1px solid rgba(255,255,255,.14);border-radius:14px;background:transparent;cursor:pointer}.nav-toggle span:not(.sr-only){display:block;width:1.1rem;height:2px;margin:0 auto;background:#fff}
.hero{position:relative;overflow:clip;padding:4.4rem 0 3.8rem;background:radial-gradient(circle at 100% 0,rgba(242,116,5,.18),transparent 30%),radial-gradient(circle at 0 20%,rgba(23,61,125,.10),transparent 24%),linear-gradient(180deg,#fff2e5 0%,#fff8f2 38%,#fff 72%,#f8fbff 100%)}.hero:before{content:'';position:absolute;right:-8rem;top:-6rem;width:22rem;height:22rem;border-radius:50%;background:radial-gradient(circle,rgba(255,155,61,.18),transparent 65%);filter:blur(10px)}.hero-layout{display:grid;grid-template-columns:minmax(0,1.02fr) minmax(340px,.98fr);gap:2.6rem;align-items:center}.eyebrow,.section-label{display:inline-flex;align-items:center;gap:.5rem;margin:0 0 1rem;color:var(--orange);font-size:.8rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase}.eyebrow:before,.section-label:before{content:'';width:1.2rem;height:2px;border-radius:999px;background:linear-gradient(90deg,var(--orange),var(--orange-2))}h1,h2,h3,p,ul{margin-top:0}h1{margin-bottom:1.15rem;font-size:clamp(2.8rem,7vw,5.2rem);line-height:.95;letter-spacing:-.065em;max-width:11ch}h2{margin-bottom:1rem;font-size:clamp(2rem,4vw,3.1rem);line-height:1.04;letter-spacing:-.05em}h3{margin-bottom:.7rem;font-size:1.2rem;letter-spacing:-.03em}.lead,.section-head p,.card p,.split-copy p,.story p,.footer-note,.hero-badges span,.hero-stats span,.breadcrumb a,.breadcrumb span,.section-nav-shell small{color:var(--muted)}.hero-copy{position:relative;z-index:1}.hero-actions{flex-wrap:wrap;margin:2rem 0 1.4rem}.button{display:inline-flex;align-items:center;justify-content:center;min-height:52px;padding:0 1.25rem;border-radius:999px;text-decoration:none;font-weight:800;transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease,background .2s ease}.button:hover{transform:translateY(-1px)}.button.primary{background:linear-gradient(135deg,var(--orange) 0%,#d66704 100%);color:#fff;box-shadow:0 14px 30px rgba(242,116,5,.24)}.button.secondary,.button.ghost{background:#fff;border:1px solid var(--line);color:var(--ink)}.button.light{background:#fff;color:var(--navy)}.hero-badges{display:flex;gap:.7rem;flex-wrap:wrap}.hero-badges span{padding:.72rem .95rem;border-radius:999px;background:rgba(255,255,255,.82);border:1px solid rgba(0,26,61,.08);font-weight:700}.hero-panel,.card,.split-card,.story,.timeline article,.cta-box,.metric,.pillars article,.spotlight{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-xl);box-shadow:var(--shadow-lg)}.hero-panel{padding:1.4rem;background:linear-gradient(180deg,var(--navy) 0%,var(--navy-2) 78%,var(--navy-3) 100%);color:#fff;box-shadow:var(--shadow-xl)}.panel-topline{height:10px;width:42%;border-radius:999px;background:linear-gradient(90deg,var(--orange),var(--orange-2));margin-bottom:1.2rem}.hero-stats,.cards,.timeline,.pillars,.story-grid,.metrics-grid,.section-nav-shell{display:grid;gap:1rem}.hero-stats{grid-template-columns:repeat(2,minmax(0,1fr))}.hero-stats article{padding:1.15rem;border:1px solid rgba(255,255,255,.14);border-radius:18px;background:rgba(255,255,255,.06);backdrop-filter:blur(8px)}.hero-stats strong{display:block;margin-bottom:.35rem;font-size:1.55rem}.breadcrumb{align-items:center;flex-wrap:wrap;padding:1rem 0 0}.breadcrumb a{text-decoration:none}.section-nav{margin-top:-1.3rem;position:relative;z-index:3}.section-nav-panel{border-radius:18px;overflow:hidden;box-shadow:0 10px 25px -5px rgba(0,0,0,.1),0 8px 10px -6px rgba(0,0,0,.1);border-top:4px solid var(--orange);background:#fff}.section-nav-heading{padding:1rem 1.25rem;background:linear-gradient(180deg,#fff,#fff7ef);font-weight:800;color:var(--navy);border-bottom:1px solid rgba(0,26,61,.08)}.section-nav-shell{grid-template-columns:repeat(5,minmax(0,1fr));padding:1.1rem}.section-link{display:flex;flex-direction:column;gap:.24rem;padding:1rem 1rem;border-radius:14px;text-decoration:none;color:var(--ink);background:#fff;border:1px solid transparent;min-height:102px;justify-content:center}.section-link.is-active{background:linear-gradient(180deg,#fff3e7,#fff);border-color:rgba(242,116,5,.24);box-shadow:inset 0 0 0 1px rgba(242,116,5,.08)}.section-link:hover{transform:translateY(-1px);border-color:rgba(242,116,5,.18);background:linear-gradient(180deg,#fff8f1,#fff)}.section-nav-shell strong{font-size:1rem;color:var(--navy)}.section-nav-shell small{font-size:.88rem;line-height:1.45}.hero-subpage{padding-top:3.5rem;padding-bottom:3rem}.hero-subpage .hero-layout{grid-template-columns:minmax(0,1fr) minmax(300px,.72fr)}.hero-subpage{background:linear-gradient(rgba(255,248,242,.92),rgba(248,251,255,.96)),var(--hero-image) center/cover no-repeat}.hero-subpage .hero-copy{background:rgba(255,255,255,.72);border:1px solid rgba(0,26,61,.08);box-shadow:var(--shadow-lg);border-radius:28px;padding:2rem}.hero-subpage .hero-panel{background:linear-gradient(180deg,#fff 0%,#f8fbff 100%);color:var(--ink)}.hero-subpage .hero-stats article{background:linear-gradient(180deg,#fff8f1,#fff);border-color:rgba(0,26,61,.08)}.hero-subpage .hero-stats span{color:var(--muted)}.section{padding:4.6rem 0}.section-head{align-items:end;justify-content:space-between;margin-bottom:1.9rem}.section-head>*{flex:1}.cards.cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.cards.cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.cards.cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.card,.split-card,.story,.timeline article,.metric,.spotlight{padding:1.55rem}.card{position:relative;overflow:hidden;background:linear-gradient(180deg,#fff 0%,#fbfdff 100%);transition:transform .2s ease,box-shadow .2s ease}.card:hover{transform:translateY(-3px);box-shadow:0 24px 44px rgba(0,26,61,.12)}.card:after{content:'';position:absolute;right:-2.5rem;bottom:-2.5rem;width:7rem;height:7rem;border-radius:50%;background:rgba(242,116,5,.10)}.card a{font-weight:800;color:var(--navy);text-decoration:none}.cards-showcase .card-featured{grid-column:span 2;background:linear-gradient(135deg,#fff 0%,#fff4e8 55%,#eef6ff 100%);border-top:4px solid var(--orange);box-shadow:0 26px 50px rgba(0,26,61,.12)}.cards-showcase .card-featured h3{font-size:1.5rem}.cards-showcase .card-featured p{max-width:42ch}.icon{display:inline-grid;place-items:center;width:3rem;height:3rem;margin-bottom:1rem;border-radius:16px;background:linear-gradient(135deg,#fff0e2,#ffe0c0);color:var(--orange);font-weight:800}.split{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2rem;align-items:center}.split-card{background:linear-gradient(180deg,#fff8f0 0%,#fff 100%);border-top:4px solid var(--orange)}.mini-list{margin:1rem 0 0;padding-left:1.15rem}.mini-list li+li{margin-top:.45rem}.metrics-grid{grid-template-columns:repeat(4,minmax(0,1fr))}.metric{text-align:center;background:linear-gradient(180deg,#fff7ef 0%,#fff 100%);border-top:4px solid rgba(242,116,5,.72)}.metric strong{display:block;font-size:2rem;letter-spacing:-.04em;color:var(--navy)}.timeline{grid-template-columns:repeat(4,minmax(0,1fr))}.timeline article{background:linear-gradient(180deg,#fff 0%,#f8fbff 100%);border-top:4px solid rgba(0,26,61,.08)}.step-no{display:inline-grid;place-items:center;width:2.35rem;height:2.35rem;margin-bottom:1rem;border-radius:999px;background:var(--navy);color:#fff;font-weight:800}.story-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.story-grid-editorial .story-featured{grid-column:span 2;background:linear-gradient(135deg,#0d1c2f 0%,#173d7d 100%);color:#fff;border-top:none;box-shadow:var(--shadow-xl)}.story-grid-editorial .story-featured strong,.story-grid-editorial .story-featured p{color:#fff}.story-kicker{display:inline-flex;margin-bottom:.8rem;padding:.35rem .7rem;border-radius:999px;background:rgba(255,255,255,.14);font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}.story{background:linear-gradient(180deg,#fff 0%,#fff9f4 100%);border-top:4px solid rgba(242,116,5,.72)}.story strong{display:block;margin-bottom:.45rem;color:var(--navy)}.quote-panel{padding:2rem;border-radius:var(--radius-xl);background:linear-gradient(135deg,var(--navy) 0%,var(--navy-2) 66%,var(--navy-3) 100%);color:#fff;box-shadow:var(--shadow-xl)}.quote-panel p,.quote-panel .section-label{color:rgba(255,255,255,.82)}.quote-panel h2{color:#fff;max-width:18ch}.spotlight-wrap{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(280px,.95fr);gap:1.5rem;align-items:stretch;padding:1.4rem;border:1px solid rgba(242,116,5,.16);border-radius:var(--radius-xl);background:linear-gradient(135deg,#fff 0%,#fff6ee 52%,#f5f9ff 100%);box-shadow:var(--shadow-lg)}.spotlight-copy{padding:1rem}.spotlight-media{position:relative;min-height:320px;border-radius:24px;overflow:hidden}.spotlight-media img{width:100%;height:100%;object-fit:cover}.cta-strip{padding:1.4rem 1.5rem;border-radius:var(--radius-lg);background:linear-gradient(180deg,#fff4e8 0%,#fff 100%);border:1px solid rgba(242,116,5,.18);display:flex;gap:1rem;justify-content:space-between;align-items:center}.cta-strip-copy{max-width:46rem}.pillars{grid-template-columns:repeat(3,minmax(0,1fr))}.pillars article{padding:1.35rem 1.4rem;background:linear-gradient(180deg,#fff 0%,#fff8f1 100%)}.pillars strong{display:block;margin-bottom:.3rem;color:var(--navy)}.cta-box{padding:2rem;background:linear-gradient(135deg,var(--navy) 0%,var(--navy-2) 62%,var(--navy-3) 100%);color:#fff;box-shadow:var(--shadow-xl)}.cta-box .section-label,.cta-box h2,.cta-box p,.cta-box .button.ghost{color:#fff}.cta-box .button.ghost{border-color:rgba(255,255,255,.24);background:transparent}.site-footer{padding:1.7rem 0 2.3rem;border-top:1px solid rgba(0,26,61,.08)}.footer-wrap p{margin:0}.muted{background:linear-gradient(180deg,#fff8f1 0%,#fff 100%)}

.hero-home{min-height:560px;display:flex;align-items:center}.hero-home:after{content:'';position:absolute;inset:0;background:linear-gradient(rgba(0,26,61,.58),rgba(0,26,61,.54)),var(--hero-image) center/cover no-repeat;z-index:0}.hero-home .container,.hero-home .hero-copy,.hero-home .hero-panel{position:relative;z-index:1}.hero-home .hero-copy h1,.hero-home .hero-copy .lead,.hero-home .hero-copy .eyebrow,.hero-home .hero-badges span{color:#fff}.hero-home .eyebrow:before{background:linear-gradient(90deg,#fff,var(--orange-2))}.hero-home .hero-badges span{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.16)}
.feature-services{margin-top:-5.5rem;position:relative;z-index:5;padding-bottom:1rem}.feature-services-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.5rem}.feature-service-card{display:flex;flex-direction:column;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.08);min-height:100%}.feature-service-top{background:var(--navy);padding:2.2rem 1.8rem;text-align:center;color:#fff}.feature-service-top h3{margin:0;color:#fff}.feature-service-icon{width:4rem;height:4rem;border-radius:999px;margin:0 auto 1rem;display:grid;place-items:center;background:rgba(255,255,255,.08);color:var(--orange);font-weight:800;border:1px solid rgba(255,255,255,.14)}.feature-service-body{padding:1.8rem;text-align:center;flex:1}.feature-service-body a{color:var(--orange);font-weight:800;text-decoration:none}.feature-service-bar{height:.45rem;background:var(--orange)}
.news-section{background:#fff}.news-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2rem}.news-card{display:flex;gap:1.25rem;align-items:flex-start;padding:1rem;border-radius:18px;transition:background .2s ease}.news-card:hover{background:#fff8f1}.news-card img{width:12rem;height:9rem;object-fit:cover;border-radius:14px;box-shadow:0 8px 20px rgba(0,0,0,.08)}.news-card-copy h3{margin-bottom:.45rem;color:var(--navy)}.news-card-copy a{color:var(--orange);font-weight:800;text-decoration:none}
.site-footer{background:var(--navy);color:#fff;padding:4.5rem 0 2rem;border-top:none}.footer-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:2rem;margin-bottom:2.5rem}.footer-grid h4{margin:0 0 1rem;color:rgba(255,255,255,.76);text-transform:uppercase;letter-spacing:.08em;font-size:.95rem}.footer-grid p,.footer-grid a,.footer-grid li{color:rgba(255,255,255,.72);text-decoration:none;list-style:none}.footer-grid ul{margin:0;padding:0;display:grid;gap:.65rem}.footer-grid a:hover{color:#fff}.footer-bottom{padding-top:1.4rem;border-top:1px solid rgba(255,255,255,.1);display:flex;justify-content:space-between;gap:1rem;align-items:center}.footer-bottom p{margin:0}.site-footer .footer-note{color:rgba(255,255,255,.56)}

@media (max-width:1100px){.hero-layout,.split,.metrics-grid,.timeline,.story-grid,.pillars,.cards.cols-4,.cards.cols-3,.feature-services-grid,.footer-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.section-nav-shell{grid-template-columns:repeat(2,minmax(0,1fr))}.news-grid{grid-template-columns:1fr}}
@media (max-width:900px){.container{width:min(calc(100% - 1.5rem),var(--container))}.nav-toggle{display:inline-flex}.nav{position:absolute;top:calc(100% + .75rem);right:.75rem;left:.75rem;display:none;flex-direction:column;align-items:stretch;padding:.9rem;max-height:calc(100vh - 110px);overflow:auto;border:1px solid rgba(255,255,255,.08);border-radius:18px;background:rgba(13,45,97,.98);backdrop-filter:blur(12px);box-shadow:var(--shadow-xl)}.nav.is-open{display:flex}.nav a{padding:1rem;border-radius:12px}.nav-cta{margin-left:0}.hero{padding:3.75rem 0 3.15rem}.hero-layout,.split,.section-head,.cta-strip,.cta-box,.footer-bottom,.spotlight-wrap{grid-template-columns:1fr;flex-direction:column;align-items:flex-start}.hero-stats,.metrics-grid,.timeline,.story-grid,.pillars,.cards.cols-4,.cards.cols-3,.cards.cols-2,.feature-services-grid,.footer-grid,.cards-showcase,.story-grid-editorial{grid-template-columns:1fr}.cards-showcase .card-featured,.story-grid-editorial .story-featured{grid-column:span 1}.hero-subpage .hero-copy{padding:1.4rem;border-radius:22px}.hero-stats{grid-template-columns:repeat(2,minmax(0,1fr))}.section{padding:3.6rem 0}.section-nav{margin-top:-.4rem}.section-nav-panel{border-radius:16px}.section-nav-shell{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(220px,80%);grid-template-columns:none;overflow-x:auto;overscroll-behavior-x:contain;scroll-snap-type:x proximity;padding:.95rem;gap:.85rem}.section-link{min-height:unset;scroll-snap-align:start;padding:.95rem}.feature-services{margin-top:-1.5rem}.feature-service-card,.card,.story,.split-card,.timeline article,.metric,.cta-strip,.spotlight-wrap{border-radius:18px}.spotlight-copy{padding:0}.spotlight-media{min-height:220px;width:100%}.news-card{flex-direction:column}.news-card img{width:100%;height:12rem}.button-row{width:100%;flex-wrap:wrap}.button-row .button{flex:1 1 220px}.page-contact .hero-actions,.page-admissions-enquiry .hero-actions{width:100%}.page-contact .hero-actions .button,.page-admissions-enquiry .hero-actions .button{flex:1 1 100%}}
@media (max-width:640px){.brand{gap:.7rem}.brand-mark{width:2.5rem;height:2.5rem}.brand span:last-child{max-width:10.5rem;font-size:.92rem;line-height:1.12}h1{max-width:100%;font-size:clamp(2.25rem,12vw,3.55rem)}h2{font-size:clamp(1.7rem,8vw,2.35rem)}.lead{font-size:1rem}.button,.button-row .button,.nav-cta{width:100%}.hero-actions{width:100%}.hero-badges span{width:100%}.hero-stats{grid-template-columns:1fr 1fr}.hero-stats article,.hero-panel,.hero-subpage .hero-copy{padding:1.1rem}.feature-service-top,.feature-service-body,.card,.story,.split-card,.timeline article,.metric,.quote-panel,.cta-box{padding:1.2rem}.news-card{padding:.4rem 0}.news-card img{height:10.5rem}.breadcrumb{display:none}}
'''

SCRIPT = """const y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();const t=document.querySelector('.nav-toggle');const n=document.getElementById('site-nav');if(t&&n){t.addEventListener('click',()=>{const o=n.classList.toggle('is-open');t.setAttribute('aria-expanded',String(o))});n.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{n.classList.remove('is-open');t.setAttribute('aria-expanded','false')}))}"""


def rel_prefix(path: str) -> str:
    depth = len(Path(path).parts) - 1
    return './' if depth == 0 else '../' * depth


def href_from(page_path: str, target: str) -> str:
    if target == '#':
        return '#'
    page_dir = Path(page_path).parent
    target_path = Path(target.lstrip('/'))
    return Path(os.path.relpath(target_path, page_dir)).as_posix()


def page_url(path: str) -> str:
    return f"{SITE['domain']}/" if path == 'index.html' else f"{SITE['domain']}/{path}"


def breadcrumbs(path: str, section: str, title: str):
    crumbs = [('Home', '/index.html')]
    if section != 'Home':
        section_lookup = {label: href for label, href in NAV}
        crumbs.append((section, section_lookup.get(section, '/index.html')))
    items = []
    for label, href in crumbs:
        items.append(f'<a href="{href_from(path, href)}">{escape(label)}</a>')
    items.append(f'<span>{escape(title)}</span>')
    return '<nav class="breadcrumb">' + '<span>›</span>'.join(items) + '</nav>'


def render_nav(page_path: str, section: str) -> str:
    html = []
    for label, href in NAV:
        cls = 'active' if label == section else ''
        extra = ' nav-cta' if label == 'Contact' else ''
        html.append(f'<a class="{cls}{extra}" href="{href_from(page_path, href)}">{escape(label)}</a>')
    return ''.join(html)


def render_section_nav(page_path: str, section: str) -> str:
    current = '/' + page_path.replace('index.html', 'index.html').lstrip('./')
    if current == '/index.html':
        current = '/index.html'
    if section == 'Home':
        items = [
            ('About', '/about/index.html', 'Institutional story'),
            ('Admissions', '/admissions/index.html', 'Apply with clarity'),
            ('Academics', '/academics/index.html', 'Programs and pathways'),
            ('Campus Life', '/campus/index.html', 'Student experience'),
            ('Placements', '/placements/index.html', 'Career outcomes'),
        ]
        nav_label = 'Explore the School'
        heading = 'Explore the School'
    else:
        items = MEGA.get(section, [])
        nav_label = f'{section} navigation'
        heading = section
    if not items:
        return ''
    link_html = []
    for label, href, desc in items:
        active = ' is-active' if href == current else ''
        link_html.append(f'<a class="section-link{active}" href="{href_from(page_path, href)}"><strong>{escape(label)}</strong><small>{escape(desc)}</small></a>')
    return f'<section class="section-nav" aria-label="{escape(nav_label)}"><div class="container"><div class="section-nav-panel"><div class="section-nav-heading">{escape(heading)}</div><div class="section-nav-shell">{"".join(link_html)}</div></div></div></section>'


def render_feature_grid(page_path: str, block: dict) -> str:
    cols = min(max(len(block['cards']), 2), 4)
    variant = block.get('variant', '')
    cards = []
    for idx, (title, text, href) in enumerate(block['cards'], start=1):
        link = '' if href == '#' else f'<p><a href="{href_from(page_path, href)}">Open page →</a></p>'
        card_cls = 'card'
        if variant == 'showcase' and idx == 1:
            card_cls += ' card-featured'
        cards.append(f'<article class="{card_cls}"><div class="icon">{idx:02d}</div><h3>{escape(title)}</h3><p>{escape(text)}</p>{link}</article>')
    wrap_cls = f'cards cols-{cols}' + (' cards-showcase' if variant == 'showcase' else '')
    return f'<section class="section"><div class="container"><p class="section-label">{escape(block["kicker"])}</p><div class="section-head"><h2>{escape(block["title"])}</h2><p>{escape(block["text"])}</p></div><div class="{wrap_cls}">{"".join(cards)}</div></div></section>'


def render_split(block: dict) -> str:
    bullets = ''.join(f'<li>{escape(item)}</li>' for item in block['bullets'])
    return f'<section class="section muted"><div class="container split"><div class="split-copy"><p class="section-label">{escape(block["kicker"])}</p><h2>{escape(block["title"])}</h2><p>{escape(block["text"])}</p></div><div class="split-card"><ul class="mini-list">{bullets}</ul></div></div></section>'


def render_spotlight(page_path: str, block: dict) -> str:
    bullets = ''.join(f'<li>{escape(item)}</li>' for item in block.get('bullets', []))
    actions = ''
    for label, href, style in block.get('actions', []):
        cls = 'button primary' if style == 'primary' else 'button secondary'
        actions += f'<a class="{cls}" href="{href_from(page_path, href)}">{escape(label)}</a>'
    media = ''
    if block.get('image'):
        media = f'<div class="spotlight-media"><img src="{escape(block["image"])}" alt="{escape(block.get("image_alt", block["title"]))}" /></div>'
    return f'<section class="section"><div class="container"><div class="spotlight-wrap"><div class="spotlight-copy"><p class="section-label">{escape(block["kicker"])}</p><h2>{escape(block["title"])}</h2><p>{escape(block["text"])}</p><ul class="mini-list">{bullets}</ul><div class="button-row">{actions}</div></div>{media}</div></div></section>'


def render_metrics_band(block: dict) -> str:
    items = ''.join(f'<article class="metric"><strong>{escape(a)}</strong><span>{escape(b)}</span></article>' for a, b in block['items'])
    return f'<section class="section"><div class="container"><div class="metrics-grid">{items}</div></div></section>'


def render_story_cards(block: dict) -> str:
    variant = block.get('variant', '')
    items = []
    for idx, (a, b) in enumerate(block['items'], start=1):
        cls = 'story'
        badge = ''
        if variant == 'editorial' and idx == 1:
            cls += ' story-featured'
            badge = '<span class="story-kicker">Featured</span>'
        items.append(f'<article class="{cls}">{badge}<strong>{escape(a)}</strong><p>{escape(b)}</p></article>')
    grid_cls = 'story-grid' + (' story-grid-editorial' if variant == 'editorial' else '')
    return f'<section class="section"><div class="container"><p class="section-label">{escape(block["kicker"])}</p><div class="section-head"><h2>{escape(block["title"])}</h2><p></p></div><div class="{grid_cls}">{"".join(items)}</div></div></section>'


def render_quote_panel(block: dict) -> str:
    return f'<section class="section"><div class="container"><div class="quote-panel"><p class="section-label">{escape(block["kicker"])}</p><h2>{escape(block["title"])}</h2><p>{escape(block["text"])}</p></div></div></section>'


def render_timeline(block: dict) -> str:
    items = []
    for idx, step in enumerate(block['steps'], start=1):
        heading = f'Step {idx}'
        items.append(f'<article><span class="step-no">{idx}</span><h3>{heading}</h3><p>{escape(step)}</p></article>')
    return f'<section class="section muted"><div class="container"><p class="section-label">{escape(block["kicker"])}</p><div class="section-head"><h2>{escape(block["title"])}</h2><p>{escape(block["text"])}</p></div><div class="timeline">{"".join(items)}</div></div></section>'


def render_cta_strip(page_path: str, block: dict) -> str:
    p_label, p_href = block['primary']
    s_label, s_href = block['secondary']
    return f'<section class="section"><div class="container"><div class="cta-strip"><div class="cta-strip-copy"><h3>{escape(block["title"])}</h3><p>{escape(block["text"])}</p></div><div class="button-row"><a class="button primary" href="{href_from(page_path, p_href)}">{escape(p_label)}</a><a class="button secondary" href="{href_from(page_path, s_href)}">{escape(s_label)}</a></div></div></div></section>'


def render_content(page_path: str, blocks: list[dict]) -> str:
    out = []
    for block in blocks:
        t = block['type']
        if t == 'feature_grid':
            out.append(render_feature_grid(page_path, block))
        elif t == 'split':
            out.append(render_split(block))
        elif t == 'spotlight':
            out.append(render_spotlight(page_path, block))
        elif t == 'metrics_band':
            out.append(render_metrics_band(block))
        elif t == 'story_cards':
            out.append(render_story_cards(block))
        elif t == 'quote_panel':
            out.append(render_quote_panel(block))
        elif t == 'timeline':
            out.append(render_timeline(block))
        elif t == 'cta_strip':
            out.append(render_cta_strip(page_path, block))
    return '\n'.join(out)


def render_homepage_snippet_sections(page_path: str, cfg: dict) -> str:
    if page_path != 'index.html':
        return ''
    cards = ''.join(
        f'<article class="feature-service-card"><div class="feature-service-top"><div class="feature-service-icon">0{i+1}</div><h3>{escape(title)}</h3></div><div class="feature-service-body"><p>{escape(text)}</p><a href="{href_from(page_path, href)}">Read More →</a></div><div class="feature-service-bar"></div></article>'
        for i, (title, text, href) in enumerate(cfg.get('service_cards', []))
    )
    news = ''.join(
        f'<article class="news-card"><img src="{escape(img)}" alt="{escape(title)}" /><div class="news-card-copy"><h3>{escape(title)}</h3><p>{escape(text)}</p><a href="{href_from(page_path, href)}">Read More →</a></div></article>'
        for title, text, href, img in cfg.get('news_items', [])
    )
    return f'<section class="feature-services"><div class="container"><div class="feature-services-grid">{cards}</div></div></section><section class="section news-section"><div class="container"><div class="section-head"><h2>Latest Updates</h2><p>A more editorial presentation gives the homepage stronger movement and freshness while still supporting admissions and trust.</p></div><div class="news-grid">{news}</div></div></section>'

def schema_json(path: str, cfg: dict) -> str:
    data = {
        '@context': 'https://schema.org',
        '@type': 'CollegeOrUniversity' if path in ('index.html', 'about/index.html') else 'WebPage',
        'name': SITE['title'],
        'url': page_url(path),
        'description': cfg['description'],
    }
    if path == 'index.html':
        data['alternateName'] = 'SSE'
        data['email'] = SITE['email']
        data['address'] = {'@type': 'PostalAddress', 'addressRegion': 'Andhra Pradesh', 'addressCountry': 'IN'}
    return json.dumps(data, ensure_ascii=False)


def page_html(path: str, cfg: dict) -> str:
    prefix = rel_prefix(path)
    title_plain = cfg['title'].replace('|', '–')
    hero_stats = cfg.get('hero_stats', [('Puttaparthi', 'Sri Sathya Sai District campus'), ('Autonomous', 'Core institutional positioning'), ('Admissions 2026', 'Current student-intake framing'), ('3 routes', 'General, admissions, and placement contact paths')])
    stats_html = ''.join(f'<article><strong>{escape(a)}</strong><span>{escape(b)}</span></article>' for a, b in hero_stats)
    badges = ''.join(f'<span>{escape(item)}</span>' for item in cfg.get('hero_badges', []))
    highlights = cfg.get('highlights')
    highlight_html = ''
    if highlights:
        items = ''.join(f'<article><strong>{escape(a)}</strong><span>{escape(b)}</span></article>' for a, b in highlights)
        highlight_html = f'<section class="section"><div class="container"><div class="pillars">{items}</div></div></section>'
    return f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{escape(SITE['title'])} | {escape(cfg['title'])}</title>
    <meta name="description" content="{escape(cfg['description'])}" />
    <meta name="keywords" content="Sanskrithi School of Engineering, Sanskriti School of Engineering, engineering college, admissions 2026, placements, campus life, academics" />
    <meta property="og:title" content="{escape(SITE['title'])} | {escape(cfg['title'])}" />
    <meta property="og:description" content="{escape(cfg['description'])}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{escape(page_url(path))}" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="canonical" href="{escape(page_url(path))}" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="{prefix}styles.css" />
    <script type="application/ld+json">{schema_json(path, cfg)}</script>
  </head>
  <body class="page-shell page-{path.replace('/', '-').replace('.html', '').replace('index', 'overview')}">
    <header class="site-header">
      <div class="container nav-wrap">
        <a class="brand" href="{href_from(path, '/index.html')}">
          <img class="brand-mark" src="{escape(SITE['logo'])}" alt="{escape(SITE['title'])} logo" />
          <span>{escape(SITE['title'])}</span>
        </a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
          <span></span><span></span><span></span><span class="sr-only">Toggle navigation</span>
        </button>
        <nav class="nav" id="site-nav">{render_nav(path, cfg['section'])}</nav>
      </div>
    </header>

    <main>
      {'' if path == 'index.html' else f'<div class="container">{breadcrumbs(path, cfg['section'], title_plain)}</div>'}
      <section class="hero{' hero-home' if path == 'index.html' else ' hero-subpage'}"{f' style="--hero-image:url(\'{cfg.get("hero_image", "")}\')"' if cfg.get('hero_image') else ''}>
        <div class="container hero-layout">
          <div class="hero-copy">
            <p class="eyebrow">{escape(cfg['hero_kicker'])}</p>
            <h1>{escape(cfg['hero_title'])}</h1>
            <p class="lead">{escape(cfg['hero_text'])}</p>
            <div class="hero-actions">
              <a class="button primary" href="{href_from(path, '/admissions/index.html')}">Admissions</a>
              <a class="button secondary" href="{href_from(path, '/academics/index.html')}">Academics</a>
            </div>
            <div class="hero-badges">{badges}</div>
          </div>
          <aside class="hero-panel">
            <div class="panel-topline"></div>
            <div class="hero-stats">{stats_html}</div>
          </aside>
        </div>
      </section>

      {render_section_nav(path, cfg['section'])}
      {render_homepage_snippet_sections(path, cfg)}
      {highlight_html}
      {render_content(path, cfg['content'])}

      <section class="section">
        <div class="container cta-box">
          <div>
            <p class="section-label">Next Step</p>
            <h2>Ready to explore admissions, academics, placements, or campus life in more detail?</h2>
            <p>Explore the school through a clearer admissions, academics, campus, placements, and contact experience built around SSETP’s real strengths and published information.</p>
          </div>
          <div class="button-row">
            <a class="button primary light" href="mailto:{SITE['email']}">{SITE['email']}</a>
            <a class="button ghost" href="{href_from(path, '/contact.html')}">Contact page</a>
          </div>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="container footer-grid">
        <div>
          <h4>Our Office</h4>
          <p>{escape(SITE['title'])}<br/>{escape(SITE['address'])}<br/>Phone: {escape(SITE['phone'])}</p>
        </div>
        <div>
          <h4>Explore</h4>
          <ul><li><a href="{href_from(path, '/about/index.html')}">About</a></li><li><a href="{href_from(path, '/admissions/index.html')}">Admissions</a></li><li><a href="{href_from(path, '/academics/index.html')}">Academics</a></li></ul>
        </div>
        <div>
          <h4>Student Life</h4>
          <ul><li><a href="{href_from(path, '/campus/index.html')}">Campus Life</a></li><li><a href="{href_from(path, '/campus/hostel.html')}">Hostel</a></li><li><a href="{href_from(path, '/placements/index.html')}">Placements</a></li></ul>
        </div>
        <div>
          <h4>Contact</h4>
          <p>Admissions: <a href="mailto:{SITE['enquiry_email']}">{SITE['enquiry_email']}</a><br/>Placements / HR: <a href="mailto:{SITE['hr_email']}">{SITE['hr_email']}</a><br/>General: <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
        </div>
      </div>
      <div class="container footer-bottom">
        <p>© <span id="year"></span> {escape(SITE['title'])}. All rights reserved.</p>
        <p class="footer-note">Built around SSETP’s published structure, original visual assets, and a clearer admissions-first experience.</p>
      </div>
    </footer>

    <script src="{prefix}script.js"></script>
  </body>
</html>'''


(ROOT / 'styles.css').write_text(STYLE)
(ROOT / 'script.js').write_text(SCRIPT)
(ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://sseptp.org/sitemap.xml\n')

for path, cfg in PAGES.items():
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page_html(path, cfg))

sitemap_urls = '\n'.join(f'  <url><loc>{page_url(p)}</loc></url>' for p in PAGES)
(ROOT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap_urls}\n</urlset>\n')
print(f'Wrote {len(PAGES)} pages')
