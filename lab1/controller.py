from model import Model
from view import View

class Controller:

    def __init__ (self, f_name):
        self.file_name = f_name
        self.dbase = Model(f_name)

    def menu(self):
        choice = -1
        while choice != 4:
            View.clear()
            View.menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                self.comp_menu()
                
            elif choice == 2:
                self.hard_menu()
                
            elif choice == 3:
                View.clear()
                print '\tComputers with built-in video adapter:'
                res = self.dbase.find()
                View.display(res)
                print '0)   Back'
                item = -1
                while item < 0 or item > len (res):
                    try:
                        item = int(raw_input('Enter number item:\n'))
                    except ValueError:
                        View.error_message('Incorrect value')
                if item != 0:
                    View.clear()
                    View.display(self.dbase.hard_comp(res[item-1]['id']))
                    raw_input('Press Enter to continue...')
                
            elif choice == 4:
                self.dbase.save(self.file_name)
        View.clear()

    def comp_menu (self):
        choice = -1
        while choice != 5:
            View.clear()
            View.comp_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                View.clear()
                View.display(self.dbase.get_comp())
                print '0)   Back'
                item = -1
                while item < 0 or item > len (self.dbase.get_comp()):
                    try:
                        item = int(raw_input('Enter number item:\n'))
                    except ValueError:
                        View.error_message('Incorrect value')
                if item != 0:
                     id = self.dbase.get_comp()
                     id = id[item-1]['id']
                     View.clear()
                     View.display(self.dbase.hard_comp(id))
                     raw_input('Press Enter to continue...')
                    
            elif choice == 2:
                View.clear()
                name = raw_input('Enter name:\n')
                series = raw_input('Enter series:\n')
                pc_type = raw_input('Enter pc_type:\n')
                self.dbase.add_comp(name, series, pc_type)
                
            elif choice == 3 or choice == 4:
                View.clear()
                View.display(self.dbase.get_comp())
                print '0) Back'
                item = -1
                while item != 0:
                    try:
                        item = int(raw_input('\nEnter number item:\n'))
                    except ValueError:
                        View.error_message('Incorrect value')

                    if item > 0 and item <= len(self.dbase.get_comp()):
                        id = self.dbase.get_comp()
                        id = id[item-1]['id']
                        if choice == 3:
                            self.dbase.del_comp(id)
                            View.success_message('Item deleted!')
                        else:
                            key = raw_input('\nEnter title attr:\n')
                            while not (key in ['name', 'series', 'pc_type']):
                                View.error_message('Incorrect key attr')
                                key = raw_input('\nEnter title attr:\n')
                            val = raw_input('Enter value attr:\n')
                            self.dbase.update_comp(id, key, val)
                            View.success_message('Item update!')
                        item = 0

                        
    def hard_menu (self):                               
        choice = -1
        while choice != 5:
            View.clear()
            View.hard_menu()
            try:
                choice = int(raw_input('Enter menu item:\n'))
            except ValueError:
                View.error_message('Incorrect value')

            if choice == 1:
                View.clear()
                View.display(self.dbase.get_hard())
                raw_input('Press Enter to continue...')
                
            elif choice == 2:
                View.clear()
                View.display(self.dbase.get_comp())
                print '0)   Back'
                item = -1
                while item <0 or item > len(self.dbase.get_comp()):
                    if item == 0:
                        break
                    try:
                        item = int(raw_input('\nEnter number item:\n'))
                    except ValueError:
                        View.error_message('Incorrect value')
                if item != 0:    
                    id = self.dbase.get_comp()
                    id = id[item-1]['id']
                    hdd = raw_input('Enter hdd:\n')
                    video_adapter = raw_input('Enter video_adapter (default None):\n')
                    memory_module = raw_input('Enter memory_module:\n')
                    if video_adapter =='':
                        video_adapter = None;
                    self.dbase.add_hard(id, hdd, video_adapter, memory_module)
                
            elif choice == 3 or choice == 4:
                View.clear()
                View.display(self.dbase.get_hard())
                print '0)   Back'
                item = -1
                while item != 0:
                    try:
                        item = int(raw_input('\nEnter number item:\n'))
                    except ValueError:
                        View.error_message('Incorrect value')

                    if item > 0 and item <= len(self.dbase.get_hard()):
                        id = self.dbase.get_hard()
                        id = id[item-1]['id']
                        if choice == 3:
                            self.dbase.del_hard(id)
                            View.success_message('Item deleted!')
                        else:
                            key = raw_input('\nEnter title attr:\n')
                            while not (key in ['hdd', 'memory_module', 'video_adapter']):
                                View.error_message('Incorrect key attr')
                                key = raw_input('\nEnter title attr:\n')
                            val = raw_input('Enter value attr:\n')
                            self.dbase.update_hard(id, key, val)
                            View.success_message('Item update!')
                        item = 0
