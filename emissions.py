import subprocess
from codecarbon import EmissionsTracker

# Definisci i percorsi degli script che vuoi eseguire
make_dataset = 'src/data/make_dataset.py'
preprocessing = 'src/data/preprocessing.py'
splitting = 'src/data/split_dataset.py'
knr = 'src/models/knr.py'
lr = 'src/models/linear_regressor.py'
rf = 'src/models/random_forest_regressor.py'
xgb = 'src/models/xgbooster.py'
compare = 'src/models/compare.py'


tracker=EmissionsTracker(output_dir="reports/codecarbon", output_file="TotalEmissions.csv")
tracker.start()
subprocess.run(['python', make_dataset])
subprocess.run(['python', preprocessing])
subprocess.run(['python', splitting])
subprocess.run(['python', knr])
subprocess.run(['python', lr])
subprocess.run(['python', rf])
subprocess.run(['python', xgb])
subprocess.run(['python', compare])
tracker.stop()