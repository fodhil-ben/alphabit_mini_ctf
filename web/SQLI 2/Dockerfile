# Use a specific Node.js version
FROM node:14

# Set the working directory
WORKDIR /app

# Copy both package.json and package-lock.json
COPY challenge/package.json .
COPY challenge/package-lock.json .

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port on which the application will run
EXPOSE 1337

# Set the working directory to the challenge directory
WORKDIR /app/challenge

# Start the application
CMD ["npm", "start"]
