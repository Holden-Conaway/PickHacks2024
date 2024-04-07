
console.log("HELLO")

window.hands = {
  left: { 
    visible: false,
    numFingers: 0,
  },
  right: {
    visible: false,
    numFingers: 0,
  },
  altConfirm: false
}

Leap.loop({
  frame: function(frame) {
   window.hands.right.visible = false
   window.hands.left.visible = false
   window.hands.altConfirm = false
  },
  hand: function(hand) {
    var thishand = window.hands[hand.type]
    thishand.visible = true
    thishand.numFingers = 0
    for (let finger of hand.fingers) {
      thishand.numFingers += finger.extended
    }
    
   
    if (hand.type == "left" 
        && hand.fingers[0].extended 
        && hand.fingers[4].extended
        && ! hand.fingers[1].extended
        && ! hand.fingers[2].extended
        && ! hand.fingers[3].extended
    ) {
      window.hands.altConfirm = true
      console.log("alt confirm")
    }

  }
})


