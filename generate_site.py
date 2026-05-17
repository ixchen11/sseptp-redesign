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
        'hero_image': 'https://sseptp.org/assets/outside-CBfboUlb.jpg',
        'content': [
            {'type': 'spotlight', 'kicker': 'Institutional profile', 'title': 'SSETP brings location, leadership, recognition, and academic direction into one institutional story.', 'text': 'The published About material already covers mission, leadership, quality systems, and industry relevance. Grouped together, those pieces give a clearer picture of what the institution stands for.', 'image': 'https://sseptp.org/assets/ChairmanMessage-7pVMSzx5.jpg', 'image_alt': 'SSETP institutional leadership', 'bullets': ['Puttaparthi identity with a clear educational purpose', 'Autonomous positioning supported by visible quality signals', 'Leadership, NAAC, IQAC, and industry relevance in one narrative'], 'actions': [('View Vision & Mission', '/about/vision-mission.html', 'primary'), ('Quality & Recognition', '/about/quality.html', 'secondary')]},
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Inside About', 'title': 'The institutional story is grouped around the themes already published on the live site.', 'text': 'Mission, leadership, recognition, advisory structures, and quality systems are now easier to scan as one section.', 'cards': [
                ('Vision & Mission', 'The school’s published vision, mission, and student-development intent.', '/about/vision-mission.html'),
                ('Leadership', 'Chairman, Principal, and Secretary messages collected into one coherent section.', '/about/leadership.html'),
                ('Quality & Recognition', 'Autonomous status, AICTE / UGC recognition, NAAC, and IQAC context.', '/about/quality.html'),
                ('Industry Advisory', 'Board members and the industry-academia bridge described on the current site.', '/about/industry-interface.html'),
            ]},
            {'type': 'story_cards', 'variant': 'editorial', 'kicker': 'Institutional reading', 'title': 'Three recurring themes stand out across the published About pages.', 'items': [('Heritage', 'Puttaparthi provides the school’s place-based identity and context.'), ('Credibility', 'Recognition, NAAC, IQAC, and leadership are visible trust signals for students and parents.'), ('Direction', 'Industry relevance, global exposure, and student development recur throughout the institutional copy.')]},
        ],
    },
    'about/vision-mission.html': {
        'section': 'About',
        'title': 'Vision & Mission',
        'description': 'The published vision and mission of Sanskrithi School of Engineering, focused on dynamic, socially responsible engineers with wisdom, initiative, and character.',
        'hero_kicker': 'Vision & Mission',
        'hero_title': 'To develop dynamic and socially responsible engineers.',
        'hero_text': 'The existing SSETP site already articulates a specific educational intention: wisdom, positive attitude, character, innovation, initiative, teamwork, and the ability to respond to change.',
        'hero_image': 'https://sseptp.org/assets/ChairmanMessage-7pVMSzx5.jpg',
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
        'hero_title': 'Leadership messages add institutional voice and accountability.',
        'hero_text': 'The existing website already publishes Chairman, Principal, and Secretary-facing content. This section makes those voices easier to reach and easier to understand in context.',
        'hero_image': 'https://sseptp.org/assets/viceprincipal_directoradmissions-CY8iho05.jpeg',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Leadership voices', 'title': 'Three message pages now read as one coherent leadership layer.', 'text': 'Families want to know how the institution speaks for itself. These pages support that trust decision.', 'cards': [('Chairman Message', 'Institutional vision and educational direction.', '#'), ('Principal Message', 'Academic environment, standards, and student growth.', '#'), ('Secretary Message', 'Continuity, administration, and institutional support.', '#'), ('Shared purpose', 'Together these pages reinforce values, seriousness, and accountability.', '#')]},
            {'type': 'split', 'kicker': 'Why it helps', 'title': 'Leadership pages support trust for students, parents, and stakeholders.', 'text': 'Chairman, Principal, and Secretary messages make the institution’s voice, values, and accountability more visible.', 'bullets': ['Shows who leads the institution', 'Connects values to the student experience', 'Supports trust for parents and stakeholders', 'Adds substance beyond pure marketing copy']},
        ],
    },
    'about/quality.html': {
        'section': 'About',
        'title': 'Quality & Recognition',
        'description': 'Autonomous status, affiliation and recognition, NAAC accreditation, IQAC, and institutional quality signals at Sanskrithi School of Engineering.',
        'hero_kicker': 'Quality & Recognition',
        'hero_title': 'Recognition matters more when it is easy to verify.',
        'hero_text': 'SSE already shows a real quality framework: autonomous positioning, AICTE and UGC recognition, NAAC A Grade accreditation, and an IQAC structure aimed at continuous improvement.',
        'hero_image': 'https://sseptp.org/assets/awards-CZjWnbrq.jpg',
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
        'hero_title': 'Industry interface adds a visible bridge between academics and employers.',
        'hero_text': 'The current site names an Industry Advisory Board with members from RISE, TCS, CGI, HCLTech, Brillio, HP, Mphasis, and Capgemini. That published board gives this page clear institutional substance.',
        'hero_image': 'https://sseptp.org/assets/recruiters-B_A9F7qO.png',
        'content': [
            {'type': 'story_cards', 'kicker': 'What the page already proves', 'title': 'The board shows international linkage and employer relevance.', 'items': [('International connection', 'RISE-linked members strengthen the school’s global academic positioning.'), ('Employer relevance', 'Indian industry leaders help connect curriculum with market expectations.'), ('Academic bridge', 'The industry page supports the wider employability and placement story.')]},
            {'type': 'split', 'kicker': 'Functional role', 'title': 'Industry input appears here as curriculum, mentoring, and employability support.', 'text': 'The industry interface ties curriculum relevance, mentorship, guest talks, internships, and employability into one visible academic-support layer.', 'bullets': ['Curriculum relevance', 'Internships and guest sessions', 'Board-level external guidance', 'Stronger placement credibility']},
        ],
    },
    'admissions/index.html': {
        'section': 'Admissions',
        'title': 'Admissions Overview',
        'description': 'Admissions guidance for Sanskrithi School of Engineering with overview, process, fees, scholarship information, and direct enquiry routes.',
        'hero_kicker': 'Admissions',
        'hero_title': 'A clearer front door for students and families.',
        'hero_text': 'This section brings together overview, process, fees, scholarship support, and the real enquiry contacts already published by SSETP.',
        'hero_stats': [('2026', 'Admissions cycle surfaced prominently'), ('3', 'core enquiry mailboxes available'), ('1', 'clear admissions journey'), ('Puttaparthi', 'Campus destination now visible')],
        'hero_image': 'https://sseptp.org/assets/admission-Ca7U3rvN.jpg',
        'content': [
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Admissions routes', 'title': 'Overview, process, fees, and enquiry are now grouped into one admissions path.', 'text': 'Students and families usually need orientation, process, money clarity, and a direct human contact route.', 'cards': [('Admissions Overview', 'What SSE is, where it is, and why a student might shortlist it.', '/admissions/index.html'), ('Admission Process', 'A simplified step-by-step view for prospective students and families.', '/admissions/process.html'), ('Fees & Scholarship Support', 'Fee clarity plus Sai Prudent Scholarship visibility.', '/admissions/fees.html'), ('Enquiry', 'Direct access to enquiry@sseptp.org and institutional contact points.', '/admissions/enquiry.html')]},
            {'type': 'quote_panel', 'kicker': 'Why this matters', 'title': 'Good admissions structure reduces hesitation.', 'text': 'Parents and students can now move from orientation to process, support, and contact without jumping across unrelated pages.'},
        ],
    },
    'admissions/process.html': {
        'section': 'Admissions',
        'title': 'Admission Process',
        'description': 'Step-by-step admission journey for prospective students at Sanskrithi School of Engineering.',
        'hero_kicker': 'Admission Process',
        'hero_title': 'A simple process view removes unnecessary uncertainty.',
        'hero_text': 'This page turns admissions intent into a clean sequence so students and families know what to do next instead of guessing across multiple pages.',
        'hero_image': 'https://sseptp.org/assets/admission-Ca7U3rvN.jpg',
        'content': [
            {'type': 'timeline', 'kicker': 'How to move forward', 'title': 'A practical admissions sequence', 'text': 'The information architecture here follows the applicant journey from first enquiry to admission confirmation.', 'steps': ['Start with an enquiry or admissions conversation to identify the right program and route.', 'Review eligibility, required documents, and any counselling or admission guidance shared by the institution.', 'Submit documents and complete the formal admission steps for the selected program.', 'Confirm fees, onboarding instructions, and campus reporting before joining.']},
            {'type': 'cta_strip', 'title': 'Need help before applying?', 'text': 'For many students, the right next step is still a conversation.', 'primary': ('Send an enquiry', '/admissions/enquiry.html'), 'secondary': ('View fees', '/admissions/fees.html')},
        ],
    },
    'admissions/fees.html': {
        'section': 'Admissions',
        'title': 'Fees & Scholarships',
        'description': 'Admissions fee clarity and Sai Prudent Scholarship information at Sanskrithi School of Engineering.',
        'hero_kicker': 'Fees & Scholarships',
        'hero_title': 'Financial clarity sits beside student support on this page.',
        'hero_text': 'SSE already publishes the Sai Prudent Scholarship story. This page brings cost conversations and support visibility into the same admissions decision flow.',
        'hero_image': 'https://sseptp.org/assets/girlsStudying-CS9EcCsH.jpg',
        'content': [
            {'type': 'story_cards', 'kicker': 'Sai Prudent Scholarship', 'title': 'The existing scholarship story is already concrete.', 'items': [('Established in 2010', 'The scholarship is presented as a long-running support initiative.'), ('Supported by partners', 'The current site references Anahata Stiftung and RISE, Austria.'), ('Merit + need', 'The program is described for deserving students from economically disadvantaged backgrounds.')]},
            {'type': 'split', 'kicker': 'Fees & support', 'title': 'Students need both cost clarity and confidence that support exists.', 'text': 'This page connects fees, scholarship logic, and enquiry support so students and families can make decisions with more confidence.', 'bullets': ['Explain fee structure clearly', 'Show scholarship support prominently', 'Link questions to admissions contact', 'Reduce early uncertainty for families']},
        ],
    },
    'admissions/enquiry.html': {
        'section': 'Admissions',
        'title': 'Admissions Enquiry',
        'description': 'Admissions enquiry routes for Sanskrithi School of Engineering.',
        'hero_kicker': 'Admissions Enquiry',
        'hero_title': 'Admissions contact is direct, published, and easy to reach.',
        'hero_text': 'The page uses the institution’s real enquiry routes instead of treating contact as an afterthought.',
        'hero_image': 'https://sseptp.org/assets/outside-CBfboUlb.jpg',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Contact routes', 'title': 'Use the right route for the right question.', 'text': 'This page prioritizes response paths over decoration.', 'cards': [('Admissions Enquiry', 'enquiry@sseptp.org for student and parent admissions questions.', '#'), ('General Office', 'info@sseptp.org for broader institutional questions.', '#'), ('Phone Contact', '+91 9100064545 / 74545 for direct office contact.', '#'), ('Visit / Reach Campus', 'Puttaparthi, Sri Sathya Sai District, AP - 515134.', '#')]},
            {'type': 'quote_panel', 'kicker': 'Live contact data', 'title': 'enquiry@sseptp.org | info@sseptp.org | +91 9100064545 / 74545', 'text': 'The admissions contact layer uses the same published contact data across hero, body, and footer.'},
        ],
    },
    'academics/index.html': {
        'section': 'Academics',
        'title': 'Academics Overview',
        'description': 'Academics at Sanskrithi School of Engineering: departments, curriculum process, laboratories, scholarship support, and the RIT pathway.',
        'hero_kicker': 'Academics',
        'hero_title': 'Academic depth, practical learning, and curriculum governance in one place.',
        'hero_text': 'The live site explains that SSE continuously revises curriculum through departmental committees, Boards of Studies, and the Academic Council while strengthening labs, research, and industry readiness.',
        'hero_image': 'https://sseptp.org/assets/classroomStylish2-D-33iv0T.jpg',
        'hero_stats': [('6', 'engineering departments surfaced'), ('BoS', 'Board of Studies layer present in current copy'), ('DAC', 'Department Academic Committees referenced'), ('RIT', 'international academic differentiator')],
        'content': [
            {'type': 'spotlight', 'kicker': 'Featured pathway', 'title': 'RIT, laboratories, scholarship support, and curriculum governance define the academic picture.', 'text': 'SSETP already publishes clear academic proof points: curriculum governance, practical labs, student support, and the RIT pathway.', 'image': 'https://sseptp.org/assets/girlsStudying-CS9EcCsH.jpg', 'image_alt': 'Academic experience at SSETP', 'bullets': ['RIT pathway as a visible international software-engineering differentiator', 'Laboratories and curriculum review as practical academic proof', 'Scholarship support and departmental depth kept within the same academic journey'], 'actions': [('Explore RIT Pathway', '/academics/rit.html', 'primary'), ('View Programs', '/academics/programs.html', 'secondary')]},
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Academic structure', 'title': 'Programs, labs, support, and international pathways now read as one academic system.', 'text': 'The academic section combines undergraduate pathways, department-wise labs, scholarship support, and the RIT differentiator.', 'cards': [('Programs', 'Core departments and engineering pathways currently highlighted by SSE.', '/academics/programs.html'), ('Laboratories', 'Practical infrastructure across computing, electronics, civil, electrical, and mechanical domains.', '/academics/labs.html'), ('Sai Prudent Scholarship', 'Student support tied to progression and access.', '/academics/scholarships.html'), ('RIT Pathway', 'Software-engineering learning in cooperation with RISE and INSO.', '/academics/rit.html')]},
            {'type': 'split', 'kicker': 'Published academic process', 'title': 'Curriculum revision is part of the academic story.', 'text': 'The current SSETP copy explicitly references DACs, Boards of Studies, and the Academic Council. That governance detail signals structured academic review.', 'bullets': ['Departments review and discuss syllabus content', 'Board of Studies finalizes course structure and syllabus', 'Academic Council approves broader academic matters', 'Infrastructure and research are framed as part of academic quality']},
        ],
    },
    'academics/programs.html': {
        'section': 'Academics',
        'title': 'Programs',
        'description': 'B.Tech programmes, seats, eligibility, and academic pathways at Sanskrithi School of Engineering.',
        'hero_kicker': 'Programs',
        'hero_title': 'Five B.Tech programmes are presented here as distinct academic pathways.',
        'hero_text': 'The current SSETP site publishes five undergraduate engineering programmes with seats, eligibility, labs, course structure, and career outcomes. That published detail is carried into this page.',
        'hero_image': 'https://sseptp.org/assets/classroomStylish3-DMqiH9ca.jpg',
        'content': [],
    },
    'academics/labs.html': {
        'section': 'Academics',
        'title': 'Laboratory Facilities',
        'description': 'Laboratory infrastructure and practical learning environments at Sanskrithi School of Engineering.',
        'hero_kicker': 'Laboratory Facilities',
        'hero_title': 'Hands-on learning is one of the clearest academic proof points at SSE.',
        'hero_text': 'The live site presents a deep laboratory story across departments, from programming and networking labs to VLSI, manufacturing, structures, and power systems.',
        'hero_image': 'https://sseptp.org/assets/computerLabFocused-CXPA2eOi.jpg',
        'content': [
            {'type': 'story_cards', 'kicker': 'Examples from the live site', 'title': 'The published lab story already covers department-wise facilities.', 'items': [('CSE labs', 'Programming, databases, computer networks, and AI / machine learning are explicitly called out.'), ('ECE / EEE labs', 'Digital electronics, communication systems, VLSI, electrical machines, power systems, and control labs are part of the published story.'), ('Core engineering labs', 'Mechanical, civil, manufacturing, structural, geotechnical, and environmental labs broaden the practical picture.')]},
            {'type': 'split', 'kicker': 'Lab role', 'title': 'Practical infrastructure connects theory, experimentation, and project work.', 'text': 'The laboratory section now emphasizes department-specific facilities, experimentation, and project-readiness.', 'bullets': ['Department-specific facilities', 'Equipment and experimentation context', 'Practical relevance to curriculum', 'Research and project-readiness signals']},
        ],
    },
    'academics/scholarships.html': {
        'section': 'Academics',
        'title': 'Sai Prudent Scholarship',
        'description': 'Sai Prudent Scholarship support at Sanskrithi School of Engineering.',
        'hero_kicker': 'Student Support',
        'hero_title': 'Scholarship support is a visible part of the student journey.',
        'hero_text': 'The Sai Prudent Scholarship is one of the more concrete support stories on the current site and stays visible here from both academics and admissions.',
        'hero_image': 'https://sseptp.org/assets/Saipriya-Ca1D8LTw.jpeg',
        'content': [
            {'type': 'story_cards', 'kicker': 'Key facts', 'title': 'What the current site already states clearly.', 'items': [('Purpose', 'Support deserving students from economically disadvantaged backgrounds.'), ('Partners', 'Supported by Anahata Stiftung and RISE, Austria according to the current site.'), ('Selection logic', 'Academic merit, need, attendance, conduct, and participation are part of the eligibility story.')]},
            {'type': 'cta_strip', 'title': 'Need support or clarification?', 'text': 'Scholarship questions connect directly back to admissions and enquiry routes.', 'primary': ('Admissions enquiry', '/admissions/enquiry.html'), 'secondary': ('Contact SSE', '/contact.html')},
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
            {'type': 'feature_grid', 'kicker': 'Program structure', 'title': 'The current RIT page already has a usable four-module logic.', 'text': 'That structure is preserved here and made easier to understand through a clearer academic presentation.', 'cards': [('Module 1', 'Foundation setup: tools, communication habits, typing, and programming mindset.', '#'), ('Module 2', 'Programming basics with introductory Java problem solving.', '#'), ('Module 3', 'Advanced Java assignments with more depth and longer timelines.', '#'), ('Module 4', 'Software architecture, OOP, design patterns, SQLite, Git, and GitHub.', '#')]},
            {'type': 'story_cards', 'kicker': 'Why it matters', 'title': 'RIT strengthens SSE’s software-engineering identity.', 'items': [('International mentors', 'The live page names mentors connected to RISE and European universities.'), ('Practical focus', 'The program is assignment-heavy and problem-solving oriented.'), ('Career relevance', 'It gives CSE students a visible pathway beyond generic department copy.')]},
        ],
    },
    'campus/index.html': {
        'section': 'Campus Life',
        'title': 'Campus Life Overview',
        'description': 'Campus life, facilities, hostel, wellbeing, and student experience at Sanskrithi School of Engineering.',
        'hero_kicker': 'Campus Life',
        'hero_title': 'Campus pages help families picture daily student life beyond classrooms.',
        'hero_text': 'The current SSETP material covers accommodation, dining, facilities, student activities, and sports. This section brings those themes into one clearer student-life path.',
        'hero_image': 'https://sseptp.org/assets/campusGreenary-CPeVGuil.jpg',
        'content': [
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Student experience', 'title': 'Campus life is organized around facilities, hostel, wellbeing, and participation.', 'text': 'The live site already provides material on accommodation, dining, academic spaces, and sports.', 'cards': [('Facilities', 'Academic and support spaces that shape the day-to-day experience.', '/campus/facilities.html'), ('Hostel Life', 'Accommodation, dining, safety, and student community.', '/campus/hostel.html'), ('Health & Safety', 'Wellbeing, support, and trust signals for parents and students.', '/campus/health-safety.html'), ('Sports', 'Participation, energy, and campus-life balance.', '/campus/sports.html')]},
            {'type': 'quote_panel', 'kicker': 'Campus reading', 'title': 'Campus information helps families picture everyday student life.', 'text': 'Students do not choose only on academics. Families also want to see where a student will live, move, eat, and feel supported.'},
        ],
    },
    'campus/facilities.html': {
        'section': 'Campus Life',
        'title': 'Facilities',
        'description': 'Campus facilities at Sanskrithi School of Engineering.',
        'hero_kicker': 'Facilities',
        'hero_title': 'Facilities pages show the spaces students use every day.',
        'hero_text': 'The campus content points to academic spaces, accommodation support, common areas, dining, and connectivity. This page brings those facility stories together in one place.',
        'hero_image': 'https://sseptp.org/assets/LectureHall-C3cw9cxh.jpg',
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
        'hero_title': 'Hostel content answers the parental trust question directly.',
        'hero_text': 'The live site already gives hostel-specific detail on boys and girls blocks, common rooms, Wi-Fi, dining, security, activities, and rules.',
        'hero_image': 'https://sseptp.org/assets/HostelMenSSE-ktx82EVM.jpg',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Residential life', 'title': 'The current hostel story already has useful structure.', 'text': 'Specific details about accommodation, dining, common rooms, and rules help families evaluate residential life with more confidence.', 'cards': [('Accommodation', 'Separate hostel blocks, furnished rooms, and supervised residential arrangements.', '#'), ('Dining & Mess', 'Meal support, kitchen facilities, and dining-hall context are already part of the live copy.', '#'), ('Student Activities', 'Cultural events, sports, and hostel committees contribute to community life.', '#'), ('Safety & Rules', 'Security, timings, conduct, and support expectations matter to families.', '#')]},
            {'type': 'story_cards', 'kicker': 'Concrete points from the live content', 'title': 'The page already has trust-building detail.', 'items': [('24×7 security', 'Security is explicitly part of the current hostel presentation.'), ('Common spaces', 'Common rooms and shared facilities make the residential environment feel more real.'), ('Dining support', 'Mess and meal arrangements are already described, so they remain prominent here.')]},
        ],
    },
    'campus/health-safety.html': {
        'section': 'Campus Life',
        'title': 'Health & Safety',
        'description': 'Health, safety, and student wellbeing information at Sanskrithi School of Engineering.',
        'hero_kicker': 'Health & Safety',
        'hero_title': 'Wellbeing pages need calm clarity, not promotional noise.',
        'hero_text': 'The broader campus and hostel material already references medical support, first aid, security, and student rules. This page gives those concerns a dedicated place in the navigation.',
        'hero_image': 'https://sseptp.org/assets/studentCommonArea-C2A_66qp.jpg',
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
        'hero_title': 'Sports pages show a more balanced picture of student life.',
        'hero_text': 'Campus-life content is stronger when it shows that SSE is not only about classrooms and placements, but also about teamwork, participation, and student energy.',
        'hero_image': 'https://sseptp.org/assets/cricketSSE-DZl_BJbB.jpg',
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
        'hero_text': 'The current site already publishes strong placement evidence: 1675 total offers, 800 students placed, 150 recruiting companies, 36 LPA highest package, and 95% placement rate for 2024-25.',
        'hero_stats': [('1675', 'Total offers'), ('800', 'Students placed'), ('150', 'Recruiting companies'), ('36 LPA', 'Highest package')],
        'hero_image': 'https://sseptp.org/assets/techMahindra-Dl36r2aB.jpg',
        'content': [
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Placement section', 'title': 'Published numbers, recruiter visibility, and training routes are now grouped together.', 'text': 'SSE already has enough live material to present placements as a major institutional strength.', 'cards': [('Placement Highlights', 'Published numbers, recruiter relationships, and internship visibility.', '/placements/index.html'), ('Success Stories', 'Outcome-led examples framed without unnecessary filler.', '/placements/success-stories.html'), ('Placement Contact', 'CDC team, coordinators, and recruiter-facing routes.', '/placements/contact.html'), ('Training Readiness', 'Aptitude, technical, communication, and interview-prep support described on the current site.', '#')]},
            {'type': 'split', 'kicker': 'Placement narrative', 'title': 'The live copy already explains the student-readiness model.', 'text': 'SSE frames its placement cell as more than a recruitment desk: it starts early, shapes readiness, and connects training with market expectations.', 'bullets': ['Training starts from the second year', 'Technical, aptitude, and communication preparation are all emphasized', 'Recruiter trust is reinforced visually through company visibility', 'The CDC team is visible and reachable']},
        ],
    },
    'placements/success-stories.html': {
        'section': 'Placements',
        'title': 'Success Stories',
        'description': 'Placement outcome snapshots at Sanskrithi School of Engineering.',
        'hero_kicker': 'Success Stories',
        'hero_title': 'Outcome pages work best when they stay close to evidence.',
        'hero_text': 'This page extends the published placement performance and recruiter ecosystem without inventing fictional student profiles.',
        'hero_image': 'https://sseptp.org/assets/recruiters-B_A9F7qO.png',
        'content': [
            {'type': 'story_cards', 'kicker': 'Outcome lens', 'title': 'Three published placement signals carry this page.', 'items': [('High-value offers', 'The current site already highlights strong top-end packages.'), ('Broad recruiter base', 'The number of recruiting companies signals scale, not just a few standout cases.'), ('Training-to-offer logic', 'Success stories connect back to the placement training model instead of reading like isolated testimonials.')]},
            {'type': 'metrics_band', 'items': [('95%', 'placement rate'), ('1500', 'internship offers'), ('2', 'international offers'), ('7.5 LPA', 'average package highlighted')]},
        ],
    },
    'placements/contact.html': {
        'section': 'Placements',
        'title': 'Placement Contact',
        'description': 'Training & Placement / CDC contact routes at Sanskrithi School of Engineering.',
        'hero_kicker': 'Placement Contact',
        'hero_title': 'Recruiter and placement contact is easy to find here.',
        'hero_text': 'The current site already names members of the CDC / Training & Placement team including Kiran Ravi Srivastava, Dr. Bala Koteswari, and Rakesh Yadav Kodari.',
        'hero_image': 'https://sseptp.org/assets/placement-D9x0hLK2.jpg',
        'content': [
            {'type': 'story_cards', 'kicker': 'Published team visibility', 'title': 'The live site already gives this page strong raw material.', 'items': [('CDC Head', 'Ms. Kiran Ravi Srivastava is named as CDC – Head.'), ('Coordinators', 'Dr. Bala Koteswari and Mr. Rakesh Yadav Kodari are visible as coordinators.'), ('Training layer', 'The team structure supports the broader placement-readiness narrative.')]},
            {'type': 'cta_strip', 'title': 'Need the placements mailbox?', 'text': 'Recruiters and career-related queries are routed clearly to the team here.', 'primary': ('Contact page', '/contact.html'), 'secondary': ('Placement overview', '/placements/index.html')},
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
        'hero_image': 'https://sseptp.org/assets/campusRoad-CeUGNEHg.jpg',
        'content': [
            {'type': 'spotlight', 'kicker': 'Start here', 'title': 'Admissions, general office, and placements each use distinct published contact routes.', 'text': 'Students, parents, recruiters, and institutional visitors can reach the right route without scanning through generic information blocks.', 'image': 'https://sseptp.org/assets/LectureHall-C3cw9cxh.jpg', 'image_alt': 'SSETP campus and enquiry routes', 'bullets': ['Admissions: enquiry@sseptp.org for prospective students and parents', 'General: info@sseptp.org for institutional questions', 'Placements / HR: hr@sseptp.org for recruiter and career-related contact'], 'actions': [('Send Admissions Enquiry', '/admissions/enquiry.html', 'primary'), ('View Placements', '/placements/index.html', 'secondary')]},
            {'type': 'feature_grid', 'variant': 'showcase', 'kicker': 'Contact paths', 'title': 'Choose the right route quickly.', 'text': 'The page now prioritizes the actual next action: mail, call, or visit.', 'cards': [('Admissions', 'enquiry@sseptp.org for prospective-student and parent conversations.', '#'), ('General Office', 'info@sseptp.org for institutional and broad enquiries.', '#'), ('Placements / HR', 'hr@sseptp.org for recruiter and placement-related questions.', '#'), ('Call or Visit', '+91 9100064545 / 74545 | Puttaparthi, Sri Sathya Sai District, AP - 515134', '#')]},
            {'type': 'split', 'kicker': 'Social presence', 'title': 'The institution already publishes its main public channels.', 'text': 'Alongside social channels, the primary user need remains fast, trustworthy institutional contact.', 'bullets': ['Facebook: sseptp', 'X: SanskrithiGroup', 'Instagram: sanskrithigroup_ptp', 'Address and phone remain the primary trust anchors']},
        ],
    },

}

