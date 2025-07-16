def format_research_prompt(topic, goal, data):
    return f"""
You are a chemistry research assistant.

Given:
- Topic: {topic}
- Goal: {goal}
- Known data: {data}

Generate 3 original and practical chemistry research ideas. Each idea should be 2–3 sentences. Focus on feasibility, novelty, and relevance.
"""
