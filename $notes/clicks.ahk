f8::
  createManyQuests()
  return
  
f9::
  questAddMilesReward()
  return

f12::
  ExitApp

createManyQuests(){
  Loop, 333
  {
    customItemCollectionQuest()
  }
}

customItemCollectionQuest(){
  send {Click 963 545 Right} ; right click the center of the screen
  send {Click 1034 228} ; select item quest (need to be updated each time)

  ; create item task
  send obsidi
  send {Click 624 383} ; select first item (need to be updated each time)
  send {Click 1191 782} ; select "Accept"

  ; create reward
  send {Click 1166 522} ; click "+" on rewards
  send {Click 1251 485} ; select "item"
  Send miles ticket
  send {Click 624 383} ; select first item (need to be updated each time)
  send {Click 1191 782} ; select "Accept"
  Send {Esc}
}

questAddItemReward(){
  MouseGetPos, xpos, ypos 
  Send {Click 1156 550 }
  Send {Click 1138 445 }
  Sleep, 200
  Send {Click 1138 445 }
  Send {Click 1188 830 }
  Send {Esc}
  MouseMove, %xpos%, %ypos%
  return
}

addItemQuest(){
  MouseGetPos, xpos, ypos 
  Send obsidi
  Send {Click 709 480 }
  Send {Click 1083 782 }
  MouseMove, %xpos%, %ypos%
  return
}
questAddMilesReward(){
  ; MouseGetPos, xpos, ypos 
  ; Send {Click 1131 576 }
  ; Send {Click 1131 576 }
  ; Sleep, 200
  Send miles
  Send {Click 709 480 }
  Send {Click 1083 782 }
  Send {Esc}
  MouseMove, %xpos%, %ypos%
  return
}

editFirstTaskNumber(){
  MouseGetPos, xpos, ypos 
  Send {Click 721 580 Right } ;rClick on task
  Send {Click 807 670 } ;edit
  Send {Click 643 395 } ;count
  Send {BackSpace}
  Send {BackSpace}
  Send 64
  Send {Click 1105 655 } ;accept
  Send {Click 1886 69 } ;top accept
  Send {Esc}
  MouseMove, %xpos%, %ypos%
  return
}