STYLE = r'''
:root{--navy:#001A3D;--navy-2:#0d2d61;--navy-3:#173d7d;--orange:#f26522;--orange-2:#ff8c42;--orange-3:#ffd2ad;--ink:#162230;--muted:#64748b;--line:rgba(0,26,61,.1);--surface:#ffffff;--surface-2:#f8fbff;--surface-3:#fff7ef;--shadow-xl:0 28px 80px rgba(0,26,61,.16);--shadow-lg:0 18px 42px rgba(0,26,61,.10);--radius-xl:30px;--radius-lg:22px;--radius-md:16px;--container:1180px}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,system-ui,sans-serif;color:var(--ink);background:linear-gradient(180deg,#fffaf6 0%,#fff 16%,#f8fbff 100%);line-height:1.68;overflow-x:hidden}img{display:block;max-width:100%}a{-webkit-tap-highlight-color:transparent}.container{width:min(calc(100% - 2rem),var(--container));margin:0 auto}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.site-header{position:sticky;top:0;z-index:80;background:var(--navy);color:#fff;box-shadow:0 10px 24px rgba(0,0,0,.08)}.nav-wrap,.footer-wrap,.section-head,.hero-actions,.button-row,.cta-box,.breadcrumb{display:flex;gap:1rem}.nav-wrap,.footer-wrap,.cta-box{align-items:center;justify-content:space-between}.nav-wrap{min-height:80px}.brand{display:inline-flex;align-items:center;gap:.9rem;color:#fff;text-decoration:none;font-weight:800;letter-spacing:-.04em}.brand span:last-child{max-width:20rem}.brand-mark{display:block;width:3rem;height:3rem;object-fit:contain;filter:drop-shadow(0 10px 24px rgba(242,101,34,.18))}.nav{display:flex;align-items:center;gap:.15rem;flex-wrap:wrap}.nav-link,.nav-parent{text-decoration:none;color:rgba(255,255,255,.92);font-weight:700;padding:1.2rem 1rem;position:relative;display:inline-flex;align-items:center;gap:.45rem;background:transparent;border:none;font:inherit;cursor:pointer}.nav-link.active,.nav-link:hover,.nav-item.active>.nav-parent,.nav-item:hover>.nav-parent,.nav-item.is-open>.nav-parent{color:#fff;background:rgba(255,255,255,.08)}.nav-link.active,.nav-item.active>.nav-parent{background:var(--orange)}.nav-item{position:relative}.nav-caret{font-size:.8rem;opacity:.72}.nav-menu{position:absolute;top:calc(100% + .35rem);left:0;min-width:280px;padding:.8rem;display:grid;gap:.45rem;background:#fff;border:1px solid rgba(0,26,61,.08);border-radius:18px;box-shadow:var(--shadow-xl);opacity:0;pointer-events:none;transform:translateY(8px);transition:opacity .18s ease,transform .18s ease}.nav-item.is-open>.nav-menu{opacity:1;pointer-events:auto;transform:translateY(0)}.nav-menu-link{display:grid;gap:.2rem;padding:.85rem .95rem;border-radius:14px;color:var(--ink);text-decoration:none}.nav-menu-link strong{font-size:.98rem;color:var(--navy)}.nav-menu-link small{color:var(--muted);line-height:1.4}.nav-menu-link:hover,.nav-menu-link.active{background:linear-gradient(180deg,#fff4e8,#fff)}.nav-cta{margin-left:.5rem;padding:1rem 1rem !important;border-radius:12px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12)}.nav-cta:hover{background:rgba(255,255,255,.16) !important}.nav-toggle{display:none;flex-direction:column;justify-content:center;gap:.26rem;width:2.9rem;height:2.9rem;border:1px solid rgba(255,255,255,.14);border-radius:14px;background:transparent;cursor:pointer}.nav-toggle span:not(.sr-only){display:block;width:1.1rem;height:2px;margin:0 auto;background:#fff}
.hero{position:relative;overflow:clip;padding:4.4rem 0 3.8rem;background:radial-gradient(circle at 100% 0,rgba(242,116,5,.18),transparent 30%),radial-gradient(circle at 0 20%,rgba(23,61,125,.10),transparent 24%),linear-gradient(180deg,#fff2e5 0%,#fff8f2 38%,#fff 72%,#f8fbff 100%)}.hero:before{content:'';position:absolute;right:-8rem;top:-6rem;width:22rem;height:22rem;border-radius:50%;background:radial-gradient(circle,rgba(255,155,61,.18),transparent 65%);filter:blur(10px)}.hero-layout{display:grid;grid-template-columns:minmax(0,1.02fr) minmax(340px,.98fr);gap:2.6rem;align-items:center}.eyebrow,.section-label{display:inline-flex;align-items:center;gap:.5rem;margin:0 0 1rem;color:var(--orange);font-size:.8rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase}.eyebrow:before,.section-label:before{content:'';width:1.2rem;height:2px;border-radius:999px;background:linear-gradient(90deg,var(--orange),var(--orange-2))}h1,h2,h3,p,ul{margin-top:0}h1{margin-bottom:1.15rem;font-size:clamp(2.8rem,7vw,5.2rem);line-height:.95;letter-spacing:-.065em;max-width:11ch}h2{margin-bottom:1rem;font-size:clamp(2rem,4vw,3.1rem);line-height:1.04;letter-spacing:-.05em}h3{margin-bottom:.7rem;font-size:1.2rem;letter-spacing:-.03em}.lead,.section-head p,.card p,.split-copy p,.story p,.footer-note,.hero-badges span,.hero-stats span,.breadcrumb a,.breadcrumb span,.section-nav-shell small{color:var(--muted)}.hero-copy{position:relative;z-index:1}.hero-actions{flex-wrap:wrap;margin:2rem 0 1.4rem}.button{display:inline-flex;align-items:center;justify-content:center;min-height:52px;padding:0 1.25rem;border-radius:999px;text-decoration:none;font-weight:800;transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease,background .2s ease}.button:hover{transform:translateY(-1px)}.button.primary{background:linear-gradient(135deg,var(--orange) 0%,#d66704 100%);color:#fff;box-shadow:0 14px 30px rgba(242,116,5,.24)}.button.secondary,.button.ghost{background:#fff;border:1px solid var(--line);color:var(--ink)}.button.light{background:#fff;color:var(--navy)}.hero-badges{display:flex;gap:.7rem;flex-wrap:wrap}.hero-badges span{padding:.72rem .95rem;border-radius:999px;background:rgba(255,255,255,.82);border:1px solid rgba(0,26,61,.08);font-weight:700}.hero-panel,.card,.split-card,.story,.timeline article,.cta-box,.metric,.pillars article,.spotlight{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-xl);box-shadow:var(--shadow-lg)}.hero-panel{padding:1.4rem;background:linear-gradient(180deg,var(--navy) 0%,var(--navy-2) 78%,var(--navy-3) 100%);color:#fff;box-shadow:var(--shadow-xl)}.panel-topline{height:10px;width:42%;border-radius:999px;background:linear-gradient(90deg,var(--orange),var(--orange-2));margin-bottom:1.2rem}.hero-stats,.cards,.timeline,.pillars,.story-grid,.metrics-grid,.section-nav-shell{display:grid;gap:1rem}.hero-stats{grid-template-columns:repeat(2,minmax(0,1fr))}.hero-stats article{padding:1.15rem;border:1px solid rgba(255,255,255,.14);border-radius:18px;background:rgba(255,255,255,.06);backdrop-filter:blur(8px)}.hero-stats strong{display:block;margin-bottom:.35rem;font-size:1.55rem}.breadcrumb{align-items:center;flex-wrap:wrap;padding:1rem 0 0}.breadcrumb a{text-decoration:none}.section-nav{margin-top:-1.3rem;position:relative;z-index:3}.section-nav-panel{border-radius:18px;overflow:hidden;box-shadow:0 10px 25px -5px rgba(0,0,0,.1),0 8px 10px -6px rgba(0,0,0,.1);border-top:4px solid var(--orange);background:#fff}.section-nav-heading{padding:1rem 1.25rem;background:linear-gradient(180deg,#fff,#fff7ef);font-weight:800;color:var(--navy);border-bottom:1px solid rgba(0,26,61,.08)}.section-nav-shell{grid-template-columns:repeat(5,minmax(0,1fr));padding:1.1rem}.section-link{display:flex;flex-direction:column;gap:.24rem;padding:1rem 1rem;border-radius:14px;text-decoration:none;color:var(--ink);background:#fff;border:1px solid transparent;min-height:102px;justify-content:center}.section-link.is-active{background:linear-gradient(180deg,#fff3e7,#fff);border-color:rgba(242,116,5,.24);box-shadow:inset 0 0 0 1px rgba(242,116,5,.08)}.section-link:hover{transform:translateY(-1px);border-color:rgba(242,116,5,.18);background:linear-gradient(180deg,#fff8f1,#fff)}.section-nav-shell strong{font-size:1rem;color:var(--navy)}.section-nav-shell small{font-size:.88rem;line-height:1.45}.hero-subpage{padding-top:3.5rem;padding-bottom:3rem}.hero-subpage .hero-layout{grid-template-columns:minmax(0,1fr) minmax(300px,.72fr)}.hero-subpage{background:linear-gradient(rgba(255,248,242,.92),rgba(248,251,255,.96)),var(--hero-image) center/cover no-repeat}.hero-subpage .hero-copy{background:rgba(255,255,255,.72);border:1px solid rgba(0,26,61,.08);box-shadow:var(--shadow-lg);border-radius:28px;padding:2rem}.hero-subpage .hero-panel{background:linear-gradient(180deg,#fff 0%,#f8fbff 100%);color:var(--ink)}.hero-subpage .hero-stats article{background:linear-gradient(180deg,#fff8f1,#fff);border-color:rgba(0,26,61,.08)}.hero-subpage .hero-stats span{color:var(--muted)}.section{padding:4.6rem 0}.section-head{align-items:end;justify-content:space-between;margin-bottom:1.9rem}.section-head>*{flex:1}.cards.cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.cards.cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.cards.cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.card,.split-card,.story,.timeline article,.metric,.spotlight{padding:1.55rem}.card{position:relative;overflow:hidden;background:linear-gradient(180deg,#fff 0%,#fbfdff 100%);transition:transform .2s ease,box-shadow .2s ease}.card:hover{transform:translateY(-3px);box-shadow:0 24px 44px rgba(0,26,61,.12)}.card:after{content:'';position:absolute;right:-2.5rem;bottom:-2.5rem;width:7rem;height:7rem;border-radius:50%;background:rgba(242,116,5,.10)}.card a{font-weight:800;color:var(--navy);text-decoration:none}.cards-showcase .card-featured{grid-column:span 2;background:linear-gradient(135deg,#fff 0%,#fff4e8 55%,#eef6ff 100%);border-top:4px solid var(--orange);box-shadow:0 26px 50px rgba(0,26,61,.12)}.cards-showcase .card-featured h3{font-size:1.5rem}.cards-showcase .card-featured p{max-width:42ch}.icon{display:inline-grid;place-items:center;width:3rem;height:3rem;margin-bottom:1rem;border-radius:16px;background:linear-gradient(135deg,#fff0e2,#ffe0c0);color:var(--orange);font-weight:800}.split{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2rem;align-items:center}.split-card{background:linear-gradient(180deg,#fff8f0 0%,#fff 100%);border-top:4px solid var(--orange)}.mini-list{margin:1rem 0 0;padding-left:1.15rem}.mini-list li+li{margin-top:.45rem}.metrics-grid{grid-template-columns:repeat(4,minmax(0,1fr))}.metric{text-align:center;background:linear-gradient(180deg,#fff7ef 0%,#fff 100%);border-top:4px solid rgba(242,116,5,.72)}.metric strong{display:block;font-size:2rem;letter-spacing:-.04em;color:var(--navy)}.timeline{grid-template-columns:repeat(4,minmax(0,1fr))}.timeline article{background:linear-gradient(180deg,#fff 0%,#f8fbff 100%);border-top:4px solid rgba(0,26,61,.08)}.step-no{display:inline-grid;place-items:center;width:2.35rem;height:2.35rem;margin-bottom:1rem;border-radius:999px;background:var(--navy);color:#fff;font-weight:800}.story-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.story-grid-editorial .story-featured{grid-column:span 2;background:linear-gradient(135deg,#0d1c2f 0%,#173d7d 100%);color:#fff;border-top:none;box-shadow:var(--shadow-xl)}.story-grid-editorial .story-featured strong,.story-grid-editorial .story-featured p{color:#fff}.story-kicker{display:inline-flex;margin-bottom:.8rem;padding:.35rem .7rem;border-radius:999px;background:rgba(255,255,255,.14);font-size:.78rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}.story{background:linear-gradient(180deg,#fff 0%,#fff9f4 100%);border-top:4px solid rgba(242,116,5,.72)}.story strong{display:block;margin-bottom:.45rem;color:var(--navy)}.quote-panel{padding:2rem;border-radius:var(--radius-xl);background:linear-gradient(135deg,var(--navy) 0%,var(--navy-2) 66%,var(--navy-3) 100%);color:#fff;box-shadow:var(--shadow-xl)}.quote-panel p,.quote-panel .section-label{color:rgba(255,255,255,.82)}.quote-panel h2{color:#fff;max-width:18ch}.spotlight-wrap{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(280px,.95fr);gap:1.5rem;align-items:stretch;padding:1.4rem;border:1px solid rgba(242,116,5,.16);border-radius:var(--radius-xl);background:linear-gradient(135deg,#fff 0%,#fff6ee 52%,#f5f9ff 100%);box-shadow:var(--shadow-lg)}.spotlight-copy{padding:1rem}.spotlight-media{position:relative;min-height:320px;border-radius:24px;overflow:hidden}.spotlight-media img{width:100%;height:100%;object-fit:cover}.cta-strip{padding:1.4rem 1.5rem;border-radius:var(--radius-lg);background:linear-gradient(180deg,#fff4e8 0%,#fff 100%);border:1px solid rgba(242,116,5,.18);display:flex;gap:1rem;justify-content:space-between;align-items:center}.cta-strip-copy{max-width:46rem}.pillars{grid-template-columns:repeat(3,minmax(0,1fr))}.pillars article{padding:1.35rem 1.4rem;background:linear-gradient(180deg,#fff 0%,#fff8f1 100%)}.pillars strong{display:block;margin-bottom:.3rem;color:var(--navy)}.cta-box{padding:2rem;background:linear-gradient(135deg,var(--navy) 0%,var(--navy-2) 62%,var(--navy-3) 100%);color:#fff;box-shadow:var(--shadow-xl)}.cta-box .section-label,.cta-box h2,.cta-box p,.cta-box .button.ghost{color:#fff}.cta-box .button.ghost{border-color:rgba(255,255,255,.24);background:transparent}.site-footer{padding:1.7rem 0 2.3rem;border-top:1px solid rgba(0,26,61,.08)}.footer-wrap p{margin:0}.muted{background:linear-gradient(180deg,#fff8f1 0%,#fff 100%)}

.hero-home{min-height:560px;display:flex;align-items:center}.hero-home:after{content:'';position:absolute;inset:0;background:linear-gradient(rgba(0,26,61,.58),rgba(0,26,61,.54)),var(--hero-image) center/cover no-repeat;z-index:0}.hero-home .container,.hero-home .hero-copy,.hero-home .hero-panel{position:relative;z-index:1}.hero-home .hero-copy h1,.hero-home .hero-copy .lead,.hero-home .hero-copy .eyebrow,.hero-home .hero-badges span{color:#fff}.hero-home .eyebrow:before{background:linear-gradient(90deg,#fff,var(--orange-2))}.hero-home .hero-badges span{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.16)}.hero-about:after,.hero-academics:after,.hero-contact:after,.hero-admissions:after,.hero-campus:after,.hero-placements:after{content:'';position:absolute;inset:0;z-index:0}.hero-about:after{background:linear-gradient(90deg,rgba(8,19,37,.82) 0%,rgba(8,19,37,.58) 46%,rgba(8,19,37,.18) 100%),var(--hero-image) center/cover no-repeat}.hero-academics:after{background:linear-gradient(90deg,rgba(13,28,47,.82) 0%,rgba(13,28,47,.5) 52%,rgba(13,28,47,.3) 100%),var(--hero-image) center/cover no-repeat}.hero-contact:after{background:linear-gradient(180deg,rgba(13,28,47,.76),rgba(13,28,47,.58)),var(--hero-image) center/cover no-repeat}.hero-admissions:after{background:linear-gradient(90deg,rgba(27,16,4,.78) 0%,rgba(27,16,4,.48) 48%,rgba(27,16,4,.18) 100%),var(--hero-image) center/cover no-repeat}.hero-campus:after{background:linear-gradient(90deg,rgba(10,28,41,.78) 0%,rgba(10,28,41,.48) 50%,rgba(10,28,41,.2) 100%),var(--hero-image) center/cover no-repeat}.hero-placements:after{background:linear-gradient(90deg,rgba(0,26,61,.82) 0%,rgba(0,26,61,.56) 52%,rgba(0,26,61,.24) 100%),var(--hero-image) center/cover no-repeat}.hero-editorial,.hero-immersive,.hero-contact-shell{position:relative;z-index:1}.hero-editorial{min-height:600px;display:grid;grid-template-columns:minmax(0,1.08fr) minmax(280px,.7fr);gap:2rem;align-items:end}.hero-editorial .hero-copy,.hero-immersive .hero-copy,.hero-contact-shell .hero-copy{padding:3rem 0;color:#fff}.hero-editorial .hero-copy .lead,.hero-immersive .hero-copy .lead,.hero-contact-shell .hero-copy .lead,.hero-editorial .eyebrow,.hero-immersive .eyebrow,.hero-contact-shell .eyebrow{color:#fff}.hero-editorial .eyebrow:before,.hero-immersive .eyebrow:before,.hero-contact-shell .eyebrow:before{background:linear-gradient(90deg,#fff,var(--orange-2))}.hero-editorial-card{margin-bottom:2rem;padding:1.35rem;border-radius:24px;background:rgba(255,255,255,.9);box-shadow:var(--shadow-xl)}.hero-card-label{margin:0 0 .7rem;color:var(--orange);font-size:.82rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase}.hero-card-metrics{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.85rem;margin-top:1rem}.hero-card-metrics article{padding:1rem;border-radius:16px;background:linear-gradient(180deg,#fff8f1,#fff);border:1px solid rgba(0,26,61,.08)}.hero-card-metrics strong{display:block;margin-bottom:.35rem;font-size:1.3rem;color:var(--navy)}.hero-immersive{min-height:620px;display:flex;align-items:center}.hero-immersive .hero-badges span{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.14);color:#fff}.hero-contact-shell{min-height:430px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}.contact-badges{justify-content:center;max-width:54rem}
.about-story-grid,.academic-spotlight,.contact-layout,.admissions-flow,.placements-band{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2rem;align-items:center}.about-portrait-wrap{position:relative}.about-portrait{width:100%;min-height:460px;object-fit:cover;border-radius:28px;box-shadow:var(--shadow-xl)}.portrait-caption{position:absolute;right:1rem;bottom:1rem;display:grid;gap:.25rem;padding:1rem 1.1rem;border-radius:18px;background:rgba(255,255,255,.92);box-shadow:var(--shadow-lg)}.portrait-caption strong{color:var(--navy)}.about-story-copy blockquote{margin:1.2rem 0;padding-left:1rem;border-left:4px solid var(--orange);font-size:1.25rem;line-height:1.5;color:var(--navy)}.about-quality-grid .card-featured{grid-column:span 1}.about-links{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:2rem;align-items:start}.about-link-list{display:grid;gap:1rem}.about-link-list a{display:grid;gap:.35rem;padding:1.1rem 1.2rem;border-radius:20px;background:linear-gradient(180deg,#fff8f1,#fff);border:1px solid rgba(0,26,61,.08);text-decoration:none;color:var(--ink);box-shadow:var(--shadow-lg)}.about-link-list strong{color:var(--navy)}.academic-spotlight-media img{width:100%;min-height:420px;object-fit:cover;border-radius:28px;box-shadow:var(--shadow-xl)}.academic-spotlight-copy{padding:1rem 0}.text-link{display:inline-block;margin-top:1rem;color:var(--orange);font-weight:800;text-decoration:none}.governance-band{display:grid;grid-template-columns:minmax(0,1fr) minmax(280px,.95fr);gap:1.5rem;align-items:start}.governance-list{display:grid;gap:1rem}.governance-list article,.contact-card,.contact-panel{padding:1.35rem;border-radius:22px;background:#fff;border:1px solid rgba(0,26,61,.08);box-shadow:var(--shadow-lg)}.governance-list strong{display:block;margin-bottom:.3rem;color:var(--navy);font-size:1.1rem}.contact-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.2rem}.contact-card a{color:var(--navy);font-weight:700;text-decoration:none}.contact-panel h3{margin-bottom:.75rem;color:var(--navy)}
.feature-services{margin-top:-5.5rem;position:relative;z-index:5;padding-bottom:1rem}.feature-services-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.5rem}.feature-service-card{display:flex;flex-direction:column;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.08);min-height:100%}.feature-service-top{background:var(--navy);padding:2.2rem 1.8rem;text-align:center;color:#fff}.feature-service-top h3{margin:0;color:#fff}.feature-service-icon{width:4rem;height:4rem;border-radius:999px;margin:0 auto 1rem;display:grid;place-items:center;background:rgba(255,255,255,.08);color:var(--orange);font-weight:800;border:1px solid rgba(255,255,255,.14)}.feature-service-body{padding:1.8rem;text-align:center;flex:1}.feature-service-body a{color:var(--orange);font-weight:800;text-decoration:none}.feature-service-bar{height:.45rem;background:var(--orange)}
.news-section{background:#fff}.news-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2rem}.news-card{display:flex;gap:1.25rem;align-items:flex-start;padding:1rem;border-radius:18px;transition:background .2s ease}.news-card:hover{background:#fff8f1}.news-card img{width:12rem;height:9rem;object-fit:cover;border-radius:14px;box-shadow:0 8px 20px rgba(0,0,0,.08)}.news-card-copy h3{margin-bottom:.45rem;color:var(--navy)}.news-card-copy a{color:var(--orange);font-weight:800;text-decoration:none}
.site-footer{background:var(--navy);color:#fff;padding:4.5rem 0 2rem;border-top:none}.footer-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:2rem;margin-bottom:2.5rem}.footer-grid h4{margin:0 0 1rem;color:rgba(255,255,255,.76);text-transform:uppercase;letter-spacing:.08em;font-size:.95rem}.footer-grid p,.footer-grid a,.footer-grid li{color:rgba(255,255,255,.72);text-decoration:none;list-style:none}.footer-grid ul{margin:0;padding:0;display:grid;gap:.65rem}.footer-grid a:hover{color:#fff}.footer-bottom{padding-top:1.4rem;border-top:1px solid rgba(255,255,255,.1);display:flex;justify-content:space-between;gap:1rem;align-items:center}.footer-bottom p{margin:0}.site-footer .footer-note{color:rgba(255,255,255,.56)}

@media (max-width:1100px){.hero-layout,.split,.metrics-grid,.timeline,.story-grid,.pillars,.cards.cols-4,.cards.cols-3,.feature-services-grid,.footer-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.section-nav-shell{grid-template-columns:repeat(2,minmax(0,1fr))}.news-grid{grid-template-columns:1fr}}
@media (max-width:900px){.container{width:min(calc(100% - 1.5rem),var(--container))}.nav-toggle{display:inline-flex}.nav{position:absolute;top:calc(100% + .75rem);right:.75rem;left:.75rem;display:none;flex-direction:column;align-items:stretch;padding:.9rem;max-height:calc(100vh - 110px);overflow:auto;overflow-x:hidden;border:1px solid rgba(255,255,255,.08);border-radius:18px;background:rgba(13,45,97,.98);backdrop-filter:blur(12px);box-shadow:var(--shadow-xl)}.nav.is-open{display:flex}.nav-link,.nav-parent{width:100%;min-width:0;justify-content:space-between;padding:1rem;border-radius:12px;color:#fff}.nav-item{width:100%;max-width:100%;min-width:0;display:block}.nav-menu{position:static!important;left:auto!important;right:auto!important;top:auto!important;min-width:0!important;width:100%!important;max-width:100%!important;padding:.45rem .25rem 0;background:transparent;border:none;box-shadow:none;display:none;flex-direction:column;gap:.45rem;opacity:1;pointer-events:auto;transform:none!important;overflow:hidden}.nav-item.is-open>.nav-menu{display:flex}.nav-menu-link{display:flex!important;flex-direction:column!important;align-items:flex-start;width:100%!important;max-width:100%!important;min-width:0!important;white-space:normal!important;word-break:break-word;overflow-wrap:anywhere;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.08);color:#fff}.nav-menu-link strong,.nav-menu-link small{display:block;max-width:100%;white-space:normal!important;word-break:break-word;overflow-wrap:anywhere}.nav-menu-link strong{color:#fff}.nav-menu-link small{color:rgba(255,255,255,.72)}.nav-menu-link:hover,.nav-menu-link.active{background:rgba(242,101,34,.18);border-color:rgba(242,101,34,.45)}.nav-menu-link.active strong,.nav-menu-link:hover strong{color:#fff}.nav-menu-link.active small,.nav-menu-link:hover small{color:rgba(255,255,255,.82)}.nav-cta{margin-left:0}.hero{padding:3.75rem 0 3.15rem}.hero-layout,.split,.section-head,.cta-strip,.cta-box,.footer-bottom,.spotlight-wrap,.about-story-grid,.academic-spotlight,.contact-layout,.about-links,.governance-band,.hero-editorial,.admissions-flow,.placements-band{grid-template-columns:1fr;flex-direction:column;align-items:flex-start}.hero-stats,.metrics-grid,.timeline,.story-grid,.pillars,.cards.cols-4,.cards.cols-3,.cards.cols-2,.feature-services-grid,.footer-grid,.cards-showcase,.story-grid-editorial,.contact-grid,.hero-card-metrics{grid-template-columns:1fr}.cards-showcase .card-featured,.story-grid-editorial .story-featured{grid-column:span 1}.hero-subpage .hero-copy{padding:1.4rem;border-radius:22px}.hero-stats{grid-template-columns:repeat(2,minmax(0,1fr))}.section{padding:3.6rem 0}.feature-services{margin-top:-1.5rem}.feature-service-card,.card,.story,.split-card,.timeline article,.metric,.cta-strip,.spotlight-wrap,.contact-card,.contact-panel{border-radius:18px}.spotlight-copy{padding:0}.spotlight-media{min-height:220px;width:100%}.about-portrait,.academic-spotlight-media img{min-height:280px}.hero-editorial,.hero-immersive,.hero-contact-shell{min-height:auto}.hero-editorial-card{margin-bottom:0}.news-card{flex-direction:column}.news-card img{width:100%;height:12rem}.button-row{width:100%;flex-wrap:wrap}.button-row .button{flex:1 1 220px}.page-contact .hero-actions,.page-admissions-enquiry .hero-actions{width:100%}.page-contact .hero-actions .button,.page-admissions-enquiry .hero-actions .button{flex:1 1 100%}}
@media (max-width:640px){.brand{gap:.7rem}.brand-mark{width:2.5rem;height:2.5rem}.brand span:last-child{max-width:10.5rem;font-size:.92rem;line-height:1.12}h1{max-width:100%;font-size:clamp(2.25rem,12vw,3.55rem)}h2{font-size:clamp(1.7rem,8vw,2.35rem)}.lead{font-size:1rem}.button,.button-row .button,.nav-cta{width:100%}.hero-actions{width:100%}.hero-badges span{width:100%}.hero-stats{grid-template-columns:1fr 1fr}.hero-stats article,.hero-panel,.hero-subpage .hero-copy{padding:1.1rem}.feature-service-top,.feature-service-body,.card,.story,.split-card,.timeline article,.metric,.quote-panel,.cta-box{padding:1.2rem}.news-card{padding:.4rem 0}.news-card img{height:10.5rem}.breadcrumb{display:none}}
'''

