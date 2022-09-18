#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
HOSPITAL=$(echo $DATA | jq '.[0].hospitalizedCurrently')
VENTIL=$(echo $DATA | jq '.[0].onVentilatorCurrently')
DEATH=$(echo $DATA | jq '.[0].death')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $HOSPITAL people hospitalized, $VENTIL people on ventilators, and $DEATH total people have died."
