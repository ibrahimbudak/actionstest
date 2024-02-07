# Use the official golang image as a base image
FROM golang:latest AS build

# Set the current working directory inside the container
WORKDIR /app

# Copy go mod and sum files
COPY go.mod ./

# Copy the source code into the container
COPY . .

# Build the Go app
RUN go build -o main .

# Use a minimal alpine image to create a final image
FROM alpine:latest

# Set the current working directory inside the container
WORKDIR /root/

# Copy the executable from the build stage
COPY --from=build /app/main .

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the executable
CMD ["./main"]
