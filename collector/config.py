import os
DATABASE_URL=os.getenv("DATABASE_URL","postgresql://postgres:password@postgres:5432/moex")
REDIS_HOST=os.getenv("REDIS_HOST","redis")
REDIS_PORT=int(os.getenv("REDIS_PORT","6379"))
