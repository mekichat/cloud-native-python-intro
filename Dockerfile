FROM python:3.13-slim
WORKDIR /app
COPY src/ ./src
CMD [ "python", "-m", "src.main" ]