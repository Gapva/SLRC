with open("example.sfvc", "r") as chartfile:
    chartprocessed = chartfile.read().splitlines()

configidx = chartprocessed.index('-config')
chartidx = chartprocessed.index('-chart')

configkeys = chartprocessed[configidx+1:chartidx] # +1 to skip the -config line itself
chartnotes = chartprocessed[chartidx+1:] # +1 to skip the -chart line itself

offset = int(configkeys[0].split("_")[1])
tempo = int(configkeys[1].split("_")[1])

print(f"CHART INFO\noffset\t{offset}ms\ntempo\t{tempo}bpm\n")
print("CHART NOTES")
for note in range(len(chartnotes)):
    notetype = chartnotes[note].split("_")[0].lower()
    noteinfo = chartnotes[note].split("_")[1].split(":")
    notecol = int(noteinfo[0])
    notetiming = [int(timing) for timing in noteinfo[1].split("-")]
    match notetype:
        case "rg":
            print(f"{note}\trice grain\tcolumn {notecol}\tat {notetiming[0]}ms")
        case _:
            print(f"{note}\tnoodle strand\tcolumn {notecol}\tfrom {notetiming[0]}ms to {notetiming[1]}ms")
