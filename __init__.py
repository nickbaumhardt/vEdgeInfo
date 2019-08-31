import paramiko
from getpass import getpass
import re
import sys
import time
from pprint import pprint
import datetime

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sh_run_det_command = 'sh run | det'
sh_hard_inv_command = 'show hardware inventory'
serial_pattern = re.compile('serial-number  ([0-9A-Z]{10,18})')
deviceId_pattern = re.compile('(system-ip)([ ]{10,20})([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
hostname_pattern = re.compile('(host-name)([ ]{10,20})(.{1,25})')
latitude_pattern = re.compile('(gps-location latitude )(.{1,15})')
longitude_pattern = re.compile('(gps-location longitude )(.{1,15})')
site_pattern = re.compile('(site-id)([ ]{10,20})([0-9]{1,4})')
timezone_pattern = re.compile('(clock timezone )(.{1,30})')
desc_pattern = re.compile('(description           )(.{1,30})')
ip_pattern = re.compile('ip address[ ]{1,10}([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2})')
ip_pattern2 = re.compile('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
nat_pattern = re.compile(' nat')
tracker_pattern = re.compile('nat-tracker')
color_pattern = re.compile('(color )([a-zA-Z]{1,20}-?[a-zA-Z]{1,10}?)( restrict)')
bwup_pattern = re.compile('(bandwidth-upstream    )([0-9]{1,8})')
bwdown_pattern = re.compile('(bandwidth-downstream  )([0-9]{1,8})')
autoneg_pattern = re.compile('autonegotiate')
noshut_pattern = re.compile('no shutdown')
speed_pattern = re.compile('(speed-mbps        )([0-9]{1,6})')
duplex_pattern = re.compile('(duplex            )([a-zA-Z]{1,10})')
static_route_pattern = re.compile('(ip route )([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2} )([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
int_pattern = re.compile('(ge0/[0-4]{1})([ ]{3,15})([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
# function to establish persistent SSH session


def ssh_connect(ip):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=ip,
                    username=username,
                    password=password)
        session = ssh_client.invoke_shell()
        return session
    except:
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=ip,
                            username=username1,
                            password=password2)
            session = ssh_client.invoke_shell()
            return session
        except:
            return


def parse(response, pattern, match_group_num):
    try:
        ssh_output = response.read()
        raw_output = ssh_output.decode(encoding='utf-8')
    except:
        raw_output = response
    #print(raw_output)
    match = pattern.search(raw_output)
#    return matched_value
    if match:
        matched_value = match.group(match_group_num)
        return matched_value

def get_serial(ip):
    try:
        session = ssh_connect(ip)
        print('*\n'*10)
        print(f'---------Logging into {ip}-------')
        print('*\n'*10)
        time.sleep(3)
        session.send('terminal length 0\n')
        time.sleep(1)
        session.send(sh_hard_inv_command+'\n')
        time.sleep(3)
        session.send(' ')
        time.sleep(.5)
        session.send(' ')
        time.sleep(.5)
        session.send('q\n')
        time.sleep(.5)
        output = session.recv(100000)
        raw_output = output.decode()
        print(raw_output)
        response = parse(raw_output, serial_pattern, 1)
        session.close()
        print(response)
        return response
    except:
        session = ssh_connect(ip)
        print('*\n'*10)
        print(f'---------Logging into {ip}-------')
        print('*\n'*10)
        time.sleep(3)
        session.send('terminal length 0\n')
        time.sleep(1)
        session.send(sh_hard_inv_command+'\n')
        time.sleep(3)
        session.send(' ')
        time.sleep(.5)
        session.send(' ')
        time.sleep(.5)
        session.send('q\n')
        time.sleep(.5)
        output = session.recv(100000)
        raw_output = output.decode()
        print(raw_output)
        response = parse(raw_output, serial_pattern, 1)
        session.close()
        print(response)
        return response

def getRun(ip):
    session = ssh_connect(ip)
    session.send('terminal length 0\n')
    time.sleep(.5)
    session.send(sh_run_det_command+'\n')
    time.sleep(3)
    session.send(' ')
    time.sleep(.5)
    session.send(' ')
    time.sleep(.5)
    session.send(' ')
    time.sleep(.5)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    session.send(' ')
    time.sleep(.1)
    output = session.recv(10000000000)
    raw_output = output.decode()
    #print(raw_output)
    session.close()
    return raw_output

def getRunInt(int):
    int_lines = running_config.split(f' interface {int}')
    try:
        pre_int_run = int_lines[1]
    except:
        return
    pre1_int_run = pre_int_run.split('block-non')
    int_run_list = pre1_int_run[0].strip().split('\r\n')
    int_first_line = (f'interface {int}')
    int_run_list.insert(0, int_first_line)
    #pprint(int_run_list)
    return int_run_list

def getStaticRoutes(ip):
    session = ssh_connect(ip)
    session.send('terminal length 0\n')
    time.sleep(1)
    session.send('show ip route | incl static \n')
    time.sleep(3)
    session.send('q\n')
    time.sleep(.5)
    output = session.recv(10000000000)
    raw_output = output.decode()
    print(raw_output)
    output = raw_output.strip().split('\r\n')
    ge00_route = 0
    ge01_route = 0
    ge02_route = 0
    ge03_route = 0
    ge04_route = 0
    for line in output:
        route_int = parse(line, int_pattern, 1)
        if route_int != None:
            print(route_int)
            if route_int == 'ge0/0':
                stat_route0 = parse(line, int_pattern, 3)
                ge00_route = 1
            if route_int == 'ge0/1':
                stat_route1 = parse(line, int_pattern, 3)
                ge01_route = 1
            if route_int == 'ge0/2':
                stat_route2 = parse(line, int_pattern, 3)
                ge02_route = 1
            if route_int == 'ge0/3':
                stat_route3 = parse(line, int_pattern, 3)
                ge03_route = 1
            if route_int == 'ge0/4':
                stat_route4 = parse(line, int_pattern, 3)
                get04_route = 1
    if ge00_route == 1:
        final_file.write(f'{stat_route0},')
    else:
        final_file.write(f',')
    if ge01_route == 1:
        final_file.write(f'{stat_route1},')
    else:
        final_file.write(f',')
    if ge02_route == 1:
        final_file.write(f'{stat_route2},')
    else:
        final_file.write(f',')
    if ge03_route == 1:
        final_file.write(f'{stat_route3},')
    else:
        final_file.write(f',')
    if ge04_route == 1:
        final_file.write(f'{stat_route4},')
    else:
        final_file.write(f',')
    session.close()
    return

def getIntLinkInfo(ip, int):
    sh_int_command = 'sh int '+int
    session = ssh_connect(ip)
    session.send('terminal length 0\n')
    time.sleep(1)
    session.send(f'sh int {int}\n')
    time.sleep(3)
    output = session.recv(1000000)
    raw_output = output.decode()
    #print(raw_output)
    session.close()
    link_info_list = raw_output.split('\r\n')
    return link_info_list

def checkStaticRoutes(running_config):
    pre_run = running_config.split('\r\n')
    #pprint(pre_run)
    for line in pre_run:
        route = parse(line, static_route_pattern, 3)
        #print(route)
        if route != None:
            route_octets = route.split('.')
            #pprint(route_octets[0])
            if route_octets[0] == '10':
                #print('equal')
                final_file.write(f'{route},')
                print(f'The old subnet for this site is: {route} ')
            if route_octets[0] == '172':
                final_file.write(f'{route},')
                print(f'The old subnet for this site is: {route} ')
            if route_octets[0] == '192':
                final_file.write(f'{route},')
                print(f'The old subnet for this site is: {route} ')
            if route_octets[0] != '10':
                if route_octets[0] != '172':
                    if route_octets[0] != '192':
                        print('not equal')
                        continue
    return

# get creds from user
username = input('Username: ')
password = getpass('Password: ')
username1 = input('Secondary Username: ')
password2 = getpass('Secondary Password: ')

now = datetime.datetime.now()
print(now)
year = str(now.year)
month = str(now.month)
day = str(now.day)
hour = str(now.hour)
minute = str(now.minute)
filetime = (f"{year}-{month}-{day} {hour}.{minute}")

file = open('vEdgeList2.txt', 'r')
#file = open('vEdgeTempList', 'r')
for line in file:
    device_ip_list = line.strip().split(',')
pprint(device_ip_list)
file.close()

exception_file = open(f'vEdgeTemplateScan{filetime} Exception.csv', 'w+')
final_file = open(f'vEdgeTemplateScan{filetime}.csv', 'w+')
final_file.write('csv-deviceId,csv-deviceIP,csv-host-name,site-name,latitude,longitude,system_ip,site_id,timezone,ge0/0_description,ge0/0_ip,ge0/0_LAN_ip,ge0/0_nat,ge0/0 tracker nat-tracker,ge0/0_color,ge0/0_speed,ge0/0_duplex,ge0/0_autonegotiate,ge0/0_shutdown,ge0/0_bandwidth_up,ge0/0_bandwidth_down,ge0/1_description,ge0/1_ip,ge0/1_nat,ge0/1 tracker nat-tracker,ge0/1_color,ge0/1_speed,ge0/1_duplex,ge0/1_autonegotiate,ge0/1_shutdown,ge0/1_bandwidth_up,ge0/1_bandwidth_down,ge0/2_description,ge0/2_ip,ge0/2_nat,ge0/2 tracker nat-tracker,ge0/2_color,ge0/2_speed,ge0/2_duplex,ge0/2_autonegotiate,ge0/2_shutdown,ge0/2_bandwidth_up,ge0/2_bandwidth_down,ge0/3_description,ge0/3_ip,ge0/3_nat,ge0/3 tracker nat-tracker,ge0/3_color,ge0/3_speed,ge0/3_duplex,ge0/3_autonegotiate,ge0/3_shutdown,ge0/3_bandwidth_up,ge0/3_bandwidth_down,ge0/4_description,ge0/4_ip,ge0/4_nat,ge0/4 tracker nat-tracker,ge0/4_color,ge0/4_speed,ge0/4_duplex,ge0/4_autonegotiate,ge0/4_shutdown,ge0/4_bandwidth_up,ge0/4_bandwidth_down,ge0/0n_next_hop,ge/01_next_hop,ge0/2_next_hop,ge0/3_next_hop,ge0/4_next_hop,Old Switch Subnet,Old Switch Subnet2,Old Switch Subnet3,\n')


for ip in device_ip_list:
    try:
        serial = get_serial(ip)
        final_file.write(f'{serial},')
        running_config = getRun(ip)
        #print(running_config)
        print(f'The Device ID (serial number) is: {serial}')
        predeviceId = parse(running_config, deviceId_pattern, 3)
        deviceId = predeviceId.rstrip()
        print(f'The Device IP is: {deviceId}')
        final_file.write(f'{deviceId},')
        pre_hostname = parse(running_config, hostname_pattern, 3)
        hostname = pre_hostname.rstrip()
        print(f'The Hostname is: {hostname}')
        final_file.write(f'{hostname},')
        #write hostname again since it's the same as site name
        print(f'The Site Name is: {hostname}')
        final_file.write(f'{hostname},')
        pre_latitude = parse(running_config, latitude_pattern, 2)
        latitude = pre_latitude.rstrip()
        print(f'The latitude is: {latitude}')
        final_file.write(f'{latitude},')
        pre_longitude = parse(running_config, longitude_pattern, 2)
        longitude = pre_longitude.rstrip()
        print(f'The longitude is: {longitude}')
        final_file.write(f'{longitude},')
        #write deviceId next since it's the same as system ip
        print(f'The System IP is: {deviceId}')
        final_file.write(f'{deviceId},')
        pre_siteId = parse(running_config, site_pattern, 3)
        siteId = pre_siteId.rstrip()
        print(f'The site id is: {siteId}')
        final_file.write(f'{siteId},')
        pre_timezone = parse(running_config, timezone_pattern, 2)
        timezone = pre_timezone.rstrip()
        print(f'The timezone is: {timezone}')
        final_file.write(f'{timezone},')
        output_list = running_config.split('vpn 0')
        new_running_config = output_list[1]
    except:
        exception_file.write(f'{ip}\n')
        final_file.write('\n')
        continue

#### GE0/0##########################################################
    try:
        print('Interface ge0/0==========================================')
        ge00_runlist = getRunInt('ge0/0')

        for line in ge00_runlist:
            ge00_desc = parse(line, desc_pattern, 2)
            if ge00_desc != None:
                final_file.write(f'"{ge00_desc}",')
                print(f'The description for ge0/0 is: {ge00_desc}')
                break
            else:
                continue
        if ge00_desc == None:
            final_file.write(f'"",')
            print(f'The description for ge0/0 is: {ge00_desc}')

        for line in ge00_runlist:
            int_ip = parse(line, ip_pattern, 1)
            if int_ip != None:
                final_file.write(f'{int_ip},')
                final_file.write(f'{int_ip},')
                print(f'The IP Address for ge0/0 is: {int_ip}')
                break
            else:
                continue
        if int_ip == None:
            final_file.write(f'{int_ip},')
            print(f'The IP Address for ge0/0 is: {int_ip}')

        for line in ge00_runlist:
            nat_stat = parse(line, nat_pattern, 0)
            if nat_stat != None:
                final_file.write(f'{nat_stat},')
                print(f'NAT status for ge0/0 is: {nat_stat}')
                break
            else:
                continue
        if nat_stat == None:
            final_file.write(f'no nat,')
            print(f'NAT status for ge0/0 is: {nat_stat}')

        for line in ge00_runlist:
            nat_tracker = parse(line, tracker_pattern, 0)
            if nat_tracker != None:
                final_file.write(f'{nat_tracker},')
                print(f'NAT Tracker status for ge0/0 is: {nat_tracker}')
                break
            else:
                continue
        if nat_tracker == None:
            final_file.write(f'no tracker,')
            print(f'NAT tracker status for ge0/0 is: {nat_tracker}')

        for line in ge00_runlist:
            color_stat = parse(line, color_pattern, 2)
            if color_stat != None:
                final_file.write(f'{color_stat},')
                print(f'The color for ge0/0 is: {color_stat} restrict')
                break
            else:
                continue
        if color_stat == None:
            final_file.write(f'red,')
            print(f'The color for ge0/0 is: {color_stat}')

        for line in ge00_runlist:
            speed_stat = parse(line, speed_pattern, 2)
            if speed_stat != None:
                final_file.write(f'speed {speed_stat},')
                print(f'The speed for ge0/0 is: {speed_stat}')
                break
            else:
                continue
        if speed_stat == None:
            final_file.write('no speed,')
            print(f'The speed for ge0/0 is: {speed_stat}')

        for line in ge00_runlist:
            duplex_stat = parse(line, duplex_pattern, 2)
            if duplex_stat != None:
                final_file.write(f'duplex {duplex_stat},')
                print(f'The duplex for ge0/0 is: {duplex_stat}')
                break
            else:
                continue
        if duplex_stat == None:
            final_file.write('no duplex,')
            print(f'The duplex for ge0/0 is: {duplex_stat}')


        for line in ge00_runlist:
            autoneg_stat = parse(line, autoneg_pattern, 0)
            if autoneg_stat != None:
                final_file.write(f'{autoneg_stat},')
                print(f'Interface ge0/0 autonegotiation is set to: {autoneg_stat} ')
                break
            else:
                continue
        if autoneg_stat == None:
            final_file.write(f'{autoneg_stat},')
            print(f'Interface ge0/0 autonegotiation is set to: {autoneg_stat}')

        for line in ge00_runlist:
            shut_stat = parse(line, noshut_pattern, 0)
            if shut_stat != None:
                final_file.write(f'{shut_stat},')
                print(f'Interface ge0/0 is: {shut_stat} ')
                break
            else:
                continue
        if shut_stat == None:
            final_file.write(f'shutdown,')
            print(f'Interface ge0/0 autonegotiation is set to: shutdown')

        for line in ge00_runlist:
            bwup_stat = parse(line, bwup_pattern, 2)
            if bwup_stat != None:
                final_file.write(f'{bwup_stat},')
                print(f'The bandwidth-upstream for ge0/0 is: {bwup_stat} ')
                break
            else:
                continue
        if bwup_stat == None:
            final_file.write(f'{bwup_stat},')
            print(f'The bandwidth-upstream for ge0/0 is: {bwup_stat}')

        for line in ge00_runlist:
            bwdown_stat = parse(line, bwdown_pattern, 2)
            if bwdown_stat != None:
                final_file.write(f'{bwdown_stat},')
                print(f'The bandwidth-downstream for ge0/0 is: {bwdown_stat} ')
                break
            else:
                continue
        if bwdown_stat == None:
            final_file.write(f'{bwdown_stat},')
            print(f'The bandwidth-downstream for ge0/0 is: {bwdown_stat}')
    except:
        print(f'No Config on ge0/0')
        final_file.write(',,,,,,,,,,,,')

#### GE0/1##########################################################
    try:
        print('Interface ge0/1==========================================')
        ge01_runlist = getRunInt('ge0/1')

        for line in ge01_runlist:
            pre_ge01_desc = parse(line, desc_pattern, 2)
            if pre_ge01_desc != None:
                ge01_desc = pre_ge01_desc.rstrip()
                final_file.write(f'"{ge01_desc}",')
                print(f'The description for ge0/1 is: {ge01_desc}')
                break
            else:
                ge01_desc = pre_ge01_desc
                continue
        if ge01_desc == None:
            final_file.write(f'"",')
            print(f'The description for ge0/1 is: {ge01_desc}')

        for line in ge01_runlist:
            int_ip = parse(line, ip_pattern, 1)
            if int_ip != None:
                final_file.write(f'{int_ip},')
                print(f'The IP Address for ge0/1 is: {int_ip}')
                #global ge01_firstoctet
                ge01_firstoctet = int_ip.split('.')[0]
                if ge01_firstoctet == None:
                    ge01_firstoctet = ''
                break
            else:
                continue
        if int_ip == None:
            final_file.write(f'{int_ip},')
            print(f'The IP Address for ge0/1 is: {int_ip}')

        for line in ge01_runlist:
            nat_stat = parse(line, nat_pattern, 0)
            if nat_stat != None:
                final_file.write(f'{nat_stat},')
                print(f'NAT status for ge0/1 is: {nat_stat}')
                break
            else:
                continue
        if nat_stat == None:
            final_file.write(f'no nat,')
            print(f'NAT status for ge0/1 is: {nat_stat}')

        for line in ge01_runlist:
            nat_tracker = parse(line, tracker_pattern, 0)
            if nat_tracker != None:
                final_file.write(f'{nat_tracker},')
                print(f'NAT Tracker status for ge0/1 is: {nat_tracker}')
                break
            else:
                continue
        if nat_tracker == None:
            final_file.write(f'no tracker,')
            print(f'NAT tracker status for ge0/1 is: {nat_tracker}')

        for line in ge01_runlist:
            color_stat = parse(line, color_pattern, 2)
            if color_stat != None:
                final_file.write(f'{color_stat},')
                print(f'The color for ge0/1 is: {color_stat} restrict')
                break
            else:
                continue
        if color_stat == None:
            final_file.write(f'red,')
            print(f'The color for ge0/1 is: {color_stat}')

        for line in ge01_runlist:
            speed_stat = parse(line, speed_pattern, 2)
            if speed_stat != None:
                final_file.write(f'speed {speed_stat},')
                print(f'The speed for ge0/1 is: {speed_stat}')
                break
            else:
                continue
        if speed_stat == None:
            final_file.write('no speed,')
            print(f'The speed for ge0/1 is: {speed_stat}')

        for line in ge01_runlist:
            duplex_stat = parse(line, duplex_pattern, 2)
            if duplex_stat != None:
                final_file.write(f'duplex {duplex_stat},')
                print(f'The duplex for ge0/1 is: {duplex_stat}')
                break
            else:
                continue
        if duplex_stat == None:
            final_file.write(f'no duplex,')
            print(f'The duplex for ge0/1 is: {duplex_stat}')

        for line in ge01_runlist:
            autoneg_stat = parse(line, autoneg_pattern, 0)
            if autoneg_stat != None:
                final_file.write(f'{autoneg_stat},')
                print(f'Interface ge0/1 autonegotiation is set to: {autoneg_stat} ')
                break
            else:
                continue
        if autoneg_stat == None:
            final_file.write(f'{autoneg_stat},')
            print(f'Interface ge0/1 autonegotiation is set to: {autoneg_stat}')

        for line in ge01_runlist:
            shut_stat = parse(line, noshut_pattern, 0)
            if shut_stat != None:
                final_file.write(f'{shut_stat},')
                print(f'Interface ge0/1 is: {shut_stat} ')
                break
            else:
                continue
        if shut_stat == None:
            final_file.write(f'shutdown,')
            print(f'Interface ge0/1 autonegotiation is set to: shutdown')

        for line in ge01_runlist:
            bwup_stat = parse(line, bwup_pattern, 2)
            if bwup_stat != None:
                final_file.write(f'{bwup_stat},')
                print(f'The bandwidth-upstream for ge0/1 is: {bwup_stat} ')
                break
            else:
                continue
        if bwup_stat == None:
            final_file.write(f'{bwup_stat},')
            print(f'The bandwidth-upstream for ge0/1 is: {bwup_stat}')

        for line in ge01_runlist:
            bwdown_stat = parse(line, bwdown_pattern, 2)
            if bwdown_stat != None:
                final_file.write(f'{bwdown_stat},')
                print(f'The bandwidth-downstream for ge0/1 is: {bwdown_stat} ')
                break
            else:
                continue
        if bwdown_stat == None:
            final_file.write(f'{bwdown_stat},')
            print(f'The bandwidth-downstream for ge0/1 is: {bwdown_stat}')
    except:
        print(f'No Config on ge0/1')
        final_file.write(',,,,,,,,,,,')

#### GE0/2##########################################################
    print('Interface ge0/2==========================================')
    try:
        ge02_runlist = getRunInt('ge0/2')

        for line in ge02_runlist:
            pre_ge02_desc = parse(line, desc_pattern, 2)
            if pre_ge02_desc != None:
                ge02_desc = pre_ge02_desc.rstrip()
                final_file.write(f'"{ge02_desc}",')
                print(f'The description for ge0/2 is: {ge02_desc}')
                break
            else:
                ge02_desc = pre_ge02_desc
                continue
        if ge02_desc == None:
            final_file.write(f'"",')
            print(f'The description for ge0/2 is: {ge02_desc}')

        for line in ge02_runlist:
            int_ip = parse(line, ip_pattern, 1)
            if int_ip != None:
                final_file.write(f'{int_ip},')
                print(f'The IP Address for ge0/2 is: {int_ip}')
                ge02_firstoctet = int_ip.split('.')[0]
                break
            else:
                continue
        if int_ip == None:
            final_file.write(f'{int_ip},')
            print(f'The IP Address for ge0/2 is: {int_ip}')

        for line in ge02_runlist:
            nat_stat = parse(line, nat_pattern, 0)
            if nat_stat != None:
                final_file.write(f'{nat_stat},')
                print(f'NAT status for ge0/2 is: {nat_stat}')
                break
            else:
                continue
        if nat_stat == None:
            final_file.write(f'no nat,')
            print(f'NAT status for ge0/2 is: {nat_stat}')

        for line in ge02_runlist:
            nat_tracker = parse(line, tracker_pattern, 0)
            if nat_tracker != None:
                final_file.write(f'{nat_tracker},')
                print(f'NAT Tracker status for ge0/2 is: {nat_tracker}')
                break
            else:
                continue
        if nat_tracker == None:
            final_file.write(f'no tracker,')
            print(f'NAT tracker status for ge0/2 is: {nat_tracker}')

        for line in ge02_runlist:
            color_stat = parse(line, color_pattern, 2)
            if color_stat != None:
                final_file.write(f'{color_stat},')
                print(f'The color for ge0/2 is: {color_stat} restrict')
                break
            else:
                continue
        if color_stat == None:
            final_file.write(f'red,')
            print(f'The color for ge0/2 is: {color_stat}')

        for line in ge02_runlist:
            speed_stat = parse(line, speed_pattern, 2)
            if speed_stat != None:
                final_file.write(f'speed {speed_stat},')
                print(f'The speed for ge0/2 is: {speed_stat}')
                break
            else:
                continue
        if speed_stat == None:
            final_file.write('no speed,')
            print(f'The speed for ge0/2 is: {speed_stat}')

        for line in ge02_runlist:
            duplex_stat = parse(line, duplex_pattern, 2)
            if duplex_stat != None:
                final_file.write(f'duplex {duplex_stat},')
                print(f'The duplex for ge0/2 is: {duplex_stat}')
                break
            else:
                continue
        if duplex_stat == None:
            final_file.write(f'no duplex,')
            print(f'The duplex for ge0/2 is: {duplex_stat}')


        for line in ge02_runlist:
            autoneg_stat = parse(line, autoneg_pattern, 0)
            if autoneg_stat != None:
                final_file.write(f'{autoneg_stat},')
                print(f'Interface ge0/2 autonegotiation is set to: {autoneg_stat} ')
                break
            else:
                continue
        if autoneg_stat == None:
            final_file.write(f'{autoneg_stat},')
            print(f'Interface ge0/2 autonegotiation is set to: {autoneg_stat}')

        for line in ge02_runlist:
            shut_stat = parse(line, noshut_pattern, 0)
            if shut_stat != None:
                final_file.write(f'{shut_stat},')
                print(f'Interface ge0/2 is: {shut_stat} ')
                break
            else:
                continue
        if shut_stat == None:
            final_file.write(f'shutdown,')
            print(f'Interface ge0/2 autonegotiation is set to: shutdown')

        for line in ge02_runlist:
            bwup_stat = parse(line, bwup_pattern, 2)
            if bwup_stat != None:
                final_file.write(f'{bwup_stat},')
                print(f'The bandwidth-upstream for ge0/2 is: {bwup_stat} ')
                break
            else:
                continue
        if bwup_stat == None:
            final_file.write(f'{bwup_stat},')
            print(f'The bandwidth-upstream for ge0/2 is: {bwup_stat}')

        for line in ge02_runlist:
            bwdown_stat = parse(line, bwdown_pattern, 2)
            if bwdown_stat != None:
                final_file.write(f'{bwdown_stat},')
                print(f'The bandwidth-downstream for ge0/2 is: {bwdown_stat} ')
                break
            else:
                continue
        if bwdown_stat == None:
            final_file.write(f'{bwdown_stat},')
            print(f'The bandwidth-downstream for ge0/2 is: {bwdown_stat}')
    except:
        print(f'No Config on ge0/2')
        final_file.write(',,,,,,,,,,,')
#### GE0/3##########################################################
    try:
        print('Interface ge0/3==========================================')
        ge03_runlist = getRunInt('ge0/3')

        for line in ge03_runlist:
            pre_ge03_desc = parse(line, desc_pattern, 2)
            if pre_ge03_desc != None:
                ge03_desc = pre_ge03_desc.rstrip()
                final_file.write(f'"{ge03_desc}",')
                print(f'The description for ge0/3 is: {ge03_desc}')
                break
            else:
                ge03_desc = pre_ge03_desc
                continue
        if ge03_desc == None:
            final_file.write(f'"",')
            print(f'The description for ge0/3 is: {ge03_desc}')

        for line in ge03_runlist:
            int_ip = parse(line, ip_pattern, 1)
            if int_ip != None:
                final_file.write(f'{int_ip},')
                print(f'The IP Address for ge0/3 is: {int_ip}')
                ge03_firstoctet = int_ip.split('.')[0]
                if ge03_firstoctet == None:
                    ge03_firstoctet = ''
                break
            else:
                continue
        if int_ip == None:
            final_file.write(f'{int_ip},')
            print(f'The IP Address for ge0/3 is: {int_ip}')

        for line in ge03_runlist:
            nat_stat = parse(line, nat_pattern, 0)
            if nat_stat != None:
                final_file.write(f'{nat_stat},')
                print(f'NAT status for ge0/3 is: {nat_stat}')
                break
            else:
                continue
        if nat_stat == None:
            final_file.write(f'no nat,')
            print(f'NAT status for ge0/3 is: {nat_stat}')

        for line in ge03_runlist:
            nat_tracker = parse(line, tracker_pattern, 0)
            if nat_tracker != None:
                final_file.write(f'{nat_tracker},')
                print(f'NAT Tracker status for ge0/3 is: {nat_tracker}')
                break
            else:
                continue
        if nat_tracker == None:
            final_file.write(f'no tracker,')
            print(f'NAT tracker status for ge0/3 is: {nat_tracker}')

        for line in ge03_runlist:
            color_stat = parse(line, color_pattern, 2)
            if color_stat != None:
                final_file.write(f'{color_stat},')
                print(f'The color for ge0/3 is: {color_stat} restrict')
                break
            else:
                continue
        if color_stat == None:
            final_file.write(f'red,')
            print(f'The color for ge0/3 is: {color_stat}')

        for line in ge03_runlist:
            speed_stat = parse(line, speed_pattern, 2)
            if speed_stat != None:
                final_file.write(f'speed {speed_stat},')
                print(f'The speed for ge0/3 is: {speed_stat}')
                break
            else:
                continue
        if speed_stat == None:
            final_file.write('no speed,')
            print(f'The speed for ge0/3 is: {speed_stat}')

        for line in ge03_runlist:
            duplex_stat = parse(line, duplex_pattern, 2)
            if duplex_stat != None:
                final_file.write(f'duplex {duplex_stat},')
                print(f'The duplex for ge0/3 is: {duplex_stat}')
                break
            else:
                continue
        if duplex_stat == None:
            final_file.write(f'no duplex,')
            print(f'The duplex for ge0/3 is: {duplex_stat}')


        for line in ge03_runlist:
            autoneg_stat = parse(line, autoneg_pattern, 0)
            if autoneg_stat != None:
                final_file.write(f'{autoneg_stat},')
                print(f'Interface ge0/3 autonegotiation is set to: {autoneg_stat} ')
                break
            else:
                continue
        if autoneg_stat == None:
            final_file.write(f'{autoneg_stat},')
            print(f'Interface ge0/3 autonegotiation is set to: {autoneg_stat}')

        for line in ge03_runlist:
            shut_stat = parse(line, noshut_pattern, 0)
            if shut_stat != None:
                final_file.write(f'{shut_stat},')
                print(f'Interface ge0/3 is: {shut_stat} ')
                break
            else:
                continue
        if shut_stat == None:
            final_file.write(f'shutdown,')
            print(f'Interface ge0/3 autonegotiation is set to: shutdown')

        for line in ge03_runlist:
            bwup_stat = parse(line, bwup_pattern, 2)
            if bwup_stat != None:
                final_file.write(f'{bwup_stat},')
                print(f'The bandwidth-upstream for ge0/3 is: {bwup_stat} ')
                break
            else:
                continue
        if bwup_stat == None:
            final_file.write(f'{bwup_stat},')
            print(f'The bandwidth-upstream for ge0/3 is: {bwup_stat}')

        for line in ge03_runlist:
            bwdown_stat = parse(line, bwdown_pattern, 2)
            if bwdown_stat != None:
                final_file.write(f'{bwdown_stat},')
                print(f'The bandwidth-downstream for ge0/3 is: {bwdown_stat} ')
                break
            else:
                continue
        if bwdown_stat == None:
            final_file.write(f'{bwdown_stat},')
            print(f'The bandwidth-downstream for ge0/3 is: {bwdown_stat}')
    except:
        print(f'No Config on ge0/3')
        final_file.write(',,,,,,,,,,,,')

#### GE0/4##########################################################
    try:
        print('Interface ge0/4==========================================')
        ge04_runlist = getRunInt('ge0/4')

        for line in ge04_runlist:
            pre_ge04_desc = parse(line, desc_pattern, 2)
            if pre_ge04_desc != None:
                ge04_desc = pre_ge04_desc.rstrip()
                final_file.write(f'"{ge04_desc}",')
                print(f'The description for ge0/4 is: {ge04_desc}')
                break
            else:
                ge04_desc = pre_ge04_desc
                continue
        if ge04_desc == None:
            final_file.write(f'"",')
            print(f'The description for ge0/4 is: {ge04_desc}')

        for line in ge04_runlist:
            int_ip = parse(line, ip_pattern, 1)
            if int_ip != None:
                final_file.write(f'{int_ip},')
                print(f'The IP Address for ge0/4 is: {int_ip}')
                ge04_firstoctet = int_ip.split('.')[0]
                if ge04_firstoctet == None:
                    ge04_firstoctet = ''
                break
            else:
                continue
        if int_ip == None:
            final_file.write(f'{int_ip},')
            print(f'The IP Address for ge0/4 is: {int_ip}')

        for line in ge04_runlist:
            nat_stat = parse(line, nat_pattern, 0)
            if nat_stat != None:
                final_file.write(f'{nat_stat},')
                print(f'NAT status for ge0/4 is: {nat_stat}')
                break
            else:
                continue
        if nat_stat == None:
            final_file.write(f'no nat,')
            print(f'NAT status for ge0/4 is: {nat_stat}')

        for line in ge04_runlist:
            nat_tracker = parse(line, tracker_pattern, 0)
            if nat_tracker != None:
                final_file.write(f'{nat_tracker},')
                print(f'NAT Tracker status for ge0/4 is: {nat_tracker}')
                break
            else:
                continue
        if nat_tracker == None:
            final_file.write(f'no tracker,')
            print(f'NAT tracker status for ge0/4 is: {nat_tracker}')

        for line in ge04_runlist:
            color_stat = parse(line, color_pattern, 2)
            if color_stat != None:
                final_file.write(f'{color_stat},')
                print(f'The color for ge0/4 is: {color_stat} restrict')
                break
            else:
                continue
        if color_stat == None:
            final_file.write(f'red,')
            print(f'The color for ge0/4 is: {color_stat}')

        for line in ge04_runlist:
            speed_stat = parse(line, speed_pattern, 2)
            if speed_stat != None:
                final_file.write(f'speed {speed_stat},')
                print(f'The speed for ge0/4 is: {speed_stat}')
                break
            else:
                continue
        if speed_stat == None:
                final_file.write('no speed,')
                print(f'The speed for ge0/4 is: {speed_stat}')

        for line in ge04_runlist:
            duplex_stat = parse(line, duplex_pattern, 2)
            if duplex_stat != None:
                final_file.write(f'duplex {duplex_stat},')
                print(f'The duplex for ge0/4 is: {duplex_stat}')
                break
            else:
                continue
        if duplex_stat == None:
                final_file.write(f'no duplex,')
                print(f'The duplex for ge0/4 is: {duplex_stat}')


        for line in ge04_runlist:
            autoneg_stat = parse(line, autoneg_pattern, 0)
            if autoneg_stat != None:
                final_file.write(f'{autoneg_stat},')
                print(f'Interface ge0/4 autonegotiation is set to: {autoneg_stat} ')
                break
            else:
                continue
        if autoneg_stat == None:
            final_file.write(f'{autoneg_stat},')
            print(f'Interface ge0/4 autonegotiation is set to: {autoneg_stat}')

        for line in ge04_runlist:
            shut_stat = parse(line, noshut_pattern, 0)
            if shut_stat != None:
                final_file.write(f'{shut_stat},')
                print(f'Interface ge0/4 is: {shut_stat} ')
                break
            else:
                continue
        if shut_stat == None:
            final_file.write(f'shutdown,')
            print(f'Interface ge0/4 autonegotiation is set to: shutdown')

        for line in ge04_runlist:
            bwup_stat = parse(line, bwup_pattern, 2)
            if bwup_stat != None:
                final_file.write(f'{bwup_stat},')
                print(f'The bandwidth-upstream for ge0/4 is: {bwup_stat} ')
                break
            else:
                continue
        if bwup_stat == None:
            final_file.write(f'{bwup_stat},')
            print(f'The bandwidth-upstream for ge0/4 is: {bwup_stat}')

        for line in ge04_runlist:
            bwdown_stat = parse(line, bwdown_pattern, 2)
            if bwdown_stat != None:
                final_file.write(f'{bwdown_stat},')
                print(f'The bandwidth-downstream for ge0/4 is: {bwdown_stat} ')
                break
            else:
                continue
        if bwdown_stat == None:
            final_file.write(f'{bwdown_stat},')
            print(f'The bandwidth-downstream for ge0/4 is: {bwdown_stat}')
    except:
        print(f'No Config on ge0/4')
        final_file.write(',,,,,,,,,,,,')
    getStaticRoutes(ip)
    checkStaticRoutes(running_config)
    final_file.write('\n')
final_file.close()
exception_file.close()
