#!/usr/bin/python

import os

VAULTCMD="/usr/bin/ansible-vault"
os.putenv("ANSIBLE_VAULT_PASSWORD_FILE", "/etc/ansible/autoconfig-jumbo/.vault_pass")

os.system('clear')
print("Welcome to Ansible Vault Encryption utility.")

def addtovault():
   try:
      FILEPATH = raw_input("Please enter file or directory path(e.g. /etc/ansible/template/java-generic)::")
      os.stat(FILEPATH)
   except:
      print "Oops!  That was not a valid path.  Try again..."
   else:
      if os.path.isdir(FILEPATH):
          all_files = sorted([os.path.join(FILEPATH, file) for file in os.listdir(FILEPATH)], key=os.path.getctime)
          for filename in all_files:
              os.system("%s encrypt %s" % (VAULTCMD, filename))
          print "##################################################################################################"
          print "Ansible Vault Encrypted all files under the directory: %s" % (FILEPATH)
          print "##################################################################################################"
      elif os.path.isfile(FILEPATH):
          filename = FILEPATH
          os.system("%s encrypt %s" % (VAULTCMD, filename))
          print "##################################################################################################"
          print "Ansible Vault Encrypted file: %s" % (filename)
          print "##################################################################################################"

def rekeyfiles():
   try:
      FILEPATH = raw_input("Please enter file or directory path(e.g. /etc/ansible/template/java-generic)::")
      os.stat(FILEPATH)
      VAULTPASS_NEWFILE = raw_input("Please enter new vault password file path(e.g. /tmp/.vault_pass)::")
      os.stat(VAULTPASS_NEWFILE)
   except:
      print "Oops!  That was not a valid path.  Try again..."
   else:
      if os.path.isdir(FILEPATH):
          all_files = sorted([os.path.join(FILEPATH, file) for file in os.listdir(FILEPATH)], key=os.path.getctime)
          for filename in all_files:
              os.system("%s rekey %s --new-vault-password-file=%s" % (VAULTCMD, filename, VAULTPASS_NEWFILE))
          print "##################################################################################################"
          print "Ansible Vault Rekey all files under the directory: %s"   %  (FILEPATH)
          print "##################################################################################################"
      elif os.path.isfile(FILEPATH):
          filename = FILEPATH
          os.system("%s rekey %s --new-vault-password-file=%s" % (VAULTCMD, filename, VAULTPASS_NEWFILE))
          print "##################################################################################################"
          print "Ansible Vault Rekey file: %s"   % (filename)
          print "##################################################################################################"

while True:
    opt = raw_input("Do you want to: A) Add Approach new files to ansible vault. B) Approach to rekey vaulted files. Q) Quit [A/B/Q]? : ")
    if opt == "A" or opt == "a":
        print ("You approach to add new files to ansible vault.")
        addtovault()
        break
    elif opt == "B" or opt == "b":
        print ("You approach to rekey encrytped files")
        rekeyfiles()
        break
    elif opt == "Q" or opt == "q":
        break
