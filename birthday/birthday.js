const s = [2, 3, 1, 3, 2]
const d = 4
const m = 2

const s2 = [1, 2, 1, 3, 2]
const d2 = 3
const m2 = 2

const s3 = [1, 1, 1, 1, 1, 1]

const s4 = [4]
const d4 = 4
const m4 = 1

const s5 = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
const d5 = 18
const m5 = 7

function birthday(s, d, m){
    const segment = m
    let counter = 0

    for (i=0;i<s.length-segment+1;i++){
        // console.log(i, i+segment);
        const slice = s.slice(i,i+(segment))
        const sum = slice.reduce((acc, current) => acc + current, 0)
        console.log(slice, sum);
        if (sum==d){counter+=1}
    }

    console.log(counter);
    return counter
}

// birthday(s, d, m)
// birthday(s2, d2, m2)
// birthday(s3, d2, m2)
birthday(s5, d5, m5)