# Execute the data pipeline
python3 AutoPipeLine.py

data_files="Bicycle_data.sqlite"

# Check if the output file(s) exist
if [ -f "$data_files" ]; then
    echo "Yes! Output file $data_files is available."
else
    echo "No! Output file $data_files is not available."
fi
echo "Test if pipeline works correctly"
pytest ./data/unitTest.py
