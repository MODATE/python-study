## if practice

#accuracy = 0.72

#if accuracy >= 0.8:
#    print("high accuracy")
#elif accuracy >= 0.7:
#    print("Moderate")
#else:
#    print("low accuracy")

## for practice

#accuracies = [0.72, 0.81, 0.76, 0.91, 0.68] ## list type

#accuracies[0] # 0.72
#accuracies[1] # 0.81

#for accuracy in accuracies:
#    print("accuracy is ", accuracy)

#for accuracy in accuracies:
#    if accuracy >= 0.8:
#        print(accuracy, "High")
#    else:
#        print(accuracy, "Low")

## Practice code1

#accuracies = [0.72, 0.81, 0.76, 0.91, 0.68]
#acc_count = 0

#for accuracy in accuracies:
#    if accuracy >= 0.8:
#        acc_count += 1

#print(f"Number of accuracies >= 0.8: {acc_count}")

## Practice code2

accuracies_b = [0.72, 0.81, 0.76, 0.91, 0.68]
num_trials_b = [120, 80, 150, 110, 200]

Perf_Experiments_count = 0

for i in range(5):
    if accuracies_b[i] >= 0.8 and num_trials_b[i] >= 100:
        Perf_Experiments_count += 1

print(f"Number of experiments accuracy >= 0.8 and num_trials >= 100 is {Perf_Experiments_count}")



