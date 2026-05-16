from pathlib import Path
from html import escape
import os

ROOT = Path('/root/.openclaw/workspace/sseptp-redesign')

site = {
    'title': 'Sanskrithi School of Engineering',
    'email': 'info@sseptp.org',
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
        ('Overview', '/about/index.html'),
        ('Vision & Mission', '/about/vision-mission.html'),
        ('Leadership', '/about/leadership.html'),
        ('Quality & Recognition', '/about/quality.html'),
        ('Industry Interface', '/about/industry-interface.html'),
    ],
    'Admissions': [
        ('Overview', '/admissions/index.html'),
        ('Admission Process', '/admissions/process.html'),
        ('Fees & Scholarships', '/admissions/fees.html'),
        ('Enquiry', '/admissions/enquiry.html'),
    ],
    'Academics': [
        ('Overview', '/academics/index.html'),
        ('Programs', '/academics/programs.html'),
        ('Labs', '/academics/labs.html'),
        ('Scholarships', '/academics/scholarships.html'),
        ('RIT Pathway', '/academics/rit.html'),
    ],
    'Campus Life': [
        ('Overview', '/campus/index.html'),
        ('Facilities', '/campus/facilities.html'),
        ('Hostel Life', '/campus/hostel.html'),
        ('Health & Safety', '/campus/health-safety.html'),
        ('Sports', '/campus/sports.html'),
    ],
    'Placements': [
        ('Overview', '/placements/index.html'),
        ('Success Stories', '/placements/success-stories.html'),
        ('Placement Contact', '/placements/contact.html'),
    ],
}

