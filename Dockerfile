FROM python:3.9-slim AS builder
WORKDIR /app
COPY . .
RUN pip install pytest && pytest tests/

FROM openhab/openhab:4.1.0
LABEL maintainer="Mira"
COPY --from=builder /app/openhab/conf /openhab/conf
EXPOSE 8080