dataRecived ={
    "type": "object",
    "properties": {
      "review": {
        "type": "string",
        "minLength": 1
      },
      "movie": {
        "type": "string",
        "minLength": 1,
        "maxLength": 20
      }
    },
    "required": [
      "review",
      "movie"
    ]
}
