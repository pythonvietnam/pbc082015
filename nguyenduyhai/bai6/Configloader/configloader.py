#Configloader.py
#haind
#python


def config_parse(configfile):

    D = {}
    config_file = open(configfile,'r')
    for line in config_file:
        line = line.strip()
        if line.startswith('#') or line == '':
            pass
        else:
            line = line.split('=')

    return D

def main(configfile = 'D:\Learning\config.cfg'):
    
    D = config_parse(configfile)
    
    for key in config_parse(configfile):
        if key == 'database':
            print "Database name is: ", D[key]
        elif key == 'user':
            print "User name is: ", D[key]
        elif key == 'password':
            print "Password is: ", D[key]
            
if __name__ == '__main__':
    main()