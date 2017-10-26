print("Starting...")
print("Enter the domain name:")
name=raw_input()
f=open('/scratch/u01/Middleware/Oracle_Home/domain-registry.xml','r');
path1='location="'
path3='"/>'
for line in f:
        line=line.split()
        path2=("/scratch/u01/Middleware/Oracle_Home/user_projects/domains/%s"%name)
        path=path1+path2+path3
	if path in line:
                print("---Domain already exist....")
                exit()
newpath=("/scratch/u01/Middleware/Oracle_Home/user_projects/domains/%s"%name) 
os.makedirs(newpath)
print("......executing....")
# Read the template to use for creating the domain
readTemplate('/scratch/u01/Middleware/Oracle_Home/wlserver/common/templates/wls/wls.jar')

# Set the listen address and listen port for the Administration Server
cd('Servers/AdminServer')
set('ListenAddress','')
set('ListenPort', 7001)

# Enable SSL on the Administration Server and set the SSL listen address and
# port
create('AdminServer','SSL')
cd('SSL/AdminServer')
set('Enabled', 'True')
set('ListenPort', 7002)
print("Setting the password of the domain:...please wait......")
# Set the domain password for the WebLogic Server administration user
cd('/')
path_user=('Security/base_domain/User/weblogic')
cd(path_user)
cmo.setPassword('weblogic1')

# If the domain already exists, overwrite the domain
setOption('OverwriteDomain', 'false')

# write the domain and close the template
writeDomain('/scratch/u01/Middleware/Oracle_Home/user_projects/domains/%s'%name)
closeTemplate()
print("Successfully completed...Domain has been created.....")
exit()