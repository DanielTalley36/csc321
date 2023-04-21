""" In this folder holds the docker-compose.yml file for the docker container used, python source code, and packet capture files for:
0MQ examples Getting the Message Out, and Divide and Conquer. As well as the attempt of a P2P Chat server using 0MQ """

Part 1:
To capture the packets of the program tcpdump was used while docker container was running. (each individual script) (tcpdump -i eth0 -w example.pcap)

Part 2:
Next Mergecap was used to collect all the files into one pcap file (full-take.pcap)  (mergecap -w example.pcap input.pcap input.pcap input.pcap)

Part 3:
Then the full-take.pcap file was seperated into two pcap files in regard to the program it came from. 
    To do this I used a bash script in the terminal using a portrange command to seperate the packets to which program they belonged.
        eg: tcpdump -r full-take.pcap portrange 5557-5558 -w task.pcap
            this script took all the packets from ports 5557-5558 in full-take.pcap and wrote them to task.pcap
        then this was done for the other program port 5556

Part 4:
Lastly the chat files are they as an attempt to the P2P chat server