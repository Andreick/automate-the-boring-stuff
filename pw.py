#! python3
#pw.py - An insecure password locker program.

import sys, pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    sys.exit('Usage: python pw.py [account] - copy account password')

account = sys.argv[1] #First command line arg is the account name.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for %s copied to clipboard.' %(account))

else:
    print('There is no account named', account)
