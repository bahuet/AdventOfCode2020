#!/bin/bash
day=$1
year='2020'
echo "Downloading input for ${day}"
source GETSESSION.sh
curl "https://adventofcode.com/$year/day/$day/input" --cookie "session=${session}" > "inputs/$1.txt"
echo "Done"