SCRIPT = """const y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();const t=document.querySelector('.nav-toggle');const n=document.getElementById('site-nav');if(t&&n){const syncMobileSubmenu=(item,open)=>{const menu=item&&item.querySelector('.nav-menu');if(!menu)return; if(window.innerWidth<=900){menu.style.display=open?'block':'none';menu.style.width='100%';menu.style.maxWidth='100%';menu.style.minWidth='0';menu.style.overflow='hidden';menu.querySelectorAll('.nav-menu-link').forEach(link=>{link.style.display='block';link.style.width='100%';link.style.maxWidth='100%';link.style.minWidth='0';link.style.boxSizing='border-box';});}else{menu.style.display='';menu.style.width='';menu.style.maxWidth='';menu.style.minWidth='';menu.style.overflow='';menu.querySelectorAll('.nav-menu-link').forEach(link=>{link.style.display='';link.style.width='';link.style.maxWidth='';link.style.minWidth='';link.style.boxSizing='';});}};const closeMenus=()=>{n.classList.remove('is-open');t.setAttribute('aria-expanded','false');n.querySelectorAll('.nav-item.is-open').forEach(i=>{i.classList.remove('is-open');const b=i.querySelector('.nav-parent');if(b)b.setAttribute('aria-expanded','false');syncMobileSubmenu(i,false)})};t.addEventListener('click',e=>{e.stopPropagation();const o=n.classList.toggle('is-open');t.setAttribute('aria-expanded',String(o))});n.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>closeMenus()));n.querySelectorAll('.nav-parent').forEach(b=>b.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();const i=b.parentElement;const o=i.classList.toggle('is-open');b.setAttribute('aria-expanded',String(o));syncMobileSubmenu(i,o);n.querySelectorAll('.nav-item').forEach(x=>{if(x!==i){x.classList.remove('is-open');const xb=x.querySelector('.nav-parent');if(xb)xb.setAttribute('aria-expanded','false');syncMobileSubmenu(x,false)}})}));window.addEventListener('resize',()=>{n.querySelectorAll('.nav-item').forEach(i=>syncMobileSubmenu(i,i.classList.contains('is-open')))});document.addEventListener('click',e=>{if(!n.contains(e.target)&&!t.contains(e.target))closeMenus()})}"""


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
    current_abs = '/' + page_path.lstrip('./')
    for label, href in NAV:
        if label in MEGA:
            parent_cls = 'nav-item has-menu' + (' active' if label == section else '')
            children = []
            for child_label, child_href, child_desc in MEGA[label]:
                child_cls = 'nav-menu-link'
                if child_href == current_abs:
                    child_cls += ' active'
                children.append(f'<a class="{child_cls}" href="{href_from(page_path, child_href)}"><strong>{escape(child_label)}</strong><small>{escape(child_desc)}</small></a>')
            html.append(f'<div class="{parent_cls}"><button class="nav-parent" type="button" aria-expanded="false">{escape(label)}<span class="nav-caret">▾</span></button><div class="nav-menu">{"".join(children)}</div></div>')
        else:
            cls = 'active' if label == section else ''
            extra = ' nav-cta' if label == 'Contact' else ''
            html.append(f'<a class="nav-link {cls}{extra}" href="{href_from(page_path, href)}">{escape(label)}</a>')
    return ''.join(html)


