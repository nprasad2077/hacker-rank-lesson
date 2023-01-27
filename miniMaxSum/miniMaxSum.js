const arr = [1, 2, 3, 4, 5]
const arrTwo = [7, 69, 2, 221, 8974]

function miniMaxSum(arr){
    let i = 0
    let j = 0
    let max = []
    let min = []
    let maxSum = 0
    let minSum = 0

    for (i=0; i<arr.length; i++){
        for (j=0; j<(arr.length + 1); j++){
            if (i>j) {
                max.push(arr[i])
            }
        }
    }

    for (i=0; i<arr.length; i++){
        for(j=0; j<(arr.length + 1); j++){
            if (i > j){
                min.push(i)
            }

        }
    }

    let maxSingle = [...new Set(max)]
    let minSingle = [...new Set(min)]


    for (i=0; i< maxSingle.length; i++){
        maxSum += maxSingle[i]

    }

    for (i=0; i< minSingle.length; i++){
        minSum += minSingle[i]
    }


    console.log(minSum, maxSum);


}


miniMaxSum(arr)