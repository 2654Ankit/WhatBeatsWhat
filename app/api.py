from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
# from .core import limiter
from app.extensions import redis_client
from .linked_list import LinkedList
from .database import SessionLocal
from .models import GuessCounter
from .llm import check_if_beats
from .utils import  format_response
from sqlalchemy.future import select
# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


game_data = {}

@router.post("/guess")
# @limiter.limit("10/minute")
async def make_guess(request: Request, guess: str,db: Session = Depends(get_db),persona='serious'):
    user_id = request.client.host
    user = user_id
    if user_id in game_data.keys():
        hist = game_data[user_id].history()
        seed = hist[-1]
    else:
        seed = 'Rock'

    # Profanity check
    guess = guess.lower()

    # Init user linked list
    if user_id not in game_data:
        game_data[user_id] = LinkedList()

    # Check repeat guess
    if not game_data[user_id].add(guess):
        return {"game_over": True, "message": "Game Over! You repeated a guess."}

    # Check cache
    cache_key = f"{seed}:{guess}"
    cached_result =  redis_client.get(cache_key)
    if cached_result == "yes":
        verdict = True
    elif cached_result == "no":
        verdict = False
    else:
        verdict = await check_if_beats(seed, guess,persona)
        redis_client.set(cache_key, "yes" if verdict else "no")

    if not verdict:
        
        return {"game_over": True, "message": "Game Over! Wrong guess.","seed":seed}
    
    # Update DB
    result =  db.execute(select(GuessCounter).where(GuessCounter.word == guess))

    guess_counter = result.scalar_one_or_none()
    if guess_counter:
        guess_counter.count += 1
    else:
        guess_counter = GuessCounter(word=guess, count=1)
        db.add(guess_counter)
    db.commit()

    return {
        "game_over": False,
        "message": format_response(seed, guess, guess_counter.count),
        "history": game_data[user_id].history()
    }

@router.get("/history")
async def history(request: Request):
    user_id = request.client.host
    if user_id in game_data:
        return {"history": game_data[user_id].history()}
    else:
        return {"history": []}
