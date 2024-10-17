This is a simple starlette app to demonstrate that using `resquest.stream()` inside a
`StreamingResponse` will cause the app to hang indefinitely (if the client does not timeout) instead of parsing the request body.

## How to reproduce

```bash
pip install -r requirements.txt
```

Then, in one terminal:

```bash
python main.py
```

Then, in another terminal:

```bash
curl -F "foo=bar" http://localhost:7000
```

Both terminals will hang indefinitely.


