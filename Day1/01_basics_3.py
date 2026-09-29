signal = [10, 20, 30, 40, 50, 60] # definition of list type

signal[0] == 10
signal[2] == 30

## practice how to slicing

signal_a = signal[1:4]
# 1 to 3 
# [20, 30, 40]
signal_b = signal[:3]
# 0 to 3
# [10, 20, 30]
signal_c = signal[3:]
# 3 to last
# [40, 50, 60]
signal_d = signal[-1]
# last 
# [60]
signal_e = signal[-2]
# 2nd from last
# [50]
signal_f = signal[::2]
# 2칸 씩 건너 뜀
# [10, 30, 50]
signal_g = signal[::-1]
# 마지막에서 1개씩 감소함
# [60, 50, 40, 30, 20, 10]

#print(signal_a)
#print(signal_b)
#print(signal_c)
#rint(signal_d)
#print(signal_e)
#print(signal_f)
#print(signal_g)

eeg_signal = [3, 7, 2, 8, 5, 1, 9, 4, 6, 0]

a = eeg_signal[2:8:2] # [2,5, 9]
b = eeg_signal[1:-2] # [7, 2, 8, 5, 1, 9, 4]
c = eeg_signal[-5:-1] # [1, 9, 4, 6]
d = eeg_signal[7:2:-2] # [4, 1, 8]
e = eeg_signal[3] # 8
f = eeg_signal[3:4] # [8]

## Practice indexing & Slicing of list

new_signals = [10, 20, 30]

new_signals.append(40)
# [10, 20, 30, 40]
new_signals.insert(1, 15)
# [10, 15, 20, 30, 40]
new_signals.remove(30)
# [10, 15, 20, 40]

x = new_signals.pop()
# x = 40
# new_signals = [10, 15, 20]

n = len(new_signals)
# n == 3