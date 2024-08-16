from render_utils import *
from render_index import generate_index_html
from render_courses import generate_courses_html
from render_Research import generate_Research_html
from render_resume import generate_resume_html

with open("../../index.html", "w") as file:
    file.write(generate_index_html())

with open("../../resume.html", "w") as file:
    file.write(generate_resume_html())

with open("../../Research.html", "w") as file:
    file.write(generate_Research_html())

with open("../../courses.html", "w") as file:
    file.write(generate_courses_html())

import render_til