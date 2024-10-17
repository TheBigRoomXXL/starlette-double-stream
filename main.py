from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import StreamingResponse
from starlette.routing import Route


async def main(request: Request):
    return StreamingResponse(request.stream(), media_type="text/plain")


app = Starlette(
    debug=True,
    routes=[
        Route("/", main, methods=["GET", "POST"]),
    ],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=7000)
