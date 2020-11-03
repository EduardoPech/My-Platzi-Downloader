#!/usr/bin/python3
import sys, os, re, getpass, io
from subprocess import Popen, PIPE, STDOUT
import time

# GLOBAL VARIABLES
PLATZI_MAIN_URL = "https://platzi.com/clases/"
USER_NAME = input(" -> Ingrese su usuario (correo): ")
PASSWORD = input(" ->Ingrese su contraseña: ")
TOOL_NAME = "youtube-dl"
SLEEP_INTERVAL = 10
MAX_SLEEP_INTERVAL = "15"
FILE_OUTPUT = ""
FILE_LINKS_NAME = input(" -> Nombre del archivo: ")
LINK = ""

course_name = ""
section_name = ""


def get_and_set_course_dir():
    global course_name

    course_name = input("  -> Nombre del curso: ")
    if not os.path.exists(course_name):
        os.mkdir(course_name)
        pass



def get_section_name(str_line):
    return str_line[1:-2]

video_section_count = 1
def set_video_data():
    global video_section_count, LINK, FILE_LINKS_NAME, FILE_OUTPUT, course_name, section_name

    LINK = ""
    with open(FILE_LINKS_NAME, "rt") as courselinks:
        for line in courselinks.readlines():
            if "[" in line:
                video_section_count = 1
                if not os.path.exists(course_name + '/' + get_section_name(line)):
                    os.mkdir(course_name + '/' + get_section_name(line))
                section_name = get_section_name(line)
                continue
            else:
                if "/" in line:
                    LINK = PLATZI_MAIN_URL + line
                    LINK = LINK[:-1]
                    get_video_name(line)
                    FILE_OUTPUT = course_name + '/' + section_name + '/' + FILE_OUTPUT
                    video_section_count += 1
                    if not os.path.exists(FILE_OUTPUT):
                        cli_request(get_cli_commands())
                        while not os.path.exists(FILE_OUTPUT):
                            time.sleep(10)
                    else:
                        print("Skiping: {}".format(FILE_OUTPUT))
                    




def get_video_name(str_line):
    global video_section_count
    global FILE_OUTPUT

    video_name = ""
    back_slash = False
    for char in str_line:
        if back_slash:
            if char.isdigit():
                continue
            else:
                video_name += char
        if not "/" == char:
            continue
        elif "/" == char:
            back_slash = True

    if "-" in video_name[0:1]:
        video_name = video_name.replace("-", "", 1)
    elif "_" in video_name[0:1]:
        video_name = video_name.replace("_", "", 1)

    if "-" or "_" in video_name:
        video_name = video_name.replace("-", " ")
        video_name = video_name.replace("_", " ")

    video_name = str(video_section_count) + ". " + video_name
    video_name = video_name[0:-1] + ".ts"
    FILE_OUTPUT = video_name


def cli_request(command):
    with Popen(command, shell=True, stdout=PIPE, stderr=STDOUT) as process:
        for line in io.TextIOWrapper(process.stdout, newline=''):
            sys.stdout.write(line)
    
def get_cli_commands():
    global LINK, USER_NAME, PASSWORD, FILE_OUTPUT, TOOL_NAME, SLEEP_INTERVAL, MAX_SLEEP_INTERVAL
    sp = " "; qu = '"'
    usr = "--username" + sp + USER_NAME
    pw = "--password" + sp + PASSWORD
    minsl = "--sleep-interval" + sp + str(SLEEP_INTERVAL)
    maxsl = "--max-sleep-interval" + sp + MAX_SLEEP_INTERVAL
    lrate = "--limit-rate" + sp + "1M"
    fo = "-o" + sp + qu + FILE_OUTPUT + qu
    vrb = "--verbose"
    url = qu + LINK + qu
    cli_componets = [TOOL_NAME, usr, pw, fo, url]
    command = sp.join(cli_componets)
    
    return command


get_and_set_course_dir()
set_video_data()
# get_cli_commands()
