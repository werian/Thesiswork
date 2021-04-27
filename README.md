# Thesiswork
 code for thesis "Verkkojen Ohjelmoitavuus"

 how to use:

 Have latest python version installed.

 Have virtual machine or Cisco router with Cisco IOS-XE, I used virtual machine with csr1000 image on it.

Verify that you have enabled ssh on your router, also have enabled RESTCONF API on it.

Have your virtual machine or router running before running the code.

To run the code navigate to the folder of the code, have the txt files within that folder also. Type python, then the name of the program.py, then --count, after which you can give number of your machines.
Example "python test.py --count 1" this will configure one router.

Make sure your device_list.txt contains ip addresses of your devices. Also the hostname.txt is configurable to your taste.