def render_hero(page_path: str, cfg: dict) -> str:
    badges = ''.join(f'<span>{escape(item)}</span>' for item in cfg.get('hero_badges', []))
    stats_html = ''.join(f'<article><strong>{escape(value)}</strong><span>{escape(label)}</span></article>' for value, label in cfg.get('hero_stats', []))
    stats_block = f'<div class="hero-card-metrics">{stats_html}</div>' if stats_html else ''
    badges_block = f'<div class="hero-badges">{badges}</div>' if badges else ''
    if page_path == 'about/index.html':
        return f'''<section class="hero hero-about" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-editorial"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, '/about/vision-mission.html')}">Vision &amp; Mission</a><a class="button secondary" href="{href_from(page_path, '/about/quality.html')}">Quality &amp; Recognition</a></div></div><div class="hero-editorial-card"><p class="hero-card-label">Institutional profile</p><p>SSETP connects place, leadership, accreditation, and academic intent into one clearer institutional story.</p>{stats_block}</div></div></section>'''
    if page_path == 'academics/index.html':
        return f'''<section class="hero hero-academics" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-immersive"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, '/academics/programs.html')}">Explore Programs</a><a class="button ghost" href="{href_from(page_path, '/academics/rit.html')}">Research Portal</a></div><div class="hero-badges">{badges or '<span>RIT Pathway</span><span>Curriculum Governance</span><span>Applied Labs</span>'}</div></div></div></section>'''
    if page_path == 'contact.html':
        return f'''<section class="hero hero-contact" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-contact-shell"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p></div>{f'<div class="hero-badges contact-badges">{badges}</div>' if badges else ''}</div></section>'''
    if page_path == 'admissions/index.html':
        return f'''<section class="hero hero-admissions" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-editorial"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, '/admissions/process.html')}">Admission Process</a><a class="button secondary" href="{href_from(page_path, '/admissions/fees.html')}">Fees &amp; Scholarships</a></div></div><div class="hero-editorial-card"><p class="hero-card-label">Admissions focus</p><p>Students and families need orientation, process, and financial clarity without hunting across multiple pages.</p>{stats_block}</div></div></section>'''
    if page_path == 'admissions/process.html':
        return f'''<section class="hero hero-admissions" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-editorial"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, '/admissions/enquiry.html')}">Send an Enquiry</a><a class="button secondary" href="{href_from(page_path, '/admissions/fees.html')}">View Fees</a></div></div><div class="hero-editorial-card"><p class="hero-card-label">Process clarity</p><p>Applicants can understand the next step quickly: ask, prepare, submit, confirm.</p><div class="hero-card-metrics"><article><strong>Ask</strong><span>Start with the right admissions route</span></article><article><strong>Prepare</strong><span>Review eligibility and documents</span></article><article><strong>Submit</strong><span>Complete formal admission steps</span></article><article><strong>Join</strong><span>Confirm fees and reporting details</span></article></div></div></div></section>'''
    if page_path == 'admissions/fees.html':
        return f'''<section class="hero hero-admissions" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-editorial"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, '/admissions/enquiry.html')}">Ask Admissions</a><a class="button secondary" href="{href_from(page_path, '/admissions/process.html')}">Admission Process</a></div></div><div class="hero-editorial-card"><p class="hero-card-label">Family decision</p><p>This page keeps affordability, support, and scholarship visibility in one calm place for families.</p><div class="hero-card-metrics"><article><strong>2010</strong><span>Sai Prudent Scholarship established</span></article><article><strong>Support</strong><span>Merit and need-sensitive framing</span></article></div></div></div></section>'''
    if page_path == 'admissions/enquiry.html':
        return f'''<section class="hero hero-admissions" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-editorial"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="mailto:{SITE['enquiry_email']}">{SITE['enquiry_email']}</a><a class="button secondary" href="tel:+919100064545">Call Admissions</a></div></div><div class="hero-editorial-card"><p class="hero-card-label">Direct routes</p><p>Use the published admissions channels instead of searching through unrelated pages.</p><div class="hero-card-metrics"><article><strong>Email</strong><span>{SITE['enquiry_email']}</span></article><article><strong>Phone</strong><span>{SITE['phone']}</span></article></div></div></div></section>'''
    if page_path == 'campus/index.html':
        return f'''<section class="hero hero-campus" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-editorial"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, '/campus/facilities.html')}">Facilities</a><a class="button secondary" href="{href_from(page_path, '/campus/hostel.html')}">Hostel Life</a></div></div><div class="hero-editorial-card"><p class="hero-card-label">Student experience</p><p>Campus life is presented here as a practical student experience: facilities, hostel, wellbeing, and activity in one recognisable section.</p>{stats_block}</div></div></section>'''
    if page_path in {'about/vision-mission.html','about/leadership.html','about/quality.html','about/industry-interface.html'}:
        labels = {
            'about/vision-mission.html': ('Vision focus', 'Purpose, values, and student-development intent are presented here as the institution’s published direction.'),
            'about/leadership.html': ('Leadership focus', 'Leadership messages add visible institutional voice for students, parents, and stakeholders.'),
            'about/quality.html': ('Quality focus', 'Recognition matters most when it is verifiable, grouped, and easy to understand.'),
            'about/industry-interface.html': ('Industry focus', 'Industry linkage is presented here as academic relevance and employability proof.')
        }
        cta = {
            'about/vision-mission.html': (("Leadership", '/about/leadership.html'), ("Quality & Recognition", '/about/quality.html')),
            'about/leadership.html': (("Vision & Mission", '/about/vision-mission.html'), ("Industry Interface", '/about/industry-interface.html')),
            'about/quality.html': (("Leadership", '/about/leadership.html'), ("Industry Interface", '/about/industry-interface.html')),
            'about/industry-interface.html': (("Placements", '/placements/index.html'), ("About Overview", '/about/index.html')),
        }
        primary, secondary = cta[page_path]
        card_label, card_text = labels[page_path]
        return f'''<section class="hero hero-about" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-editorial"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, primary[1])}">{escape(primary[0])}</a><a class="button secondary" href="{href_from(page_path, secondary[1])}">{escape(secondary[0])}</a></div></div><div class="hero-editorial-card"><p class="hero-card-label">{escape(card_label)}</p><p>{escape(card_text)}</p></div></div></section>'''
    if page_path in {'academics/programs.html','academics/labs.html','academics/scholarships.html','academics/rit.html'}:
        labels = {
            'academics/programs.html': ('Program map', 'Departments and pathways are easier to scan here before moving into detailed programme information.'),
            'academics/labs.html': ('Applied learning', 'Laboratories are one of the clearest academic proof points because they show practice, not just claims.'),
            'academics/scholarships.html': ('Student support', 'Scholarship visibility reinforces confidence and access as part of the wider student journey.'),
            'academics/rit.html': ('International differentiator', 'RIT appears here as a flagship pathway with visible structure and academic purpose.')
        }
        cta = {
            'academics/programs.html': (("Labs", '/academics/labs.html'), ("RIT Pathway", '/academics/rit.html')),
            'academics/labs.html': (("Programs", '/academics/programs.html'), ("RIT Pathway", '/academics/rit.html')),
            'academics/scholarships.html': (("Admissions", '/admissions/fees.html'), ("Ask Admissions", '/admissions/enquiry.html')),
            'academics/rit.html': (("Programs", '/academics/programs.html'), ("Academics Overview", '/academics/index.html')),
        }
        primary, secondary = cta[page_path]
        card_label, card_text = labels[page_path]
        return f'''<section class="hero hero-academics" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-editorial"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, primary[1])}">{escape(primary[0])}</a><a class="button secondary" href="{href_from(page_path, secondary[1])}">{escape(secondary[0])}</a></div></div><div class="hero-editorial-card"><p class="hero-card-label">{escape(card_label)}</p><p>{escape(card_text)}</p></div></div></section>'''
    if page_path in {'campus/facilities.html','campus/hostel.html','campus/health-safety.html','campus/sports.html'}:
        labels = {
            'campus/facilities.html': ('Practical campus support', 'Facilities pages help families picture how students study and live on campus.'),
            'campus/hostel.html': ('Residential trust', 'Hostel life becomes credible when rooms, dining, community, and rules stay specific.'),
            'campus/health-safety.html': ('Calm reassurance', 'Health and safety information reduces uncertainty with concrete signals and direct routes.'),
            'campus/sports.html': ('Student participation', 'Sports and participation reinforce that campus life is active, social, and balanced.')
        }
        card_label, card_text = labels[page_path]
        return f'''<section class="hero hero-campus" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-editorial"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, '/campus/index.html')}">Campus Overview</a><a class="button secondary" href="{href_from(page_path, '/contact.html')}">Contact SSE</a></div></div><div class="hero-editorial-card"><p class="hero-card-label">{escape(card_label)}</p><p>{escape(card_text)}</p></div></div></section>'''
    if page_path in {'placements/success-stories.html','placements/contact.html'}:
        labels = {
            'placements/success-stories.html': ('Outcome proof', 'Success pages are grounded here in packages, recruiter range, and training-to-offer logic.'),
            'placements/contact.html': ('Recruiter route', 'Employer-facing contact is direct, visible, and tied closely to the placement story.')
        }
        card_label, card_text = labels[page_path]
        return f'''<section class="hero hero-placements" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-editorial"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, '/placements/index.html')}">Placements Overview</a><a class="button secondary" href="{href_from(page_path, '/placements/contact.html' if page_path.endswith('success-stories.html') else '/placements/success-stories.html')}">{'Placement Contact' if page_path.endswith('success-stories.html') else 'Success Stories'}</a></div></div><div class="hero-editorial-card"><p class="hero-card-label">{escape(card_label)}</p><p>{escape(card_text)}</p></div></div></section>'''
    if page_path == 'placements/index.html':
        return f'''<section class="hero hero-placements" style="--hero-image:url('{cfg.get("hero_image", "")}')"><div class="container hero-immersive"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, '/placements/success-stories.html')}">Success Stories</a><a class="button ghost" href="{href_from(page_path, '/placements/contact.html')}">Placement Contact</a></div>{badges_block}</div></div></section>'''
    return f'''<section class="hero{' hero-home' if page_path == 'index.html' else ' hero-subpage'}"{f' style="--hero-image:url(\'{cfg.get("hero_image", "")}\')"' if cfg.get('hero_image') else ''}><div class="container hero-layout"><div class="hero-copy"><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(page_path, '/admissions/index.html')}">Admissions</a><a class="button secondary" href="{href_from(page_path, '/academics/index.html')}">Academics</a></div><div class="hero-badges">{badges}</div></div><aside class="hero-panel"><div class="panel-topline"></div><div class="hero-stats">{stats_html}</div></aside></div></section>'''


