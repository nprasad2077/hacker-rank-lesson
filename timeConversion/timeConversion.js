const time = '07:05:45PM'
const timeTwo = '02:05:20AM'
const timeThree = '12:03:20AM'
const timeFour = '10:05:15PM'
const timeFive = '11:15:30AM'

function timeConversion(time) {
    let day = time.slice(8,9)
    let hours = time.slice(0,2)
    let minutes = time.slice(3,5)
    let seconds = time.slice(6,8)
    let twelve = time.slice(0,2)
    let timeReturn = ''

    if (twelve === '12') {
        hours = '00'
        timeReturn = `${hours}:${minutes}:${seconds}`
    }

    if (day === 'P'){
        hours = parseInt(hours) + 12
        timeReturn = `${hours}:${minutes}:${seconds}`
    }

    if (day === 'A'){
        timeReturn = `${hours}:${minutes}:${seconds}`
    }

    console.log(timeReturn);
    return timeReturn
}


timeConversion(time)
timeConversion(timeTwo)
timeConversion(timeThree)
timeConversion(timeFour)
timeConversion(timeFive)