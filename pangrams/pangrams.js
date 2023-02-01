const s = 'The quick brown fox jumps over the lazy dog'
const s2 = 'We promptly judged antique ivory buckles for the next prize'
const s3 = 'not one'


function pangram(s){
    let bank = []
    let words = ((s.split(" ").join('')).toUpperCase()).split('')
    let pangram = true

    for (i=0;i<26;i++){
        bank.push(0)
    }

    for (i=0;i<words.length; i++){
        let position = words[i].charCodeAt(0) - 65;
        bank[position] = bank[position] + 1
    }

    bank.forEach((element) => {if (element === 0 ){ pangram = false}})

    console.log(pangram);

    if (pangram) {return 'pangram'}
    else {return 'not pangram'}

}

// console.log('A'.charCodeAt(0));
// console.log(((s.split(" ").join('')).toUpperCase()).split(''))

pangram(s)
pangram(s2)
pangram(s3)
