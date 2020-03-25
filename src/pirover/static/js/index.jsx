// add handler to each button
import axios from 'axios';

// MOVE ACTIONS

var currMove = null

function move() {
  if(currMove != null) {
    axios.post('/api/action/move', {
      direction: currMove,
      args: {
        wait: false,
        duration: 0.5
      }
    })
    .catch(function (error) {
      console.log(error)
    });
  }
}

setInterval(move, 50);

// handle buttons

document.getElementById('leftButton').onmousedown = function() { currMove = 'left' }
document.getElementById('leftButton').onmouseup = function() { currMove = null }
document.getElementById('rightButton').onmousedown = function() { currMove = 'right' }
document.getElementById('rightButton').onmouseup = function() { currMove = null }
document.getElementById('forwardButton').onmousedown = function() { currMove = 'forward' }
document.getElementById('forwardButton').onmouseup = function() { currMove = null }
document.getElementById('backwardButton').onmousedown = function() { currMove = 'backward' }
document.getElementById('backwardButton').onmouseup = function() { currMove = null }

// handle keys

document.addEventListener('keydown', function(event) {
    if(event.keyCode == 37) {
        currMove = 'left'
    }
    else if (event.keyCode == 38) {
        currMove = 'forward'
    }
    else if (event.keyCode == 39) {
        currMove = 'right'
    }
    else if (event.keyCode == 40) {
        currMove = 'backward'
    }
})


var keys_ = [37, 38, 39, 40]
document.addEventListener('keyup', function(event) {
    if (keys_.includes(event.keyCode)) {
        currMove = null
    }

})

// handle touch

document.getElementById('leftButton').addEventListener('touchstart', () => currMove = 'left')
document.getElementById('leftButton').addEventListener('touchend', () => currMove = null)
document.getElementById('rightButton').addEventListener('touchstart', () => currMove = 'right')
document.getElementById('rightButton').addEventListener('touchend', () => currMove = null)
document.getElementById('forwardButton').addEventListener('touchstart', () => currMove = 'forward')
document.getElementById('forwardButton').addEventListener('touchend', () => currMove = null)
document.getElementById('backwardButton').addEventListener('touchstart', () => currMove = 'backward')
document.getElementById('backwardButton').addEventListener('touchend', () => currMove = null)

