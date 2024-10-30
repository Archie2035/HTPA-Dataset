
# HTPA Dataset

**Dataset Name**: HTPA(HTTPS Tunneling Predictive Analysis Dataset)



## Table of Contents
1. [Overview](#overview)
2. [Dataset Structure](#dataset-structure)
3. [Data Collection Methodology](#data-collection-methodology)
4. [Privacy Considerations](#privacy-considerations)
5. [Feature Descriptions](#feature-descriptions)
6. [Usage Instructions](#usage-instructions)
7. [Contact](#contact)


## Overview
The HTPA dataset is designed for research and development in detecting HTTPS tunnel traffic versus normal HTTPS traffic. It is especially suitable for knowledge-graph-based algorithms, such as the HINT method, due to its inclusion of multi-dimensional traffic features and large-scale network interactions. 

### Key Features
- HTTPS tunnel traffic, VPN.



## Dataset Structure

The HTPA dataset is provided as a compressed file with the following structure:

```
HTPA/
├── tunnel_traffic.pickle 
├── normal_traffic.pickle 
├── load_data.py 
└── splited_data/                                       
```

## Data Collection Methodology

HTPA was generated to capture diverse traffic interactions in a server-client setup. Tunnel traffic data was gathered from popular VPN services—Hotspot Shield Free, Browsec VPN, ZenMate VPN, Hoxx VPN, and ShadowsocksR—all of which utilize HTTPS tunneling for data transfer. In collecting HTTPS tunnel traffic, we developed a crawler script that automated the process of visiting websites via these VPNs. To simulated realistic user behavior patterns, the crawler script was designed to browse at preset intervals with random pauses, closely mimicking human interaction habits. Specifically, clients (computers and mobile devices) were connected to VPN servers with configured client software. The crawler then launched a Chrome browser to visit randomly chosen sites from the Alexa Top 10,000 websites. All traffic was routed through a configured router that mirrored it to a storage server, archiving it in pcap format, and this process was repeated multiple times to ensure dataset diversity.

For non-VPN (normal HTTPS) traffic, data was collected passively from a corporate network environment with over one hundred users. Five volunteers logged their regular online activities without VPNs or proxies over a month, allowing us to record their service IPs and ports as non-VPN traffic. 


## Privacy Considerations

Due to the dataset's scale and privacy concerns, we provide extracted features rather than raw network packets. All IP addresses and domain names have been hashed to preserve anonymity.


## Feature Descriptions

The feature data files (`tunnel_traffic.pickle` and `normal_traffic.pickle`) include:

| Field      | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| StartTime  | The timestamp (second) marking the beginning of a traffic flow.                       |
| EndTime    | The timestamp (second)  marking the end of a traffic flow.                             |
| ServerIP   | The hashed IP address of source.                  |
| ServerPort | The port number of source.                                         |
| ClientIP   | The hashed IP address of destination.                   |
| ClientPort | The port number of destination.                                         |
| Domain     | The hashed domain name.                                 |
| SizeSeq    | The sequence of packet sizes (byte) for each packet within the flow.         |
| TimeSeq    | The sequence of relative timestamps (second) for each packet within the flow. |
| UpBytes    | The total number of bytes sent from the source to the destination during the flow.|
| DownBytes  | The total number of bytes received by the source from the destination during the flow. |
| UpPackets  | The total number of packets sent from the source to the destination during the flow. |
| DownPackets| The total number of packets received by the source from the destination during the flow. |
| TcpRtt     | The round-trip time (second) of TCP packets during the three-way handshake. |

## Usage Instructions
In past experiments, using a simple random sampling to split train and test data led to very high accuracy (around 0.99) for some baseline models like Random Forest. However, in real-world scenarios, models face greater challenges, including unknown data and concept drift. To better mimic open-world scenarios, we suggest using the following two data split strategies:

By Service: Here, we used 'ServerIP' and 'ServerPort' as unique identifiers for each service, ensuring the same service wasn’t present in both train and test data. This approach prevents the model from overfitting to specific service characteristics, encouraging it to generalize.

By Date: For example, we used data before “2024-04-25” for training and data after that date for testing. This time-based split introduces more uncertainty, simulating future data patterns and helping the model prepare for real-world shifts.



## Contact

For questions or further assistance, please contact:
- **Research Team**: [warchie560@gmail.com]