def render_custom_sections(page_path: str) -> str:
    if page_path == 'about/index.html':
        return f'''<section class="section about-story"><div class="container about-story-grid"><div class="about-portrait-wrap"><img class="about-portrait" src="https://sseptp.org/assets/secretary-lbPm4mOq.jpg" alt="SSETP leadership" /><div class="portrait-caption"><strong>Leadership voice</strong><span>Institutional direction, purpose, and accountability</span></div></div><div class="about-story-copy"><p class="section-label">Leadership &amp; Purpose</p><h2>Vision, leadership, quality, and industry linkage form the core institutional picture.</h2><blockquote>Puttaparthi identity, autonomous status, and published quality signals give the About section its strongest anchors.</blockquote><p>SSETP already publishes the underlying material: vision and mission, leadership messages, quality structures, and industry interface. This page now brings those strands into one readable entry point.</p><div class="button-row"><a class="button primary" href="{href_from(page_path, '/about/leadership.html')}">Leadership</a><a class="button secondary" href="{href_from(page_path, '/about/industry-interface.html')}">Industry Interface</a></div></div></div></section><section class="section muted"><div class="container"><p class="section-label">Quality &amp; Standards</p><div class="section-head"><h2>Published credentials and quality systems are now easier to verify.</h2><p>Autonomous status, NAAC, and IQAC are shown together because they are central institutional trust signals.</p></div><div class="cards cols-3 about-quality-grid"><article class="card"><div class="icon">01</div><h3>IQAC Cell</h3><p>The Internal Quality Assurance Cell is presented as an active catalyst for academic and administrative enhancement.</p></article><article class="card card-featured"><div class="icon">02</div><h3>NAAC A Grade</h3><p>SSETP highlights NAAC A Grade accreditation with a published 3.17 / 4 score as a key quality proof point.</p></article><article class="card"><div class="icon">03</div><h3>Autonomous Institute</h3><p>Autonomous status reinforces curricular independence, quality control, and institutional seriousness.</p></article></div></div></section><section class="section"><div class="container about-links"><div><p class="section-label">Explore About</p><h2>Follow the main institutional themes from one place.</h2></div><div class="about-link-list"><a href="{href_from(page_path, '/about/vision-mission.html')}"><strong>Vision &amp; Mission</strong><span>Purpose, values, and student-development intent</span></a><a href="{href_from(page_path, '/about/quality.html')}"><strong>Quality &amp; Recognition</strong><span>Autonomous status, NAAC, IQAC, AICTE, and UGC context</span></a><a href="{href_from(page_path, '/about/industry-interface.html')}"><strong>Industry Interface</strong><span>Advisory board, academic relevance, and employer linkage</span></a></div></div></section>'''
    if page_path == 'academics/index.html':
        return f'''<section class="section"><div class="container academic-spotlight"><div class="academic-spotlight-media"><img src="https://sseptp.org/assets/rite-BzQ2Jteo.png" alt="RIT pathway" /></div><div class="academic-spotlight-copy"><p class="section-label">Innovation Core</p><h2>Research Integrated Training (RIT)</h2><p>At SSETP, learning extends beyond the classroom. The RIT pathway is one of the clearest differentiators on the current site and now leads the academic story more directly.</p><ul class="mini-list"><li>Software-engineering learning in cooperation with RISE and INSO</li><li>International academic positioning made visible early</li><li>Practical training linked to employability and innovation</li></ul><a class="text-link" href="{href_from(page_path, '/academics/rit.html')}">Learn more about RIT →</a></div></div></section><section class="section muted"><div class="container"><p class="section-label">Undergraduate Programs</p><div class="section-head"><h2>Undergraduate engineering paths are now easier to compare.</h2><p>Computer Science, Mechanical, Civil, and Electronics appear here as part of the broader departmental journey into detailed programme pages.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">CS</div><h3>Computer Science</h3><p>Programs, labs, and pathways shaped around contemporary computing disciplines.</p><p><a href="{href_from(page_path, '/academics/programs.html')}">View programs →</a></p></article><article class="card"><div class="icon">ME</div><h3>Mechanical Engineering</h3><p>Practical engineering depth supported by laboratories and applied learning.</p><p><a href="{href_from(page_path, '/academics/labs.html')}">View labs →</a></p></article><article class="card"><div class="icon">CV</div><h3>Civil Engineering</h3><p>Infrastructure-oriented learning tied to academic rigor and departmental depth.</p><p><a href="{href_from(page_path, '/academics/programs.html')}">Explore pathway →</a></p></article><article class="card"><div class="icon">EC</div><h3>Electronics &amp; Communication</h3><p>Applied technical education supported by structured curriculum review.</p><p><a href="{href_from(page_path, '/academics/programs.html')}">See academic routes →</a></p></article></div></div></section><section class="section"><div class="container governance-band"><div><p class="section-label">Academic Governance</p><h2>Curriculum revision is part of the academic story.</h2><p>The current SSETP copy explicitly references DACs, Boards of Studies, and the Academic Council, making curriculum governance part of the published academic model.</p></div><div class="governance-list"><article><strong>DAC</strong><span>Departments review and discuss syllabus content.</span></article><article><strong>BoS</strong><span>Boards of Studies finalise course structure and syllabus.</span></article><article><strong>Academic Council</strong><span>Approves broader academic matters and program direction.</span></article></div></div></section>'''
    if page_path == 'contact.html':
        return f'''<section class="section"><div class="container"><div class="contact-grid"><article class="contact-card"><div class="icon">01</div><h3>Admissions</h3><p><a href="mailto:enquiry@sseptp.org">enquiry@sseptp.org</a></p><p><a href="tel:+919100064545">+91 9100064545</a></p></article><article class="contact-card"><div class="icon">02</div><h3>General Office</h3><p><a href="mailto:info@sseptp.org">info@sseptp.org</a></p><p>Puttaparthi, Sri Sathya Sai District</p></article><article class="contact-card"><div class="icon">03</div><h3>Placements &amp; HR</h3><p><a href="mailto:hr@sseptp.org">hr@sseptp.org</a></p><p>Recruiter and career-related queries</p></article></div></div></section><section class="section muted"><div class="container contact-layout"><div><p class="section-label">Visit Campus</p><h2>Direct contact is clearer when each route is explicit.</h2><p>Students, parents, and recruiters can choose the right route immediately without scanning through broad marketing copy.</p><ul class="mini-list"><li>{escape(SITE['address'])}</li><li>{escape(SITE['phone'])}</li><li>Admissions, general, and HR routes kept distinct</li></ul></div><div class="contact-panel"><h3>Public channels</h3><p>Facebook: sseptp</p><p>X: SanskrithiGroup</p><p>Instagram: sanskrithigroup_ptp</p><div class="button-row"><a class="button primary" href="{href_from(page_path, '/admissions/enquiry.html')}">Admissions Enquiry</a><a class="button secondary" href="{href_from(page_path, '/placements/index.html')}">Placements</a></div></div></div></section>'''
    if page_path == 'admissions/index.html':
        return f'''<section class="section"><div class="container admissions-flow"><div><p class="section-label">Start here</p><h2>Admissions information is staged here as one practical sequence.</h2><p>SSETP already has the right ingredients: orientation, process, fee context, scholarship support, and direct enquiry routes. This page makes that journey clearer.</p><div class="button-row"><a class="button primary" href="{href_from(page_path, '/admissions/enquiry.html')}">Admissions Enquiry</a><a class="button secondary" href="{href_from(page_path, '/admissions/process.html')}">View Process</a></div></div><div class="governance-list"><article><strong>Overview</strong><span>What SSETP is, where it is, and why a student might shortlist it.</span></article><article><strong>Process</strong><span>Clear next steps instead of disconnected admissions fragments.</span></article><article><strong>Fees &amp; Support</strong><span>Sai Prudent Scholarship and cost clarity kept close together.</span></article></div></div></section><section class="section muted"><div class="container"><p class="section-label">Admissions routes</p><div class="section-head"><h2>The first four admissions questions are answered in one place.</h2><p>Orientation, process, money clarity, and a human contact route belong in one decision flow.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">01</div><h3>Admissions Overview</h3><p>Shortlist the institution with the right overall context.</p><p><a href="{href_from(page_path, '/admissions/index.html')}">Overview →</a></p></article><article class="card"><div class="icon">02</div><h3>Admission Process</h3><p>Move from interest to the next practical step without guessing.</p><p><a href="{href_from(page_path, '/admissions/process.html')}">See process →</a></p></article><article class="card"><div class="icon">03</div><h3>Fees &amp; Scholarships</h3><p>See financial clarity and support on the same path.</p><p><a href="{href_from(page_path, '/admissions/fees.html')}">View support →</a></p></article><article class="card"><div class="icon">04</div><h3>Enquiry</h3><p>Talk to a real person through the published admissions routes.</p><p><a href="{href_from(page_path, '/admissions/enquiry.html')}">Contact admissions →</a></p></article></div></div></section>'''
    if page_path == 'campus/index.html':
        return f'''<section class="section"><div class="container academic-spotlight"><div class="academic-spotlight-media"><img src="https://sseptp.org/assets/studentCommonArea-C2A_66qp.jpg" alt="Campus life at SSETP" /></div><div class="academic-spotlight-copy"><p class="section-label">Campus rhythm</p><h2>Campus life combines facilities, hostel living, support systems, and student activity.</h2><p>The live site already shows classrooms, common areas, dining, hostel spaces, health-related support, and sports participation as part of one student experience.</p><ul class="mini-list"><li>Facilities and support spaces surfaced clearly</li><li>Hostel life treated as a practical decision factor</li><li>Wellbeing, safety, and activity visible in one student-life route</li></ul><a class="text-link" href="{href_from(page_path, '/campus/hostel.html')}">Explore hostel life →</a></div></div></section><section class="section muted"><div class="container"><p class="section-label">Campus experience</p><div class="section-head"><h2>Facilities, accommodation, safety, and sports now sit in one clearer campus layer.</h2><p>Student experience is easier to understand when accommodation, facilities, activity, and trust signals are grouped together.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">01</div><h3>Facilities</h3><p>Academic buildings, campus spaces, and daily support infrastructure.</p><p><a href="{href_from(page_path, '/campus/facilities.html')}">View facilities →</a></p></article><article class="card"><div class="icon">02</div><h3>Hostel Life</h3><p>Comfort, community, and residential trust factors for students.</p><p><a href="{href_from(page_path, '/campus/hostel.html')}">See hostel →</a></p></article><article class="card"><div class="icon">03</div><h3>Health &amp; Safety</h3><p>Wellbeing and security expectations framed as student trust essentials.</p><p><a href="{href_from(page_path, '/campus/health-safety.html')}">View support →</a></p></article><article class="card"><div class="icon">04</div><h3>Sports</h3><p>Participation, energy, and activity beyond classroom routines.</p><p><a href="{href_from(page_path, '/campus/sports.html')}">Explore sports →</a></p></article></div></div></section>'''
    if page_path == 'placements/index.html':
        return f'''<section class="section"><div class="container placements-band"><div><p class="section-label">Placement proof</p><h2>Placement outcomes and recruiter trust lead this section.</h2><p>SSETP already publishes strong proof points: offers, recruiters, placement rate, and employer-facing contact.</p><div class="button-row"><a class="button primary" href="{href_from(page_path, '/placements/contact.html')}">Placement Contact</a><a class="button secondary" href="{href_from(page_path, '/placements/success-stories.html')}">Success Stories</a></div></div><div class="governance-list"><article><strong>1675 Offers</strong><span>Total offers highlighted on the live site.</span></article><article><strong>150 Recruiters</strong><span>Company reach used as a visible employer-trust signal.</span></article><article><strong>95% Rate</strong><span>Placement rate highlighted for 2024–25.</span></article></div></div></section><section class="section muted"><div class="container"><p class="section-label">Career routes</p><div class="section-head"><h2>Placements connect outcomes, students, and recruiters.</h2><p>Overview, success stories, and recruiter contact now sit closer together as one placement narrative.</p></div><div class="cards cols-3 about-quality-grid"><article class="card"><div class="icon">01</div><h3>Placement Overview</h3><p>High-level outcomes and readiness signals in one view.</p><p><a href="{href_from(page_path, '/placements/index.html')}">Overview →</a></p></article><article class="card card-featured"><div class="icon">02</div><h3>Success Stories</h3><p>Student outcomes and proof-driven placement narrative.</p><p><a href="{href_from(page_path, '/placements/success-stories.html')}">See stories →</a></p></article><article class="card"><div class="icon">03</div><h3>Placement Contact</h3><p>Career cell and recruiter route for direct employer engagement.</p><p><a href="{href_from(page_path, '/placements/contact.html')}">Contact cell →</a></p></article></div></div></section><section class="section"><div class="container"><p class="section-label">Why recruiters trust SSE</p><div class="section-head"><h2>Published placement data gives this page real substance.</h2><p>Recruiter confidence is shown through scale, recurring outcomes, and a visible mix of training, coordination, and employer access.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">800</div><h3>Students placed</h3><p>The current placement data set includes a published students-placed signal alongside overall offers.</p></article><article class="card"><div class="icon">36</div><h3>Highest package</h3><p>A 36 LPA peak package stays visible as a headline outcome signal.</p></article><article class="card"><div class="icon">7.5</div><h3>Average package</h3><p>The live page also provides an average-package signal, which makes the outcomes story more grounded.</p></article><article class="card card-featured"><div class="icon">150</div><h3>Recruiting companies</h3><p>Company breadth suggests repeatability rather than a few isolated placement wins.</p></article></div></div></section><section class="section muted"><div class="container contact-layout"><div><p class="section-label">Training to placement</p><h2>Placement readiness is shown as a pipeline from preparation to recruiter access.</h2><p>The public materials consistently point to aptitude work, coding practice, communication support, coordinators, and recruiter access working together.</p></div><div class="contact-panel"><h3>Pipeline signals</h3><p>Aptitude and interview preparation</p><p>Technical and coding readiness</p><p>Coordinator-led placement support</p><p>Direct recruiter-facing career cell route</p></div></div></section><section class="section"><div class="container"><p class="section-label">Recruiter visibility</p><div class="section-head"><h2>Recognizable employers are now surfaced more clearly.</h2><p>The current placement materials reference familiar employers and a broader recruiter ecosystem.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">T</div><h3>TCS &amp; Infosys</h3><p>Large-scale IT employers reinforce recurring campus-hiring credibility.</p></article><article class="card"><div class="icon">A</div><h3>Amazon &amp; Accenture</h3><p>Recognizable brands make placement performance more legible for students and parents.</p></article><article class="card"><div class="icon">C</div><h3>Cognizant &amp; Wipro</h3><p>Broader service and enterprise recruiters support consistency across batches.</p></article><article class="card"><div class="icon">L</div><h3>L&amp;T and core roles</h3><p>The placement story also suggests breadth beyond software-only hiring.</p></article></div></div></section>'''
    if page_path == 'admissions/process.html':
        return f'''<section class="section"><div class="container governance-band"><div><p class="section-label">Application journey</p><h2>The process page is organized as a sequential and practical student flow.</h2><p>Students and parents mostly need reassurance about the next step, the expected documents, and who to contact if something is unclear.</p></div><div class="governance-list"><article><strong>Step 1</strong><span>Check basic eligibility for the programme route you want.</span></article><article><strong>Step 2</strong><span>Prepare application details and required documents.</span></article><article><strong>Step 3</strong><span>Complete the application, entrance-exam, counselling, and confirmation flow.</span></article></div></div></section><section class="section muted"><div class="container"><p class="section-label">Step-by-step</p><div class="section-head"><h2>The live site gives a clearer admissions sequence than the redesign previously showed.</h2><p>That practical order stays visible here so applicants understand both the process and the checkpoints.</p></div><div class="cards cols-3 about-quality-grid"><article class="card"><div class="icon">01</div><h3>Eligibility check</h3><p>Confirm that you meet the minimum academic criteria for the programme, especially PCM-based requirements for B.Tech admission.</p></article><article class="card"><div class="icon">02</div><h3>Application</h3><p>Complete the online application and prepare supporting documents in advance instead of treating them as a later step.</p></article><article class="card"><div class="icon">03</div><h3>Entrance examination</h3><p>Appear for the relevant state-level or national engineering entrance examination route referenced by the current site.</p></article><article class="card"><div class="icon">04</div><h3>Counselling</h3><p>Participate in counselling and seat-allocation stages based on merit and the applicable admission framework.</p></article><article class="card"><div class="icon">05</div><h3>Admission confirmation</h3><p>Verify documents, confirm fees, and complete final formalities to secure the seat.</p></article><article class="card card-featured"><div class="icon">?</div><h3>Need help mid-process?</h3><p>Admissions questions usually become easier when the applicant can verify the right route, documents, and fee expectations directly.</p></article></div></div></section><section class="section"><div class="container contact-layout"><div><p class="section-label">Basic eligibility</p><h2>Applicants can now see the core requirement set without hunting for it.</h2><p>The current site already provides usable admissions criteria for B.Tech pathways and general entrance logic.</p></div><div class="contact-panel"><h3>B.Tech baseline</h3><p>10+2 or equivalent with Physics, Chemistry, and Mathematics</p><p>Minimum 50% aggregate in PCM (45% for reserved categories)</p><p>Valid entrance-exam route as applicable</p><p>Age note: current site mentions a not-more-than-23 reference for the 2025 cycle</p></div></div></section><section class="section muted"><div class="container"><p class="section-label">Required documents</p><div class="section-head"><h2>Document readiness is part of the process, not an afterthought.</h2><p>The current site names a practical document set that is summarized here for applicants and families.</p></div><div class="cards cols-3 about-quality-grid"><article class="card"><div class="icon">A</div><h3>Academic records</h3><p>10th and 12th mark sheets / certificates, plus equivalent qualification records where relevant.</p></article><article class="card"><div class="icon">B</div><h3>Admission records</h3><p>Transfer Certificate and the relevant entrance-exam score card should be prepared early.</p></article><article class="card"><div class="icon">C</div><h3>Identity & support records</h3><p>Aadhar Card, passport-size photographs, and category certificate where applicable.</p></article></div><div class="button-row"><a class="button primary" href="{href_from(page_path, '/admissions/enquiry.html')}">Send an enquiry</a><a class="button secondary" href="{href_from(page_path, '/admissions/fees.html')}">View fees</a></div></div></section>'''
    if page_path == 'admissions/fees.html':
        return f'''<section class="section"><div class="container academic-spotlight"><div class="academic-spotlight-copy"><p class="section-label">Scholarship support</p><h2>Fees and scholarships belong in the same decision space.</h2><p>The Sai Prudent Scholarship is one of the most concrete support signals on the current site. This page connects support, affordability, and confidence for families.</p><ul class="mini-list"><li>Established in 2010 as a long-running support initiative</li><li>Linked on the current site to Anahata Stiftung and RISE, Austria</li><li>Positioned for deserving students from economically disadvantaged backgrounds</li></ul></div><div class="contact-panel"><h3>What families need here</h3><p>Clear fee framing</p><p>Scholarship visibility</p><p>Direct enquiry route when affordability questions remain</p><div class="button-row"><a class="button primary" href="{href_from(page_path, '/admissions/enquiry.html')}">Ask admissions</a></div></div></div></section><section class="section muted"><div class="container"><p class="section-label">Before families decide</p><div class="section-head"><h2>The live site supports guidance here, but not a fully reliable public fee table.</h2><p>This page helps families understand what to clarify without inventing numbers the source site does not clearly support.</p></div><div class="cards cols-3 about-quality-grid"><article class="card"><div class="icon">01</div><h3>Programme fee clarity</h3><p>Confirm tuition expectations for the chosen route instead of assuming one flat cost structure across all programmes.</p></article><article class="card"><div class="icon">02</div><h3>Additional cost heads</h3><p>Families usually also need clarity on hostel, transport, examination, and other joining-related charges where relevant.</p></article><article class="card card-featured"><div class="icon">03</div><h3>Scholarship interaction</h3><p>Ask directly how scholarship support may reduce or influence the payable fee burden in the student’s case.</p></article></div></div></section><section class="section"><div class="container"><p class="section-label">What to ask admissions</p><div class="section-head"><h2>A useful fees page reduces uncertainty even when it avoids unsupported public numbers.</h2><p>This page gives families the right questions so they can reach a confident decision quickly.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">A</div><h3>Tuition</h3><p>What is the current tuition for the selected programme and academic year?</p></article><article class="card"><div class="icon">B</div><h3>Residential costs</h3><p>If hostel accommodation is needed, what are the expected boarding and lodging charges?</p></article><article class="card"><div class="icon">C</div><h3>Other charges</h3><p>Are there transport, examination, or one-time admission-related costs families should plan for?</p></article><article class="card"><div class="icon">D</div><h3>Payment timing</h3><p>How are payment milestones structured, and what changes if scholarship support is approved?</p></article></div></div></section><section class="section muted"><div class="container placements-band"><div><p class="section-label">Support context</p><h2>Scholarship support stays visible from the fees page.</h2><p>The current site gives stronger scholarship substance than fee-table substance, so that support route remains prominent here.</p></div><div class="governance-list"><article><strong>2010</strong><span>Sai Prudent Scholarship established</span></article><article><strong>300+</strong><span>Total beneficiaries highlighted on the live site</span></article><article><strong>Merit + Need</strong><span>Selection is framed around both academic promise and financial need</span></article></div></div><div class="button-row"><a class="button primary" href="{href_from(page_path, '/academics/scholarships.html')}">View scholarship</a><a class="button secondary" href="{href_from(page_path, '/admissions/enquiry.html')}">Talk to admissions</a></div></section>'''
    if page_path == 'admissions/enquiry.html':
        return f'''<section class="section"><div class="container contact-grid"><article class="contact-card"><div class="icon">01</div><h3>Admissions Enquiry</h3><p><a href="mailto:enquiry@sseptp.org">enquiry@sseptp.org</a></p><p>Prospective-student and parent questions</p></article><article class="contact-card"><div class="icon">02</div><h3>General Office</h3><p><a href="mailto:info@sseptp.org">info@sseptp.org</a></p><p>Broader institutional questions</p></article><article class="contact-card"><div class="icon">03</div><h3>Phone Contact</h3><p><a href="tel:+919100064545">+91 9100064545 / 74545</a></p><p>Direct office contact</p></article></div></section><section class="section muted"><div class="container contact-layout"><div><p class="section-label">Admissions routing</p><h2>Use the right route for the right question.</h2><p>This page acts as a calm contact hub for admissions, fee, scholarship, campus-visit, and joining questions.</p></div><div class="contact-panel"><h3>Best use cases</h3><p>Admissions questions</p><p>Fee and scholarship clarification</p><p>Campus visit or joining guidance</p></div></div></section>'''
    if page_path == 'campus/facilities.html':
        return f'''<section class="section"><div class="container about-links"><div><p class="section-label">Facility lens</p><h2>Facilities show how students study, live, and move through the campus day to day.</h2><p>Families read this page as a practical signal of academic spaces, residential support, and everyday usability.</p></div><div class="about-link-list"><a href="{href_from(page_path, '/academics/labs.html')}"><strong>Academic environment</strong><span>Labs, classrooms, and department spaces support the academic promise.</span></a><a href="{href_from(page_path, '/campus/hostel.html')}"><strong>Residential support</strong><span>Hostel blocks, common rooms, dining, and Wi‑Fi shape the lived experience.</span></a><a href="{href_from(page_path, '/contact.html')}"><strong>Daily usability</strong><span>Students and families often want to confirm practical details directly.</span></a></div></div></section>'''
    if page_path == 'campus/hostel.html':
        return f'''<section class="section"><div class="container"><p class="section-label">Residential life</p><div class="section-head"><h2>Hostel trust comes from specifics.</h2><p>Separate blocks, supervision, dining, common areas, rules, and activities are exactly the details parents look for.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">01</div><h3>Accommodation</h3><p>Separate hostel blocks, furnished rooms, and supervised residential arrangements.</p></article><article class="card"><div class="icon">02</div><h3>Dining &amp; Mess</h3><p>Meal support, kitchen facilities, and dining-hall context are part of the trust story.</p></article><article class="card"><div class="icon">03</div><h3>Community</h3><p>Cultural events, sports, and hostel committees contribute to daily life.</p></article><article class="card"><div class="icon">04</div><h3>Safety &amp; Rules</h3><p>Security, timings, conduct, and support expectations matter to families.</p></article></div></div></section>'''
    if page_path == 'campus/health-safety.html':
        return f'''<section class="section"><div class="container governance-band"><div><p class="section-label">Calm clarity</p><h2>Health and safety information is strongest when it stays concrete and easy to follow.</h2><p>Medical support, first aid, security, hostel oversight, and clear contact routes are usually more important than polished wording.</p></div><div class="governance-list"><article><strong>Security</strong><span>Campus and hostel oversight is easy to understand.</span></article><article><strong>Support</strong><span>Medical or first-aid availability matters because families expect it.</span></article><article><strong>Contact</strong><span>When a question is urgent, direct routes are obvious.</span></article></div></div></section>'''
    if page_path == 'campus/sports.html':
        return f'''<section class="section"><div class="container placements-band"><div><p class="section-label">Student energy</p><h2>Sports help show a balanced campus life.</h2><p>This page reinforces participation, teamwork, and a campus culture that extends beyond classrooms.</p></div><div class="governance-list"><article><strong>Balance</strong><span>Sports rounds out the academic and residential story.</span></article><article><strong>Teamwork</strong><span>It reinforces collaborative values visible elsewhere on the site.</span></article><article><strong>Participation</strong><span>Activity makes student life feel real rather than static.</span></article></div></div></section>'''
    if page_path == 'placements/success-stories.html':
        return f'''<section class="section"><div class="container"><p class="section-label">Outcome lens</p><div class="section-head"><h2>Success stories stay close to published placement proof.</h2><p>This page connects package levels, recruiter spread, and training-to-offer logic instead of inventing glossy profiles.</p></div><div class="cards cols-3 about-quality-grid"><article class="card"><div class="icon">01</div><h3>High-value offers</h3><p>The current site already highlights strong top-end packages.</p></article><article class="card card-featured"><div class="icon">02</div><h3>Broad recruiter base</h3><p>The number of recruiting companies matters because it signals scale, not just a few standout cases.</p></article><article class="card"><div class="icon">03</div><h3>Training-to-offer logic</h3><p>Success connects back to the placement-readiness model.</p></article></div></div></section>'''
    if page_path == 'placements/contact.html':
        return f'''<section class="section"><div class="container contact-grid"><article class="contact-card"><div class="icon">01</div><h3>CDC Head</h3><p>Ms. Kiran Ravi Srivastava</p><p>Visible on the current site as CDC – Head.</p></article><article class="contact-card"><div class="icon">02</div><h3>Coordinators</h3><p>Dr. Bala Koteswari</p><p>Mr. Rakesh Yadav Kodari</p></article><article class="contact-card"><div class="icon">03</div><h3>Routing</h3><p><a href="mailto:hr@sseptp.org">hr@sseptp.org</a></p><p>Recruiter and career-related queries</p></article></div></section><section class="section muted"><div class="container contact-layout"><div><p class="section-label">Employer route</p><h2>Recruiter contact is visible here without searching.</h2><p>This page acts as a direct career-cell access point linked to the wider placement proof.</p></div><div class="contact-panel"><h3>Best next steps</h3><p>Use the placements mailbox for recruiter contact</p><p>Review outcomes on the overview page</p><p>See proof framing in success stories</p></div></div></section>'''
    if page_path == 'about/vision-mission.html':
        return f'''<section class="section"><div class="container about-links"><div><p class="section-label">Published direction</p><h2>Vision and mission act here as the institution’s north star.</h2><p>This page highlights the school’s own language around character, initiative, innovation, teamwork, and social responsibility.</p></div><div class="about-link-list"><a href="{href_from(page_path, '/about/leadership.html')}"><strong>Leadership</strong><span>See how institutional voice supports the same direction.</span></a><a href="{href_from(page_path, '/about/quality.html')}"><strong>Quality & Recognition</strong><span>Connect purpose with visible quality signals and governance.</span></a></div></div></section>'''
    if page_path == 'about/leadership.html':
        return f'''<section class="section"><div class="container about-story-grid"><div class="about-portrait-wrap"><img class="about-portrait" src="https://sseptp.org/assets/principal-Cgd9y_bj.jpg" alt="SSETP leadership" /></div><div class="about-story-copy"><p class="section-label">Leadership voices</p><h2>Leadership messages strengthen trust for students and families.</h2><blockquote>Who leads the institution, how it speaks, and what it emphasizes are part of the admissions decision.</blockquote><p>The Chairman, Principal, and Secretary messages reinforce values, seriousness, and student confidence as part of the school’s published leadership layer.</p></div></div></section>'''
    if page_path == 'about/quality.html':
        return f'''<section class="section"><div class="container"><p class="section-label">Core credentials</p><div class="section-head"><h2>Quality proof points are grouped clearly on this page.</h2><p>Autonomous status, AICTE and UGC recognition, NAAC, and IQAC sit together here as verifiable trust signals.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">01</div><h3>Autonomous Institute</h3><p>Academic independence is a key institutional proof point.</p></article><article class="card"><div class="icon">02</div><h3>AICTE Approved</h3><p>Programs are framed within the expected engineering approval structure.</p></article><article class="card"><div class="icon">03</div><h3>UGC Recognized</h3><p>Recognition contributes directly to trust and legitimacy.</p></article><article class="card"><div class="icon">04</div><h3>NAAC A Grade</h3><p>The current site highlights an A Grade with a 3.17 / 4 score.</p></article></div></div></section>'''
    if page_path == 'about/industry-interface.html':
        return f'''<section class="section"><div class="container placements-band"><div><p class="section-label">Industry linkage</p><h2>Industry interface connects academics and placements.</h2><p>RISE-linked members and industry names from TCS, CGI, HCLTech, Brillio, HP, Mphasis, and Capgemini give this page a clear academic-relevance and employability context.</p></div><div class="governance-list"><article><strong>International connection</strong><span>RISE-linked members strengthen global academic positioning.</span></article><article><strong>Employer relevance</strong><span>Industry leaders connect curriculum to market expectations.</span></article><article><strong>Placement bridge</strong><span>The page supports employability and recruiter trust.</span></article></div></div></section>'''
    if page_path == 'academics/programs.html':
        return f'''<section class="section"><div class="container academic-spotlight"><div class="academic-spotlight-copy"><p class="section-label">B.Tech at SSE</p><h2>The current site provides substantial programme detail across departments.</h2><p>SSE presents its undergraduate engineering offer as AICTE-aligned, industry-informed, practical, and lab-supported. This page keeps that published substance in a scan-friendly structure.</p><ul class="mini-list"><li>AICTE-approved B.Tech structure</li><li>Industry-aligned syllabus and practical learning emphasis</li><li>Experienced faculty and state-of-the-art labs</li><li>Innovation, research, and internship orientation</li></ul></div><div class="contact-panel"><h3>What matters most here</h3><p>Clear programme choices</p><p>Seats and eligibility</p><p>Real academic depth by discipline</p></div></div></section><section class="section muted"><div class="container"><p class="section-label">Undergraduate programmes</p><div class="section-head"><h2>Five B.Tech programmes appear here as distinct choices.</h2><p>The current live site provides enough information to treat each programme as a proper academic route, not just a short department label.</p></div><div class="cards cols-3 about-quality-grid"><article class="card card-featured"><div class="icon">CSE</div><h3>Computer Science &amp; Engineering</h3><p>Algorithms, software systems, AI/ML, databases, networking, and strong computing depth.</p><p><strong>4 Years</strong> · <strong>120 Seats</strong></p><p><small>Eligibility: 10+2 with Mathematics, Physics, Chemistry and minimum 50% marks (45% reserved categories).</small></p></article><article class="card"><div class="icon">ECE</div><h3>Electronics &amp; Communication</h3><p>Electronic systems, communication networks, VLSI, embedded systems, and signal processing.</p><p><strong>4 Years</strong> · <strong>120 Seats</strong></p><p><small>Eligibility: 10+2 with Mathematics, Physics, Chemistry and minimum 50% marks (45% reserved categories).</small></p></article><article class="card"><div class="icon">EEE</div><h3>Electrical &amp; Electronics</h3><p>Power systems, control, electrical machines, smart grids, and renewable-energy context.</p><p><strong>4 Years</strong> · <strong>60 Seats</strong></p><p><small>Eligibility: 10+2 with Mathematics, Physics, Chemistry and minimum 50% marks (45% reserved categories).</small></p></article><article class="card"><div class="icon">ME</div><h3>Mechanical Engineering</h3><p>Design, manufacturing, thermodynamics, CAD/CAM, robotics, and industrial engineering.</p><p><strong>4 Years</strong> · <strong>120 Seats</strong></p><p><small>Eligibility: 10+2 with Mathematics, Physics, Chemistry and minimum 50% marks (45% reserved categories).</small></p></article><article class="card"><div class="icon">CE</div><h3>Civil Engineering</h3><p>Structures, infrastructure, transportation, geotechnics, environment, and construction management.</p><p><strong>4 Years</strong> · <strong>60 Seats</strong></p><p><small>Eligibility: 10+2 with Mathematics, Physics, Chemistry and minimum 50% marks (45% reserved categories).</small></p></article><article class="card"><div class="icon">PG</div><h3>Postgraduate pathways</h3><p>The live site also highlights M.Tech routes in CSE, ECE, and Electrical Engineering.</p><p><strong>2 Years</strong> · <strong>18 Seats each</strong></p><p><small>Shown here as a follow-on pathway separate from the undergraduate grid.</small></p></article></div></div></section><section class="section"><div class="container"><p class="section-label">Programme detail</p><div class="section-head"><h2>Each programme includes enough detail for serious comparison.</h2><p>The structure moves from a scan-first overview into curriculum rhythm, labs, careers, and outcome signals.</p></div><div class="cards cols-1"> <article class="card"><h3>Computer Science &amp; Engineering</h3><p>The current page positions CSE around software systems, data structures, algorithms, databases, networking, artificial intelligence, and machine learning.</p><ul class="mini-list"><li><strong>Course structure:</strong> First year foundations, then data structures / DBMS / OS, then software engineering / networks / AI / ML / cloud, then distributed systems / cybersecurity / big data / IoT.</li><li><strong>Lab facilities:</strong> Advanced Computing Lab, Network &amp; Security Lab, Database Systems Lab, Software Development Lab, AI &amp; ML Lab, IoT Lab.</li><li><strong>Career routes:</strong> Software Developer, Systems Analyst, DBA, Network Engineer, Web / Mobile Developer, AI/ML Engineer, Data Scientist.</li><li><strong>Achievement signal:</strong> national coding competitions, hackathons, and placements into firms like TCS, Infosys, Wipro, and startups.</li></ul></article><article class="card"><h3>Electronics &amp; Communication Engineering</h3><p>ECE is described through electronic systems, circuits, communication networks, VLSI, embedded systems, signal processing, and wireless communication.</p><ul class="mini-list"><li><strong>Course structure:</strong> electronics and communication foundations, then electronic devices / digital systems / analog circuits, then DSP / VLSI / microcontrollers / control / wireless, then embedded, optical, satellite, and IoT systems.</li><li><strong>Lab facilities:</strong> Basic Electronics Lab, Communication Systems Lab, VLSI Design Lab, Microprocessor &amp; Microcontroller Lab, DSP Lab, IoT &amp; Embedded Systems Lab.</li><li><strong>Career routes:</strong> Electronics Design Engineer, Communication Systems Engineer, VLSI Design Engineer, IoT Developer, Network Planning Engineer, Embedded Systems Designer.</li><li><strong>Achievement signal:</strong> technical-competition wins and placements into electronics, telecom, and PSU environments.</li></ul></article><article class="card"><h3>Electrical &amp; Electronics Engineering</h3><p>EEE is framed around generation, transmission, distribution, and utilization of electrical energy, with power systems and renewable energy as strong themes.</p><ul class="mini-list"><li><strong>Course structure:</strong> electric circuits and machines, then power systems / control / power electronics / microcontrollers / drives, then high-voltage engineering, smart grids, protection, and renewable-energy systems.</li><li><strong>Lab facilities:</strong> Electrical Machines Lab, Power Systems Lab, Control Systems Lab, Power Electronics Lab, Electrical Measurements Lab, Microprocessor &amp; Microcontroller Lab.</li><li><strong>Career routes:</strong> Electrical Design Engineer, Power Systems Engineer, Control Systems Engineer, Renewable Energy Specialist, Automation Engineer.</li><li><strong>Achievement signal:</strong> technical-festival recognition and placements into power, manufacturing, and automation companies.</li></ul></article><article class="card"><h3>Mechanical Engineering</h3><p>Mechanical Engineering is presented through design, manufacturing, maintenance, thermodynamics, fluid mechanics, materials science, CAD/CAM, and robotics.</p><ul class="mini-list"><li><strong>Course structure:</strong> strong first-year basics, then mechanics / thermodynamics / materials / manufacturing, then heat transfer / design / hydraulics / CAD-CAM, then robotics, industrial engineering, automotive, HVAC, and project work.</li><li><strong>Lab facilities:</strong> Engineering Mechanics Lab, Thermal Engineering Lab, Fluid Mechanics Lab, Manufacturing Technology Lab, CAD/CAM Lab, Robotics Lab.</li><li><strong>Career routes:</strong> Mechanical Design Engineer, Production Engineer, Quality Control Engineer, Automotive Engineer, HVAC Engineer, CAD/CAM Specialist, Robotics Engineer.</li><li><strong>Achievement signal:</strong> SAE BAJA, Go-Kart, and related design challenges, plus placements into manufacturing and automotive firms.</li></ul></article><article class="card"><h3>Civil Engineering</h3><p>Civil Engineering is described through buildings, roads, bridges, water systems, structural design, geotechnics, transportation, environmental engineering, and construction management.</p><ul class="mini-list"><li><strong>Course structure:</strong> surveying / strength of materials / fluids / soil mechanics, then reinforced concrete / steel / highways / foundations / water resources / environmental engineering, then advanced design and construction-management topics.</li><li><strong>Lab facilities:</strong> Material Testing Lab, Surveying Lab, Structural Engineering Lab, Geotechnical Engineering Lab, Environmental Engineering Lab, CAD Lab.</li><li><strong>Career routes:</strong> Structural Engineer, Construction Manager, Geotechnical Engineer, Transportation Engineer, Environmental Engineer, Urban Planner, Site Engineer.</li><li><strong>Achievement signal:</strong> national design competitions and placements into construction, consulting, and government organisations.</li></ul></article></div></div></section><section class="section muted"><div class="container"><p class="section-label">Admissions alignment</p><div class="section-head"><h2>Programme information connects to admissions without duplicating the full admissions section.</h2><p>The live site also includes programme-level admission framing. A compact summary is enough here; the detailed process belongs on the admissions pages.</p></div><div class="cards cols-3 about-quality-grid"><article class="card"><div class="icon">01</div><h3>General eligibility</h3><p>Pass in 10+2 or equivalent with PCM subjects and minimum 50% aggregate marks, with 45% for reserved categories.</p></article><article class="card"><div class="icon">02</div><h3>Common admission route</h3><p>Eligibility check, application, entrance examination, counselling, and admission confirmation are summarised here and linked out.</p></article><article class="card"><div class="icon">03</div><h3>Related support</h3><p>Scholarship and fee questions route to Fees &amp; Scholarships and the admissions enquiry page instead of being expanded fully here.</p></article></div><div class="button-row"><a class="button primary" href="{href_from(page_path, '/admissions/process.html')}">Admission Process</a><a class="button secondary" href="{href_from(page_path, '/admissions/fees.html')}">Fees &amp; Scholarships</a></div></div></section>'''
    if page_path == 'academics/labs.html':
        return f'''<section class="section"><div class="container academic-spotlight"><div class="academic-spotlight-copy"><p class="section-label">Practical infrastructure</p><h2>Labs are one of the clearest academic proof points.</h2><p>The published lab story is already strong: computing, electronics, machines, structures, chemistry, physics, research, workshops, and innovation projects all appear on the current site.</p><ul class="mini-list"><li>Department-wise lab depth matters more than one generic lab claim</li><li>Infrastructure becomes believable when tied to actual teaching and experimentation</li><li>Practical spaces connect directly to programmes and employability</li></ul></div><div class="contact-panel"><h3>Why it matters</h3><p>Hands-on depth</p><p>Practical academic proof</p><p>Stronger programme credibility</p></div></div></section><section class="section muted"><div class="container"><p class="section-label">Department-wise facilities</p><div class="section-head"><h2>The lab page shows academic practice by discipline.</h2><p>The current site gives enough material to present labs as real learning environments rather than a flat facility list.</p></div><div class="cards cols-3 about-quality-grid"><article class="card card-featured"><div class="icon">CSE</div><h3>Computing &amp; software labs</h3><p>Computer Science Lab, programming environments, database work, network practice, AI/ML-adjacent computing, and software-development workflows.</p></article><article class="card"><div class="icon">ECE</div><h3>Electronics &amp; communication labs</h3><p>ECE Laboratory, communication systems, VLSI-oriented work, microcontrollers, DSP-style experimentation, and embedded-systems practice.</p></article><article class="card"><div class="icon">EEE</div><h3>Electrical systems labs</h3><p>Electrical machines, power systems, control systems, power electronics, measurement environments, and microprocessor-linked practical work.</p></article><article class="card"><div class="icon">ME</div><h3>Mechanical labs &amp; workshop</h3><p>Mechanical Engineering Lab, Mechanical Workshop, manufacturing setups, prototyping environments, and hands-on machinery training.</p></article><article class="card"><div class="icon">CE</div><h3>Civil &amp; core science support</h3><p>Structures- and materials-adjacent environments supported by physics, chemistry, surveying-style, and engineering-foundation practice spaces.</p></article><article class="card"><div class="icon">R&amp;D</div><h3>Research &amp; innovation spaces</h3><p>Research Laboratory, Innovation Projects, and the Atal Incubation Centre strengthen the move from coursework into experimentation and applied ideas.</p></article></div></div></section><section class="section"><div class="container"><p class="section-label">What students actually do here</p><div class="section-head"><h2>Labs are presented here as learning environments, not inventory.</h2><p>This page connects facility types to what students practice inside them.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">01</div><h3>Experiment</h3><p>Test circuits, code, machines, materials, and systems in structured lab settings.</p></article><article class="card"><div class="icon">02</div><h3>Build</h3><p>Move from theory into prototypes, workshop tasks, innovation projects, and applied assignments.</p></article><article class="card"><div class="icon">03</div><h3>Measure</h3><p>Use lab environments for observation, validation, troubleshooting, and engineering judgement.</p></article><article class="card"><div class="icon">04</div><h3>Prepare</h3><p>Translate practical familiarity into project readiness, internships, and stronger placement confidence.</p></article></div></div></section>'''
    if page_path == 'academics/scholarships.html':
        return f'''<section class="section"><div class="container placements-band"><div><p class="section-label">Access & support</p><h2>Scholarship support reinforces student confidence when eligibility and purpose are visible early.</h2><p>The Sai Prudent Scholarship is clearest when purpose, partners, and selection logic appear together and connect directly to admissions support.</p></div><div class="governance-list"><article><strong>Purpose</strong><span>Support deserving students from economically disadvantaged backgrounds.</span></article><article><strong>Partners</strong><span>Anahata Stiftung and RISE, Austria are named on the current site.</span></article><article><strong>Selection logic</strong><span>Merit, need, attendance, conduct, and participation shape eligibility.</span></article></div></div></section><section class="section muted"><div class="container"><p class="section-label">Scholarship snapshot</p><div class="section-head"><h2>The live site provides enough real data to make this page more useful.</h2><p>The redesign now shows the scholarship as an established support programme with visible scale and continuity.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">2010</div><h3>Established</h3><p>The Sai Prudent Scholarship is presented as a long-running programme started in 2010.</p></article><article class="card"><div class="icon">13+</div><h3>Years of legacy</h3><p>The current site frames the scholarship as an ongoing institutional commitment rather than a one-off campaign.</p></article><article class="card"><div class="icon">2800+</div><h3>Annual participation</h3><p>The programme is positioned with substantial annual student participation.</p></article><article class="card card-featured"><div class="icon">300+</div><h3>Total beneficiaries</h3><p>The published scholarship page gives a clear beneficiary signal that remains visible here.</p></article></div></div></section><section class="section"><div class="container"><p class="section-label">Eligibility</p><div class="section-head"><h2>Eligibility is presented as a practical scan-first checklist.</h2><p>The live page already names the key filters that matter for applicants and families.</p></div><div class="cards cols-2 about-quality-grid"><article class="card"><div class="icon">01</div><h3>Academic and financial basis</h3><p>Applicants are assessed through academic merit, consistent performance, and family income below the stated threshold.</p></article><article class="card"><div class="icon">02</div><h3>Student conduct and participation</h3><p>Regular attendance, good conduct, and extracurricular participation are explicitly part of the current eligibility framing.</p></article></div></div></section><section class="section muted"><div class="container"><p class="section-label">How to apply</p><div class="section-head"><h2>Application flow connects scholarship questions directly to admissions support.</h2><p>Families can use this page to see how scholarship questions fit into the wider admission journey.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">01</div><h3>Check fit</h3><p>Review merit, need, attendance, conduct, and participation expectations first.</p></article><article class="card"><div class="icon">02</div><h3>Prepare context</h3><p>Keep academic records and relevant financial-information proof ready for clarification.</p></article><article class="card"><div class="icon">03</div><h3>Contact admissions</h3><p>Use the admissions enquiry route to ask about scholarship support alongside programme admission.</p></article><article class="card"><div class="icon">04</div><h3>Selection review</h3><p>The current page frames final consideration around both merit and financial-need assessment.</p></article></div><div class="button-row"><a class="button primary" href="{href_from(page_path, '/admissions/enquiry.html')}">Ask about scholarship support</a><a class="button secondary" href="{href_from(page_path, '/admissions/fees.html')}">Fees &amp; Scholarships</a></div></div></section>'''
    if page_path == 'academics/rit.html':
        return f'''<section class="section"><div class="container"><p class="section-label">Program structure</p><div class="section-head"><h2>RIT appears here as a flagship pathway.</h2><p>The module structure is one of the clearest differentiators on the current site and is shown here as a structured, international, and deliberate learning route.</p></div><div class="cards cols-4 academic-program-grid"><article class="card"><div class="icon">M1</div><h3>Foundation</h3><p>Tools, communication habits, typing, and programming mindset.</p></article><article class="card"><div class="icon">M2</div><h3>Programming basics</h3><p>Introductory Java problem solving and core development practice.</p></article><article class="card"><div class="icon">M3</div><h3>Advanced assignments</h3><p>Longer Java assignments with more depth and complexity.</p></article><article class="card"><div class="icon">M4</div><h3>Industry transition</h3><p>Professional readiness and stronger real-world orientation.</p></article></div></div></section><section class="section muted"><div class="container placements-band"><div><p class="section-label">Why RIT stands out</p><h2>RIT is presented on the live site as more than a side programme.</h2><p>RIT is framed through Vienna-linked mentors, European software expertise, real projects, and a software-engineering pathway designed to feel different from a standard engineering add-on.</p></div><div class="governance-list"><article><strong>4-Year Pathway</strong><span>RIT is positioned as a long-form learning track, not a short certificate.</span></article><article><strong>Vienna Mentors</strong><span>European experts and mentor visibility are part of the public positioning.</span></article><article><strong>Real Projects</strong><span>The programme is framed around applied software work, not only theory.</span></article></div></div></section><section class="section"><div class="container"><p class="section-label">What students gain</p><div class="section-head"><h2>RIT shows outcomes as clearly as modules.</h2><p>The current site suggests a software-engineering route built around daily practice, collaboration habits, and real-world readiness.</p></div><div class="cards cols-3 about-quality-grid"><article class="card card-featured"><div class="icon">01</div><h3>Software-engineering mindset</h3><p>Students move from tools and typing discipline into programming logic, assignments, and structured delivery habits.</p></article><article class="card"><div class="icon">02</div><h3>International learning signal</h3><p>The Europe / Vienna / Graz connection makes RIT feel internationally mentored rather than locally isolated.</p></article><article class="card"><div class="icon">03</div><h3>Career readiness</h3><p>Real projects, GitHub-style workflow framing, and stronger applied habits support internship and employability positioning.</p></article></div></div></section><section class="section muted"><div class="container contact-layout"><div><p class="section-label">Who this pathway fits</p><h2>RIT is positioned for students who want more than a standard classroom path.</h2><p>It appeals to students interested in software practice, international academic connection, project work, and a more deliberate transition toward real engineering work.</p></div><div class="contact-panel"><h3>Best-fit signals</h3><p>Interest in software development</p><p>Comfort with structured, long-form learning</p><p>Motivation for projects and mentor-led growth</p></div></div></section>'''
    return ''


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
      {render_hero(path, cfg)}

      {render_homepage_snippet_sections(path, cfg)}
      {highlight_html}
      {render_custom_sections(path) or render_content(path, cfg['content'])}

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
