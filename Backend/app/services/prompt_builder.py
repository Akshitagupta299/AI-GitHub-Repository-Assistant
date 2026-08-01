from typing import Dict


def build_prompt(
    question: str,
    retrieval_results: Dict
) -> str:
    """
    Builds the final prompt for Gemini
    using retrieved repository chunks.
    """

    documents = retrieval_results["documents"][0]

    context = "\n\n------------------------\n\n".join(documents)

    prompt = f"""
    You are an AI assistant that helps developers understand GitHub repositories.

    Rules:
    - Answer only using the provided repository context.
    - If the answer is not present, say:
    "I couldn't find that information in the repository."
    - Keep your answers clear and concise.

    User Question:

    {question}

    Repository Context:

    {context}
    """

    return prompt