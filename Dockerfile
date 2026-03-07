FROM openhab/openhab:4.1.0 AS builder
COPY ./openhab/conf /openhab/conf

FROM openhab/openhab:4.1.0-alpine
LABEL maintainer="Mira"

COPY --from=builder /openhab/conf /openhab/conf
COPY ./openhab/addons /openhab/addons

EXPOSE 8080