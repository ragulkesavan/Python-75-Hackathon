import logging

#creation of log and
logging.basicConfig(filename="logdetails.log",format='%(asctime)s-%(message)s')


#to record the admin log in with date and time
logging.basicConfig(format='%(asctime)s-%(message)s',level=logging.INFO)
logging.info('Root login occurs')

#day month year hour minute second with log out message
logging.basicConfig(format='%(asctime)s-%(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('root logged out')

#there are many logging levels
#logging takes place only above info level
#obj creation:
logs=logging.getLogger() 
  
#Setting the threshold to DEBUG 
logs.setLevel(logging.DEBUG) 

logs.debug("Debug message")  
logs.info("Info message")
logs.warning("Warning message")
logs.error("Error message")
logs.critical("Critical message")
  
#Making to log debug messages also
logs.getLogger().setLevel(logging.DEBUG)
logs.debug("Debug message")



f=open("logdetails.log","r")
print(f.read())
f.close()