pages = {
    'index.html': {
        'section': 'Home',
        'title': 'Admissions Open 2026',
        'description': 'Future-ready engineering education with academic depth, placements, campus life, and industry direction.',
        'hero_kicker': 'Admissions Open 2026',
        'hero_title': 'A modern engineering school website built around real student decisions.',
        'hero_text': 'Sanskrithi School of Engineering deserves more than a flat brochure page. This structure gives students and families a clear path through admissions, academics, campus life, accreditation, and placements.',
        'hero_stats': [('600+', 'Offers highlighted on the current site'), ('80+', 'Corporate partners referenced'), ('95%', 'Placement rate claim carried forward'), ('Autonomous', 'Prominent institutional claim retained')],
        'content': [
            {'type': 'cards', 'kicker': 'Quick Pathways', 'title': 'The new homepage points people to the right decision fast.', 'text': 'Instead of forcing everything into one long page, the homepage now routes visitors into the key journeys that actually matter.', 'cards': [
                ('Admissions', 'Overview, process, fees, and enquiry now sit in one clear stream.', '/admissions/index.html'),
                ('Academics', 'Programs, labs, scholarships, and the RIT / Europe-facing angle.', '/academics/index.html'),
                ('Campus Life', 'Facilities, hostel life, health & safety, and sports.', '/campus/index.html'),
                ('Placements', 'Placement outcomes, success stories, and recruiter-facing trust signals.', '/placements/index.html'),
            ]},
            {'type': 'split', 'kicker': 'What we kept', 'title': 'The real content from the current site is preserved, not replaced blindly.', 'text': 'The current site already contains valuable structure: leadership, vision & mission, IQAC, committees, admissions routes, detailed academics, campus life, and placement messaging. The redesign keeps those pillars and presents them more clearly.', 'bullets': ['About College, Heritage, Vision & Mission', 'Leadership messages and institutional governance', 'NAAC, IQAC, Recognition, and Committees', 'Programs, labs, scholarships, and CSE detail', 'Life @ SSE including hostel, health & safety, and sports']},
        ],
    },
    'about/index.html': {
        'section': 'About',
        'title': 'About the School',
        'description': 'Overview of Sanskrithi School of Engineering, its vision, leadership, and institutional profile.',
        'hero_kicker': 'About SSE',
        'hero_title': 'Shaping engineers for tomorrow’s world.',
        'hero_text': 'The current site positions SSE as a premier engineering institution in Andhra Pradesh focused on academic excellence and holistic student development. This page keeps that identity, but presents it with more structure and clarity.',
        'content': [
            {'type': 'cards', 'kicker': 'About Structure', 'title': 'Institutional content deserves a real home.', 'text': 'The previous site scattered this material across many routes. It now sits in a cleaner section tree.', 'cards': [
                ('Vision & Mission', 'Core purpose, long-term direction, and educational values.', '/about/vision-mission.html'),
                ('Leadership', 'Chairman, principal, dean, secretary, and institutional guidance.', '/about/leadership.html'),
                ('Quality & Recognition', 'NAAC, IQAC, recognition, and committee structure.', '/about/quality.html'),
                ('Industry Interface', 'How academic learning is connected to real-world relevance.', '/about/industry-interface.html'),
            ]},
        ],
    },
    'about/vision-mission.html': {
        'section': 'About', 'title': 'Vision & Mission', 'description': 'Vision, mission, and educational direction.',
        'hero_kicker': 'Vision & Mission', 'hero_title': 'Academic purpose should be easy to find and easy to trust.',
        'hero_text': 'This page gives the school a focused place to present its long-term educational direction, student development goals, and engineering ethos.',
        'content': [{'type':'split','kicker':'Direction','title':'A better place for institutional intent.','text':'The current site already signals academic seriousness through accreditation, leadership messaging, and program design. This page gathers that intent into one clear narrative.','bullets':['Student growth alongside technical excellence','Industry relevance without losing academic depth','Engineering education shaped for future careers','Holistic development, not only classroom outcomes']}],
    },
    'about/leadership.html': {
        'section': 'About', 'title': 'Leadership', 'description': 'Leadership, institutional messages, and governance.',
        'hero_kicker': 'Leadership', 'hero_title': 'Leadership content should feel credible, not buried.',
        'hero_text': 'The current site contains multiple leadership and message pages. Here they become one coherent part of the school experience, with room for detail pages later if needed.',
        'content': [{'type':'cards','kicker':'Leadership Pages','title':'Existing leadership content now fits one clear structure.','text':'These are all present on the current site and now belong to a clear institutional section.','cards':[
            ('Chairman Message','Leadership voice and long-term institutional direction.','#'),('Principal Message','Academic leadership and student-facing school vision.','#'),('Dean Message','Program quality, learning standards, and academic delivery.','#'),('Secretary Message','Institutional stewardship and administrative direction.','#')]}],
    },
    'about/quality.html': {
        'section': 'About', 'title': 'Quality, NAAC & Recognition', 'description': 'NAAC, IQAC, committees, and recognition.',
        'hero_kicker': 'Quality & Recognition', 'hero_title': 'NAAC, IQAC, and governance need stronger visibility.',
        'hero_text': 'The current site contains real quality-assurance content, including NAAC, IQAC, committees, and recognition. This page makes those trust signals far easier to discover.',
        'hero_stats': [('NAAC', 'A-grade quality messaging retained'), ('IQAC', 'Institutional improvement focus'), ('Committees', 'Academic and industry governance'), ('Recognition', 'Affiliation and credibility signals')],
        'content': [{'type':'cards','kicker':'Included Topics','title':'The underlying content is broader than a single badge.', 'text':'Quality is not just accreditation. It is also process, governance, and academic improvement.','cards':[
            ('NAAC','The current site explicitly references NAAC A-grade quality messaging.','#'),('IQAC','Internal Quality Assurance Cell content is preserved as a dedicated trust area.','#'),('Committees','Academic audit, industry interaction, and related committees remain visible.','#'),('Recognition','Affiliation and recognition continue to support institutional trust.','#')]}],
    },
    'about/industry-interface.html': {
        'section': 'About', 'title': 'Industry Interface', 'description': 'Industry interaction and relevance.',
        'hero_kicker': 'Industry Interface', 'hero_title': 'Students need to see the bridge between learning and work.',
        'hero_text': 'The current site already leans into industry relevance through placements, partner references, and Europe-facing program claims. This page makes that relationship more explicit.',
        'content': [{'type':'split','kicker':'Why it matters','title':'Industry relevance becomes a visible institutional story.','text':'This is where the school can connect curriculum, guest sessions, internship exposure, software pathways, placement preparation, and mentoring into one message.','bullets':['Industry leaders referenced in placement messaging','Curriculum aligned with employability outcomes','Real-world training and project orientation','A clearer link between academics and careers']}],
    },
    'admissions/index.html': {
        'section': 'Admissions', 'title': 'Admissions Overview', 'description': 'Admissions overview for 2026.',
        'hero_kicker': 'Admissions Open 2026', 'hero_title': 'A clearer admissions path builds trust immediately.',
        'hero_text': 'The current site already contains overview, process, fee, form, and enquiry pages. The redesign groups them into one admissions journey instead of scattering them.',
        'content': [{'type':'cards','kicker':'Admissions Journey','title':'Everything a student looks for is now grouped together.','text':'The structure below reflects the current site’s own content tree, but in a cleaner order.','cards':[
            ('Admission Process','Step-by-step flow from interest to application.', '/admissions/process.html'),('Fees & Scholarships','Cost visibility and support information.', '/admissions/fees.html'),('Admission Enquiry','Lead capture and contact path.', '/admissions/enquiry.html'),('Programs First','Route students back to academics when they need fit before applying.', '/academics/programs.html')]}],
    },
    'admissions/process.html': {
        'section': 'Admissions', 'title': 'Admission Process', 'description': 'Admission process and steps.',
        'hero_kicker': 'Admission Process', 'hero_title': 'The process should feel simple, not hidden.',
        'hero_text': 'This page gives a real place for the current process content, so students do not need to guess what happens next.',
        'content': [{'type':'timeline','kicker':'How to Apply','title':'A more useful structure for the current admissions routes.','text':'The current site has both process and form-related paths. This page turns them into a single understandable flow.','steps':['Choose the right program and check eligibility.','Review the admission process and required documents.','Understand fee structure, scholarship options, and support.','Submit enquiry or application and continue to counselling.']}],
    },
    'admissions/fees.html': {
        'section': 'Admissions', 'title': 'Fees & Scholarships', 'description': 'Fees, scholarship, and affordability.',
        'hero_kicker': 'Fees & Scholarships', 'hero_title': 'Financial clarity reduces friction for families.',
        'hero_text': 'The old site separates fees and scholarship content. This structure makes them work together as part of one decision page.',
        'content': [{'type':'split','kicker':'Clarity for families','title':'Fees and support belong in the same decision space.','text':'On many college sites, affordability information is too hard to find. This page gives it dedicated room and connects it to scholarship visibility from the academics section.','bullets':['Fee structure visibility','Scholarship opportunities','Program-wise cost clarity','Admission support and counselling follow-up']}],
    },
    'admissions/enquiry.html': {
        'section': 'Admissions', 'title': 'Admission Enquiry', 'description': 'Admission enquiry and next steps.',
        'hero_kicker': 'Admission Enquiry', 'hero_title': 'Interest should turn into action without dead ends.',
        'hero_text': 'The current site includes enquiry and form routes. This page becomes the conversion hub for both.',
        'content': [{'type':'cards','kicker':'Best next steps','title':'This is where the site should convert curiosity into contact.','text':'A strong enquiry page should be simple, reassuring, and direct.','cards':[
            ('Talk to Admissions','Phone, email, and response expectations.','#'),('Share Your Interest','Program, background, and preferred contact mode.','#'),('Ask About Eligibility','Clarify intake, documents, and timelines.','#'),('Continue to Application','Move directly to the official form if ready.','#')]}],
    },
    'academics/index.html': {
        'section': 'Academics', 'title': 'Academics Overview', 'description': 'Programs, courses, labs, and academic pathways.',
        'hero_kicker': 'Academics', 'hero_title': 'Programs, labs, and learning pathways need stronger structure.',
        'hero_text': 'The current site already contains all-programs, undergraduate, M.Tech, CSE detail, courses, labs, and scholarship routes. This section pulls them into one academic hub.',
        'content': [{'type':'cards','kicker':'Academic Navigation','title':'The new structure reflects the current academic content more honestly.','text':'Instead of a generic programs section, this site now gives different academic decisions their own pages.','cards':[
            ('Programs', 'Undergraduate, M.Tech, and department-level pathways.', '/academics/programs.html'),
            ('Labs', 'Hands-on infrastructure and practical learning environments.', '/academics/labs.html'),
            ('Scholarships', 'Academic support and accessibility signals.', '/academics/scholarships.html'),
            ('RIT Pathway', 'The Europe / Vienna / software differentiator.', '/academics/rit.html')
        ]}],
    },
    'academics/programs.html': {
        'section': 'Academics', 'title': 'Programs', 'description': 'Programs and departments.',
        'hero_kicker': 'Programs', 'hero_title': 'Program information should guide fit, not overwhelm it.',
        'hero_text': 'The current site explicitly includes all-programme, undergraduate, M.Tech, and department-specific routes like CSE. This page gives those options a cleaner academic home.',
        'hero_stats': [('CSE', 'Detailed route found in current site'), ('4 Years', 'CSE duration visible'), ('120', 'CSE seats referenced'), ('10+2', 'Eligibility reference found')],
        'content': [{'type':'cards','kicker':'Current program signals','title':'What the current site already tells us about academics.', 'text':'At least one department route already contains structured detail. That gives this redesign a stronger academic base than a generic brochure rewrite.', 'cards':[
            ('Computer Science & Engineering', 'Advanced programming labs, AI and machine learning, industry partnerships, and modern software development methodologies.', '#'),
            ('Undergraduate Routes', 'A clearer home for all B.Tech pathways and student decision support.', '#'),
            ('M.Tech Routes', 'Advanced study options should stand alongside undergraduate choices, not disappear under them.', '#'),
            ('Courses Overview', 'A better summary layer above detailed department pages.', '#')]}],
    },
    'academics/labs.html': {
        'section': 'Academics', 'title': 'Labs & Applied Learning', 'description': 'Labs and applied learning.',
        'hero_kicker': 'Labs & Applied Learning', 'hero_title': 'Practical learning deserves visual and structural weight.',
        'hero_text': 'The current site includes a dedicated labs route. This page turns that into a stronger academic selling point.',
        'content': [{'type':'split','kicker':'Hands-on depth','title':'Labs are where engineering becomes real.', 'text':'Students and families evaluate labs as proof that learning is practical. This page creates room for facilities, equipment, project work, demos, and discipline-specific lab stories.', 'bullets':['Department labs and workshop spaces','Applied problem-solving environments','Project-based and practical learning','Stronger visual storytelling potential']}],
    },
    'academics/scholarships.html': {
        'section': 'Academics', 'title': 'Scholarships', 'description': 'Scholarship pathways and academic support.',
        'hero_kicker': 'Scholarships', 'hero_title': 'Support options should be easy to find, not hidden in navigation.',
        'hero_text': 'The existing scholarship route is important enough to keep as its own page. It helps families understand that access and affordability matter here too.',
        'content': [{'type':'cards','kicker':'Support Signals','title':'Scholarship content works best when it is practical and direct.', 'text':'This page can later hold merit support, need-based guidance, special categories, and application instructions.', 'cards':[
            ('Eligibility', 'Who can apply and on what basis.', '#'),('Application Support', 'When and how to request scholarship guidance.', '#'),('Merit Recognition', 'Academic achievement and excellence pathways.', '#'),('Affordability Clarity', 'How scholarship support connects to fees and admissions.', '#')]}],
    },
    'academics/rit.html': {
        'section': 'Academics', 'title': 'RIT / Europe Pathway', 'description': 'RIT, Vienna mentors, and software-focused differentiator.',
        'hero_kicker': 'RIT / Europe Pathway', 'hero_title': 'The Europe-facing software message should not be buried in homepage slides.',
        'hero_text': 'The current site strongly emphasizes Europe, Vienna mentors, real-world training, and software-oriented learning. That is a differentiator, so it deserves its own page.',
        'content': [{'type':'cards','kicker':'Current messaging kept alive','title':'This content already exists on the current site and should remain visible.', 'text':'Instead of reducing it to one marketing line, the redesign gives it room and context.', 'cards':[
            ('Europe to India', '“We Brought Europe to India | For You”', '#'),('European Experts', '“Learn From European Software Experts. Every Day”', '#'),('Vienna Mentors', '“4-Year RIT Program | Vienna Mentors | Real Projects | Java to GitHub”', '#'),('Career Relevance', 'A cleaner bridge from academic story to employability story.', '#')]}],
    },
    'campus/index.html': {
        'section': 'Campus Life', 'title': 'Campus Life Overview', 'description': 'Student life, facilities, hostel, sports, and wellbeing.',
        'hero_kicker': 'Life @ SSE', 'hero_title': 'Campus life should feel vibrant, not like an afterthought.',
        'hero_text': 'The current site already has a richer student-life structure than most simple college websites. This redesign gives it the visibility it deserves.',
        'content': [{'type':'cards','kicker':'Campus Sections', 'title':'Student experience already exists in the old site. Now it is easier to navigate.', 'text':'Life overview, academic facilities, campus facilities, hostel life, health & safety, and sports all now sit in one clear section tree.', 'cards':[
            ('Facilities', 'Academic and on-campus infrastructure in one clearer destination.', '/campus/facilities.html'),
            ('Hostel Life', 'Accommodation, food, recreation, and student comfort.', '/campus/hostel.html'),
            ('Health & Safety', 'A visible space for wellbeing and trust.', '/campus/health-safety.html'),
            ('Sports', 'Student activity, balance, and energy beyond the classroom.', '/campus/sports.html')]}],
    },
    'campus/facilities.html': {
        'section': 'Campus Life', 'title': 'Facilities', 'description': 'Academic and campus facilities.',
        'hero_kicker': 'Facilities', 'hero_title': 'Facilities help students picture daily life here.',
        'hero_text': 'The original site separates academic facilities and campus facilities. This structure lets them work together while still allowing detail blocks underneath.',
        'content': [{'type':'split','kicker':'What belongs here', 'title':'A better home for environment and infrastructure.', 'text':'This page can combine classrooms, labs, campus resources, learning spaces, support spaces, and other visible infrastructure that shapes confidence.', 'bullets':['Academic facilities and learning spaces','On-campus support infrastructure','Study environment and accessibility','A better photo-driven storytelling layer']}],
    },
    'campus/hostel.html': {
        'section': 'Campus Life', 'title': 'Hostel Life', 'description': 'Hostel life and student comfort.',
        'hero_kicker': 'Hostel Life', 'hero_title': 'Hostel content should reassure both students and families.',
        'hero_text': 'The current site already mentions comfortable accommodations, nutritious mess food, recreation rooms, and 24/7 security. Those are exactly the right trust points to preserve.',
        'content': [{'type':'cards','kicker':'Current hostel signals','title':'The existing hostel messaging already has the right instincts.', 'text':'The redesign simply gives it stronger presentation and clearer discoverability.', 'cards':[
            ('Comfortable Accommodations','A safer, more grounded living environment for students.','#'),('Nutritious Mess Food','Daily life support matters in decision-making.','#'),('Recreation Rooms','Student comfort and community beyond classes.','#'),('24/7 Security','A strong reassurance signal for families.','#')]}],
    },
    'campus/health-safety.html': {
        'section': 'Campus Life', 'title': 'Health & Safety', 'description': 'Health, safety, and student wellbeing.',
        'hero_kicker': 'Health & Safety', 'hero_title': 'Safety information should be visible, not assumed.',
        'hero_text': 'Because the current site already includes health and safety as a dedicated route, the redesign keeps it visible and student-centered.',
        'content': [{'type':'split','kicker':'Why it matters', 'title':'Wellbeing content supports trust and conversion.', 'text':'Health and safety content helps families understand that student care is taken seriously. It also helps the institution appear more complete and responsible.', 'bullets':['Campus safety information','Student support and wellbeing','Residential reassurance','Operational readiness and care']}],
    },
    'campus/sports.html': {
        'section': 'Campus Life', 'title': 'Sports & Student Activities', 'description': 'Sports and student activities.',
        'hero_kicker': 'Sports & Activities', 'hero_title': 'A youthful school brand needs visible energy.',
        'hero_text': 'Sports and student activities make the institution feel more alive. This page gives that side of school life real space.',
        'content': [{'type':'cards','kicker':'Student energy','title':'Beyond academics, the site should show momentum and participation.', 'text':'A modern school site should not feel static. This page supports that by highlighting movement, community, and balance.', 'cards':[
            ('Sports Culture','Competitive and recreational student participation.','#'),('Events','Inter-college, campus, and community events.','#'),('Clubs','Technical, cultural, and leadership communities.','#'),('Student Confidence','Growth through teamwork, discipline, and visibility.','#')]}],
    },
    'placements/index.html': {
        'section': 'Placements', 'title': 'Placements Overview', 'description': 'Placement outcomes, partners, and readiness.',
        'hero_kicker': 'Placements', 'hero_title': 'Career outcomes are one of the strongest stories on the current site.',
        'hero_text': 'The current site surfaces strong placement marketing: 600+ offers, 80+ corporate partners, 95% placement rate, and curriculum design by industry leaders. That deserves real structure.',
        'hero_stats': [('600+', 'Offers'), ('80+', 'Corporate Partners'), ('95%', 'Placement Rate'), ('19.6 LPA', 'Highest-paying internship claim found')],
        'content': [{'type':'cards','kicker':'Placement Structure','title':'Placement content becomes an actual section, not just a slide.', 'text':'Students, parents, and recruiters can now move through the placement story more intentionally.', 'cards':[
            ('Placement Story', 'Overview of outcomes, preparation, and employer trust.', '/placements/index.html'),
            ('Success Stories', 'Proof through named journeys and results.', '/placements/success-stories.html'),
            ('Placement Contact', 'A clear path for recruiter or student enquiry.', '/placements/contact.html'),
            ('Academics Link', 'Tighter connection back to programs and industry interface.', '/academics/rit.html')]}],
    },
    'placements/success-stories.html': {
        'section': 'Placements', 'title': 'Success Stories', 'description': 'Placement success stories and student outcomes.',
        'hero_kicker': 'Success Stories', 'hero_title': 'Outcomes feel stronger when people can imagine themselves in them.',
        'hero_text': 'The current site already includes success-story style placement content and testimonial language. This page gives that proof a cleaner destination.',
        'content': [{'type':'cards','kicker':'What this page should show','title':'Success stories should be specific, aspirational, and credible.', 'text':'The extracted current-site content already uses testimonial-style proof points. The new design turns that into a proper format.', 'cards':[
            ('Dream Outcomes','Aspirational but believable examples of student success.','#'),('Training Impact','How curriculum and placement preparation contributed.','#'),('Industry Readiness','Projects, confidence, and interview preparation.','#'),('Progression Stories','Employment, internships, and higher-growth pathways.','#')]}],
    },
    'placements/contact.html': {
        'section': 'Placements', 'title': 'Placement Contact', 'description': 'Placement contact for students and recruiters.',
        'hero_kicker': 'Placement Contact', 'hero_title': 'Recruiter and placement enquiries need a direct path.',
        'hero_text': 'The current site includes a placement contact route. That deserves a dedicated page so the school looks easier to work with and more professionally organized.',
        'content': [{'type':'split','kicker':'Who this helps', 'title':'This page serves both opportunity and trust.', 'text':'Placement contact is useful for recruiters, students, and parents. It signals openness, confidence, and a functioning career-support structure.', 'bullets':['Recruiter enquiries','Student placement support','Internship and partnership conversations','Career cell visibility']}],
    },
    'contact.html': {
        'section': 'Contact', 'title': 'Contact & Enquiry', 'description': 'Contact SSE for admissions and institutional enquiry.',
        'hero_kicker': 'Contact SSE', 'hero_title': 'A serious school website needs clear contact routes.',
        'hero_text': 'This page gives admissions, institutional, and placement-related conversations a clearer front door, instead of leaving contact as a footer afterthought.',
        'content': [{'type':'cards','kicker':'Contact Routes','title':'Different users need different next steps.', 'text':'This page can later expand with forms, department contacts, phone numbers, maps, and office hours.', 'cards':[
            ('Admissions Enquiry','For students and families beginning the process.', '/admissions/enquiry.html'),('Placement Contact','For employer and career-cell conversations.', '/placements/contact.html'),('Academic Questions','Route deeper program questions to academics.', '/academics/index.html'),('General Information','Institutional queries, visits, and campus-level contact.', '#')]}],
    },
}

