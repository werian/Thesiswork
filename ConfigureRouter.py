import argparse
from netmiko import ConnectHandler



# Command line argument for amount of routers user can choose
def get_cmd_line_args():
    parser = argparse.ArgumentParser(description="Router configuration settings")
    parser.add_argument("--count",
                        default="1",
                        type=int,
                        help="Give an amount of routers to send configuration to as CLI parameter",
                        dest="count")
    return parser.parse_args()


# Function which have tester, recieves n as user argument
def tester(n):
    # Read router Hostnames
    with open('hostnames.txt') as f:
        hostnames = f.read().splitlines()

    # Read list of IP addresses from file
    with open('devices_list.txt') as f:
        devices_list = f.read().splitlines()

    # Read router configuration
    with open('router_config.txt') as f:
        config_commands = f.read().splitlines()

    # Router IP list, read by n given as user argument
    router_ip = devices_list[n]
    router_hostname = hostnames[n]

    # Replace hostname and loopback name/IP to correct value before passing it to netmiko
    config_commands[0] = router_hostname
    config_commands[9] = f"int loopback {n+1}"
    config_commands[10] = f"ip address 10.10.10.{10+n+1} 255.255.255.0"

    # Device connection info passed to netmiko for log in into router
    device_info = {
        'device_type':'cisco_ios',
        'host':router_ip,
        'port':22,
        'username':'cisco',
        'password':'cisco123!'
        }

    # Netmiko library connection and sending config to router
    device_connect = ConnectHandler(**device_info)
    output = device_connect.send_config_set(config_commands)
    
    print(f"Connected to Router",router_hostname[-2:] ,"with IP address :", router_ip)
    print(output)



def main(args):
    # Initiate empty task list
    tasks = []
    # Run n amount of tasks based on user argument list
    for n in range(0, args.count):
        tasks.append(tester(n))

    

if __name__ == "__main__":
    args = get_cmd_line_args()     
    main(args)
