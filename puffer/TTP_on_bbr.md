Google developed a TCP Congestion Control Algorithm (CCA) called TCP Bottleneck Bandwidth and RRT (BBR) that overcomes many of the issues found in both Reno and CUBIC (the default CCAs). This new algorithm not only achieves significant bandwidth improvements, but also lower latency. TCP BBR is already employed with google.com servers, and now you can make it happen--so long as your Linux machine is running kernel 4.9 or newer.

Out of the box, Linux uses Reno and CUBIC. You can test this by issuing the command:

sysctl net.ipv4.tcp_available_congestion_control  
The above command should report  

net.ipv4.tcp_available_congestion_control = cubic reno  
Let's make the change to BBR.  
 
# What you'll need  
The first thing you need to do is make sure your Linux machine is running a supported kernel. Issue the command uname -r. If your kernel is earlier than 4.9, this won't work. You'll have to upgrade your kernel. For instance, out of the box Ubuntu 16.04 runs kernel 4.4. If your server is such that the kernel can be updated, Ubuntu now has a very easy means of updating to a much newer kernel. To do this, open a terminal window and issue the following two commands:  

sudo apt update  
sudo apt install --install-recommends linux-generic-hwe-16.04  
After running the above commands, reboot the server. Once the server is booted, login and issue the uname -r command. You should now see the server running at least kernel 4.13 (as of this writing).  

Now that you have a supporting kernel, let's set BBR as the default congestion control algorithm.

# Setting BBR 
Setting BBR as the default is simple. Open up a terminal window and issue the command  
sudo nano /etc/sysctl.conf  
At the bottom of this file, add the following two lines:  

net.core.default_qdisc=fq  
net.ipv4.tcp_congestion_control=bbr  

Save and close that file.  
Reload sysctl with the command:  
sudo sysctl -p  
Now when you check which congestion control algorithm is in use (with the command sysctl net.ipv4.tcp_congestion_control), you will see output containing bbr.     
# check available congestion control algorithm.  
# sysctl net.ipv4.tcp_available_congestion_control  
net.ipv4.tcp_available_congestion_control = reno cubic bbr lp  
# check tcp congestion control algorithm.  
# sysctl net.ipv4.tcp_congestion_control  
net.ipv4.tcp_congestion_control = bbr  
