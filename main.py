import json
from datetime import datetime

_format = "%Y-%m-%dT%H:%M:%S.%fZ"
while True:
    is_first_message = True
    datetime_last_update = None
    with open("output.txt", "r") as file:
        correct_id_inputted = False
        while not correct_id_inputted:
            requestedID = input("Input the Provider ID you would like to see\nAlternatively, "
                                "type 'q' or 'quit' to quit.\n").split(',', -1)
            if requestedID[0].lower() == "quit" or requestedID[0].lower() == "q":
                exit(0)

            for i in range(len(requestedID)):
                requestedID[i] = requestedID[i].strip()

            if len(requestedID) > 1:
                print("Please only input a single ID.", end="\n\n")
            else:
                correct_id_inputted = True

        print("Checking for Prover ID(s): \n", end='')
        firstMessage = True
        for entry in requestedID:
            if firstMessage:
                print("{", entry, "}", sep='', end='')
                firstMessage = False
            else:
                print(", {", entry, "}", sep='', end='')
        print("\n")
        for line in file:
            if line not in ['\n', '\r\n']:
                json_object = json.loads(line)
                try:
                    assert json_object[0]["accuracy"]
                    # Example Provider ID: 70B3:D50F:7030:1E37
                    objectProviderId = json_object[0]["provider_id"]
                    if objectProviderId in requestedID:
                        datetime_generated = datetime.strptime(json_object[0]["timestamp_generated"], _format)
                        datetime_sent = datetime.strptime(json_object[0]["timestamp_sent"], _format)
                        time_difference_generated_sent = datetime_sent - datetime_generated

                        print("Coordinates X,Y,Z: ", end="")
                        print(json_object[0]["position"]["coordinates"])
                        print("Generated : " + datetime_generated.__str__())
                        print("Sent : " + datetime_sent.__str__())
                        print("Time Difference between 'Generated' and 'Sent': " +
                              time_difference_generated_sent.total_seconds().__str__())
                        if not is_first_message:
                            time_difference_updates = datetime_generated - datetime_last_update
                            print("Time Difference between this and the last update: "
                                  + time_difference_updates.total_seconds().__str__(), end="\n\n")
                        else:
                            is_first_message = False
                        datetime_last_update = datetime_generated

                except KeyError:
                    continue
                except AssertionError:
                    continue
