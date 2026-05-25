skills_list = [
    "python",
    "sql",
    "power bi",
    "excel",
    "machine learning",
    "tableau"
]

def extract_skills(text):

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills