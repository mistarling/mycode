#!/usr/bin/env python3

import shutil
import os

def main():
    #set dir
    os.chdir("/Users/mstarling/Documents/repos/mycode")

    #copy file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    
    #copy tree
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()