from __future__ import annotations

from pydantic import BaseModel

Iso8601 = str
AnyUrl = str

State = str  # two character abbreviation for US states, e.g. CA, NY


class Basics(BaseModel):
    class Location(BaseModel):
        address: str = ""
        postalCode: str = ""
        city: str = ""
        # Code as per ISO-3166-1 ALPHA-2, e.g. US, AU, IN
        countryCode: str = ""
        # The general region where you live. Can be a US state, or a province, for instance.
        region: State = ""

    class Profiles(BaseModel):
        # e.g. Facebook or Twitter
        network: str = ""
        username: str = ""
        url: AnyUrl = ""

    name: str = ""
    # e.g. Web Developer
    label: str = ""
    # URL (as per RFC 3986) to a image in JPEG or PNG format
    image: AnyUrl = ""
    # e.g. thomas@gmail.com
    email: str = ""
    # Phone numbers are stored as strings so use any format you like, e.g. 712-117-2923
    phone: str = ""
    # URL (as per RFC 3986) to your website, e.g. personal homepage
    url: AnyUrl = ""
    # Write a short 2-3 sentence biography about yourself
    summary: str = ""
    location: Location = Location()
    profiles: list[Profiles] = []

    @staticmethod
    def get_default() -> Basics:
        return Basics(
            name="Austin Yu",
            label="Software Engineer",
            image="",
            email="yuxm.austin1023@gmail.com",
            phone="+1 (xxx) xxx-xxxx",
            url="https://www.google.com",
            summary="A dedicated software engineer with experience in cloud services, AI, and autonomous systems.",
            location=Basics.Location(
                address="",
                postalCode="",
                city="Bay Area",
                countryCode="US",
                region="CA",
            ),
            profiles=[
                Basics.Profiles(
                    network="GitHub",
                    username="austinyu",
                    url="https://github.com/austinyu",
                ),
                Basics.Profiles(
                    network="LinkedIn",
                    username="xinmiao-yu-619128174",
                    url="https://linkedin.com/in/xinmiao-yu-619128174",
                ),
            ],
        )


class Education(BaseModel):
    # e.g. Massachusetts Institute of Technology
    institution: str = ""
    location: str = ""
    # e.g. http://facebook.example.com
    url: AnyUrl | None = None
    # e.g. Arts
    area: str = ""
    # e.g. Bachelor
    studyType: str = ""
    # Start date in ISO 8601 format
    startDate: Iso8601 = ""
    # End date in ISO 8601 format
    endDate: Iso8601 = ""
    # Grade point average, e.g. 3.67/4.0
    score: str = ""
    # List notable courses/subjects
    courses: list[str] = []

    @staticmethod
    def get_default() -> list[Education]:
        return [
            Education(
                institution="Stanford University",
                location="Stanford, CA",
                url="https://stanford.edu",
                area="Physics and Computer Science",
                studyType="Bachelor of Science",
                startDate="2019-09-01",
                endDate="2023-06-01",
                score="3.9/4.0",
                courses=[
                    "Data Structures",
                    "Algorithms",
                    "Operating Systems",
                    "Computer Networks",
                    "Quantum Mechanics",
                    "Linear Algebra",
                    "Machine Learning",
                    "Multivariable Calculus",
                ],
            ),
            Education(
                institution="University of California, Berkeley",
                location="Berkeley, CA",
                url="https://berkeley.edu",
                area="Computer Science",
                studyType="Master of Science",
                startDate="2023-08-01",
                endDate="2025-05-01",
                score="4.0/4.0",
                courses=[
                    "Advanced Machine Learning",
                    "Distributed Systems",
                    "Cryptography",
                    "Artificial Intelligence",
                    "Database Systems",
                    "Convex Optimization",
                    "Natural Language Processing",
                    "Computer Vision",
                ],
            ),
        ]


