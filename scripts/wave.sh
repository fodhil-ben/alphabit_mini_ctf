#!/bin/bash

# List of paths to Docker Compose files for list 1
compose_paths_1=(
  "./misc/jail1/docker-compose.yml"
  "./misc/privilege/docker-compose.yml"
  "./pwn/executed/docker-compose.yml"
  "./pwn/format/docker-compose.yml"
  "./pwn/Bird_Cage/docker-compose.yml"
  "./pwn/deadc0de/docker-compose.yml"
  "./pwn/secret_number_game/docker-compose.yml"
  "./rev/AfricanCup/docker-compose.yml"
  "./web/inspection/docker-compose.yml"
  "./web/headers_hunter/docker-compose.yml"
  "./web/mongoDB/docker-compose.yml"
  "./web/SQLI/docker-compose.yml"
  "./web/Skill_Hunter_1/docker-compose.yml"
)

compose_paths_2=(
  "./misc/snake/docker-compose.yml"
  "./misc/jail2/docker-compose.yml"
  "./pwn/jail/docker-compose.yml"
  "./pwn/sixty_four/docker-compose.yml"
  "./pwn/thirty_two/docker-compose.yml"
  "./pwn/strings/docker-compose.yml"
  "./rev/seed/docker-compose.yml"
  "./web/Skill_Hunter_2/docker-compose.yml"
  "./web/Skill_Hunter_3/docker-compose.yml"
  "./web/template/docker-compose.yml"
  "./web/forgery/docker-compose.yml"

)


# Check if an integer argument was passed
if [[ ! $1 =~ ^[0-9]+$ ]]; then
  echo "Please provide an integer argument."
  exit 1
fi

# Choose the list of paths based on the input integer
if (( $1 == 1 )); then
  compose_paths=("${compose_paths_1[@]}")
elif (( $1 == 2 )); then
  compose_paths=("${compose_paths_2[@]}")
elif (( $1 == 3 )); then
  compose_paths=("${compose_paths_3[@]}")
else
  echo "Invalid integer argument. Please choose 1 or 2."
  exit 1
fi

# Iterate through the list of Docker Compose paths and run docker-compose up
for path in "${compose_paths[@]}"; do
  echo "Running Docker Compose for $path"
  docker-compose -f "$path" up --build -d
done