const stringsOne = [ 'aba', 'baba', 'aba', 'xzxb' ]
const queriesOne = [ 'aba', 'xzxb', 'ab' ]


function matchingStrings(strings, queries) {
    let answer = []
    let answerTwo = ['2', '1', '0']

    for(i=0; i<queries.length; i++){
        let counter = 0
        for(j=0; j<strings.length; j++){
            if (queries[i] == strings[j]){
                counter += 1
            }
        }
        answer.push(counter)
    }
    console.log(answer)
    return answer

}

matchingStrings(stringsOne, queriesOne)