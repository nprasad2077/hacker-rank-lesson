const a = [1, 2, 3, 4, 3, 2, 1]


function lonelyinteger(a) {
    let answer = 0

    for (i=0; i<a.length; i++){
        let counter = 0
        for (j=0; j<a.length; j++) {
            if (a[i]==a[j]) {
                counter +=1
            }
        }
        if (counter == 1) {
            answer = a[i]
        }

    }
    console.log(answer);
    return(answer)
}

lonelyinteger(a)