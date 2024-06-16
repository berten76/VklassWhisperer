
def extract_week_from_query(query_text: str) -> str:
    import re
    # The pattern now looks for "week", "vecka", or "v." followed by a space or not, and then one or more digits
    # It is case-insensitive due to re.IGNORECASE
    pattern = r'(week|vecka|v\.?)\s*(\d+)'
    match = re.search(pattern, query_text, re.IGNORECASE)
    return match.group(2) if match else None