STYLE = r'''
:root{--navy:#10233f;--navy-2:#173761;--orange:#ff7a1a;--orange-2:#ff9f3f;--ink:#16202c;--muted:#66758a;--line:rgba(16,35,63,.12);--bg:#fffaf5;--white:#fff;--card:#ffffff;--soft:#eef4fb;--soft-orange:#fff1e5;--shadow:0 22px 60px rgba(16,35,63,.12);--radius:24px;--container:1180px}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,system-ui,sans-serif;color:var(--ink);background:linear-gradient(180deg,#fff8f2 0%,#fff 18%);line-height:1.65}a{-webkit-tap-highlight-color:transparent}.container{width:min(calc(100% - 2rem),var(--container));margin:0 auto}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.site-header{position:sticky;top:0;z-index:50;background:rgba(255,250,245,.88);backdrop-filter:blur(16px);border-bottom:1px solid rgba(16,35,63,.06)}.nav-wrap,.footer-wrap,.section-head,.cta-box{display:flex;gap:1.5rem;align-items:center;justify-content:space-between}.nav-wrap{min-height:82px}.brand{display:inline-flex;align-items:center;gap:.8rem;color:var(--ink);text-decoration:none;font-weight:800;letter-spacing:-.04em}.brand span:last-child{max-width:20rem}.brand-mark{display:grid;place-items:center;width:2.55rem;aspect-ratio:1;border-radius:14px;background:linear-gradient(135deg,var(--orange),#ff5d1a);color:#fff;font-size:.82rem;letter-spacing:.08em}.nav{display:flex;align-items:center;gap:1rem;flex-wrap:wrap}.nav a{text-decoration:none;color:var(--muted);font-weight:700}.nav a.active,.nav a:hover{color:var(--navy)}.nav-cta{padding:.72rem 1rem;border-radius:999px;background:rgba(255,122,26,.1);border:1px solid rgba(255,122,26,.18)}.nav-toggle{display:none;flex-direction:column;justify-content:center;gap:.26rem;width:2.9rem;height:2.9rem;border:1px solid var(--line);border-radius:14px;background:#fff;cursor:pointer}.nav-toggle span:not(.sr-only){display:block;width:1.1rem;height:2px;margin:0 auto;background:var(--ink)}
.hero{padding:5.8rem 0 4rem;background:radial-gradient(circle at top right,rgba(255,122,26,.18),transparent 28%),radial-gradient(circle at top left,rgba(23,55,97,.10),transparent 25%),linear-gradient(180deg,#fff3e7 0%,#fff 62%,#f9fbff 100%)}.hero-grid,.grid-2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2rem;align-items:center}.eyebrow,.section-label{margin:0 0 .9rem;color:var(--orange);font-size:.78rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase}h1,h2,h3,p,ul{margin-top:0}h1{font-size:clamp(2.7rem,7vw,5.3rem);line-height:.97;letter-spacing:-.06em;margin-bottom:1.1rem;max-width:11ch}h2{font-size:clamp(1.9rem,4vw,3.15rem);line-height:1.04;letter-spacing:-.05em;margin-bottom:1rem}h3{font-size:1.22rem;letter-spacing:-.03em;margin-bottom:.65rem}.lead,.section-head p,.card p,.split-copy p,.timeline p,.footer-note,.hero-stats span,.mini-list li,.mega a small{color:var(--muted)}.hero-actions,.button-row{display:flex;gap:1rem;flex-wrap:wrap}.hero-actions{margin:2rem 0 1.2rem}.button{display:inline-flex;align-items:center;justify-content:center;min-height:50px;padding:0 1.2rem;border-radius:999px;text-decoration:none;font-weight:800;transition:.2s ease}.button:hover{transform:translateY(-1px)}.button.primary{background:linear-gradient(135deg,var(--orange),#ff5d1a);color:#fff;box-shadow:0 12px 28px rgba(255,93,26,.24)}.button.secondary,.button.ghost{background:#fff;border:1px solid var(--line);color:var(--ink)}.button.light{background:#fff;color:var(--navy)}
.hero-panel,.card,.split-card,.stat,.timeline article,.cta-box,.mega{background:#fff;border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow)}.hero-panel{padding:1.3rem;background:linear-gradient(180deg,var(--navy) 0%,var(--navy-2) 100%);color:#fff}.panel-topline{height:10px;width:42%;border-radius:999px;background:linear-gradient(90deg,var(--orange),var(--orange-2));margin-bottom:1.2rem}.hero-stats,.cards,.timeline,.mega-grid{display:grid;gap:1rem}.hero-stats{grid-template-columns:repeat(2,minmax(0,1fr))}.hero-stats article{padding:1.1rem;border:1px solid rgba(255,255,255,.14);border-radius:18px;background:rgba(255,255,255,.06)}.hero-stats strong{display:block;font-size:1.4rem;margin-bottom:.35rem}.section{padding:5rem 0}.section-head{align-items:end;margin-bottom:1.8rem}.section-head>*{flex:1}.cards.cards-4{grid-template-columns:repeat(4,minmax(0,1fr))}.cards.cards-3{grid-template-columns:repeat(3,minmax(0,1fr))}.cards.cards-2{grid-template-columns:repeat(2,minmax(0,1fr))}.card,.split-card,.timeline article,.stat{padding:1.5rem}.card{position:relative;overflow:hidden}.card:after{content:'';position:absolute;right:-2.2rem;bottom:-2.2rem;width:6rem;height:6rem;border-radius:50%;background:rgba(255,122,26,.10)}.card a{font-weight:800;color:var(--navy);text-decoration:none}.icon{display:inline-grid;place-items:center;width:3rem;height:3rem;margin-bottom:1rem;border-radius:14px;background:linear-gradient(135deg,#fff1e5,#ffe0c2);color:var(--orange);font-weight:800}.split-card{background:linear-gradient(180deg,#fff9f4 0%,#fff 100%)}.mini-list{padding-left:1.1rem;margin:1rem 0 0}.timeline{grid-template-columns:repeat(4,minmax(0,1fr))}.timeline article{background:linear-gradient(180deg,#fff 0%,#f8fbff 100%)}.step-no{display:inline-grid;place-items:center;width:2.25rem;height:2.25rem;margin-bottom:1rem;border-radius:999px;background:var(--navy);color:#fff;font-weight:800}.subnav{padding:0 0 2rem}.mega{padding:1rem 1.1rem;background:linear-gradient(180deg,#f8fbff 0%,#fff 100%)}.mega-grid{grid-template-columns:repeat(5,minmax(0,1fr))}.mega h4{margin:.2rem 0 .7rem;font-size:.95rem;color:var(--navy)}.mega a{display:block;padding:.48rem .2rem;text-decoration:none;color:var(--ink)}.mega a strong{display:block;font-size:.92rem}.mega a:hover strong{color:var(--orange)}.cta-box{padding:2rem;background:linear-gradient(135deg,var(--navy) 0%,var(--navy-2) 62%,#25518b 100%);color:#fff}.cta-box .section-label,.cta-box h2,.cta-box p,.cta-box .button.ghost{color:#fff}.cta-box .button.ghost{border-color:rgba(255,255,255,.2);background:transparent}.site-footer{padding:1.6rem 0 2.2rem;border-top:1px solid var(--line)}.footer-wrap p{margin:0}.muted{background:linear-gradient(180deg,#fff8f2 0%,#fff 100%)}
@media (max-width:1050px){.cards.cards-4,.mega-grid,.timeline{grid-template-columns:repeat(2,minmax(0,1fr))}.cards.cards-3{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:900px){.nav-toggle{display:inline-flex}.nav{position:absolute;top:calc(100% + .75rem);right:1rem;left:1rem;display:none;flex-direction:column;align-items:stretch;padding:1rem;border:1px solid var(--line);border-radius:22px;background:rgba(255,251,247,.98);box-shadow:var(--shadow)}.nav.is-open{display:flex}.hero-grid,.grid-2,.section-head,.nav-wrap,.footer-wrap,.cta-box{grid-template-columns:1fr;flex-direction:column;align-items:flex-start}.hero-stats,.cards.cards-4,.cards.cards-3,.cards.cards-2,.timeline,.mega-grid{grid-template-columns:1fr}.hero,.section{padding:4.2rem 0}}
@media (max-width:640px){.brand span:last-child{max-width:11.5rem;font-size:.95rem;line-height:1.15}h1{max-width:100%;font-size:clamp(2.25rem,12vw,3.8rem)}.button,.button-row .button,.nav-cta{width:100%}}
'''

