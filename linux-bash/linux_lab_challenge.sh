#!/bin/bash

max=0

for file in Palmera*
do
    if [ "$file" == "Palmera*" ]
    then
        continue
    fi

    number=${file#Palmera}

    if [ "$number" -gt "$max" ]
    then
        max=$number
    fi
done

counter=$((max + 1))

created=0
while [ $created -lt 25 ]
do
    touch "Palmera$counter"
    counter=$((counter + 1))
    created=$((created + 1))
done

echo "Done. Created 25 files."