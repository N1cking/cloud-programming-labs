def run_command(cmd):
    match cmd:
        case "start":
            return "STARTED"
        case "stop":
            return "STOPPED"
        case "status":
            return "OK"
        case _:
            return "UNKNOWN_COMMAND"


for c in ["start", "status", "stop", "pause"]:
    print(c, run_command(c))
