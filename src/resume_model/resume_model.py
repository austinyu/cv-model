from __future__ import annotations

from pydantic import BaseModel

Iso8601 = str
AnyUrl = str


class Basics(BaseModel):
    class Location(BaseModel):
        address: str | None = None
        postalCode: str | None = None
        city: str | None = None
        # Code as per ISO-3166-1 ALPHA-2, e.g. US, AU, IN
        countryCode: str | None = None
        # The general region where you live. Can be a US state, or a province, for instance.
        region: str | None = None

    class Profiles(BaseModel):
        # e.g. Facebook or Twitter
        network: str | None = None
        username: str | None = None
        url: AnyUrl | None = None

    name: str | None = None
    # e.g. Web Developer
    label: str | None = None
    # URL (as per RFC 3986) to a image in JPEG or PNG format
    image: AnyUrl | None = None
    # e.g. thomas@gmail.com
    email: str | None = None
    # Phone numbers are stored as strings so use any format you like, e.g. 712-117-2923
    phone: str | None = None
    # URL (as per RFC 3986) to your website, e.g. personal homepage
    url: AnyUrl | None = None
    # Write a short 2-3 sentence biography about yourself
    summary: str | None = None
    location: Location | None = None
    profiles: list[Profiles] | None = None

    @staticmethod
    def get_default() -> Basics:
        return Basics(
            name="John Doe",
            label="Programmer",
            image="",
            email="john@gmail.com",
            phone="(912) 555-4321",
            url="https://johndoe.com",
            summary="A summary of John Doe…",
            location=Basics.Location(
                address="2712 Broadway St",
                postalCode="CA 94115",
                city="San Francisco",
                countryCode="US",
                region="California",
            ),
            profiles=[
                Basics.Profiles(
                    network="Twitter",
                    username="john",
                    url="https://twitter.com/john",
                ),
                Basics.Profiles(
                    network="LinkedIn",
                    username="johndoe",
                    url="https://linkedin.com/in/johndoe",
                ),
                Basics.Profiles(network="GitHub", username="johndoe", url=""),
            ],
        )


class Work(BaseModel):
    # e.g. Facebook
    name: str | None = None
    # e.g. Menlo Park, CA
    location: str | None = None
    # e.g. Social Media Company
    description: str | None = None
    # e.g. Software Engineer
    position: str | None = None
    # e.g. http://facebook.example.com
    url: AnyUrl | None = None
    # Start date in ISO 8601 format
    startDate: Iso8601 | None = None
    # End date in ISO 8601 format
    endDate: Iso8601 | None = None
    # Overview of responsibilities at the company
    summary: str | None = None
    # Specify multiple accomplishments
    highlights: list[str] | None = None

    @staticmethod
    def get_default() -> Work:
        return Work(
            name="Example Company",
            location="Example City, EX",
            description="An example company description.",
            position="Example Position",
            url="https://example.com",
            startDate="2020-01-01",
            endDate="2022-01-01",
            summary="An example summary of responsibilities.",
            highlights=[
                "Achieved a significant milestone.",
                "Implemented a key feature that improved performance.",
            ],
        )


class Volunteer(BaseModel):
    # e.g. Facebook
    organization: str | None = None
    # e.g. Software Engineer
    position: str | None = None
    # e.g. http://facebook.example.com
    url: AnyUrl | None = None
    # Start date in ISO 8601 format
    startDate: Iso8601 | None = None
    # End date in ISO 8601 format
    endDate: Iso8601 | None = None
    # Overview of responsibilities at the organization
    summary: str | None = None
    # Specify multiple accomplishments
    highlights: list[str] | None = None
    location: str | None = None

    @staticmethod
    def get_default() -> Volunteer:
        return Volunteer(
            organization="Example Organization",
            position="Volunteer Position",
            url="https://example.org",
            startDate="2019-01-01",
            endDate="2020-01-01",
            summary="An example summary of volunteer responsibilities.",
            highlights=[
                "Organized community events.",
                "Raised funds for local charities.",
            ],
        )