class Work(BaseModel):
    # e.g. Facebook
    name: str = ""
    # e.g. Menlo Park, CA
    location: str = ""
    # e.g. Social Media Company
    description: str = ""
    # e.g. Software Engineer
    position: str = ""
    # e.g. http://facebook.example.com
    url: AnyUrl | None = None
    # Start date in ISO 8601 format
    startDate: Iso8601 = ""
    # End date in ISO 8601 format
    endDate: Iso8601 = ""
    # Overview of responsibilities at the company
    summary: str = ""
    # Specify multiple accomplishments
    highlights: list[str] = []

    @staticmethod
    def get_default() -> list[Work]:
        return [
            Work(
                name="Microsoft",
                location="Redmond, WA",
                description="Azure Cloud Services Team",
                position="Software Engineer Intern",
                url="https://microsoft.com",
                startDate="2023-05-15",
                endDate="2023-08-15",
                summary="Developed solutions for Azure cloud services and improved performance metrics.",
                highlights=[
                    "Developed a distributed caching solution for Azure Functions, reducing cold start latency by 30% and improving overall performance for serverless applications.",
                    "Implemented a monitoring dashboard using Power BI to visualize key performance metrics, enabling proactive issue detection and resolution.",
                    "Collaborated with a team of engineers to refactor legacy code, improving maintainability and reducing technical debt by 25%.",
                    "Contributed to the design and development of a new API gateway, enhancing scalability and security for cloud-based applications.",
                    "Presented project outcomes to senior engineers and received commendation for delivering impactful solutions under tight deadlines.",
                ],
            ),
            Work(
                name="Amazon",
                location="Seattle, WA",
                description="Alexa Smart Home Team",
                position="Software Development Engineer Intern",
                url="https://amazon.com",
                startDate="2022-06-01",
                endDate="2022-09-01",
                highlights=[
                    "Designed and implemented a feature to integrate third-party smart home devices with Alexa, increasing compatibility by 20%.",
                    "Optimized voice recognition algorithms, reducing error rates by 15% and improving user satisfaction.",
                    "Developed automated testing frameworks to ensure the reliability of new integrations, achieving 90% test coverage.",
                    "Worked closely with product managers to define feature requirements and deliver a seamless user experience.",
                    "Participated in code reviews and contributed to team-wide best practices for software development.",
                ],
            ),
            Work(
                name="Tesla",
                location="Palo Alto, CA",
                description="Autopilot Software Team",
                position="Software Engineer Intern",
                url="https://tesla.com",
                startDate="2021-06-01",
                endDate="2021-08-31",
                highlights=[
                    "Developed and tested computer vision algorithms for lane detection, improving accuracy by 25% in challenging driving conditions.",
                    "Enhanced the performance of real-time object detection systems, reducing processing latency by 10%.",
                    "Collaborated with hardware engineers to optimize sensor data processing pipelines for autonomous vehicles.",
                    "Conducted extensive simulations to validate new features, ensuring compliance with safety standards.",
                    "Documented technical findings and contributed to research papers on advancements in autonomous driving technology.",
                ],
            ),
        ]


class Project(BaseModel):
    # e.g. The World Wide Web
    name: str = ""
    # Short summary of project. e.g. Collated works of 2017.
    description: str = ""
    # Specify multiple features
    highlights: list[str] = []
    # Specify special elements involved
    keywords: list[str] = []
    # Start date in ISO 8601 format
    startDate: Iso8601 = ""
    # End date in ISO 8601 format
    endDate: Iso8601 = ""
    # URL (as per RFC 3986) to the project
    url: AnyUrl | None = None
    # Specify your role on this project or in the company
    roles: list[str] = []
    # Specify the relevant company/entity affiliations
    entity: str = ""
    # e.g. 'volunteering', 'presentation', 'talk', 'application', 'conference'
    type: str = ""
    source_code: str = ""

    @staticmethod
    def get_default() -> list[Project]:
        return [
            Project(
                name="Hyperschedule",
                description="Developed and maintained an open-source scheduling tool used by students across the Claremont Consortium, leveraging TypeScript, React, and MongoDB.",
                highlights=[
                    "Implemented new features such as course filtering and schedule sharing, improving user experience and engagement.",
                    "Collaborated with a team of contributors to address bugs and optimize performance, reducing load times by 40%.",
                    "Coordinated with college administrators to ensure accurate and timely release of course data.",
                ],
                keywords=["React", "TypeScript", "MongoDB", "Git"],
                startDate="2022-01-01",
                endDate="2023-06-01",
                url="https://hyperschedule.io",
                roles=["Individual Contributor", "Maintainer"],
                entity="Claremont Colleges",
                type="application",
                source_code="https://github.com/hyperschedule",
            ),
            Project(
                name="Claremont Colleges Course Registration",
                description="Contributed to the development of a course registration platform for the Claremont Colleges, streamlining the enrollment process for thousands of students.",
                highlights=[
                    "Designed and implemented a user-friendly interface for course selection, increasing adoption rates by 25%.",
                    "Optimized backend systems to handle peak traffic during registration periods, ensuring system stability.",
                    "Provided technical support and documentation to assist users and administrators with platform usage.",
                ],
                keywords=["React", "Node.js", "PostgreSQL", "Git"],
                startDate="2021-09-01",
                endDate="2022-12-01",
                url="",
                roles=["Individual Contributor", "Maintainer"],
                entity="Claremont Colleges",
                type="application",
                source_code="https://github.com/claremont-colleges",
            ),
        ]


