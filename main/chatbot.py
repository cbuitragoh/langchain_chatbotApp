from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from main.helpers import respond_to_message

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/send-message", response_class=HTMLResponse)
async def send_message(message: Message):
    # Process the incoming message
    user_message = message.message
    bot_response = respond_to_message(user_message, "veterinarian")
    return JSONResponse(content={"message": bot_response})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
