# Repo admintest
Repo for Performio Admin Test

EXERCISE 1)	get_temp.py  -- Python Script
	
This is a Python script for getting the temperature/time values for the indicated cities. This can be easily expanded to include new cites by simply 
updating the citydata structure. 

Running the script we get the following output:
	$ get_temp.py

	Current Temp in Newport Beach, CA. USA is  60.25 degrees Farenheit at  2020-03-04 09:30:59 PST

	Current Temp in Melbourne, AUS is  17.44 degrees Celsius at  2020-03-05 04:31:00 AEDT 

Future improvements . . . auto adjustment for DST.

         -------------------------------------------------------------------------

EXERCISE 2) 	getOptionGroupName.sh -- bash one-liner
				dat.json -- copy of sample JSON

Extract the OptionGrouName parameter value from the JSON file.

Running the script executes the line below and produces the following output:
	$ getOptionGroupName.sh (or execute the line below at the shell prompt.)

	$ grep OptionGroupName dat.json | awk '{print $2}' | sed 's/"//g' | sed 's/,//g'
	default:mysql-5-6

Discussion: Since there is only one reference to OptionGroupName, we can use grep to return the line containing the value. Next we just filter out any
potential JSON field separators (commas) and quotes.

         -------------------------------------------------------------------------
		 
EXERCISE 3)  httpd.conf   		-- Apache Config File,
			 htpasswd.admin   	-- Apache password file for /Admin directory

Create a nginx or apache web server configuration file that performs the following.

- Hosts web traffic for a website with the domain of example.com
- Serves website data from /var/www/
- Elevates http traffic to https traffic

	See <VirtualHost> and <Dorictory> definitions at bottom of http.conf
	
			<Directory "/var/www">
				AllowOverride All
				# Allow open access:
				Require all granted
			</Directory>

			<VirtualHost *:80>
				ServerName www.example.com
				ServerAlias example.com *.example.com
				DocumentRoot /var/www
				Redirect permanent / https://www.example.com/
			</VirtualHost>


- Has a htaccess challenge when the /admin endpoint is requested

	We create an .htaccess file in the /var/www/admin directory containing:
		AuthType Basic
		AuthName "Restricted access"
		AuthUserFile /etc/httpd/conf/.htpasswd
		require valid-user

	Additionally, we need to tell the apache server to enable reading of .htaccess files by setting "AllowOverride All" in the <Directory> block 
	of the httpd.conf file.

	This will prompt for a password when the /var/www/admin directory is accessed. It will read the .htpasswd file in the /etc/httpd/conf directory 
	for the correct password.

	The .htpasswd file is created with "htpasswd -c .htpasswd.admin admin1".

	Any additional users/passwords can be added the same way with "htpasswd .htpasswd admin2", for example. Each directory that needs to be protected in this way can have its own
	.htaccess file pointing to its own .htpasswd file for access.

         -------------------------------------------------------------------------
		 
EXERCISE 4)  AWS_Diagram.pdf

This is a drawing of both the existing and improved versions. I added CloudFront, CloudShield, a WAF, a VPN, and isolated the connections internally
to only allow traffic between the EC2 instance and the RDS instance.
 

	