from os import system

system('unar ./1.tar.bz2')
for i in range(1, 1001, 1):
  system('unar ./{}/{}.*'.format(i, i+1))
