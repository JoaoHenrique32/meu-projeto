import asyncio

def retry_on_failure(func):
    async def wrapper(*args, **kwargs):
        retries = 3
        for attempt in range(retries):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                if attempt < retries - 1:
                    await asyncio.sleep(1)
                    continue
                raise e
    return wrapper
