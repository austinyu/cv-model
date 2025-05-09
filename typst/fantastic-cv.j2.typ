#import "@preview/fantastic-cv:0.1.0": *


#let name = "{{ resume.basics.name }}"
#let location = "{{ resume.basics.location.city }}, {{ resume.basics.location.region }}"
#let email = "{{ resume.basics.email }}"
#let phone = "{{ resume.basics.phone }}"
#let url = "{{ resume.basics.url }}"

// [{network: str, username: str, url: str}]
#let profiles = (
{% for profile in resume.basics.profiles %}
  (
    network: "{{ profile.network }}",
    username: "{{ profile.username }}",
    url: "{{ profile.url }}",
  ),
{% endfor %}
)

/*
[
  {
    institution: str,
    location: str,
    url: str,
    area: str,
    studyType: str,
    startDate: str,
    endDate: str,
    score: str,
    courses: [str],
  }
]
*/
#let educations = (
{% for education in resume.education %}
  (
    institution: "{{ education.institution }}",
    location: "{{ education.location }}",
    url: "{{ education.url }}",
    area: "{{ education.area }}",
    studyType: "{{ education.studyType }}",
    startDate: "{{ education.startDate }}",
    endDate: "{{ education.endDate }}",
    score: "{{ education.score }}",
    courses: (
{% for course in education.courses %}
      "{{ course }}",
{% endfor %}
    ),
  ),
{% endfor %}
)


/*
[
  {
    name: str,
    location: str,
    url: str,
    description: str,
    position: str,
    startDate: str,
    endDate: str,
    highlights: [str],
  }
]
*/
#let works = (
{% for work in resume.work %}
  (
    name: "{{ work.name }}",
    location: "{{ work.location }}",
    url: "{{ work.url }}",
    description: "{{ work.description }}",
    position: "{{ work.position }}",
    startDate: "{{ work.startDate }}",
    endDate: "{{ work.endDate }}",
    highlights: (
{% for hl in work.highlights %}
      "{{ hl }}",
{% endfor %}
    ),
  ),
{% endfor %}
)

/*
[
  {
    name: str,
    url: str,
    source_code: str,
    roles: [str],
    startDate: str,
    endDate: str,
    description: str,
    highlights: [str],
  }
]
*/
#let projects = (
{% for project in resume.projects %}
  (
    name: "{{ project.name }}",
    url: "{{ project.url }}",
    source_code: "{{ project.source_code }}",
    roles: ({% for role in project.roles %}"{{ role }}"{% if not loop.last %}, {% endif %}{% endfor %}),
    startDate: "{{ project.startDate }}",
    endDate: "{{ project.endDate }}",
    description: "{{ project.description }}",
    highlights: (
{% for hl in project.highlights %}
     "{{ hl }}",
{% endfor %}
    ),
  ),
{% endfor %}
)

/*
[
  {
    organization: str,
    position: str,
    url: str,
    startDate: str,
    endDate: str,
    summary: str,
    location: str,
    highlights: [str],
  }
]
*/
#let volunteers = (
{% for volunteer in resume.volunteer %}
  (
    organization: "{{ volunteer.organization }}",
    position: "{{ volunteer.position }}",
    url: "{{ volunteer.url }}",
    startDate: "{{ volunteer.startDate }}",
    endDate: "{{ volunteer.endDate }}",
    summary: "{{ volunteer.summary }}",
    location: "{{ volunteer.location }}",
    highlights: (
{% for hl in volunteer.highlights %}
      "{{ hl }}",
{% endfor %}
    ),
  ),
{% endfor %}
)

/*
[
  {
    title: str,
    date: str,
    url: str,
    awarder: str,
    summary: str,
  }
]
*/
#let awards = (
{% for award in resume.awards %}
  (
    title: "{{ award.title }}",
    date: "{{ award.date }}",
    url: "{{ award.url }}",
    awarder: "{{ award.awarder }}",
    summary: "{{ award.summary }}",
  ),
{% endfor %}
)

/*
[
  {
    name: str,
    issuer: str,
    url: str,
    date: str,
  }
]
*/
#let certificates = (
{% for certificate in resume.certificates %}
  (
    name: "{{ certificate.name }}",
    issuer: "{{ certificate.issuer }}",
    url: "{{ certificate.url }}",
    date: "{{ certificate.date }}",
  ),
{% endfor %}
)

/*
[
  {
    name: str,
    publisher: str,
    releaseDate: str,
    url: str,
    summary: str,
  }
]
*/
#let publications = (
{% for publication in resume.publications %}
  (
    name: "{{ publication.name }}",
    publisher: "{{ publication.publisher }}",
    releaseDate: "{{ publication.releaseDate }}",
    url: "{{ publication.url }}",
    summary: "{{ publication.summary }}",
  ),
{% endfor %}
)

/*
[
  {
    title: str,
    highlights: [
      {
        summary: str,
        description: str,
      }
    ]
  }
]
*/
#let custom_sections = (
{% for custom_section in resume.custom_sections %}
  (
    title: "{{ custom_section.title }}",
    highlights: (
{% for highlight in custom_section.highlights %}
      (
        summary: "{{ highlight.summary }}",
        description: "{{ highlight.description }}",
      ),
{% endfor %}
    ),
  ),
{% endfor %}
)

#let render_font = "New Computer Modern"
#let render_size = 10pt
#let render_size_title = render_size * 1.5
#let render_size_section = render_size * 1.3
#let render_size_entry = render_size * 1.1
#let render_page_paper = "a4"
#let render_margin = (
  top: 0.5in,
  bottom: 0.5in,
  left: 0.5in,
  right: 0.5in,
)
#let render_accent_color = "#26428b"

#let render_space_between_highlight = -0.5em
#let render_space_between_sections = -0.5em

#show: config.with(
  font: render_font,
  font_size: render_size,
  page_paper: render_page_paper,
  margin: render_margin,
  accent_color: render_accent_color,
  space_between_sections: render_space_between_sections,
  space_between_highlight: render_space_between_highlight,
)

#section_basic_info(
  name: name,
  location: location,
  email: email,
  phone: phone,
  url: url,
  profiles: profiles,
)

#section_education(educations)

#section_work(works)

#section_project(projects)

#section_volunteer(volunteers)

#section_award(awards)

#section_certificate(certificates)

#section_publication(publications)

#sections_custom(custom_sections)
