def build_prompt(resume_text: str, job_description: str) -> str:
    return f"Resume:\n{resume_text}\n\nJob Description:\n{job_description}"
