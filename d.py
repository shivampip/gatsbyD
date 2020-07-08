import logging as log
import requests
from pprint import pprint
from subprocess import Popen, PIPE
from os import path
from fabric import Connection
import sys
sys.path.append("first/")
# from c import DEVELOPEMENT

# if(DEVELOPEMENT):
# else:
#     from monitor import log

##### Remote ############################################


def connect_vps(ip="153.92.4.175", port=22, user="root", password="ramayanahs*1A"):
    return Connection(ip, port=port, user=user, connect_kwargs={"password": password})


def rexe(con, cmd):
    try:
        #log.info("remote$ {}".format(cmd))
        out = con.run(cmd)
        return out.stdout.strip()
    except Exception as e:
        print("Error aa gyi")
        return "Error: {}".format(e)


def rpull(con, repo_loc):
    with con.cd(repo_loc):
        log.info("Pulling Changes")
        rexe(con, "git fetch --all")
        rexe(con, "git reset --hard origin/master")
        rexe(con, "git pull origin master")
        log.info("Removing local changes")
        rexe(con, "git clean -f")
        rexe(con, "git status")


def rtrain(con, repo_loc):
    with con.cd(repo_loc):
        log.info("Traing Model")
        rexe(con, "rasa train")
        con.close()


def rstop_rasa(con):
    for i in range(2):
        try:
            rexe(con, "pkill rasa")
            log.info("Killed rasa process")
        except Exception as e:
            log.info("Already killed")


def rrun(con, repo_loc, cmd):
    with con.cd(repo_loc):
        rexe(con, cmd)


def show_memory_usage(con):
    with con.cd("p/pra"):
        rexe(con, "python3 ps_mem.py")

##### Local ############################################

# def lexe(con, cmd):
#    out= con.local(cmd)
#    return out.stdout.strip()


def lexe(cmd):
    cmds = cmd.split()
    out, error = Popen(cmds, stdout=PIPE, stderr=PIPE).communicate()
    print(out.decode("utf-8"), end="")
    print(error.decode("utf-8"))


def lpush():
    log.info("Adding Files to Git")
    lexe("git add .")
    log.info("Commnting Changes")
    lexe('git commit -m "updated"')
    log.info("Pushing Changes")
    lexe("git push origin master")
    lexe("git push origin master")

#######################################


SHUTDOWN_URL = "http://upload.shivampip.com/shutdown"


def rshutdown_flask():
    result = requests.get(url=SHUTDOWN_URL)
    try:
        data = result.json()
        log.info(data['description'])
    except Exception:
        log.info("Server is already shutdown")


# http://upload.shivampip.com/shutdown
#######################################

def open_shell(con):
    path = None
    while(True):
        cmd = input("$ ")
        if(cmd.startswith("cd")):
            path = cmd[3:]
            continue
        if(path):
            with con.cd(path):
                rexe(con, cmd)
        else:
            rexe(con, cmd)


if(__name__ == "__main__"):
    con = connect_vps()

    lpush()
    rpull(con, "/var/www/gatsbyD")
    rrun(con, '/var/www/gatsbyD/first', 'gatsby build')
    # rstop_rasa(con)
    # rshutdown_flask()
    #rtrain(con, "p/pro/iii/bot")
    #rrun(con, "p/pro/iii/bot")
    #run(con, "p/pro/iii/bot")
    # open_shell(con)
    # show_memory_usage(con)
    con.close()


# https://www.zabbix.com/
