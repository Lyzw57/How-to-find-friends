def check_connection(network, first, second):
    connection_groups = []

    for connection in network:
        friends = set(connection.split("-"))
        
        for group in connection_groups[:]:
            if group.intersection(friends):
                friends.update(group)
                connection_groups.remove(group)

        connection_groups.append(friends)
    
    for group in connection_groups:
        if first in group and second in group:
            return True

    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True
    assert check_connection(
        ("nikola-robin", "batman-nwing", "mr99-batman", 
        "mr99-robin", "dr101-out00", "out00-nwing"),
        "dr101", "mr99") == True
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False
    assert check_connection(
        ("scout2-plane1", "plane1-stevan", "stevan-night", "night-mega",
         "mega-sscout", "sscout-super", "super-scout3", "scout3-doc", "doc-batman"),
          "scout2", "batman") == True