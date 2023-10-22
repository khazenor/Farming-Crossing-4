ServerEvents.recipes(event => {
  event.custom({
    "type": "meadow:cooking",
    "ingredients": [
      {
        "tag": "forge:water"
      }
    ],
    "result": {
      "item":  "meadow:alpine_salt"
    }
  }
  )

})