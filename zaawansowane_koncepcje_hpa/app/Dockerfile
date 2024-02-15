# Use the official Golang image to create a build artifact.
# This is based on Debian and sets the GOPATH environment variable at /go.
FROM golang:1.21.5 as builder

# Create and change to the app directory.
WORKDIR /app

# Retrieve application dependencies.
# This allows the container build to reuse cached dependencies.
COPY go.mod ./
COPY go.sum ./
RUN go mod download

# Copy local code to the container image.
COPY . ./

# Build the binary.
# -o myapp specifies the output filename (myapp)
RUN CGO_ENABLED=0 GOOS=linux go build -v -o hpa

# Use the official Debian slim image for a lean production container.
# https://hub.docker.com/_/debian
FROM debian:buster-slim
RUN set -eux; apt-get update; apt-get install -y --no-install-recommends ca-certificates netbase

WORKDIR /

# Copy the binary to the production image from the builder stage.
COPY --from=builder /app/hpa /hpa

# Run the web service on container startup.
CMD ["/hpa"]
