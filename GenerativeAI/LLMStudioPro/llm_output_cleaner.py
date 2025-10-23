import re

def clean_llm_output(output: str) -> str:
    """
    Removes <think> tags and their content from LLM output.

    Args:
        output (str): The raw LLM output string.

    Returns:
        str: The cleaned output with <think> tags removed.
    """
    # Regex to match <think> tags and their content, including nested or multiline
    think_pattern = r'<think>.*?</think>'
    cleaned_output = re.sub(think_pattern, '', output, flags=re.DOTALL)
    # Remove any extra whitespace left after removal
    cleaned_output = re.sub(r'\n\s*\n', '\n\n', cleaned_output.strip())
    return cleaned_output

if __name__ == "__main__":
    # Example usage
    sample_output = """
<think>
This is some internal reasoning.
</think>
This is the actual response.
"""
    cleaned = clean_llm_output(sample_output)
    print("Cleaned Output:")
    print(cleaned)
