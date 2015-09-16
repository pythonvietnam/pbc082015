import cal


vonglap = 1
choice = 0
while vonglap == 1:
        choice = cal.menu()
        if choice == 1:
                cal.add()
        elif choice == 2:
                cal.sub()
        elif choice == 3:
                cal.mul()
        elif choice == 4:
                cal.div()
        elif choice == 5:
                vonglap = 0

