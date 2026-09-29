## Tuple
## tuple is immutable variable

eeg_shape = (64, 10000)

eeg_shape[0] == 64
eeg_shape[1] == 10000

## Dictionary

experiment = {
    "subject": "S01",
    "accuracy": 0.84,
    "num_trials": 120,
    "filtered": True
}

experiment["subject"]
# "S01"

experiment["accuracy"]
# 0.84

experiment["sampling_rate"] = 1000
experiment["accuracy"] = 0.87

## Practice part
experiment["duration"] = 2.5
num_samples = experiment["sampling_rate"] * experiment["duration"]
experiment["num_samples"] = num_samples

valid = experiment["accuracy"] >= 0.8 and experiment["num_trials"] >= 100
experiment["valid"] = valid

print(experiment)