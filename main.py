from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse  # noqa: F401
from starlette.routing import Route


async def request_stream(request: Request):
    return StreamingResponse(request.stream(), media_type="text/plain")


async def request_form(request: Request):
    def stream_data_from_form():
        for key, value in request.form():
            print(f"{key}: {value}")
            yield f"{key}: {value}\n"

    return StreamingResponse(request.stream(), media_type="text/plain")


app = Starlette(
    debug=True,
    routes=[
        Route("/", request_stream, methods=["GET", "POST"]),
        Route("/form", request_form, methods=["GET", "POST"]),
    ],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=7000)
