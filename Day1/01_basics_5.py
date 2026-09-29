## Practice how to definite functions
def check_validity(accuracy, num_trials):
    if accuracy >= 0.8 and num_trials >= 100:
        return True
    else:
        return False

#result = check_validity(0.87, 120)

#print(result)

## 평균 계산
def cal_mean_of_list(values):
    sum_of_list = 0

    for value in values:
        sum_of_list += value
    
    return sum_of_list / len(values)

## 분산 계산 
def cal_variance(values):
    variance = 0
    mean_of_list = cal_mean_of_list(values)
    for value in values:
        deviance = mean_of_list - value
        variance += deviance ** 2

    return variance / len(values)


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

accuracies = [0.72, 0.81, 0.76, 0.91, 0.68]
mean_accuracy = cal_mean_of_list(accuracies)
print(mean_accuracy) # 0.776

list_A = [0.78, 0.79, 0.80, 0.81, 0.82]
list_B = [0.60, 0.70, 0.80, 0.90, 1.00]

print(cal_variance(list_A))
print(cal_variance(list_B))

#0.0001999999999999995
#0.020000000000000004

a = cal_variance2(list_A) # 모집단
b = cal_variance2(list_A, True) # 표본

print(a)
print(b)