Title: Network-wide Advertisement Blocking 
Date: 2017-9-16 13:10
Category: Other

Recently, I setup my own home wifi network with Comcast.. *shudder* However, it initially hasn't been that bad despite their lackluster reputation. I consistently get 75+ Mbps for my plan that costs $35.00 per month, a decent deal for a basic necessity of mine, wireless internet. 

I am a person who has little patience for online advertising. Luckily, I saw this interesting project online about how you can use a rapsberry pi as a DNS server. A DNS server translates human-memorable domain names and hostnames into their corresponding IP addresses. The pi-hole doesn't sit in between your connected devices and the internet, but rather it is a DNS server that blacklists certain domain names, typically ones that host content. As a result, it doesn't allow any content to be retrieved if that hostname is contained within a
certain database of domain names. So, the router goes to the DNS server and says "hey I'm looking for this domain name, what's the IP address?" 

This allows all of the devices on your wireless network to enjoy advertisement-free internet browsing! Here are the steps that I took to get it set up. 

* Download the SD Formatter tool software from SanDisk
* Plug in a 8gb+ microSD card into a computer (you may have to use an adapter to SD depending on your computer) 
* Using SD Formatter tool, select and overwrite the SD card to default settings, then quick format the card
* Download the latest version of NOOBS (New Out Of Box Software) from the [Raspberry Pi Foundation's website](https://www.raspberrypi.org/downloads/noobs/). Unzip the file. 
* Copy the contents of the zip directory to the microSD card that you just formatted. 
* Safely eject the SD card adapter
* Plug in the microSD card into the bottom of the raspberry pi, facing up
* Plug the power cord into raspberry pi, hook up to monitor and keyboard
* Select Raspbian OS (Based on Debian), hit the "i" key, wait for the OS to be installed
* Connect to wifi, then open terminal and copy and paste: curl -sSL https://install.pi-hole.net | bash 
* Select the appropriate wireless/ethernet connection in setup 
* Reserve static IP adress for raspberry pi
* Make sure to modify your router's network settings to use the static IP of the raspberry pi as a static DNS server 
  
Until next time,
#### Clayton Blythe | *Deep Python*
