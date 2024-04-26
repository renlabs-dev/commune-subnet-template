from communex.module import Module, endpoint
from communex.key import generate_keypair
from keylimiter import TokenBucketLimiter


class Miner(Module):

    @endpoint
    def generate(self, prompt: str, model: str = "gpt-3.5-turbo"):
        print(f"Answering: `{prompt}` with model `{model}`")


# Example
if __name__ == "__main__":
    from communex.module.server import ModuleServer
    import uvicorn

    key = generate_keypair()
    miner = Miner()
    refill_rate = 1 / 400
    bucket = TokenBucketLimiter(2, refill_rate)
    server = ModuleServer(miner, key, ip_limiter=bucket, subnets_whitelist=[3])
    app = server.get_fastapi_app()
    # Only allow local connections
    uvicorn.run(app, host="127.0.0.1", port=8000)
