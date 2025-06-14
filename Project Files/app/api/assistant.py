from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from app.schemas.assistant_schemas import QuestionRequest, AnswerResponse, Message
from app.core.hugging_face_client import generate_answer

router = APIRouter()

# Endpoint for AJAX chat requests
@router.post("/ask")
async def ask_assistant(request: Request, question: str = Form(...)):
    session = request.session
    if "messages" not in session:
        session["messages"] = []

    # Append user message
    session["messages"].append({"role": "user", "content": question})
    

    # Generate assistant response
    answer = generate_answer(question)
    session["messages"].append({"role": "assistant", "content": answer})

    request.session.update(session)  # Save session changes
    return JSONResponse({"answer": answer, "messages": session["messages"]})

# Endpoint to clear chat history
@router.post("/clear_history")
async def clear_history(request: Request):
    request.session["messages"] = []
    return JSONResponse({"message": "Chat history cleared."})
    
