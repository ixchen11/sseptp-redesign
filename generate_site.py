from pathlib import Path
from html import escape
import os
import json

ROOT = Path('/root/.openclaw/workspace/sseptp-redesign')

SITE = {
    'title': 'Sanskrithi School of Engineering',
    'email': 'info@sseptp.org',
    'domain': 'https://sseptp.org',
    'tagline': 'Modern engineering education for ambitious students',
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
        ('Scholarships', '/academics/scholarships.html', 'Support for student progression'),
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
        'title': 'Admissions Open 2026 | Modern Engineering Education',
        'description': 'Explore admissions, academics, campus life, global pathways, placements, and student-first engineering education at Sanskrithi School of Engineering.',
        'hero_kicker': 'Admissions Open 2026',
        'hero_title': 'A flagship digital experience for a future-facing engineering school.',
        'hero_text': 'Sanskrithi School of Engineering should feel ambitious, credible, and alive. This redesign turns the website into a modern admissions and trust platform built around how students and families actually decide.',
        'hero_badges': ['Autonomous', 'Andhra Pradesh', 'NAAC quality story', 'Placement-first visibility'],
        'hero_stats': [('600+', 'Offers highlighted on the current site'), ('80+', 'Corporate partners referenced'), ('95%', 'Placement rate claim retained'), ('19.6 LPA', 'High-value internship claim surfaced')],
        'highlights': [('Student-first UX', 'Clear pathways for enquiry, programs, campus life, and placements.'), ('Content depth', 'Existing school content is preserved and reorganized, not flattened.'), ('Modern credibility', 'A stronger visual system, richer page hierarchy, and SEO-aware structure.')],
        'hero_image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDBpSzTY3Q1ZpoTD-XEZOPsQgsVFTXmYyvvZ_vs6rfJ9FroP7GUJnT03jhrCnrvK8r9n28D5r_znI_vpXdfYpv_hD6q0fCZJUEOTj2lyKXDbbnS1lwMrK5DMow5Uq-jxEeR-iGXclXChuZMO5OTmmelstgo9gmPrioIGFzOTtFEse6vuCAMqUj--XQcdxxUffgUVXlif5w1M78bXd7P1uReJESyfkiw-5w6eOPpUqoHtOOXlkaKtQ8cZBcp6WhKhjU0w35IAScUFLs',
        'service_cards': [( 'Academic Excellence', 'Build strong foundations through modern engineering education, faculty support, and structured academic growth.', '/academics/index.html'), ('Career-Ready Programs', 'Programs, labs, and industry-facing pathways that prepare students for real opportunities.', '/academics/programs.html'), ('Transition to Industry', 'Placements, mentoring, and employability support designed to help students move forward confidently.', '/placements/index.html')],
        'news_items': [('Admissions Open 2026', 'Explore admissions, process, fees, and enquiry options in a much clearer student-friendly structure.', '/admissions/index.html', 'https://lh3.googleusercontent.com/aida-public/AB6AXuCDdGlk7sV3wNJDcmjjkVoUmrtDenQX-texqwsRNC-LgSaiuEfsQVXQuUd14MR9NyIRbI_xy77XNwBupPOHoxXZJm_OHpW33LId6_KKn4vVkgbJF759qb6Nx_KKeRxPqQgRgKZ5bFrJZFey4KeXUIYU52VTyyHuOQ__vXr-Zl3vhQVkjQm5nNRFkkHCc9Afsuf6rie7Pm8Jl1gjFeO0Gvx1ZQ8xqq5knoGHXdm_W85qRoHooXootkB7qsKvAx-hEExWkP9fWcUgxj4'), ('Placements & Global Pathways', 'See how placements, RIT, and industry-aligned learning are now positioned as major strengths of the school.', '/placements/index.html', 'https://lh3.googleusercontent.com/aida-public/AB6AXuAOG3A6GF1aUHRC5VsaczxMpKFwGiakGMk5gZcYud30YgIm10lClKKmU9BwGCbkxlzQfh641mu3i7XudQ5_iKMqBhqRqH6hj1ITHQywtidTM69egOxiycQF_ZjP2NqriF_pBpQRLc1u1q-E5ItG9uYMPLICE4tRRnb3GxnNymGnmofpuN3v5yX-5yehDXdsLqjtSzUsBZtswfi5cOxflv_DADKdJ6UPUBjQja0bhi4Bhl1-oxjytbcJqWKYzRqPkD3BeY2ozweN0_c')],
        'content': [
            {'type': 'feature_grid', 'kicker': 'Explore the School', 'title': 'The homepage now guides four high-intent journeys immediately.', 'text': 'Instead of hiding key information in menus or a single long scroll, the site now routes people into the decisions they actually need to make.', 'cards': [
                ('Admissions', 'Overview, process, fees, and enquiry now sit in one clean stream.', '/admissions/index.html'),
                ('Academics', 'Programs, labs, scholarships, and the RIT / Europe-facing pathway.', '/academics/index.html'),
                ('Campus Life', 'Facilities, hostel, wellbeing, sports, and student experience.', '/campus/index.html'),
                ('Placements', 'Outcomes, success stories, recruiter trust, and readiness.', '/placements/index.html'),
            ]},
            {'type': 'metrics_band', 'items': [('24', 'structured pages'), ('5', 'core school pillars'), ('1', 'clear brand system'), ('0', 'needless dead-end navigation')]},
            {'type': 'split', 'kicker': 'Why this works', 'title': 'It looks more modern, but the bigger win is decision clarity.', 'text': 'Good school UX is not decoration. It reduces doubt, shortens the path to enquiry, and helps parents and students find trust signals quickly.', 'bullets': ['Admissions path is clearer and easier to act on', 'Academics and differentiators are easier to compare', 'Campus and wellbeing content feels more vivid', 'Placements and quality signals carry more weight']},
            {'type': 'quote_panel', 'kicker': 'Positioning', 'title': 'The school already had strong raw material.', 'text': 'Admissions Open 2026, autonomous positioning, NAAC story, RIT messaging, placement proof, hostel life, and quality governance were all present in the current site. The redesign gives those strengths a sharper stage.'},
        ],
    },
    'about/index.html': {
        'section': 'About',
        'title': 'About the School',
        'description': 'Learn about Sanskrithi School of Engineering, its identity, values, quality focus, and institutional direction.',
        'hero_kicker': 'About SSE',
        'hero_title': 'Shaping engineers for tomorrow’s world.',
        'hero_text': 'The school is positioned as a premier engineering institution in Andhra Pradesh focused on academic excellence and holistic student development. This page makes that story easier to understand and easier to trust.',
        'hero_stats': [('15+', 'years impression referenced in current content'), ('4', 'institutional trust pillars'), ('1', 'clear school narrative'), ('100%', 'better visibility of quality signals')],
        'content': [
            {'type': 'feature_grid', 'kicker': 'Inside About', 'title': 'Institutional content now has a cleaner architecture.', 'text': 'Instead of scattering school identity across disconnected pages, the new About section creates a stronger narrative flow.', 'cards': [
                ('Vision & Mission', 'Core purpose, values, and engineering direction.', '/about/vision-mission.html'),
                ('Leadership', 'Chairman, principal, dean, secretary, and institutional voice.', '/about/leadership.html'),
                ('Quality & Recognition', 'NAAC, IQAC, committees, and governance signals.', '/about/quality.html'),
                ('Industry Interface', 'How academics stay connected to real-world practice.', '/about/industry-interface.html'),
            ]},
            {'type': 'story_cards', 'kicker': 'Institutional Value', 'title': 'What students and families should feel from this section.', 'items': [('Confidence', 'The school looks organized, serious, and future-aware.'), ('Clarity', 'Important institutional information is easier to find.'), ('Trust', 'Recognition, quality systems, and leadership are more visible.') ]},
        ],
    },
    'about/vision-mission.html': {
        'section': 'About',
        'title': 'Vision & Mission',
        'description': 'Vision, mission, values, and educational direction at Sanskrithi School of Engineering.',
        'hero_kicker': 'Vision & Mission',
        'hero_title': 'Academic purpose should feel clear, modern, and credible.',
        'hero_text': 'This page gives the school a proper place to articulate long-term educational direction, student development goals, and engineering ethos.',
        'content': [
            {'type': 'split', 'kicker': 'Direction', 'title': 'A clearer home for institutional intent.', 'text': 'The current site already signals seriousness through accreditation, leadership messaging, and employability themes. This page gathers those signals into one coherent story.', 'bullets': ['Student growth alongside technical excellence', 'Industry relevance without losing academic depth', 'Engineering education for future careers', 'Holistic development beyond classroom performance']},
            {'type': 'story_cards', 'kicker': 'Design intent', 'title': 'The UX goal here is confidence, not noise.', 'items': [('Readable', 'Shorter sections and stronger hierarchy improve scanability.'), ('Trustworthy', 'Values and mission feel more substantial when given space.'), ('Shareable', 'This page becomes a useful reference for parents and academic stakeholders.')]},
        ],
    },
    'about/leadership.html': {
        'section': 'About',
        'title': 'Leadership',
        'description': 'Leadership, institutional messages, and school guidance.',
        'hero_kicker': 'Leadership',
        'hero_title': 'Leadership content should feel human, grounded, and visible.',
        'hero_text': 'The current site contains multiple leadership pages. Here they become one coherent leadership hub that feels more intentional and easier to navigate.',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Leadership Pages', 'title': 'Existing leadership content now belongs to one coordinated section.', 'text': 'This creates stronger continuity between governance, academic quality, and student-facing communication.', 'cards': [
                ('Chairman Message', 'Leadership voice and institutional direction.', '#'),
                ('Principal Message', 'Academic leadership and student-facing school vision.', '#'),
                ('Dean Message', 'Learning standards, programs, and delivery quality.', '#'),
                ('Secretary Message', 'Institutional stewardship and administration.', '#'),
            ]},
            {'type': 'quote_panel', 'kicker': 'UX note', 'title': 'This section should reassure, not overwhelm.', 'text': 'Leadership pages often become overly formal and hard to scan. The new structure uses clearer grouping and simpler progression so the content feels more approachable.'},
        ],
    },
    'about/quality.html': {
        'section': 'About',
        'title': 'Quality, NAAC & Recognition',
        'description': 'NAAC, IQAC, recognition, committees, and school quality systems.',
        'hero_kicker': 'Quality & Recognition',
        'hero_title': 'Quality systems are trust assets. They should not hide in the footer of the experience.',
        'hero_text': 'The current site contains real quality-assurance content including NAAC, IQAC, committees, and recognition. This redesign gives those signals the visibility they deserve.',
        'hero_stats': [('NAAC', 'A-grade story surfaced'), ('IQAC', 'continuous improvement positioning'), ('Committees', 'governance made visible'), ('Recognition', 'credibility kept discoverable')],
        'content': [
            {'type': 'feature_grid', 'kicker': 'Quality Framework', 'title': 'Quality is broader than a single badge or PDF link.', 'text': 'The strongest academic brands make their systems feel visible, active, and coherent.', 'cards': [
                ('NAAC', 'Current site messaging explicitly references NAAC A-grade quality focus.', '#'),
                ('IQAC', 'Internal quality improvement content remains visible and central.', '#'),
                ('Committees', 'Academic audit and industry interaction stay connected to trust.', '#'),
                ('Recognition', 'Affiliation and recognition continue to reinforce credibility.', '#'),
            ]},
            {'type': 'split', 'kicker': 'SEO value', 'title': 'This content also matters for search visibility.', 'text': 'Prospective families and students often search for accreditation, recognition, and official quality information. Making those topics clearer improves both trust and discoverability.', 'bullets': ['Better title and metadata targeting', 'Clearer topical relevance for quality queries', 'More meaningful internal linking across school pages', 'Improved scanability for official-information pages']},
        ],
    },
    'about/industry-interface.html': {
        'section': 'About',
        'title': 'Industry Interface',
        'description': 'Industry exposure, relevance, and academic-to-career connection.',
        'hero_kicker': 'Industry Interface',
        'hero_title': 'Students need to see the bridge between learning and work.',
        'hero_text': 'The current site already leans into industry relevance through placements, partner references, and Europe-facing program claims. This page gives that story more shape and intent.',
        'content': [
            {'type': 'split', 'kicker': 'Why it matters', 'title': 'Industry relevance becomes a visible institutional promise.', 'text': 'This is where the school can connect curriculum, mentorship, internships, software pathways, placement preparation, and project-based exposure into one stronger message.', 'bullets': ['Industry leaders referenced in placement messaging', 'Curriculum aligned with employability outcomes', 'Real-world training and project orientation', 'A clearer bridge between academics and careers']},
            {'type': 'story_cards', 'kicker': 'Student lens', 'title': 'This page answers the practical question behind most admissions decisions.', 'items': [('Will I be job-ready?', 'That question needs a visible answer.'), ('Will learning be practical?', 'Industry interface helps make that believable.'), ('Will the school feel connected to the real world?', 'This is where that credibility becomes tangible.')]},
        ],
    },
    'admissions/index.html': {
        'section': 'Admissions',
        'title': 'Admissions Overview 2026',
        'description': 'Admissions overview, eligibility, enquiry, and next steps for 2026.',
        'hero_kicker': 'Admissions Open 2026',
        'hero_title': 'A cleaner admissions path builds trust before a single call is made.',
        'hero_text': 'The current site already contains overview, process, form, fee, and enquiry routes. The redesign turns those pieces into one coherent admissions journey.',
        'hero_badges': ['Overview', 'Process', 'Fees', 'Enquiry'],
        'content': [
            {'type': 'feature_grid', 'kicker': 'Admissions Journey', 'title': 'Everything a student looks for is now grouped together.', 'text': 'The structure reflects the current site’s own content tree, but in a cleaner and more conversion-friendly order.', 'cards': [
                ('Admission Process', 'Step-by-step flow from interest to application.', '/admissions/process.html'),
                ('Fees & Scholarships', 'Cost visibility and support information.', '/admissions/fees.html'),
                ('Admission Enquiry', 'Lead capture and contact path.', '/admissions/enquiry.html'),
                ('Programs First', 'Route students back to academics when they need fit before applying.', '/academics/programs.html'),
            ]},
            {'type': 'timeline', 'kicker': 'Expected path', 'title': 'Good admissions UX reduces uncertainty.', 'text': 'When structure is clearer, students ask better questions and are more likely to move forward confidently.', 'steps': ['Discover the right academic pathway.', 'Check eligibility, timing, and documents.', 'Review fees, support, and scholarships.', 'Submit enquiry or continue to the application route.']},
        ],
    },
    'admissions/process.html': {
        'section': 'Admissions',
        'title': 'Admission Process',
        'description': 'Admission process, decision flow, and next steps for students.',
        'hero_kicker': 'Admission Process',
        'hero_title': 'The process should feel simple, not hidden inside the website.',
        'hero_text': 'This page gives a proper home to the school’s process content so students do not need to guess what happens next.',
        'content': [
            {'type': 'timeline', 'kicker': 'How to Apply', 'title': 'A more useful structure for the current admissions routes.', 'text': 'The current site has both process and form-related paths. This page turns them into one understandable sequence.', 'steps': ['Choose the right program and confirm fit.', 'Check eligibility and prepare the right documents.', 'Understand fees, support, and scholarship options.', 'Submit enquiry or application and move toward counselling.']},
            {'type': 'quote_panel', 'kicker': 'UX principle', 'title': 'Process pages should lower stress.', 'text': 'Parents and students rarely want marketing language here. They want clarity, confidence, and a sense that the institution is organized.'},
        ],
    },
    'admissions/fees.html': {
        'section': 'Admissions',
        'title': 'Fees & Scholarships',
        'description': 'Fees, affordability, and scholarship support for prospective students.',
        'hero_kicker': 'Fees & Scholarships',
        'hero_title': 'Financial clarity reduces friction and improves trust.',
        'hero_text': 'The old site separates fees and scholarship content. This new page brings them into the same decision space, where families actually need them.',
        'content': [
            {'type': 'split', 'kicker': 'Family confidence', 'title': 'Affordability information belongs close to admissions decisions.', 'text': 'On many college sites, cost-related information is too hard to find. This page gives it real visibility and ties it to scholarship support more naturally.', 'bullets': ['Fee structure visibility', 'Scholarship opportunities', 'Program-wise cost clarity', 'Admission support and counselling context']},
            {'type': 'story_cards', 'kicker': 'Why this page matters', 'title': 'Clarity here can strongly affect conversion.', 'items': [('Less uncertainty', 'Students and parents are more likely to reach out.'), ('Better fit', 'Financial questions become easier to raise earlier.'), ('Stronger UX', 'The site feels transparent and better organized.')]},
        ],
    },
    'admissions/enquiry.html': {
        'section': 'Admissions',
        'title': 'Admission Enquiry',
        'description': 'Admission enquiry, support, and next steps for prospective students.',
        'hero_kicker': 'Admission Enquiry',
        'hero_title': 'Interest should turn into action without confusion or dead ends.',
        'hero_text': 'The current site includes enquiry and form routes. This page becomes the conversion hub for both.',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Best next steps', 'title': 'This page should convert curiosity into contact.', 'text': 'A strong enquiry page should be clear, reassuring, and low-friction.', 'cards': [
                ('Talk to Admissions', 'Phone, email, and response expectations.', '#'),
                ('Share Your Interest', 'Program, background, and preferred contact mode.', '#'),
                ('Ask About Eligibility', 'Clarify intake, timelines, and required documents.', '#'),
                ('Continue to Application', 'Move toward the official form if ready.', '#'),
            ]},
            {'type': 'cta_strip', 'title': 'Need help choosing a program first?', 'text': 'Students who are not ready to enquire yet should not get stuck. Route them back into the academic discovery flow.', 'primary': ('Explore Programs', '/academics/programs.html'), 'secondary': ('Admissions Overview', '/admissions/index.html')},
        ],
    },
    'academics/index.html': {
        'section': 'Academics',
        'title': 'Academics Overview',
        'description': 'Programs, labs, scholarships, and academic pathways at Sanskrithi School of Engineering.',
        'hero_kicker': 'Academics',
        'hero_title': 'Programs, labs, and learning pathways deserve a stronger academic stage.',
        'hero_text': 'The current site already contains all-programs, undergraduate, M.Tech, CSE detail, courses, labs, and scholarship routes. This section turns them into one coherent academic hub.',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Academic Navigation', 'title': 'The new structure reflects the current academic content more honestly.', 'text': 'Instead of a generic programs section, this site now gives different academic decisions their own clearer pages.', 'cards': [
                ('Programs', 'Undergraduate, M.Tech, and department-level pathways.', '/academics/programs.html'),
                ('Labs', 'Hands-on infrastructure and applied learning spaces.', '/academics/labs.html'),
                ('Scholarships', 'Academic support and accessibility signals.', '/academics/scholarships.html'),
                ('RIT Pathway', 'The Europe / Vienna / software differentiator.', '/academics/rit.html'),
            ]},
            {'type': 'metrics_band', 'items': [('CSE', 'department detail found'), ('4 Years', 'visible CSE duration'), ('120', 'CSE seats referenced'), ('10+2', 'eligibility reference found')]},
        ],
    },
    'academics/programs.html': {
        'section': 'Academics',
        'title': 'Programs',
        'description': 'Programs, departments, and academic pathways.',
        'hero_kicker': 'Programs',
        'hero_title': 'Program information should guide fit, not overwhelm it.',
        'hero_text': 'The current site explicitly includes all-programme, undergraduate, M.Tech, and department-specific routes like CSE. This page gives those options a cleaner and more premium academic home.',
        'hero_stats': [('CSE', 'department route surfaced'), ('4 Years', 'duration shown in source content'), ('120', 'seats found in current bundle'), ('AI/ML', 'specialization language retained')],
        'content': [
            {'type': 'feature_grid', 'kicker': 'Program signals from the current site', 'title': 'There is already real academic substance to build on.', 'text': 'At least one department route already contains structured detail. That gives this redesign a stronger academic base than a generic brochure rewrite.', 'cards': [
                ('Computer Science & Engineering', 'Advanced programming labs, AI and machine learning, industry partnerships, and modern software development methodologies.', '#'),
                ('Undergraduate Routes', 'A clearer home for all B.Tech pathways and student decision support.', '#'),
                ('M.Tech Routes', 'Advanced study options should stand alongside undergraduate choices.', '#'),
                ('Courses Overview', 'A stronger summary layer above detailed department pages.', '#'),
            ]},
            {'type': 'story_cards', 'kicker': 'Program UX', 'title': 'A great academics page balances aspiration with usability.', 'items': [('Easy comparison', 'Students can scan broad choices before diving deeper.'), ('Sharper messaging', 'Department value feels more intentional and modern.'), ('Better SEO', 'Programs become clearer topical destinations for search intent.')]},
        ],
    },
    'academics/labs.html': {
        'section': 'Academics',
        'title': 'Labs & Applied Learning',
        'description': 'Laboratories, applied learning, and practical engineering education.',
        'hero_kicker': 'Labs & Applied Learning',
        'hero_title': 'Practical learning deserves visual and structural weight.',
        'hero_text': 'The current site includes a dedicated labs route. This page turns that into a stronger academic selling point for modern engineering education.',
        'content': [
            {'type': 'split', 'kicker': 'Hands-on depth', 'title': 'Labs are where engineering becomes real.', 'text': 'Students and families evaluate labs as proof that learning is practical. This page creates room for facilities, equipment, project work, demos, and discipline-specific lab stories.', 'bullets': ['Department labs and workshop spaces', 'Applied problem-solving environments', 'Project-based and practical learning', 'Stronger visual storytelling potential']},
            {'type': 'quote_panel', 'kicker': 'Design note', 'title': 'This page should eventually become highly visual.', 'text': 'Labs are one of the best opportunities to lift the school’s perceived quality through strong photography, diagrams, and project evidence.'},
        ],
    },
    'academics/scholarships.html': {
        'section': 'Academics',
        'title': 'Scholarships',
        'description': 'Scholarship pathways and academic support for students.',
        'hero_kicker': 'Scholarships',
        'hero_title': 'Support options should be easy to find, not hidden in navigation.',
        'hero_text': 'The existing scholarship route is important enough to keep as its own page. It helps families understand that access and affordability matter here too.',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Support Signals', 'title': 'Scholarship content works best when it is practical and direct.', 'text': 'This page can later hold merit support, need-based guidance, special categories, and application instructions.', 'cards': [
                ('Eligibility', 'Who can apply and on what basis.', '#'),
                ('Application Support', 'When and how to request scholarship guidance.', '#'),
                ('Merit Recognition', 'Academic achievement and excellence pathways.', '#'),
                ('Affordability Clarity', 'How support connects to fees and admissions.', '#'),
            ]},
            {'type': 'cta_strip', 'title': 'Need financial context first?', 'text': 'This page should work naturally with fees and admissions, not live in isolation.', 'primary': ('Fees & Scholarships', '/admissions/fees.html'), 'secondary': ('Admissions Overview', '/admissions/index.html')},
        ],
    },
    'academics/rit.html': {
        'section': 'Academics',
        'title': 'RIT / Europe Pathway',
        'description': 'RIT, Vienna mentors, European software exposure, and career-ready learning.',
        'hero_kicker': 'RIT / Europe Pathway',
        'hero_title': 'The Europe-facing software story is a differentiator. It deserves its own premium space.',
        'hero_text': 'The current site strongly emphasizes Europe, Vienna mentors, real-world training, and software-focused learning. Instead of burying that in homepage slides, the redesign turns it into a dedicated academic pathway page.',
        'hero_badges': ['Europe-facing', 'Vienna mentors', 'Real projects', 'Software career lens'],
        'content': [
            {'type': 'feature_grid', 'kicker': 'Current messaging preserved', 'title': 'This content already exists on the current site and should remain highly visible.', 'text': 'Rather than shrinking it into one marketing line, the redesign gives it context and room.', 'cards': [
                ('Europe to India', '“We Brought Europe to India | For You”', '#'),
                ('European Experts', '“Learn From European Software Experts. Every Day”', '#'),
                ('Vienna Mentors', '“4-Year RIT Program | Vienna Mentors | Real Projects | Java to GitHub”', '#'),
                ('Career Relevance', 'A clearer bridge from academic story to employability story.', '#'),
            ]},
            {'type': 'story_cards', 'kicker': 'Brand value', 'title': 'This page is one of the strongest visual and strategic differentiators on the site.', 'items': [('Distinctive', 'It gives the school a story that feels more memorable.'), ('Future-oriented', 'The software and global angle feels youthful and ambitious.'), ('SEO-useful', 'It creates a clearer landing page for RIT / Europe-themed interest.')]},
        ],
    },
    'campus/index.html': {
        'section': 'Campus Life',
        'title': 'Campus Life Overview',
        'description': 'Student life, facilities, hostel, wellbeing, and sports at Sanskrithi School of Engineering.',
        'hero_kicker': 'Life @ SSE',
        'hero_title': 'Campus life should feel vibrant, welcoming, and worth joining.',
        'hero_text': 'The current site already has a richer student-life structure than most simple college websites. This redesign gives it the visibility and emotional energy it deserves.',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Campus Sections', 'title': 'Student experience already existed in the old site. Now it is easier to discover.', 'text': 'Life overview, facilities, hostel life, health & safety, and sports all sit in one cleaner section tree.', 'cards': [
                ('Facilities', 'Academic and on-campus infrastructure in one clearer destination.', '/campus/facilities.html'),
                ('Hostel Life', 'Accommodation, food, recreation, and student comfort.', '/campus/hostel.html'),
                ('Health & Safety', 'A visible space for wellbeing and trust.', '/campus/health-safety.html'),
                ('Sports', 'Student activity, balance, and youthful energy beyond the classroom.', '/campus/sports.html'),
            ]},
            {'type': 'quote_panel', 'kicker': 'Experience matters', 'title': 'A good campus section should help students imagine belonging here.', 'text': 'This part of the website does more than inform. It builds emotional confidence around the school experience.'},
        ],
    },
    'campus/facilities.html': {
        'section': 'Campus Life',
        'title': 'Facilities',
        'description': 'Academic and campus facilities that shape the student experience.',
        'hero_kicker': 'Facilities',
        'hero_title': 'Facilities help students picture their daily life here.',
        'hero_text': 'The original site separates academic facilities and campus facilities. The new structure lets them work together while still allowing more detailed content blocks underneath.',
        'content': [
            {'type': 'split', 'kicker': 'What belongs here', 'title': 'A stronger home for environment and infrastructure.', 'text': 'This page can combine classrooms, labs, campus resources, learning spaces, support spaces, and infrastructure that shapes confidence in the school.', 'bullets': ['Academic facilities and learning spaces', 'On-campus support infrastructure', 'Study environment and accessibility', 'A stronger photo-led storytelling layer']},
            {'type': 'story_cards', 'kicker': 'Perception', 'title': 'Facilities pages strongly influence quality perception.', 'items': [('Visible resources', 'Students want to see where learning happens.'), ('Campus confidence', 'Parents want reassurance about environment and support.'), ('Brand uplift', 'High-quality facility pages make the institution feel more established.')]},
        ],
    },
    'campus/hostel.html': {
        'section': 'Campus Life',
        'title': 'Hostel Life',
        'description': 'Hostel life, accommodation, food, and student comfort.',
        'hero_kicker': 'Hostel Life',
        'hero_title': 'Hostel content should reassure both students and families.',
        'hero_text': 'The current site already mentions comfortable accommodations, nutritious mess food, recreation rooms, and 24/7 security. Those are exactly the right trust points to preserve and sharpen.',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Current hostel signals', 'title': 'The existing hostel messaging already has the right instincts.', 'text': 'The redesign simply gives that content stronger presentation and clearer discoverability.', 'cards': [
                ('Comfortable Accommodations', 'A grounded and supportive living environment for students.', '#'),
                ('Nutritious Mess Food', 'Daily life support matters in real decision-making.', '#'),
                ('Recreation Rooms', 'Community and student comfort beyond classes.', '#'),
                ('24/7 Security', 'A high-value reassurance signal for families.', '#'),
            ]},
            {'type': 'quote_panel', 'kicker': 'Why this converts', 'title': 'Accommodation content often carries more emotional weight than brochures expect.', 'text': 'When students move away from home, hostel trust becomes a major part of the admissions experience.'},
        ],
    },
    'campus/health-safety.html': {
        'section': 'Campus Life',
        'title': 'Health & Safety',
        'description': 'Health, safety, and student wellbeing on campus.',
        'hero_kicker': 'Health & Safety',
        'hero_title': 'Safety information should be visible, calm, and confidence-building.',
        'hero_text': 'Because the current site already includes health and safety as a dedicated route, the redesign keeps it visible and student-centered.',
        'content': [
            {'type': 'split', 'kicker': 'Why it matters', 'title': 'Wellbeing content supports trust and conversion.', 'text': 'Health and safety content helps families understand that student care is taken seriously. It also helps the school appear more complete and responsible.', 'bullets': ['Campus safety information', 'Student support and wellbeing', 'Residential reassurance', 'Operational readiness and care']},
            {'type': 'story_cards', 'kicker': 'Tone', 'title': 'The goal here is reassurance without alarm.', 'items': [('Clear', 'Students find what they need quickly.'), ('Calm', 'The content tone supports trust.'), ('Complete', 'The school feels more prepared and professional.')]},
        ],
    },
    'campus/sports.html': {
        'section': 'Campus Life',
        'title': 'Sports & Student Activities',
        'description': 'Sports, student activities, clubs, and campus energy.',
        'hero_kicker': 'Sports & Activities',
        'hero_title': 'A youthful school brand needs visible energy and momentum.',
        'hero_text': 'Sports and student activities make the institution feel alive. This page gives that side of the school a more expressive, modern role in the experience.',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Student energy', 'title': 'Beyond academics, the site should show movement and participation.', 'text': 'A modern school website should not feel static. This page helps communicate confidence, community, and balance.', 'cards': [
                ('Sports Culture', 'Competitive and recreational student participation.', '#'),
                ('Events', 'Inter-college, campus, and community events.', '#'),
                ('Clubs', 'Technical, cultural, and leadership communities.', '#'),
                ('Student Confidence', 'Growth through teamwork, discipline, and visibility.', '#'),
            ]},
            {'type': 'quote_panel', 'kicker': 'Brand impact', 'title': 'This page makes the school feel younger and more alive.', 'text': 'That matters because emotional perception often decides whether a school feels exciting or forgettable.'},
        ],
    },
    'placements/index.html': {
        'section': 'Placements',
        'title': 'Placements Overview',
        'description': 'Placement outcomes, recruiters, success stories, and career readiness.',
        'hero_kicker': 'Placements',
        'hero_title': 'Career outcomes are one of the strongest stories on the current site. Now they look like it.',
        'hero_text': 'The current site surfaces strong placement marketing: 600+ offers, 80+ corporate partners, 95% placement rate, and curriculum design by industry leaders. The redesign gives that story a stronger and more premium structure.',
        'hero_stats': [('600+', 'Offers'), ('80+', 'Corporate partners'), ('95%', 'Placement rate'), ('19.6 LPA', 'internship claim found in source site')],
        'content': [
            {'type': 'feature_grid', 'kicker': 'Placement Structure', 'title': 'Placement content becomes a real section, not just a homepage slide.', 'text': 'Students, parents, and recruiters can now move through the placement story with more confidence.', 'cards': [
                ('Placement Story', 'Overview of outcomes, preparation, and employer trust.', '/placements/index.html'),
                ('Success Stories', 'Proof through named journeys and student results.', '/placements/success-stories.html'),
                ('Placement Contact', 'A clear path for recruiter or student enquiry.', '/placements/contact.html'),
                ('Academics Link', 'Tighter connection back to programs and industry interface.', '/academics/rit.html'),
            ]},
            {'type': 'story_cards', 'kicker': 'Why it performs', 'title': 'Placement pages influence both trust and aspiration.', 'items': [('Students', 'want confidence that outcomes are real.'), ('Parents', 'look for return on effort and investment.'), ('Recruiters', 'respond better to clear professional presentation.')]},
        ],
    },
    'placements/success-stories.html': {
        'section': 'Placements',
        'title': 'Success Stories',
        'description': 'Student outcomes, testimonials, and placement success stories.',
        'hero_kicker': 'Success Stories',
        'hero_title': 'Outcomes feel stronger when students can imagine themselves in them.',
        'hero_text': 'The current site already includes success-story style placement content and testimonial language. This page gives that proof a cleaner, more premium destination.',
        'content': [
            {'type': 'feature_grid', 'kicker': 'What this page should prove', 'title': 'Success stories should be specific, aspirational, and credible.', 'text': 'The extracted current-site content already uses testimonial-style proof points. The new design turns that into a stronger narrative format.', 'cards': [
                ('Dream Outcomes', 'Aspirational but believable examples of student success.', '#'),
                ('Training Impact', 'How curriculum and placement preparation contributed.', '#'),
                ('Industry Readiness', 'Projects, confidence, and interview preparation.', '#'),
                ('Progression Stories', 'Employment, internships, and higher-growth pathways.', '#'),
            ]},
            {'type': 'quote_panel', 'kicker': 'Trust principle', 'title': 'Specificity creates credibility.', 'text': 'Well-structured success stories can become some of the highest-performing pages on a school site because they answer the question: what happens after admission?'}
        ],
    },
    'placements/contact.html': {
        'section': 'Placements',
        'title': 'Placement Contact',
        'description': 'Placement contact for recruiters, students, and partnership enquiries.',
        'hero_kicker': 'Placement Contact',
        'hero_title': 'Recruiter and placement enquiries need a direct, professional path.',
        'hero_text': 'The current site includes a placement contact route. This dedicated page makes the school feel easier to work with and better organized.',
        'content': [
            {'type': 'split', 'kicker': 'Who this helps', 'title': 'This page serves both opportunity and trust.', 'text': 'Placement contact is useful for recruiters, students, and parents. It signals openness, confidence, and a functioning career-support structure.', 'bullets': ['Recruiter enquiries', 'Student placement support', 'Internship and partnership conversations', 'Career cell visibility']},
            {'type': 'cta_strip', 'title': 'Looking for outcomes first?', 'text': 'Users should be able to move naturally between proof and contact.', 'primary': ('Success Stories', '/placements/success-stories.html'), 'secondary': ('Placements Overview', '/placements/index.html')},
        ],
    },
    'contact.html': {
        'section': 'Contact',
        'title': 'Contact & Enquiry',
        'description': 'Contact Sanskrithi School of Engineering for admissions, academics, and institutional queries.',
        'hero_kicker': 'Contact SSE',
        'hero_title': 'A serious school website needs contact routes that feel intentional.',
        'hero_text': 'This page gives admissions, academic, placement, and institutional conversations a clearer front door instead of leaving contact as a footer afterthought.',
        'content': [
            {'type': 'feature_grid', 'kicker': 'Contact Routes', 'title': 'Different users need different next steps.', 'text': 'This page can later expand with forms, department contacts, maps, office hours, and phone numbers.', 'cards': [
                ('Admissions Enquiry', 'For students and families beginning the process.', '/admissions/enquiry.html'),
                ('Placement Contact', 'For recruiter and career-cell conversations.', '/placements/contact.html'),
                ('Academic Questions', 'Route deeper program questions to academics.', '/academics/index.html'),
                ('General Information', 'Institutional queries, visits, and campus contact.', '#'),
            ]},
            {'type': 'story_cards', 'kicker': 'UX value', 'title': 'Contact should feel easy, not generic.', 'items': [('More confidence', 'Clear next steps reduce hesitation.'), ('Better routing', 'Users land in the right conversation faster.'), ('Higher trust', 'The school feels more operationally mature.')]},
        ],
    },
}

