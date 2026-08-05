from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.orchestrator_service import chat_with_repository

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = chat_with_repository(
    repository_name=request.repository_name,
    question=request.question
)

    return ChatResponse(answer=answer)