f8::
  mouseWrapper()
  return

f12::
  ExitApp

mouseWrapper(){
  MouseGetPos, xpos, ypos 
  createManyQuests()
  MouseMove, %xpos%, %ypos%
}
createManyQuests(){
  Loop, 2
  {
    observationQuest()
    send {Click WheelDown}
    Sleep, 100
  }
}

observationQuest(){
  send {Click 963 545 Right} ; right click the center of the screen
  send {Click 1080, 809} ; select observation

  send {Click 620, 374} ; select type: block tag
  send {Click 620, 374} ; select type: block state
  send {Click 620, 374} ; select type: block entity
  send {Click 620, 374} ; select type: block entity type
  send {Click 620, 374} ; select type: entity type

  ; icon
  send {Click 601, 189} ; select icon
  send {Click 708, 446} ; select second "item" (first one is usually blank here)
  send {Click 1186, 834} ; select "Accept"

  ; title
  send {Click 658, 141} ; select Title
  send Spot a xxx
  send {Click 1142, 650} ; select "Accept"


  send {Click 1887, 73} ; select check (accept)
  Send {Esc}
}

itemQuestWithTwoRewardsInOrder(){
  send {Click 963 545 Right} ; right click the center of the screen
  send {Click 1034 228} ; select item quest (need to be updated each time)

  ; create item task
  send {Click 624 383} ; select first item
  send {Click 1191 782} ; select "Accept"

  ; create first reward
  send {Click 1166 522} ; click "+" on rewards
  send {Click 1251 485} ; select "item"
  send {Click 700 379 } ; select second item
  send {Click 1191 782} ; select "Accept"

  ; create second reward
  send {Click 1208 522 } ; click "+" on second rewards
  send {Click 1291 486} ; select second "item"
  send {Click 770, 378} ; select third item
  send {Click 1191 782} ; select "Accept"
  Send {Esc}
}

createFirstReward(){
  ; create first reward
  send {Click 1703 412} ; click "+" on rewards
  send {Click 1251 485} ; select "item"
  send {Click 624 383} ; select first item
  send {Click 1191 782} ; select "Accept"
  Send {Esc}
}

itemQuestWithTwoRewards(){
  send {Click 963 545 Right} ; right click the center of the screen
  send {Click 1034 228} ; select item quest (need to be updated each time)

  ; create item task
  send oak
  send {Click 624 383} ; select first item
  send {Click 1191 782} ; select "Accept"

  ; create first reward
  send {Click 1166 522} ; click "+" on rewards
  send {Click 1251 485} ; select "item"
  Send dia
  send {Click 624 383} ; select first item
  send {Click 1191 782} ; select "Accept"

  ; create second reward
  send {Click 1208 522 } ; click "+" on second rewards
  send {Click 1291 486} ; select second "item"
  send san
  send {Click 624 383} ; select first item
  send {Click 1191 782} ; select "Accept"
  Send {Esc}
}

customItemCollectionQuest(){
  send {Click 963 545 Right} ; right click the center of the screen
  send {Click 996, 348} ; select item quest

  ; create item task
  send {Click 604, 440} ; select first item
  send {Click 1186, 834} ; select "Accept"

  ; create reward
  send {Click 1169, 584} ; click "+" on rewards
  send {Click 1169, 584} ; click "item" on the same location
  send {Click 708, 446} ; select second "item"
  send {Click 1186, 834} ; select "Accept"
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

