import random

def recommend_courses(goal: str):
    library = {
        "Data Scientist": [
            "Python for Data Analysis",
            "Machine Learning Foundations",
            "Data Visualization with Seaborn"
        ],
        "Web Developer": [
            "HTML, CSS & JS Bootcamp",
            "React.js from Scratch",
            "Node.js API Development"
        ],
        "AI Engineer": [
            "Deep Learning with TensorFlow",
            "Building Neural Networks",
            "Prompt Engineering 101"
        ],
        "Cloud Engineer": [
            "AWS Essentials",
            "Docker & Kubernetes Fundamentals",
            "CI/CD with Jenkins"
        ],
    }

    domain_courses = library.get(goal.title(), library["AI Engineer"])
    courses = random.sample(domain_courses, k=min(3, len(domain_courses)))

    formatted = [
        {"title": title, "duration": f"{random.randint(2,5)} weeks"} for title in courses
    ]
    return formatted
