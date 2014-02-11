#! /usr/bin/env python3
import sys
import threading

def main(argv):
    config_file = "monitor.conf"
    settings = {}
    keywords = []
    to_emails = []
    
    #create settings dictionary
    with open(config_file) as f:
        for line in f:
            #A fairly lousy comment skipper, only checks for lines that start
            #in a comment. If I was pro or less lazy I'd make it split lines at
            #the first comment and only process the first half. Whatever, its
            #not like I need it to be a bulletproof implementation, I'm the only
            #user
            if line[0] == '#' or line in ['\n','\r\n']:
                continue
            else:
                (key, val) = line.split("=")
                key = key.strip()
                val = val.strip()
                if key == "keyword":
                    keywords.append(val)
                elif key == "to_email":
                    to_emails.append(val)
                else:
                    if key.isdigit():
                        key = int(key)
                    if val.isdigit():
                        val = int(val)
                    settings[key] = val
    print(settings)
    print(to_emails)
    print(keywords)

    import MonitorNotifier
    Notifier = MonitorNotifier.Notifier(settings['mailserver'], settings['username'], settings['password'])

    import MonitorParser
    for line in MonitorParser.parseEventData(settings['monitor_ip'], settings['monitor_port']):
        print(line[1])
        if line[1] == "no event data":
            print("FULL MSG" + line[0])
        for keyword in keywords:
            if keyword.lower() in line[1].lower():
                print("-----" + line[1] + "------")
                #should probably be set up for batch mails and only attempts to establish a connection once every 5 minutes or so
                # try:
                #     t = threading.Thread(target=Notifier.notify, 
                #             args=(settings['from_email'], to_emails, line[1], line[0]))
                #     t.start()
                # except:
                #     print(sys.exc_info())
                #     print("failure")
                break

if __name__ == "__main__":
    sys.exit(main(sys.argv))