SCRIPT = """const y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();const t=document.querySelector('.nav-toggle');const n=document.getElementById('site-nav');if(t&&n){t.addEventListener('click',()=>{const o=n.classList.toggle('is-open');t.setAttribute('aria-expanded',String(o))});n.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{n.classList.remove('is-open');t.setAttribute('aria-expanded','false')}))}"""


def rel_prefix(path):
    depth = len(Path(path).parts) - 1
    return './' if depth == 0 else '../' * depth


def href_from(page_path, target):
    if target == '#':
        return '#'
    page_dir = Path(page_path).parent
    target_path = Path(target.lstrip('/'))
    return Path(os.path.relpath(target_path, page_dir)).as_posix()


def render_nav(page_path, section):
    links = []
    for label, href in NAV:
        cls = 'active' if label == section else ''
        extra = ' nav-cta' if label == 'Contact' else ''
        links.append(f'<a class="{cls}{extra}" href="{href_from(page_path, href)}">{escape(label)}</a>')
    return '\n'.join(links)


def render_mega(page_path):
    cols = []
    for group, items in MEGA.items():
        item_html = ''.join(
            f'<a href="{href_from(page_path, href)}"><strong>{escape(label)}</strong><small>{escape(href.replace("/", " / ").strip())}</small></a>'
            for label, href in items
        )
        cols.append(f'<div><h4>{escape(group)}</h4>{item_html}</div>')
    return f'<section class="subnav"><div class="container"><div class="mega"><div class="mega-grid">{"".join(cols)}</div></div></div></section>'


