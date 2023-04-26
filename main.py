import json

while True:
    with open("output.txt", "r") as file:
        requestedID = input("Input all Provider IDs you would like to see, separated by commas.\nAlternatively, "
                            "type 'q' or 'quit' to quit.\n").split(',', -1)
        if requestedID[0].lower() == "quit" or requestedID[0].lower() == "q":
            exit(0)

        for i in range(len(requestedID)):
            requestedID[i] = requestedID[i].strip()

        print("Checking for Prover ID(s): \n", end='')
        firstMessage = True
        for entry in requestedID:
            if firstMessage:
                print("{", entry, "}", sep='', end='')
                firstMessage = False
            else:
                print(", {", entry, "}", sep='', end='')
        print()
        for line in file:
            if line not in ['\n', '\r\n']:
                json_object = json.loads(line)
                try:
                    objectProviderId = json_object[0]['payload'][0]['provider_id']
                    if objectProviderId in requestedID:
                        print(json_object)
                except KeyError:
                    continue
        print("\n")
