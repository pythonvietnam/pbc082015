# hungld
import os
import zipfile
import csv
import demo
vonglap = 1
choice = 0
while vonglap == 1:
        choice = demo.menu()
        if choice == 1:
                demo.demo1()
        elif choice == 2:
                demo.demo2()
        elif choice == 3:
                demo.demo3()
        elif choice == 4:
                vonglap = 0

