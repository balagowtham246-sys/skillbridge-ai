def generate_summary(goal: str, skills: list, domain: str) -> str:
    skill_text = ", ".join(skills) if skills else "no listed skills"
    base_summary = (
        f"As an aspiring {goal}, you already have a foundation in {skill_text}. "
        f"To become proficient in {domain}, focus on mastering core tools and applying them "
        f"to hands-on projects. This roadmap will guide you step-by-step towards your target role, "
        f"balancing both theory and practical experience. "
        f"By following this path, you can be career-ready in under 12 weeks."
    )

    tips = [
        "Remember: consistency beats intensity. Learn daily!",
        "Try to build mini-projects as you learn.",
        "Collaborate with peers or open-source communities.",
        "Track progress weekly — it keeps motivation high!"
    ]

    import random
    ai_tip = random.choice(tips)
    return base_summary + " 💡 " + ai_tip