class Volunteer(BaseModel):
    # e.g. Facebook
    organization: str = ""
    # e.g. Software Engineer
    position: str = ""
    # e.g. http://facebook.example.com
    url: AnyUrl | None = None
    # Start date in ISO 8601 format
    startDate: Iso8601 = ""
    # End date in ISO 8601 format
    endDate: Iso8601 = ""
    # Overview of responsibilities at the organization
    summary: str = ""
    # Specify multiple accomplishments
    highlights: list[str] = []
    location: str = ""

    @staticmethod
    def get_default() -> list[Volunteer]:
        return [
            Volunteer(
                organization="Bay Area Homeless Shelter",
                position="Volunteer Coordinator",
                url="",
                startDate="2023-01-01",
                endDate="2023-05-01",
                summary="Coordinated volunteer efforts to support homeless individuals in the Bay Area, providing essential services and resources.",
                location="Bay Area, CA",
                highlights=[
                    "Managed a team of 20+ volunteers to organize weekly meal services",
                    "Collaborated with a team of volunteers to sort and package food donations, ensuring efficient distribution to partner agencies.",
                    "Participated in community education initiatives, promoting awareness of food insecurity and available resources.",
                ],
            ),
            Volunteer(
                organization="Stanford University",
                position="Volunteer Tutor",
                url="stanford.edu",
                startDate="2023-06-01",
                endDate="2023-09-01",
                location="Stanford, CA",
                summary="Provided tutoring support to high school students in mathematics and science subjects, fostering academic growth and confidence.",
                highlights=[
                    "Developed personalized lesson plans and study materials to address individual student needs.",
                    "Facilitated group study sessions, encouraging collaboration and peer learning.",
                    "Received positive feedback from students and parents for effective teaching methods and dedication to student success.",
                ],
            ),
        ]


class Award(BaseModel):
    # e.g. One of the 100 greatest minds of the century
    title: str = ""
    url: AnyUrl | None = None
    # Date in ISO 8601 format
    date: Iso8601 = ""
    # e.g. Time Magazine
    awarder: str = ""
    # e.g. Received for my work with Quantum Physics
    summary: str = ""

    @staticmethod
    def get_default() -> list[Award]:
        return [
            Award(
                title="Best Student Award",
                date="2023-05-01",
                url="https://stanford.edu",
                awarder="Stanford University",
                summary="",
            ),
            Award(
                title="Dean's List",
                date="2023-05-01",
                url="",
                awarder="Stanford University",
                summary="Achieved Dean's List status for maintaining a GPA of 3.9 or higher.",
            ),
            Award(
                title="Outstanding Research Assistant",
                date="2023-05-01",
                url="https://stanford.edu",
                awarder="",
                summary="Recognized for exceptional contributions to research projects in the Physics and Computer Science departments.",
            ),
            Award(
                title="Best Paper Award",
                date="2023-05-01",
                url="https://berkeley.edu",
                awarder="University of California, Berkeley",
                summary="Received Best Paper Award at the UC Berkeley Graduate Research Symposium.",
            ),
        ]


class Certificate(BaseModel):
    # e.g. Certified Kubernetes Administrator
    name: str = ""
    # Date in ISO 8601 format
    date: Iso8601 = ""
    # e.g. http://example.com
    url: AnyUrl | None = None
    # e.g. CNCF
    issuer: str = ""

    @staticmethod
    def get_default() -> list[Certificate]:
        return [
            Certificate(
                name="AWS Certified Solutions Architect",
                issuer="",
                url="https://aws.amazon.com/certification/certified-solutions-architect-associate/",
                date="2023-05-01",
            ),
            Certificate(
                name="Google Cloud Professional Data Engineer",
                issuer="Google Cloud",
                url="https://cloud.google.com/certification/data-engineer/",
                date="2023-05-01",
            ),
            Certificate(
                name="Microsoft Certified: Azure Fundamentals",
                issuer="Microsoft",
                url="https://learn.microsoft.com/en-us/certifications/azure-fundamentals/",
                date="2023-05-01",
            ),
            Certificate(
                name="Certified Kubernetes Administrator (CKA)",
                issuer="Linux Foundation",
                url="",
                date="2023-05-01",
            ),
            Certificate(
                name="Certified Ethical Hacker (CEH)",
                issuer="",
                url="https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/",
                date="2023-05-01",
            ),
        ]


