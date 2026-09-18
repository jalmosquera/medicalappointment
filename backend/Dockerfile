FROM python:3.14-slim

WORKDIR /app

COPY . .

RUN pip install uv && uv sync --frozen

CMD ["uv", "run", "uvicorn", "src.core.main:app", "--host", "0.0.0.0", "--port", "8000"]