class Education(BaseModel):
    # e.g. Massachusetts Institute of Technology
    institution: str | None = None
    location: str | None = None
    # e.g. http://facebook.example.com
    url: AnyUrl | None = None
    # e.g. Arts
    area: str | None = None
    # e.g. Bachelor
    studyType: str | None = None
    # Start date in ISO 8601 format
    startDate: Iso8601 | None = None
    # End date in ISO 8601 format
    endDate: Iso8601 | None = None
    # Grade point average, e.g. 3.67/4.0
    score: str | None = None
    # List notable courses/subjects
    courses: list[str] | None = None

    @staticmethod
    def get_default() -> Education:
        return Education(
            institution="Example University",
            url="https://example.edu",
            area="Computer Science",
            studyType="Bachelor",
            startDate="2015-09-01",
            endDate="2019-06-01",
            score="3.8/4.0",
            courses=[
                "CS101 - Introduction to Computer Science",
                "CS201 - Data Structures and Algorithms",
                "CS301 - Operating Systems",
            ],
        )


class Award(BaseModel):
    # e.g. One of the 100 greatest minds of the century
    title: str | None = None
    url: AnyUrl | None = None
    # Date in ISO 8601 format
    date: Iso8601 | None = None
    # e.g. Time Magazine
    awarder: str | None = None
    # e.g. Received for my work with Quantum Physics
    summary: str | None = None

    @staticmethod
    def get_default() -> Award:
        return Award(
            title="Example Award",
            date="2021-01-01",
            awarder="Example Organization",
            summary="An example summary of the award.",
        )


class Certificate(BaseModel):
    # e.g. Certified Kubernetes Administrator
    name: str | None = None
    # Date in ISO 8601 format
    date: Iso8601 | None = None
    # e.g. http://example.com
    url: AnyUrl | None = None
    # e.g. CNCF
    issuer: str | None = None

    @staticmethod
    def get_default() -> Certificate:
        return Certificate(
            name="Example Certificate",
            date="2022-01-01",
            url="https://example.com",
            issuer="Example Issuer",
        )


class Publication(BaseModel):
    # e.g. The World Wide Web
    name: str | None = None
    # e.g. IEEE, Computer Magazine
    publisher: str | None = None
    # Release date in ISO 8601 format
    releaseDate: Iso8601 | None = None
    # e.g. http://www.computer.org.example.com/csdl/mags/co/1996/10/rx069-abs.html
    url: AnyUrl | None = None
    # Short summary of publication
    summary: str | None = None

    @staticmethod
    def get_default() -> Publication:
        return Publication(
            name="Example Publication",
            publisher="Example Publisher",
            releaseDate="2020-01-01",
            url="https://example.com",
            summary="An example summary of the publication.",
        )


class Skill(BaseModel):
    # e.g. Web Development
    name: str | None = None
    # e.g. Master
    level: str | None = None
    # List some keywords pertaining to this skill
    keywords: list[str] | None = None

    @staticmethod
    def get_default() -> Skill:
        return Skill(
            name="Web Development",
            level="Master",
            keywords=["HTML", "CSS", "JavaScript", "React"],
        )


class Language(BaseModel):
    # e.g. English, Spanish
    language: str | None = None
    # e.g. Fluent, Beginner
    fluency: str | None = None

    @staticmethod
    def get_default() -> Language:
        return Language(language="English", fluency="Fluent")


class Interest(BaseModel):
    # e.g. Philosophy
    name: str | None = None
    # List some keywords pertaining to this interest
    keywords: list[str] | None = None

    @staticmethod
    def get_default() -> Interest:
        return Interest(
            name="Philosophy",
            keywords=["Friedrich Nietzsche", "Existentialism", "Stoicism"],
        )


class Reference(BaseModel):
    # e.g. Timothy Cook
    name: str | None = None
    # e.g. Joe blogs was a great employee, who turned up to work at least once a week. He exceeded my expectations when it came to doing nothing.
    reference: str | None = None

    @staticmethod
    def get_default() -> Reference:
        return Reference(name="Example Reference", reference="An example reference text.")


class Project(BaseModel):
    # e.g. The World Wide Web
    name: str | None = None
    # Short summary of project. e.g. Collated works of 2017.
    description: str | None = None
    # Specify multiple features
    highlights: list[str] | None = None
    # Specify special elements involved
    keywords: list[str] | None = None
    # Start date in ISO 8601 format
    startDate: Iso8601 | None = None
    # End date in ISO 8601 format
    endDate: Iso8601 | None = None
    # URL (as per RFC 3986) to the project
    url: AnyUrl | None = None
    # Specify your role on this project or in the company
    roles: list[str] | None = None
    # Specify the relevant company/entity affiliations
    entity: str | None = None
    # e.g. 'volunteering', 'presentation', 'talk', 'application', 'conference'
    type: str | None = None
    source_code: str | None = None

    @staticmethod
    def get_default() -> Project:
        return Project(
            name="Example Project",
            description="An example project description.",
            highlights=["Implemented a key feature.", "Improved performance by 20%."],
            keywords=["Python", "Django", "REST API"],
            startDate="2021-01-01",
            endDate="2021-12-31",
            url="https://example.com/project",
            roles=["Developer", "Team Lead"],
            entity="Example Company",
            type="application",
        )


