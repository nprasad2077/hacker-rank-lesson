const arr = [0, 5, 7, 20, 99, 99, 99, 0, 0]


function countingSort(arr){
    let bank = []
    
    for (i=0;i<100;i++){
        bank.push(0)
    }
    for (i=0;i<arr.length;i++){
        let change = arr[i]
        bank[change] = bank[change] + 1
    }
    console.log(bank);
    return bank
}

countingSort(arr)