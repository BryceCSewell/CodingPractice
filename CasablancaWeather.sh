#! /bin/bash
#This file will create a weather forecast for Casablanca

#create a filename for the raw wttr data
today=$(date +%Y%m%d)
weather_report=raw_data_$today

#Download weather report from wttr.in
city=Casablanca
curl wttr.in/$city --output $weather_report

grep °C $weather_report > temperatures.txt

#Extract the current temperature
obs_tmp=$(cat temperatures.txt | grep -oE '[0-9]+' | head -1)

#Extract the forecast for noon tomorrow
fc_temp=$(cat temperatures.txt | grep -oE '[0-9]+' | head -2 | tail -1)

#Storing the current hour, day, month, and year
hour=$(TZ='Morocco/Casablanca' date -u +%H)
day=$(TZ='Morocco/Casablanca' date -u +%d)
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)

record=$(echo -e "$year\t$month\t$day\t$obs_tmp\t$fc_temp")
echo $record>>rx_poc.log
