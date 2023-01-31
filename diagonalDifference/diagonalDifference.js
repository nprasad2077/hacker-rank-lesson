const arr = [ [ 11, 2, 4 ], [ 4, 5, 6 ], [ 10, 8, -12 ] ]
const arrTwo = [ [ 11, 2, 4, 2 ], [ 4, 5, 6, 1 ], [ 10, 8, -12, 2 ], [5, 7, 3, 1] ]
const arrThree = [[-1, 1, -7, -8], [-10, -8, -5, -2], [0, 9, 7, -1], [4, 4, -2, 1]]

// console.log(arr.flat());
// console.log(arr[2][2]);

function diagonalDifference(arr) {
    let primeDiagonal = 0
    let secondaryDiagonal = 0
    let counter = 0

    for (i=0;i<arr.length;i++) {
        console.log(arr[i][i]);
        primeDiagonal+=arr[i][i]
    }

    for (i=arr.length - 1;i>=0;i--) {
        console.log(arr[i][counter])
        secondaryDiagonal+=arr[i][counter]
        counter+=1

    }

    console.log(Math.abs(primeDiagonal - secondaryDiagonal));
    return Math.abs(primeDiagonal - secondaryDiagonal)


}


// diagonalDifference(arr)
// diagonalDifference(arrTwo)
// diagonalDifference(arrThree)
