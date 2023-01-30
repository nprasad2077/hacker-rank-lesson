const b2d = x => parseInt(x,2)
const d2b = x => x.toString(2)

// console.log(b2d(101), d2b(5));
// console.log(d2b(9));


const string = '00000000000000000000000000001001'
const stringOut = '11111111111111111111111111110110'

// console.log(b2d(string))
// console.log(b2d(stringOut))

function flippingBits(n){
    const binaryStart = n.toString(2).split('')
    let binaryFlip = []
    const missingZero = 32 - binaryStart.length
    for (i=0;i<missingZero;i++){
        binaryStart.unshift('0')
    }

    binaryStart.forEach(element => {
        if (element === '0') {
            binaryFlip.push('1')
        }
        if (element === '1') {
            binaryFlip.push('0')
        }
    });

    const answer = parseInt(binaryFlip.join(''), 2)

    console.log(answer);
    return (answer)

}

// flippingBits(9)
flippingBits(2147483647)
flippingBits(1)
flippingBits(0)
