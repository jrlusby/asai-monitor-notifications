#! /usr/bin/env python3
import sys

def main(argv):
    config_file = "monitor.conf"
    settings = {}
    keywords = []
    to_emails = []
    
    #create settings dictionary
    with open(config_file) as f:
        for line in f:
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
    Notifier.notify(settings['from_email'], to_emails, "test", "this is a test")

    import MonitorParser
    for line in MonitorParser.listen(settings['monitor_ip'], settings['monitor_port']):
        print(line)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
