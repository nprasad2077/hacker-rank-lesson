const arr = [1, 2, 3, 5, 4]
const arrTwo = [7, 69, 2, 221, 8974]

function miniMaxSum(arr){
    let maxSort = arr.sort((a,b) => b - a).slice(0,4).reduce((acc, num) => acc + num, 0)
    let minSort = arr.sort((a, b) => a - b).slice(0,4).reduce((acc,num) => acc + num, 0)
    
    console.log(minSort, maxSort);
}


miniMaxSum(arr)
miniMaxSum(arrTwo)