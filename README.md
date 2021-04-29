# Host your own DNS server using Technitium DNS
This repo sets up your own DNS server such that people can find your website.

If you want to host your website on your device, the internet must know where to find your website. Computers store website names as numbers (IP-adresses), whereas humans use typed names. So a DNS links the human readable website name and converts it to a number. Sometimes you need to pay someone for a DNS service, other times you need to click in some website to set it up. 

With this repo you only have to add your DNS server in the place where you registered your domain, e.g. namecheap or whatever, and you're done. (I did not yet automate that).

## How
Install conda on your device, or make sure you can run python.
```
curl -sSL https://download.technitium.com/dns/install.sh | sudo bash
conda env create --file environment.yml
conda activate technitium_dns_configuration
python -m src
```
That's it, the code will now ask you to create a password for your Technitium DNS server, what your domain is and automatically configure your dns server.

### starting and stopping technitium DNS
Source: https://blog.technitium.com/2017/11/running-dns-server-on-ubuntu-linux.html
To start the DNS server, one can first stop it with:
```
sudo systemctl stop dns.service
```
The start it again with:
```
cd /etc/dns/
sudo ./start.sh
```
Pay attention to the port that is printed in the terminal, for me it changed from `5380` to `5379` after reboot.

## How to add your DNS server to your domain registrar
This depends on where you rent your domain. An example for namecheap is attached below:
0. Goto (substitute <your domain>)
https://ap.www.namecheap.com/Domains/DomainControlPanel/<your domain >/advancedns
1. Click on "Add nameserver" and click on "Nameserver" then select `ns1` and enter your public ip4 adress.
2. Click on "Add nameserver" and click on "Nameserver" then select `ns2` and enter your public ip4 adress.
3. Goto (substitute <your domain>)
https://ap.www.namecheap.com/Domains/DomainControlPanel/<your domain>/domain/
4. At "nameservers" select: "Custom DNS"
5. Click "add nameserver" and add: `ns1.<your domain>`
5. Click "add nameserver" and add: `ns2.<your domain>`

That's it. (Pictures of this process are included in the folder `Old_manual_instructions` of this repository).