def render_cards(page_path, block):
    cards = []
    cols = min(max(len(block['cards']), 2), 4)
    for idx, (title, text, href) in enumerate(block['cards'], start=1):
        link = '' if href == '#' else f'<p><a href="{href_from(page_path, href)}">Open page →</a></p>'
        cards.append(f'<article class="card"><div class="icon">{idx:02d}</div><h3>{escape(title)}</h3><p>{escape(text)}</p>{link}</article>')
    return f'''<section class="section {'muted' if cols%2==0 else ''}"><div class="container"><p class="section-label">{escape(block['kicker'])}</p><div class="section-head"><h2>{escape(block['title'])}</h2><p>{escape(block['text'])}</p></div><div class="cards cards-{cols}">{''.join(cards)}</div></div></section>'''


def render_split(block):
    bullets = ''.join(f'<li>{escape(b)}</li>' for b in block['bullets'])
    return f'''<section class="section"><div class="container grid-2"><div class="split-copy"><p class="section-label">{escape(block['kicker'])}</p><h2>{escape(block['title'])}</h2><p>{escape(block['text'])}</p></div><div class="split-card"><ul class="mini-list">{bullets}</ul></div></div></section>'''


def render_timeline(block):
    items = ''.join(f'<article><span class="step-no">{i}</span><h3>{escape(step.split(".")[0] if "." in step else "Step")}</h3><p>{escape(step)}</p></article>' for i, step in enumerate(block['steps'], start=1))
    return f'''<section class="section muted"><div class="container"><p class="section-label">{escape(block['kicker'])}</p><div class="section-head"><h2>{escape(block['title'])}</h2><p>{escape(block['text'])}</p></div><div class="timeline">{items}</div></div></section>'''