class Publication(BaseModel):
    # e.g. The World Wide Web
    name: str = ""
    # e.g. IEEE, Computer Magazine
    publisher: str = ""
    # Release date in ISO 8601 format
    releaseDate: Iso8601 = ""
    # e.g. http://www.computer.org.example.com/csdl/mags/co/1996/10/rx069-abs.html
    url: AnyUrl | None = None
    # Short summary of publication
    summary: str = ""

    @staticmethod
    def get_default() -> list[Publication]:
        return [
            Publication(
                name="Understanding Quantum Computing",
                publisher="Springer",
                releaseDate="2023-05-01",
                url="https://arxiv.org/abs/quantum-computing",
                summary="A comprehensive overview of quantum computing principles and applications.",
            ),
            Publication(
                name="Machine Learning for Beginners",
                publisher="O'Reilly Media",
                releaseDate="2023-05-01",
                url="",
                summary="",
            ),
            Publication(
                name="Advanced Algorithms in Python",
                publisher="Packt Publishing",
                releaseDate="2023-05-01",
                url="https://packt.com/advanced-algorithms-python",
                summary="A deep dive into advanced algorithms and data structures using Python.",
            ),
            Publication(
                name="Data Science Handbook",
                publisher="Springer",
                releaseDate="2023-05-01",
                url="",
                summary="A practical guide to data science methodologies and tools.",
            ),
        ]


class Skill(BaseModel):
    # e.g. Web Development
    name: str = ""
    # e.g. Master
    level: str = ""
    # List some keywords pertaining to this skill
    keywords: list[str] = []

    @staticmethod
    def get_default() -> list[Skill]:
        return [
            Skill(
                name="Web Development",
                level="Master",
                keywords=[
                    "HTML",
                    "CSS",
                    "JavaScript",
                    "React",
                    "Node.js",
                    "Express",
                    "Django",
                    "Flask",
                    "Ruby on Rails",
                    "RESTful APIs",
                ],
            ),
            Skill(
                name="Machine Learning",
                level="Intermediate",
                keywords=[
                    "Python",
                    "TensorFlow",
                    "Keras",
                    "PyTorch",
                    "Scikit-learn",
                    "Natural Language Processing",
                    "Computer Vision",
                ],
            ),
            Skill(
                name="Cloud Computing",
                level="Intermediate",
                keywords=[
                    "AWS",
                    "Azure",
                    "Google Cloud Platform",
                    "Docker",
                    "Kubernetes",
                    "Terraform",
                    "CI/CD",
                ],
            ),
        ]


class Language(BaseModel):
    # e.g. English, Spanish
    language: str = ""
    # e.g. Fluent, Beginner
    fluency: str = ""

    @staticmethod
    def get_default() -> list[Language]:
        return [
            Language(language="English", fluency="Native speaker"),
            Language(language="Spanish", fluency="Conversational"),
            Language(language="Mandarin", fluency="Basic"),
            Language(language="French", fluency="Basic"),
        ]


class Interest(BaseModel):
    # e.g. Philosophy
    name: str = ""
    # List some keywords pertaining to this interest
    keywords: list[str] = []

    @staticmethod
    def get_default() -> list[Interest]:
        return [
            Interest(
                name="Artificial Intelligence",
                keywords=[
                    "Machine Learning",
                    "Deep Learning",
                    "Natural Language Processing",
                    "Computer Vision",
                    "Reinforcement Learning",
                ],
            ),
            Interest(
                name="Quantum Computing",
                keywords=[
                    "Quantum Algorithms",
                    "Quantum Cryptography",
                    "Quantum Machine Learning",
                    "Quantum Information Theory",
                ],
            ),
            Interest(
                name="Software Development",
                keywords=[
                    "Agile Methodologies",
                    "Version Control (Git)",
                    "Continuous Integration/Continuous Deployment (CI/CD)",
                    "Test-Driven Development (TDD)",
                    "Code Review",
                ],
            ),
        ]


