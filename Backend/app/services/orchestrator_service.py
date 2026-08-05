from app.services.vector_database import get_repository_collection
from app.services.retrieval_service import retrieve_relevant_chunks
from app.services.prompt_builder import build_prompt
from app.services.gemini_service import generate_repository_answer

def chat_with_repository(
    repository_name: str,
    question: str
):

    try:

        # Step 1
        collection = get_repository_collection(repository_name)

        # Step 2
        retrieval_results = retrieve_relevant_chunks(
            collection=collection,
            question=question
        )

        # Step 3
        if not retrieval_results["documents"][0]:
            return "I couldn't find any relevant information in this repository."

        # Step 4
        prompt = build_prompt(
            question=question,
            retrieval_results=retrieval_results
        )

        # Step 5
        return generate_repository_answer(prompt)

    except Exception as e:
        return f"Error: {str(e)}"