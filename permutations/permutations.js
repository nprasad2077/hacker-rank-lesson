const K = 10
const A = [2, 1, 3]
const B = [7, 9, 8]

const K2 = 5
const A2 = [1,2,2,1]
const B2 = [3, 3, 3, 4]

const K3 = 94
const A3 = [84, 2, 50, 51, 19, 58, 12, 90, 81, 68, 54, 73, 81, 31, 79, 85, 39, 2]
const B3 = [53, 102, 40, 17, 33, 92, 18, 79, 66, 23, 84, 25, 38, 43, 27, 55, 8, 19]


function twoArrays(k, A, B) {
    const first = A.sort((a,b) => a-b)
    const second = B.sort((a,b) => b-a)
    let answer = true

    console.log(first, second);

    for (i=0; i<first.length; i++){
        console.log(first[i], second[i]);
        if (first[i] + second[i] < k){
            console.log('NO');
            return 'NO'
            
        }
    }
    return 'YES'
}


twoArrays(K, A, B)
twoArrays(K2, A2, B2)

console.log(twoArrays(K3, A3, B3));