class Meta(BaseModel):
    # URL (as per RFC 3986) to the latest version of this document
    canonical: AnyUrl | None = None
    # A version field which follows semver - e.g. v1.0.0
    version: str | None = None
    # Using ISO 8601 with YYYY-MM-DDThh:mm:ss
    lastModified: Iso8601 | None = None

    @staticmethod
    def get_default() -> Meta:
        return Meta(
            canonical="https://example.com/resume.json",
            version="v1.0.0",
            lastModified="2023-01-01T12:00:00",
        )


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
    projects: list[Project] = []
    # The meta section of the resume
    meta: Meta | None = None

    @staticmethod
    def get_default() -> Resume:
        return Resume(
            # json_schema="https://jsonresume.org/schema.json",
            basics=Basics.get_default(),
            work=[Work.get_default()],
            volunteer=[Volunteer.get_default()],
            education=[Education.get_default()],
            awards=[Award.get_default()],
            certificates=[Certificate.get_default()],
            publications=[Publication.get_default()],
            skills=[Skill.get_default()],
            languages=[Language.get_default()],
            interests=[Interest.get_default()],
            references=[Reference.get_default()],
            projects=[Project.get_default()],
            meta=Meta.get_default(),
        )


EXAMPLE = """
{
  "basics": {
    "name": "John Doe",
    "label": "Programmer",
    "image": "",
    "email": "john@gmail.com",
    "phone": "(912) 555-4321",
    "url": "https://johndoe.com",
    "summary": "A summary of John Doe…",
    "location": {
      "address": "2712 Broadway St",
      "postalCode": "CA 94115",
      "city": "San Francisco",
      "countryCode": "US",
      "region": "California"
    },
    "profiles": [{
      "network": "Twitter",
      "username": "john",
      "url": "https://twitter.com/john"
    }]
  },
  "work": [{
    "name": "Company",
    "position": "President",
    "url": "https://company.com",
    "startDate": "2013-01-01",
    "endDate": "2014-01-01",
    "summary": "Description…",
    "highlights": [
      "Started the company"
    ]
  }],
  "volunteer": [{
    "organization": "Organization",
    "position": "Volunteer",
    "url": "https://organization.com/",
    "startDate": "2012-01-01",
    "endDate": "2013-01-01",
    "summary": "Description…",
    "highlights": [
      "Awarded 'Volunteer of the Month'"
    ]
  }],
  "education": [{
    "institution": "University",
    "url": "https://institution.com/",
    "area": "Software Development",
    "studyType": "Bachelor",
    "startDate": "2011-01-01",
    "endDate": "2013-01-01",
    "score": "4.0",
    "courses": [
      "DB1101 - Basic SQL"
    ]
  }],
  "awards": [{
    "title": "Award",
    "date": "2014-11-01",
    "awarder": "Company",
    "summary": "There is no spoon."
  }],
  "certificates": [{
    "name": "Certificate",
    "date": "2021-11-07",
    "issuer": "Company",
    "url": "https://certificate.com"
  }],
  "publications": [{
    "name": "Publication",
    "publisher": "Company",
    "releaseDate": "2014-10-01",
    "url": "https://publication.com",
    "summary": "Description…"
  }],
  "skills": [{
    "name": "Web Development",
    "level": "Master",
    "keywords": [
      "HTML",
      "CSS",
      "JavaScript"
    ]
  }],
  "languages": [{
    "language": "English",
    "fluency": "Native speaker"
  }],
  "interests": [{
    "name": "Wildlife",
    "keywords": [
      "Ferrets",
      "Unicorns"
    ]
  }],
  "references": [{
    "name": "Jane Doe",
    "reference": "Reference…"
  }],
  "projects": [{
    "name": "Project",
    "startDate": "2019-01-01",
    "endDate": "2021-01-01",
    "description": "Description...",
    "highlights": [
      "Won award at AIHacks 2016"
    ],
    "url": "https://project.com/"
  }]
}
"""

print(Resume.model_validate_json(EXAMPLE))
