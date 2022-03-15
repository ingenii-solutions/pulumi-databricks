# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.224.2/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# User vscode needs sudoers access to all users without password, for example for postgres config scripts.
RUN echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode

ENV PATH=$PATH:/home/vscode/.pulumi/bin:/home/vscode/.local/bin

USER vscode

RUN mkdir -p /home/vscode/.local/bin \
    && mkdir -p /home/vscode/.pulumi/bin

# Install Pulumi
RUN wget https://github.com/pulumi/pulumi/releases/download/v3.26.1/pulumi-v3.26.1-linux-x64.tar.gz -O - | tar xz -C /home/vscode/.pulumi/bin --strip-components 1

# Install Pulumictl
RUN wget https://github.com/pulumi/pulumictl/releases/download/v0.0.30/pulumictl-v0.0.30-linux-amd64.tar.gz -O - | tar xz -C /home/vscode/.local/bin

# Install Twine
RUN pip3 --disable-pip-version-check --no-cache-dir install twine