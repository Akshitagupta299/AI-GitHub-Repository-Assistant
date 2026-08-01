import ast
from typing import List


def create_chunks(repository_data: List[dict]) -> List[dict]:
    """
    Creates chunks from Python repository files.

    Args:
        repository_data: List containing dictionaries with:
            {
                "path": "...",
                "content": "..."
            }

    Returns:
        List of chunk dictionaries.
    """

    repository_chunks = []
    chunk_number = 1

    for file in repository_data:

        file_path = file["path"]
        content = file["content"]

        try:
            # Parse Python source code into AST
            tree = ast.parse(content)

            # Traverse every node in the AST
            for node in ast.walk(tree):

                # Process only functions and classes
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):

                    name = node.name
                    source_code = ast.get_source_segment(content, node)

                    if isinstance(node, ast.FunctionDef):
                        chunk_type = "function"
                    else:
                        chunk_type = "class"

                    chunk = {
                        "path": file_path,
                        "name": name,
                        "type": chunk_type,
                        "chunk": source_code,
                        "chunk_number": chunk_number,
                    }

                    repository_chunks.append(chunk)
                    chunk_number += 1

        except SyntaxError:
            print(f"Skipping file due to syntax error: {file_path}")
            continue

    return repository_chunks