class Reference(BaseModel):
    # e.g. Timothy Cook
    name: str = ""
    # e.g. Joe blogs was a great employee, who turned up to work at least once a week. He exceeded my expectations when it came to doing nothing.
    reference: str = ""

    @staticmethod
    def get_default() -> list[Reference]:
        return [
            Reference(
                name="Timothy Cook",
                reference="Joe blogs was a great employee, who turned up to work at least once a week. He exceeded my expectations when it came to doing nothing.",
            ),
            Reference(
                name="Bill Gates",
                reference="Joe blogs was a great employee, who turned up to work at least once a week. He exceeded my expectations when it came to doing nothing.",
            ),
            Reference(
                name="Elon Musk",
                reference="Joe blogs was a great employee, who turned up to work at least once a week. He exceeded my expectations when it came to doing nothing.",
            ),
        ]


class Meta(BaseModel):
    # URL (as per RFC 3986) to the latest version of this document
    canonical: AnyUrl | None = None
    # A version field which follows semver - e.g. v1.0.0
    version: str = ""
    # Using ISO 8601 with YYYY-MM-DDThh:mm:ss
    lastModified: Iso8601 = ""

    @staticmethod
    def get_default() -> Meta:
        return Meta(
            canonical="https://example.com/resume.json",
            version="v1.0.0",
            lastModified="2023-01-01T12:00:00",
        )


class CustomSection(BaseModel):
    class Highlight(BaseModel):
        summary: str = ""
        description: str = ""

    title: str = ""
    highlights: list[Highlight] = []

    @staticmethod
    def get_default() -> list[CustomSection]:
        return [
            CustomSection(
                title="Programming Languages",
                highlights=[
                    CustomSection.Highlight(
                        summary="Languages",
                        description="Python, Java, C++, JavaScript, TypeScript",
                    ),
                    CustomSection.Highlight(
                        summary="Frameworks",
                        description="React, Node.js, Express, Flask, Django",
                    ),
                    CustomSection.Highlight(
                        summary="Databases",
                        description="MySQL, MongoDB, PostgreSQL",
                    ),
                    CustomSection.Highlight(
                        summary="Tools",
                        description="Git, Docker, Kubernetes, AWS, GCP",
                    ),
                ],
            ),
            CustomSection(
                title="Skills",
                highlights=[
                    CustomSection.Highlight(
                        summary="Soft Skills",
                        description="Teamwork, Communication, Problem Solving, Time Management",
                    ),
                    CustomSection.Highlight(
                        summary="Technical Skills",
                        description="Data Structures, Algorithms, Software Development, Web Development",
                    ),
                    CustomSection.Highlight(
                        summary="Languages",
                        description="English (Fluent), Spanish (Conversational)",
                    ),
                ],
            ),
        ]


class Resume(BaseModel):
    # The version of the JSON Resume schema that this document conforms to
    # json_schema: str = Field(alias="$schema")
    # The basics section of the resume
    basics: Basics
    # The work experience section of the resume
    work: list[Work] = []
    # The volunteer experience section of the resume
    volunteer: list[Volunteer] = []
    # The education section of the resume
    education: list[Education] = []
    # The awards section of the resume
    awards: list[Award] = []
    # The certificates section of the resume
    certificates: list[Certificate] = []
    # The publications section of the resume
    publications: list[Publication] = []
    # The skills section of the resume
    skills: list[Skill] = []
    # The languages section of the resume
    languages: list[Language] = []
    # The interests section of the resume
    interests: list[Interest] = []
    # The references section of the resume
    references: list[Reference] = []
    # The projects section of the resume
    projects: list[Project] = []  # The meta section of the resume

    custom_sections: list[CustomSection] = []
    meta: Meta | None = None

    @staticmethod
    def get_default() -> Resume:
        return Resume(
            basics=Basics.get_default(),
            work=Work.get_default(),
            volunteer=Volunteer.get_default(),
            education=Education.get_default(),
            awards=Award.get_default(),
            certificates=Certificate.get_default(),
            publications=Publication.get_default(),
            skills=Skill.get_default(),
            languages=Language.get_default(),
            interests=Interest.get_default(),
            references=Reference.get_default(),
            projects=Project.get_default(),
            custom_sections=CustomSection.get_default(),
            meta=Meta.get_default(),
        )
