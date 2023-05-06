debug = true
const DIFFICTULTY = 1000
const EGG_SPAWN_RATE = 1000
const LIVES = 1

var audio = new Audio('assets/eggCrack.mp3');
audio.playbackRate = 2

const trail1 = ['','','','','','']
const trail2 = ['','','','','','']
const trail3 = ['','','','','','']
const trail4 = ['','','','','','']
const trails = {1: trail1, 2: trail2, 3: trail3, 4: trail4}
let cnt = 0

const addEggFor = (n) => {
    if (!isTrailEmpty(n)) {
        return
    }
    trails[n][0] = 'egg'
    console.log("added egg to trail " + n);
}

const isTrailEmpty = (n) => {
        // returns if trail is empty 
        for (let i = 0; i < trails[n].length; i++) {
            if (trails[n][i] == 'egg') {
                if (debug) {
                    console.log("found egg on trail "+ n + " on index " + i);
                }
                return false
            }
        }
        return true
}

// n: String
// moves egg to the next index
// if trail is empty does nothing
// returns true if cracked egg
const rollEggFor = (n) => {
    // if (debug) {
    //     console.log("trying to roll egg on "+n);
    // }

    if (isTrailEmpty(n)) {
        return false
    }
    
    
    // finds the index of the egg
    let i_egg = 0
    for (let i = 0; i < trails[n].length; i++) {
        if (trails[n][i] == 'egg') {
            i_egg = i
            break
        }
    }

    
    
    try {
        renderOnPage(i_egg, n)
    } catch (error) {
        console.log(error);
    }

    // if index of egg is 5 then it cracks
    if (i_egg+1 == 6) {
        // TODO: return cracked egg
        audio.play();
        trails[n][i_egg] = ''
        // alert("cracked egg")
        if (debug) {
            console.log("cracked egg on trail" + n );
        }
        return true
    }

    // rolls the egg
    trails[n][i_egg] = ''
    trails[n][i_egg+1] = 'egg'
    if (debug) {
        console.log("rolled egg on trail " + n + " from " + i_egg + " to " + (i_egg+1));
    }
    

    

    // increment counter
    return false    
}

const renderOnPage = (i_egg, n) => {
    if (debug) {
        console.log("rendering trail "+n+ " from "+ (i_egg+1) + " to "+ (i_egg+1+1));
    }
    document.querySelector('.egg'+n+(i_egg+1)).classList.remove("hidden")
    setTimeout(() => {
        document.querySelector('.egg'+n+(i_egg+1)).classList.add("hidden")
    }, DIFFICTULTY);
}

const rollAllTrails = () => {
    for (let i = 1; i <= 4; i++) {
        setInterval(
            () => rollEggFor(i),
            DIFFICTULTY
        )
    }
    
}

const collectEggFrom = (n) => {
    if (debug) {
        console.log("trying to collect egg on trail " + n, trails[n]);
    }
    if (trails[n][4] == 'egg') {
        trails[n][4] = ''
        cnt++
        console.log("caught an egg on trail " + n, trails[n]);
        console.log("your counter is "+cnt);
    }
}
let intervalId = 0
const setControllerFor = (key) => {
    document.addEventListener('keypress', (e)=>{
        clearInterval(intervalId)
        intervalId = 0
        if (e.key == key) {
            collectEggFrom(key-0)
            intervalId = setInterval(() => collectEggFrom(key-0), DIFFICTULTY/2)

            if (debug) {
                console.log("Interal Id is "+intervalId+" for key "+key);
            }
        }
    })
    if (debug) {
        console.log("Event listeners added to "+ key);
    }
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

const setButtonFor = (key, class_name) => {
    document.addEventListener('keydown', (e)=>{
        if (e.key == key) {
            for (let i = 1; i <= 4; i++) {
                document.querySelector('.wolf'+i).classList.add("hidden")
                
            }
            document.querySelector('.'+class_name).classList.remove("hidden")

        }
    })
    // document.addEventListener('keyup', (e)=>{
    //     if (e.key == key) {
    //         document.querySelector('.'+class_name).classList.add("hidden")
    //     }
    // })
    if (debug) {
        console.log("Controller added to "+ key +" for " +class_name);
    }
}



const startGame = () => {
    // makes the eggs move on trails if any
    rollAllTrails()

    setButtonFor('1', 'wolf1')
    setButtonFor('2', 'wolf2')
    setButtonFor('3', 'wolf3')
    setButtonFor('4', 'wolf4')
    setControllerFor('1')
    setControllerFor('2')
    setControllerFor('3')
    setControllerFor('4')    
    setInterval(() => addEggFor(getRandomInt(4)+1), EGG_SPAWN_RATE)
}

let leaderboard = {}
let player_name = prompt("What is your name?")
startGame()


if (cnt){
    localStorage.setItem(player_name, cnt)
}