# --- Stage 1: Build Environment ---
# We use Node 20 Alpine for a small security footprint and compatibility
FROM node:20-alpine AS base

# Set the working directory inside the container
WORKDIR /app

# Install system-level dependencies
# - python3/py3-pip/groff: Required for AWS CLI
# - build-base: Required for certain Node native modules
# - git: Required for your Cloudflare/GitHub workflow
RUN apk add --no-cache \
    python3 \
    py3-pip \
    groff \
    less \
    build-base \
    git \
    bash

# Install AWS CLI and Azure CLI via pip
# This ensures you have the tools to talk to your S3 and CosmosDB credits
RUN pip3 install --no-cache-dir --break-system-packages awscli azure-cli

# Install Wrangler (Cloudflare's CLI) globally
# This allows you to run 'wrangler deploy' from inside the container
RUN npm install -g wrangler

# --- Stage 2: Application Dependencies ---
# Copy package files first to leverage Docker layer caching
COPY package.json package-lock.json* ./

# Perform a clean install of dependencies
# 'npm ci' is more robust for CI/CD than 'npm install'
RUN npm install

# Copy the rest of your source code (including the index.html we created)
COPY . .

# Set environment variables (Placeholders for your future secrets)
ENV NODE_ENV=development

# The container will stay running so you can 'exec' into it
CMD ["tail", "-f", "/dev/null"]