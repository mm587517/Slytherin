# Use a base Linux image
FROM ubuntu:latest

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    git \
    sudo \
    vim \
    python3 \
    python3-pip

# Install Solidity compiler (solc)
RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:ethereum/ethereum && \
    apt-get update && \
    apt-get install -y solc

# Install Slither
RUN pip3 install slither-analyzer

# Set a working directory (you can choose any directory)
WORKDIR /app

RUN solc-select install 0.8.20 && solc-select use 0.8.20

# Copy your smart contract code into the container
COPY ./contracts /app/contracts

# Start a shell in the container
CMD ["/bin/bash"]
