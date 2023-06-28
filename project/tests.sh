#!/bin/bash

# Execute the data pipeline
python3 ./main/data/AutoPipeLine.py

data_file="./main/data/Bicycle_data.sqlite"


# Check if the output file exists
if [ -f "$data_file" ]; then
    echo "Yes! Output file $data_file is available."
else
    echo "No! Output file $data_file is not available."
fi






