
## Definite functions
# calcuate the number of samples
def calculate_num_samples(sampling_rate, duration):
    return sampling_rate *duration

# check the validity
def check_validity(accuracy, trials):
    return accuracy >= 0.8 and trials >= 100

# calculate the mean
def cal_mean_of_list(values):
    sum_of_list = 0

    for value in values:
        sum_of_list += value
    
    return sum_of_list / len(values)

# calculate the variance
def cal_variance2(values, sample=False):
    variance = 0
    mean_of_list = cal_mean_of_list(values)
    for value in values:
        deviance = mean_of_list - value
        variance += deviance ** 2

    if sample :
        return variance / (len(values) - 1)
    else:
        return variance / len(values)

## 변수 값 선언
subjects = ["S01", "S02", "S03", "S04", "S05"]

accuracies = [0.82, 0.76, 0.91, 0.68, 0.85]

num_trials = [120, 150, 90, 130, 110]

sampling_rate = 1000
duration = 2.5

## Generate List of Dictionaries
# 모든 실험에서 공통으로 사용되는 값은 미리 계산
num_experiments = len(subjects)
num_samples = calculate_num_samples(sampling_rate,duration)

# dictionary들을 정리할 list를 생성 및 list에 dictionary 순차적으로 추가
experiments = []
valid_accuracies = []
for i in range(num_experiments):
    # 각 실험마다의 dictionary를 생성
    sub_dict = {
        "subject": subjects[i],
        "accuracy": accuracies[i],
        "num_trials": num_trials[i],
        "num_samples": num_samples,
        "valid": check_validity(accuracies[i], num_trials[i])
    }
    
    # list에 dictionary 추가
    experiments.append(sub_dict)
    if sub_dict["valid"]:
        valid_accuracies.append(sub_dict["accuracy"])

## Print Section
# 1. 전체 피험자 수
num_experiments = len(subjects)
print(f"1. 전체 피험자 수 {num_experiments}")
# 2. valid 피험자 수
num_valid = len(valid_accuracies)
print(f"2. valid 피험자 수 {num_valid}")
# 3. valid accuracy list
valid_accuracies
print(f"3. valid accuracy list {valid_accuracies}")
# 4. valid accuracy 평균
mean_valid = cal_mean_of_list(valid_accuracies)
print(f"4. valid accuracy 평균 {mean_valid}")
# 5. 모집단 분산
var_accuracy1 = cal_variance2(accuracies)
print(f"5. 모집단 분산 {var_accuracy1}")
# 6. 표본 분산
var_accuracy2 = cal_variance2(accuracies, sample=True)
print(f"6. 표본 분산 {var_accuracy2}")
# 7. 처음 세 피험자의 dictionary
first_three = experiments[:3]
print(f"7. 처음 세 피험자의 dictionary {first_three}")