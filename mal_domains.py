'''


Script to download from several sources and normalize the domain data within.

Script should be run daily for maximum freshness.

This script is intended to be run on a pfSense box for auto-miscreant-punchery.

Authors: timmyburns, t0n1k
Email: timothyfwebster@gmail.com
Version: 0.1a


'''

# To pull the .csv file below we could use the wget Python module. From there it's a matter of parsing the data. Depending on how large the file is we may need to use a database (mongoDB, mysql, libre office) or something along those lines that can clean up the domains in a nice format. The tricky part would be loading it on to the pfsense box. I'm not sure how Squid Proxy handles files so we'll need to verify which file format it prefers. From there we can figure out a way to communicate with Squid Proxy either by remoting into the box or running it as a CRON job. 

http://www.malwaredomainlist.com/mdlcsv.php
