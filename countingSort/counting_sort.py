arr = [0, 99, 99, 99, 99]

def counting_sort(arr):
    bank = []

    for i in range(100):
        bank.append(0)

    for i in arr:
        bank[i] = bank[i] + 1
    
    print(bank)
    return bank



counting_sort(arr)