STYLE = r'''
:root{--navy:#001A3D;--navy-2:#0d2d61;--navy-3:#173d7d;--orange:#F27405;--orange-2:#ff9b3d;--orange-3:#ffd2ad;--ink:#162230;--muted:#64748b;--line:rgba(0,26,61,.1);--surface:#ffffff;--surface-2:#f8fbff;--surface-3:#fff7ef;--shadow-xl:0 28px 80px rgba(0,26,61,.16);--shadow-lg:0 18px 42px rgba(0,26,61,.10);--radius-xl:30px;--radius-lg:22px;--radius-md:16px;--container:1180px}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,system-ui,sans-serif;color:var(--ink);background:linear-gradient(180deg,#fffaf6 0%,#fff 16%,#f8fbff 100%);line-height:1.68}img{display:block;max-width:100%}a{-webkit-tap-highlight-color:transparent}.container{width:min(calc(100% - 2rem),var(--container));margin:0 auto}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.site-header{position:sticky;top:0;z-index:80;background:var(--navy);color:#fff;box-shadow:0 10px 24px rgba(0,0,0,.08)}.nav-wrap,.footer-wrap,.section-head,.hero-actions,.button-row,.cta-box,.breadcrumb{display:flex;gap:1rem}.nav-wrap,.footer-wrap,.cta-box{align-items:center;justify-content:space-between}.nav-wrap{min-height:80px}.brand{display:inline-flex;align-items:center;gap:.9rem;color:#fff;text-decoration:none;font-weight:800;letter-spacing:-.04em}.brand span:last-child{max-width:20rem}.brand-mark{display:grid;place-items:center;width:2.7rem;aspect-ratio:1;border-radius:16px;background:linear-gradient(135deg,var(--orange) 0%,#d66704 100%);color:#fff;font-size:.83rem;letter-spacing:.08em;box-shadow:0 10px 24px rgba(242,116,5,.28)}.nav{display:flex;align-items:stretch;gap:0;flex-wrap:wrap}.nav a{text-decoration:none;color:rgba(255,255,255,.9);font-weight:700;padding:1.45rem 1.25rem;position:relative;display:inline-flex;align-items:center}.nav a.active,.nav a:hover{color:#fff;background:rgba(255,255,255,.08)}.nav a.active{background:var(--orange)}.nav a.active:after{display:none}.nav-cta{margin-left:.5rem;padding:1rem 1rem !important;border-radius:12px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12)}.nav-cta:hover{background:rgba(255,255,255,.16) !important}.nav-toggle{display:none;flex-direction:column;justify-content:center;gap:.26rem;width:2.9rem;height:2.9rem;border:1px solid rgba(255,255,255,.14);border-radius:14px;background:transparent;cursor:pointer}.nav-toggle span:not(.sr-only){display:block;width:1.1rem;height:2px;margin:0 auto;background:#fff}
.hero{position:relative;overflow:clip;padding:4.4rem 0 3.8rem;background:radial-gradient(circle at 100% 0,rgba(242,116,5,.18),transparent 30%),radial-gradient(circle at 0 20%,rgba(23,61,125,.10),transparent 24%),linear-gradient(180deg,#fff2e5 0%,#fff8f2 38%,#fff 72%,#f8fbff 100%)}.hero:before{content:'';position:absolute;right:-8rem;top:-6rem;width:22rem;height:22rem;border-radius:50%;background:radial-gradient(circle,rgba(255,155,61,.18),transparent 65%);filter:blur(10px)}.hero-layout{display:grid;grid-template-columns:minmax(0,1.02fr) minmax(340px,.98fr);gap:2.6rem;align-items:center}.eyebrow,.section-label{display:inline-flex;align-items:center;gap:.5rem;margin:0 0 1rem;color:var(--orange);font-size:.8rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase}.eyebrow:before,.section-label:before{content:'';width:1.2rem;height:2px;border-radius:999px;background:linear-gradient(90deg,var(--orange),var(--orange-2))}h1,h2,h3,p,ul{margin-top:0}h1{margin-bottom:1.15rem;font-size:clamp(2.8rem,7vw,5.2rem);line-height:.95;letter-spacing:-.065em;max-width:11ch}h2{margin-bottom:1rem;font-size:clamp(2rem,4vw,3.1rem);line-height:1.04;letter-spacing:-.05em}h3{margin-bottom:.7rem;font-size:1.2rem;letter-spacing:-.03em}.lead,.section-head p,.card p,.split-copy p,.story p,.footer-note,.hero-badges span,.hero-stats span,.breadcrumb a,.breadcrumb span,.section-nav-shell small{color:var(--muted)}.hero-copy{position:relative;z-index:1}.hero-actions{flex-wrap:wrap;margin:2rem 0 1.4rem}.button{display:inline-flex;align-items:center;justify-content:center;min-height:52px;padding:0 1.25rem;border-radius:999px;text-decoration:none;font-weight:800;transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease,background .2s ease}.button:hover{transform:translateY(-1px)}.button.primary{background:linear-gradient(135deg,var(--orange) 0%,#d66704 100%);color:#fff;box-shadow:0 14px 30px rgba(242,116,5,.24)}.button.secondary,.button.ghost{background:#fff;border:1px solid var(--line);color:var(--ink)}.button.light{background:#fff;color:var(--navy)}.hero-badges{display:flex;gap:.7rem;flex-wrap:wrap}.hero-badges span{padding:.72rem .95rem;border-radius:999px;background:rgba(255,255,255,.82);border:1px solid rgba(0,26,61,.08);font-weight:700}.hero-panel,.card,.split-card,.story,.timeline article,.cta-box,.metric,.pillars article,.spotlight{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-xl);box-shadow:var(--shadow-lg)}.hero-panel{padding:1.4rem;background:linear-gradient(180deg,var(--navy) 0%,var(--navy-2) 78%,var(--navy-3) 100%);color:#fff;box-shadow:var(--shadow-xl)}.panel-topline{height:10px;width:42%;border-radius:999px;background:linear-gradient(90deg,var(--orange),var(--orange-2));margin-bottom:1.2rem}.hero-stats,.cards,.timeline,.pillars,.story-grid,.metrics-grid,.section-nav-shell{display:grid;gap:1rem}.hero-stats{grid-template-columns:repeat(2,minmax(0,1fr))}.hero-stats article{padding:1.15rem;border:1px solid rgba(255,255,255,.14);border-radius:18px;background:rgba(255,255,255,.06);backdrop-filter:blur(8px)}.hero-stats strong{display:block;margin-bottom:.35rem;font-size:1.55rem}.breadcrumb{align-items:center;flex-wrap:wrap;padding:1rem 0 0}.breadcrumb a{text-decoration:none}.section-nav{margin-top:-1.3rem;position:relative;z-index:3}.section-nav-panel{border-radius:18px;overflow:hidden;box-shadow:0 10px 25px -5px rgba(0,0,0,.1),0 8px 10px -6px rgba(0,0,0,.1);border-top:4px solid var(--orange);background:#fff}.section-nav-heading{padding:1rem 1.25rem;background:linear-gradient(180deg,#fff,#fff7ef);font-weight:800;color:var(--navy);border-bottom:1px solid rgba(0,26,61,.08)}.section-nav-shell{grid-template-columns:repeat(5,minmax(0,1fr));padding:1.1rem}.section-link{display:flex;flex-direction:column;gap:.24rem;padding:1rem 1rem;border-radius:14px;text-decoration:none;color:var(--ink);background:#fff;border:1px solid transparent;min-height:102px;justify-content:center}.section-link.is-active{background:linear-gradient(180deg,#fff3e7,#fff);border-color:rgba(242,116,5,.24);box-shadow:inset 0 0 0 1px rgba(242,116,5,.08)}.section-link:hover{transform:translateY(-1px);border-color:rgba(242,116,5,.18);background:linear-gradient(180deg,#fff8f1,#fff)}.section-nav-shell strong{font-size:1rem;color:var(--navy)}.section-nav-shell small{font-size:.88rem;line-height:1.45}.hero-subpage{padding-top:3.5rem;padding-bottom:3rem}.hero-subpage .hero-layout{grid-template-columns:minmax(0,1fr) minmax(300px,.72fr)}.hero-subpage .hero-copy{background:rgba(255,255,255,.72);border:1px solid rgba(0,26,61,.08);box-shadow:var(--shadow-lg);border-radius:28px;padding:2rem}.hero-subpage .hero-panel{background:linear-gradient(180deg,#fff 0%,#f8fbff 100%);color:var(--ink)}.hero-subpage .hero-stats article{background:linear-gradient(180deg,#fff8f1,#fff);border-color:rgba(0,26,61,.08)}.hero-subpage .hero-stats span{color:var(--muted)}.section{padding:4.6rem 0}.section-head{align-items:end;justify-content:space-between;margin-bottom:1.9rem}.section-head>*{flex:1}.cards.cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.cards.cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.cards.cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.card,.split-card,.story,.timeline article,.metric,.spotlight{padding:1.55rem}.card{position:relative;overflow:hidden;background:linear-gradient(180deg,#fff 0%,#fbfdff 100%);transition:transform .2s ease,box-shadow .2s ease}.card:hover{transform:translateY(-3px);box-shadow:0 24px 44px rgba(0,26,61,.12)}.card:after{content:'';position:absolute;right:-2.5rem;bottom:-2.5rem;width:7rem;height:7rem;border-radius:50%;background:rgba(242,116,5,.10)}.card a{font-weight:800;color:var(--navy);text-decoration:none}.icon{display:inline-grid;place-items:center;width:3rem;height:3rem;margin-bottom:1rem;border-radius:16px;background:linear-gradient(135deg,#fff0e2,#ffe0c0);color:var(--orange);font-weight:800}.split{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2rem;align-items:center}.split-card{background:linear-gradient(180deg,#fff8f0 0%,#fff 100%);border-top:4px solid var(--orange)}.mini-list{margin:1rem 0 0;padding-left:1.15rem}.mini-list li+li{margin-top:.45rem}.metrics-grid{grid-template-columns:repeat(4,minmax(0,1fr))}.metric{text-align:center;background:linear-gradient(180deg,#fff7ef 0%,#fff 100%);border-top:4px solid rgba(242,116,5,.72)}.metric strong{display:block;font-size:2rem;letter-spacing:-.04em;color:var(--navy)}.timeline{grid-template-columns:repeat(4,minmax(0,1fr))}.timeline article{background:linear-gradient(180deg,#fff 0%,#f8fbff 100%);border-top:4px solid rgba(0,26,61,.08)}.step-no{display:inline-grid;place-items:center;width:2.35rem;height:2.35rem;margin-bottom:1rem;border-radius:999px;background:var(--navy);color:#fff;font-weight:800}.story-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.story{background:linear-gradient(180deg,#fff 0%,#fff9f4 100%);border-top:4px solid rgba(242,116,5,.72)}.story strong{display:block;margin-bottom:.45rem;color:var(--navy)}.quote-panel{padding:2rem;border-radius:var(--radius-xl);background:linear-gradient(135deg,var(--navy) 0%,var(--navy-2) 66%,var(--navy-3) 100%);color:#fff;box-shadow:var(--shadow-xl)}.quote-panel p,.quote-panel .section-label{color:rgba(255,255,255,.82)}.quote-panel h2{color:#fff;max-width:18ch}.cta-strip{padding:1.4rem 1.5rem;border-radius:var(--radius-lg);background:linear-gradient(180deg,#fff4e8 0%,#fff 100%);border:1px solid rgba(242,116,5,.18);display:flex;gap:1rem;justify-content:space-between;align-items:center}.cta-strip-copy{max-width:46rem}.pillars{grid-template-columns:repeat(3,minmax(0,1fr))}.pillars article{padding:1.35rem 1.4rem;background:linear-gradient(180deg,#fff 0%,#fff8f1 100%)}.pillars strong{display:block;margin-bottom:.3rem;color:var(--navy)}.cta-box{padding:2rem;background:linear-gradient(135deg,var(--navy) 0%,var(--navy-2) 62%,var(--navy-3) 100%);color:#fff;box-shadow:var(--shadow-xl)}.cta-box .section-label,.cta-box h2,.cta-box p,.cta-box .button.ghost{color:#fff}.cta-box .button.ghost{border-color:rgba(255,255,255,.24);background:transparent}.site-footer{padding:1.7rem 0 2.3rem;border-top:1px solid rgba(0,26,61,.08)}.footer-wrap p{margin:0}.muted{background:linear-gradient(180deg,#fff8f1 0%,#fff 100%)}

.hero-home{min-height:560px;display:flex;align-items:center}.hero-home:after{content:'';position:absolute;inset:0;background:linear-gradient(rgba(0,26,61,.58),rgba(0,26,61,.54)),var(--hero-image) center/cover no-repeat;z-index:0}.hero-home .container,.hero-home .hero-copy,.hero-home .hero-panel{position:relative;z-index:1}.hero-home .hero-copy h1,.hero-home .hero-copy .lead,.hero-home .hero-copy .eyebrow,.hero-home .hero-badges span{color:#fff}.hero-home .eyebrow:before{background:linear-gradient(90deg,#fff,var(--orange-2))}.hero-home .hero-badges span{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.16)}
.feature-services{margin-top:-5.5rem;position:relative;z-index:5;padding-bottom:1rem}.feature-services-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.5rem}.feature-service-card{display:flex;flex-direction:column;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.08);min-height:100%}.feature-service-top{background:var(--navy);padding:2.2rem 1.8rem;text-align:center;color:#fff}.feature-service-top h3{margin:0;color:#fff}.feature-service-icon{width:4rem;height:4rem;border-radius:999px;margin:0 auto 1rem;display:grid;place-items:center;background:rgba(255,255,255,.08);color:var(--orange);font-weight:800;border:1px solid rgba(255,255,255,.14)}.feature-service-body{padding:1.8rem;text-align:center;flex:1}.feature-service-body a{color:var(--orange);font-weight:800;text-decoration:none}.feature-service-bar{height:.45rem;background:var(--orange)}
.news-section{background:#fff}.news-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2rem}.news-card{display:flex;gap:1.25rem;align-items:flex-start;padding:1rem;border-radius:18px;transition:background .2s ease}.news-card:hover{background:#fff8f1}.news-card img{width:12rem;height:9rem;object-fit:cover;border-radius:14px;box-shadow:0 8px 20px rgba(0,0,0,.08)}.news-card-copy h3{margin-bottom:.45rem;color:var(--navy)}.news-card-copy a{color:var(--orange);font-weight:800;text-decoration:none}
.site-footer{background:var(--navy);color:#fff;padding:4.5rem 0 2rem;border-top:none}.footer-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:2rem;margin-bottom:2.5rem}.footer-grid h4{margin:0 0 1rem;color:rgba(255,255,255,.76);text-transform:uppercase;letter-spacing:.08em;font-size:.95rem}.footer-grid p,.footer-grid a,.footer-grid li{color:rgba(255,255,255,.72);text-decoration:none;list-style:none}.footer-grid ul{margin:0;padding:0;display:grid;gap:.65rem}.footer-grid a:hover{color:#fff}.footer-bottom{padding-top:1.4rem;border-top:1px solid rgba(255,255,255,.1);display:flex;justify-content:space-between;gap:1rem;align-items:center}.footer-bottom p{margin:0}.site-footer .footer-note{color:rgba(255,255,255,.56)}

@media (max-width:1100px){.hero-layout,.split,.metrics-grid,.timeline,.story-grid,.pillars,.cards.cols-4,.cards.cols-3,.section-nav-shell,.feature-services-grid,.footer-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.news-grid{grid-template-columns:1fr}}
@media (max-width:900px){.nav-toggle{display:inline-flex}.nav{position:absolute;top:calc(100% + .75rem);right:1rem;left:1rem;display:none;flex-direction:column;align-items:stretch;padding:1rem;border:1px solid rgba(255,255,255,.08);border-radius:18px;background:var(--navy-2);box-shadow:var(--shadow-xl)}.nav.is-open{display:flex}.nav a{padding:1rem;border-radius:12px}.hero-layout,.split,.section-head,.cta-strip,.cta-box,.footer-bottom{grid-template-columns:1fr;flex-direction:column;align-items:flex-start}.hero-stats,.metrics-grid,.timeline,.story-grid,.pillars,.cards.cols-4,.cards.cols-3,.cards.cols-2,.section-nav-shell,.feature-services-grid,.footer-grid{grid-template-columns:1fr}.hero,.section{padding:4rem 0}.section-nav{margin-top:-.6rem}.section-nav-shell a{min-height:unset}.feature-services{margin-top:-2rem}.news-card{flex-direction:column}.news-card img{width:100%;height:12rem}}
@media (max-width:640px){.brand span:last-child{max-width:11.5rem;font-size:.95rem;line-height:1.15}h1{max-width:100%;font-size:clamp(2.3rem,12vw,4rem)}.button,.button-row .button,.nav-cta{width:100%}.hero-badges span{width:100%}.breadcrumb{display:none}}
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
    link_html = []
    for label, href, desc in items:
        active = ' is-active' if href == current else ''
        link_html.append(f'<a class="section-link{active}" href="{href_from(page_path, href)}"><strong>{escape(label)}</strong><small>{escape(desc)}</small></a>')
    return f'<section class="section-nav" aria-label="{escape(nav_label)}"><div class="container"><div class="section-nav-panel"><div class="section-nav-heading">{escape(heading)}</div><div class="section-nav-shell">{"".join(link_html)}</div></div></div></section>'


def render_feature_grid(page_path: str, block: dict) -> str:
    cols = min(max(len(block['cards']), 2), 4)
    cards = []
    for idx, (title, text, href) in enumerate(block['cards'], start=1):
        link = '' if href == '#' else f'<p><a href="{href_from(page_path, href)}">Open page →</a></p>'
        cards.append(f'<article class="card"><div class="icon">{idx:02d}</div><h3>{escape(title)}</h3><p>{escape(text)}</p>{link}</article>')
    return f'<section class="section"><div class="container"><p class="section-label">{escape(block["kicker"])}</p><div class="section-head"><h2>{escape(block["title"])}</h2><p>{escape(block["text"])}</p></div><div class="cards cols-{cols}">{"".join(cards)}</div></div></section>'


def render_split(block: dict) -> str:
    bullets = ''.join(f'<li>{escape(item)}</li>' for item in block['bullets'])
    return f'<section class="section muted"><div class="container split"><div class="split-copy"><p class="section-label">{escape(block["kicker"])}</p><h2>{escape(block["title"])}</h2><p>{escape(block["text"])}</p></div><div class="split-card"><ul class="mini-list">{bullets}</ul></div></div></section>'


def render_metrics_band(block: dict) -> str:
    items = ''.join(f'<article class="metric"><strong>{escape(a)}</strong><span>{escape(b)}</span></article>' for a, b in block['items'])
    return f'<section class="section"><div class="container"><div class="metrics-grid">{items}</div></div></section>'


def render_story_cards(block: dict) -> str:
    items = ''.join(f'<article class="story"><strong>{escape(a)}</strong><p>{escape(b)}</p></article>' for a, b in block['items'])
    return f'<section class="section"><div class="container"><p class="section-label">{escape(block["kicker"])}</p><div class="section-head"><h2>{escape(block["title"])}</h2><p></p></div><div class="story-grid">{items}</div></div></section>'


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
    hero_stats = cfg.get('hero_stats', [('Modern UX', 'Cleaner navigation and stronger hierarchy'), ('Orange + Navy', 'More youthful and premium visual direction'), ('SEO-ready', 'Clearer page focus and metadata'), ('Scalable', 'Prepared for richer real content later')])
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
  <body class="page-shell">
    <header class="site-header">
      <div class="container nav-wrap">
        <a class="brand" href="{href_from(path, '/index.html')}">
          <span class="brand-mark">SSE</span>
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
      <section class="hero{' hero-home' if path == 'index.html' else ' hero-subpage'}"{f' style="--hero-image:url(\'{cfg.get("hero_image", "")}\')"' if path == 'index.html' and cfg.get('hero_image') else ''}>
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
            <h2>Ready to turn this structure into a stronger admissions and brand experience?</h2>
            <p>This site now has the right architecture for richer official text, photography, enquiry flows, department detail, and stronger SEO landing pages.</p>
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
          <p>Sanskrithi School of Engineering<br/>Andhra Pradesh<br/>Email: {escape(SITE['email'])}</p>
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
          <p>Need admissions or placement support?<br/><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
        </div>
      </div>
      <div class="container footer-bottom">
        <p>© <span id="year"></span> {escape(SITE['title'])}. All rights reserved.</p>
        <p class="footer-note">Modern multi-page redesign focused on UX, admissions clarity, and stronger school positioning.</p>
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
