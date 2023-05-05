debug = true

const trail1 = ['','','','','','']
const trail2 = ['','','','','','']
const trail3 = ['','','','','','']
const trail4 = ['','','','','','']

cnt = 0

const addEgg = (trail, n) => {
    trail[0] = 'egg'
    if (debug) {
        console.log("added egg to trail" + n);
    }
}

const rollEgg = (trail, n) => {
    // returns if trail is empty 
    if (trail[0] == '') {
        return false
    }
    
    // finds the index of the egg
    let i_egg = 0
    for (let i = 0; i < trail.length; i++) {
        if (trail[i] == 'egg') {
            i_egg = i
            break
        }
    }

    // rolls the egg
    trail[i_egg] = ''
    trail[i_egg+1] = 'egg'
    if (debug) {
        console.log("rolled egg on trail " + n + " from " + i_egg + " to " + i_egg+1);
    }
    
    // if index of egg is 6 then it cracks
    if (i_egg+1 == 6) {
        // TODO: return cracked egg
        alert("cracked egg")
        if (debug) {
            console.log("cracked egg on trail" + n );
        }
    
        return true
    }

    // increment counter
    return false    
}

const rollAllTrails = (trail1, trail2, trail3, trail4) => {
    setInterval(
        () => rollEgg(trail1),
        1000
    )
    setInterval(
        () => rollEgg(trail2),
        1000
    )
    setInterval(
        () => rollEgg(trail3),
        1000
    )
    setInterval(
        () => rollEgg(trail4),
        1000
    )
    
}


const startGame = () => {
    rollAllTrails(trail1, trail2, trail3, trail4)
    setTimeout(() => addEgg(trail1, 1), 3000)
}

startGame()