import os

class View:

    @staticmethod
    def menu():
        print 'Menu:\n1. Computers menu\n2. Hardware menu\n3. Function search\n4. Exit'
    
    @staticmethod
    def comp_menu():
        print 'Computers menu:'
        print '1. Display\n2. Add\n3. Delete\n4. Update\n5. Back'

    @staticmethod
    def hard_menu():
        print 'Hardware menu:'
        print '1. Display\n2. Add\n3. Delete\n4. Update\n5. Back'

    @staticmethod
    def error_message(message):
        print 'ERROR: ' + message + '\n'

    @staticmethod
    def success_message(message):
        print message + '\n'

    @staticmethod
    def clear():
        return
        #os.system('clear')

    @staticmethod
    def display(lst):
        i = 0
        for x in lst:
            i += 1
            print  '%d) ' %i,
            for key in x:
                if key != 'id' and key != 'id_comp':
                    print "%+10s: %-15s" %(key, x[key]),
            print
            
