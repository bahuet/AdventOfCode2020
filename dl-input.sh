#!/bin/bash
day=$1
year='2020'
echo "Downloading input for day $day..."
source GETSESSION.sh
curl https://adventofcode.com/$year/day/$day/input --cookie session=$session > inputs/$day.txt
echo "Done"