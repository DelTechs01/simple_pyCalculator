players = {
    "name" : "Patrick Dogue",
    "age" : 18,
    "team" : "Manchester United",
    "position" : "Left Wing Back",
    "friends" : ["Garnacho", "Mainoo", "Bruno"],

    #Nesting in dictionary
    "personal info" : {
        "mother" : "Lisah",
        "father" : "TigerShroff"
    }
}

print(players)
print(players["friends"])
players["height"] = 5.1
print(players["height"])