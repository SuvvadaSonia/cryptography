""" 
Ubuntu Agent POC 

It connects to windows machine using WinRm
and executes installer & uninstaller scripts

-----------------------
Author: Suvvada Sonia - Jr. Software Engineer - sonia.s@tessrac.com
CopyRights - Tessrac Innovations Pvt Ltd.

"""

from winrm import Session  # WinRM allows you to perform various management tasks remotely.


class UbuntuAgent:
    
    def __init__(self, target:str, auth:tuple) -> None:
        try:
            _user, _pwd = auth

            self.__conn = Session(target, auth=(_user, _pwd))
        except (OSError, ConnectionError) as e:
            print(e)

    def getConfig(self):
        try:
            result = self.__conn.run_cmd('ipconfig', ['/all'])
            return result.std_out

        except (OSError, ConnectionError) as e:
            print(e)


if __name__ == "__main__":
    IP = '192.168.1.105'
    HOSTNAME = 'Administrator'
    PWD = 'India@123'
    r = UbuntuAgent(IP, (HOSTNAME, PWD)).getConfig()

    print(r)
