from fastapi import FastAPI
# from slowapi import Limiter
# from slowapi.util import get_remote_address
# import aioredis

# limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
# app.state.limiter = limiter

# redis = None

# async def init_redis():
#     global redis
#     redis = await aioredis.from_url("redis://redis", decode_responses=True)
