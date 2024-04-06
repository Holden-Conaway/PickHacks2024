
console.log("HELLO")

window.hands = {
  left: { 
    visible: false,
    numFingers: 0,
  },
  right: {
    visible: false,
    numFingers: 0,
  }
}

Leap.loop({
  frame: function(frame) {
   window.hands.right.visible = false
   window.hands.left.visible = false
  },
  hand: function(hand) {
    var thishand = window.hands[hand.type]
    thishand.visible = true
    thishand.numFingers = 0
    for (let finger of hand.fingers) {
      thishand.numFingers += finger.extended
    }
    console.log(thishand)    
  }
})