def render_content(page_path, blocks):
    out = []
    for block in blocks:
        if block['type'] == 'cards':
            out.append(render_cards(page_path, block))
        elif block['type'] == 'split':
            out.append(render_split(block))
        elif block['type'] == 'timeline':
            out.append(render_timeline(block))
    return '\n'.join(out)


def page_html(path, cfg):
    prefix = rel_prefix(path)
    stats = cfg.get('hero_stats', [('Structure', 'Real subpages instead of a single long scroll'), ('Orange / Navy', 'A younger, cleaner visual direction'), ('Current Content', 'Existing site content preserved and reorganized'), ('Ready for Growth', 'More detailed subpages can be expanded later')])
    stats_html = ''.join(f'<article><strong>{escape(a)}</strong><span>{escape(b)}</span></article>' for a, b in stats)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{escape(site['title'])} | {escape(cfg['title'])}</title>
<meta name="description" content="{escape(cfg['description'])}" />
<meta property="og:title" content="{escape(site['title'])} | {escape(cfg['title'])}" />
<meta property="og:description" content="{escape(cfg['description'])}" />
<meta property="og:type" content="website" /><meta property="og:url" content="https://sseptp.org/{escape(path if path!='index.html' else '')}" />
<link rel="canonical" href="https://sseptp.org/{escape(path if path!='index.html' else '')}" />
<link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{prefix}styles.css" /></head>
<body>
<header class="site-header"><div class="container nav-wrap"><a class="brand" href="{href_from(path, '/index.html')}"><span class="brand-mark">SSE</span><span>Sanskrithi School of Engineering</span></a><button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span></span><span class="sr-only">Toggle navigation</span></button><nav class="nav" id="site-nav">{render_nav(path, cfg['section'])}</nav></div></header>
<section class="hero"><div class="container hero-grid"><div><p class="eyebrow">{escape(cfg['hero_kicker'])}</p><h1>{escape(cfg['hero_title'])}</h1><p class="lead">{escape(cfg['hero_text'])}</p><div class="hero-actions"><a class="button primary" href="{href_from(path, '/admissions/index.html')}">Admissions</a><a class="button secondary" href="{href_from(path, '/academics/index.html')}">Academics</a></div></div><aside class="hero-panel"><div class="panel-topline"></div><div class="hero-stats">{stats_html}</div></aside></div></section>
{render_mega(path)}
{render_content(path, cfg['content'])}
<section class="section"><div class="container cta-box"><div><p class="section-label">Contact</p><h2>Want the next step to be clearer for students and families?</h2><p>This structure is now ready for richer real content, images, forms, and department-level detail without collapsing back into a single long page.</p></div><div class="button-row"><a class="button primary light" href="mailto:{site['email']}">{site['email']}</a><a class="button ghost" href="{href_from(path, '/contact.html')}">Contact page</a></div></div></section>
<footer class="site-footer"><div class="container footer-wrap"><p>© <span id="year"></span> Sanskrithi School of Engineering. All rights reserved.</p><p class="footer-note">Multi-page redesign aligned to the current site’s admissions, academics, campus, and placement structure.</p></div></footer>
<script src="{prefix}script.js"></script></body></html>'''


(ROOT / 'styles.css').write_text(STYLE)
(ROOT / 'script.js').write_text(SCRIPT)
(ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://sseptp.org/sitemap.xml\n')

for path, cfg in pages.items():
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page_html(path, cfg))

sitemap_urls = '\n'.join(f'  <url><loc>https://sseptp.org/{"" if p=="index.html" else p}</loc></url>' for p in pages)
(ROOT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap_urls}\n</urlset>\n')
print(f'Wrote {len(pages)} pages')
