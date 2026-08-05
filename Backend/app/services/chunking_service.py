import ast
from typing import List


def create_chunks(repository_data: List[dict]) -> List[dict]:
    """
    Creates chunks from Python repository files.
    """

    repository_chunks = []
    chunk_number = 1

    for file in repository_data:

        file_path = file["file_path"]
        content = file["content"]

        try:

            tree = ast.parse(content)

            for node in ast.walk(tree):

                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):

                    name = node.name
                    source_code = ast.get_source_segment(content, node)

                    chunk_type = (
                        "function"
                        if isinstance(node, ast.FunctionDef)
                        else "class"
                    )

                    chunk = {

                        "file_path": file_path,
                        "name": name,
                        "chunk_type": chunk_type,
                        "chunk": source_code,
                        "chunk_number": chunk_number,

                    }

                    repository_chunks.append(chunk)
                    chunk_number += 1

        except SyntaxError:

            print(f"Skipping file due to syntax error: {file_path}")

            continue

    return repository_chunks