const arr = [-4, 3, -9, 0, 4, 1]
const arrTwo = [-2]

function plusMinus(arr) {
    let positive = 0
    let negative = 0
    let zero = 0

    for (let index = 0; index < arr.length; index++) {
        const element = arr[index];
        if (element < 0) {
            negative++
        }
        if ( element > 0){
            positive++
        }
        if (element === 0) {
            zero++
        }
    }
    let positiveRatio = (positive/(arr.length)).toFixed(6)
    let negativeRatio = (negative/(arr.length)).toFixed(6)
    let zeroRatio = (zero/(arr.length)).toFixed(6)

    console.log(positiveRatio)
    console.log(negativeRatio)
    console.log(zeroRatio)
    
}

plusMinus(arr);
