s = input("Enter cells: ")


def win(pattern):
    if s[0] + s[1] + s[2] == pattern \
            or s[2] + s[5] + s[8] == pattern \
            or s[8] + s[7] + s[6] == pattern \
            or s[6] + s[3] + s[0] == pattern \
            or s[3] + s[4] + s[5] == pattern \
            or s[1] + s[4] + s[7] == pattern \
            or s[0] + s[4] + s[8] == pattern \
            or s[2] + s[4] + s[6] == pattern:
        return True

print(f"""
---------
| {s[0]} {s[1]} {s[2]} |
| {s[3]} {s[4]} {s[5]} |
| {s[6]} {s[7]} {s[8]} |
---------""")

if s[0] not in ('X', 'O'):
    print("Impossible")
elif win("XXX") and win("OOO"):
    print("Impossible")
elif win("XXX"):
    print("X wins")
elif win("OOO"):
    print("O wins")
elif not win("XXX") and not win("OOO") and "_" not in s:
    print("Draw")
else:
    print("Game not finished")
