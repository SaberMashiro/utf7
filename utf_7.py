#coding:utf-8
from imapclient import imap_utf7
s = 'AGI-d+AGMAdA-f+AHsAQABiAGw-ue+AEA-d+AG8-n+AEA-edu+AEAAfQ-'
s = s.split('+')
s = ['&'+i for i in s]
decoded = ''
for i in (imap_utf7.decode(i) for i in s):
    decoded += ''.join(i)
print decoded
