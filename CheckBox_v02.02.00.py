#  ________/\\\\\\\\\__/\\\_____________________________________________________/\\\\\\\\\\\\\_________________________________________________        
# / _____/\\\////////__\/\\\_______________________________________/\\\_________\/\\\/////////\\\_______________________________________________       
#  / ___/\\\/___________\/\\\______________________________________\/\\\_________\/\\\_______\/\\\_______________________________________________      
#   / __/\\\_____________\/\\\_____________/\\\\\\\\______/\\\\\\\\_\/\\\\\\\\____\/\\\\\\\\\\\\\\______/\\\\\_____/\\\____/\\\___________________     
#    / _\/\\\_____________\/\\\\\\\\\\____/\\\/////\\\___/\\\//////__\/\\\////\\\__\/\\\/////////\\\___/\\\///\\\__\///\\\/\\\/____________________    
#     / _\//\\\____________\/\\\/////\\\__/\\\\\\\\\\\___/\\\_________\/\\\\\\\\/___\/\\\_______\/\\\__/\\\__\//\\\___\///\\\/______________________   
#      / __\///\\\__________\/\\\___\/\\\_\//\\///////___\//\\\________\/\\\///\\\___\/\\\_______\/\\\_\//\\\__/\\\_____/\\\/\\\_____________________  
#       / ____\////\\\\\\\\\_\/\\\___\/\\\__\//\\\\\\\\\\__\///\\\\\\\\_\/\\\_\///\\\_\/\\\\\\\\\\\\\/___\///\\\\\/____/\\\/\///\\\___________________ 
#        / _______\/////////__\///____\///____\//////////_____\////////__\///____\///__\/////////////_______\/////_____\///____\///____________________
#         / ____/\\\\\_____/\\\____________________________________/\\\\\\______________________________________________________________________________
#          / ___\/\\\\\\___\/\\\___________________________________\////\\\______________________________________________________________________________
#           / ___\/\\\/\\\__\/\\\__/\\\___/\\\\\\\\____________________\/\\\______________________________________________________________________________
#            / ___\/\\\//\\\_\/\\\_\///___/\\\////\\\_____/\\\\\\\\_____\/\\\______________________________________________________________________________
#             / ___\/\\\\//\\\\/\\\__/\\\_\//\\\\\\\\\___/\\\/////\\\____\/\\\______________________________________________________________________________
#              / ___\/\\\_\//\\\/\\\_\/\\\__\///////\\\__/\\\\\\\\\\\_____\/\\\______________________________________________________________________________
#               / ___\/\\\__\//\\\\\\_\/\\\__/\\_____\\\_\//\\///////______\/\\\______________________________________________________________________________
#                / ___\/\\\___\//\\\\\_\/\\\_\//\\\\\\\\___\//\\\\\\\\\\__/\\\\\\\\\___________________________________________________________________________
#                 / ___\///_____\/////__\///___\////////_____\//////////__\/////////____________________________________________________________________________
#                  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# _____________________________________________________________________________________________________________________________________________________________

#   Initial version was built in July 2016                                       #
#                                                                                #
#   Version Number Defination:                                                   #
#   v01.01.01 201706xx                                                           #
#    -- -- --                                                                    #
#     |  |  |                                                                    #
#     |  |  +------     GUI Updates                                              #
#     |  +---------     Crypto Function Updates                                  #
#     +------------     Published Version (Major Change)                         #
#                                                                                #
# _______________________________________________________________________________#

#   01. v01.01.01 date was not recorded precisely.
#   02. v01.01.01 to v01.01.03 was not recorded precisely.
#   03. v02.00.00 was being upgraded from python2 to python3 languagese on 20230917
#   04. v02.02.00 final released on 20230919
#   05. v02.02.01 Single DES Enc has been fixed.
# ________________________________________________________________________________#

from datetime import date
from tkinter import *
from tkinter import messagebox, filedialog, messagebox, ttk
from Crypto.Cipher import DES, DES3, AES
from binascii import *
from os.path import join
# from tkMessageBox import *
# from ttk import Progressbar

import os, shutil, string, time, tkinter.filedialog
# import Tkinter as tk
# import ttk


root = Tk()
ChkB_ver = "02.02.00"
ChkB_yr = "2023.09.19"
root.title('CheckBox' + " (v" + ChkB_ver +")")
root.geometry("450x396+600+300")    #("560x480+0+0") for Linux; ("530+470+20+20") for Windows
root.minsize(450, 396)
root.maxsize(450, 396)
tab_lv_1 = ttk.Notebook(root)
tag_checking = ttk.Frame(tab_lv_1)
tag_algo = ttk.Frame(tab_lv_1)

tab_lv_1.add(tag_checking, text='*.otr\nchecking')
tab_lv_1.add(tag_algo, text='Algo\nselection')
tab_lv_1.pack()



exit_button = Button(root, text = "Exit", width = 8, bg='#FF5C5C', command = quit)
exit_button.pack(side=RIGHT, padx=5, pady=5)
exit_button.place(x=370, y=360)


algo_selection = IntVar()
mode_selection = IntVar()
total = IntVar()
default_path = StringVar(tag_checking, value = "") 
default_key = StringVar(tag_checking, value = "0123456789ABCDEF123456789ABCDEF0")
default_begin = StringVar(tag_checking, value = "1")
default_end = StringVar(tag_checking, value = "200000") # it should be "200000"
MODE_KEY_SELECTOR = IntVar()


#   need to change the path on different DPA projects
#default_path = StringVar(tag_checking, value = "C:\\\Python27\\\Captures")


class CheckBox(Tk):
    #   GUI interface definition
    print("\n\n===================================")
    print("|--  Welcome to use CheckBox    --|")
    print("|--                             --|")
    print("|-- Author  : nigel.zhai@ul.com --|")
    print("|-- Version :", ChkB_ver, "         --|")
    print("|-- Date    :", ChkB_yr, "       --|")
    print("===================================\n\n")

    #   GUI interface definition - recalculate and rename the traces
    def srename(self, oldname):

        # keysel_flag = MODE_KEY_SELECTOR.get()

        #time.sleep(0.01)
        print ("\nPOI calculation:")
        print (oldname)
        exe_algo = algo_selection.get()
        exe_mode = mode_selection.get()

        ########################################################
        #   ====================================================
        #   Single DES operation
        if exe_algo == 1:	# DES operation
            keysel_flag = MODE_KEY_SELECTOR.get()
            #	there is no mode to be selected in DES operation
            log_time_temp = time.strftime("%Y/%m/%d  %H:%M:%S")
            #realtime.configure(text=log_time_temp)
            arr=oldname.split('-')
                #   arr[0]  The number of traces
                #   arr[1]  The Channel of the CRO
                #   arr[2]  Plaintext value
                #   arr[3]  Ciphertext value
                #   arr[4]  Encryption/Decryption key value
                #   arr[5]  F/R - Fixed or Random value as the input
            plaintext= arr[2]
            # int_or_ext_key = MODE_KEY_SELECTOR.get()
            h_plaintext = bytes.fromhex(plaintext.replace(' ', ''))
            test_value = arr[4]
            # print("len of h_plaintext:")
            # print(len(h_plaintext))
            # print("plaintext:")
            # print(plaintext)
            # print("test_value (key):")
            # print(test_value, "\n\n")

            if keysel_flag == 1:    # defulat key is selected
                key = self.key_tx.get()
                if len(key)//2 != 8:
                    print("DES key length is incorrect.")
                # print("\n\n---> Check point:")
                # print("otr file key is selected:")
                # print(key)

            elif keysel_flag ==2:    # otr file key is selected
                key = arr[4]
                # print("\n\n---> Check point:")
                # print("default key is selected:")
                # print(key)
            else:
                pass

            h_key = bytes.fromhex(key.replace(' ', ''))
            # h_plaintext = plaintext.replace(' ', '').decode('hex')

            mode  = mode_selection.get()    # ECB:1, CBC:2, CFB:3, xxx:4, OFB:5, CTR:6
            if mode == 1:
                mode = DES.MODE_ECB
            elif mode == 2:
                mode = DES.MODE_CBC
            elif mode == 3:
                mode = DES.MODE_CFB
            elif mode == 4:
                mode = DES.MODE_OFB
            elif mode == 5:
                mode = DES.MODE_CTR
            else:
                pass

            if len(h_plaintext) == 8:
                obj = DES.new(h_key, DES.MODE_ECB)
                output_raw = obj.encrypt(h_plaintext)
                h_out_data = output_raw.hex().upper()
                print("h_out_data")
                print(h_out_data)
            elif len(h_plaintext) == 16 or len(h_plaintext) == 32:
                if mode == DES.MODE_ECB:
                    obj = DES3.new(h_key, mode)
                else:
                    obj = DES3.new(h_key, mode, h_iv)
                output_raw = obj.encrypt(h_plaintext)
                # h_out_data = output_raw.encode('hex')
                h_out_data = output_raw.hex().upper()
                # print("\n\n---> Check point:")
                # print("h_out_data")
                # print(h_out_data)
            else:
                pass

            # obj = DES.new(h_key, mode, h_iv)
            # output_raw = obj.encrypt(h_plaintext)
            # h_out_data = output_raw.encode('hex')
            
            if h_out_data.upper() != arr[3].upper():
                newname= arr[0]+'-'+arr[1]+'-'+arr[2]+'-'+h_out_data.upper()+'-'+arr[4]+'-'+arr[5];
                with open("CheckBox.log", "a+") as renaming:
                    renaming.write(log_time_temp + '\n')
                    renaming.write(oldname + '\n')
                    renaming.write(newname + '\n\n\n')

                #print "\n>>>>>   There is a WRONG trace !   <<<<<"
                print("The WRONG trace    :", oldname,            "<<<<< Wrong one !")
                print("It should be       :", newname+'-'+arr[5], "<<<<< Corrected !")
                print("time               :", log_time_temp)
                src = join(check_path, oldname)
                dst = join(archive, oldname)
                print("src:", src)
                print("dst:", dst)
                # shutil.move(src, dst)
            newname= arr[0]+'-'+arr[1]+'-'+arr[2]+'-'+h_out_data.upper()+'-'+arr[4]+'-'+arr[5];
            print("CheckBox result:")
            print (newname)
            print("[DES operation]")
            return newname

        ########################################################
        #   ====================================================
        #   Triple DES operation
        elif exe_algo == 2:	# TDES operation
            keysel_flag = MODE_KEY_SELECTOR.get()
            # print("\n\n---> Check point:")
            # print("keysel_flag:")
            # print(keysel_flag)
                #	there should be 4 modes to be selected
            log_time_temp = time.strftime("%Y/%m/%d  %H:%M:%S")
            #realtime.configure(text=log_time_temp)
            arr=oldname.split('-')
                #   arr[0]  The number of traces
                #   arr[1]  The Channel of the CRO
                #   arr[2]  Plaintext value
                #   arr[3]  Ciphertext value
                #   arr[4]  Encryption/Decryption key value
                #   arr[5]  F/R - Fixed or Random value as the input
            plaintext = arr[2]
            # h_plaintext = plaintext.replace(' ', '').decode('hex')
            h_plaintext = bytes.fromhex(plaintext.replace(' ', ''))
            test_value = arr[4]
            # print("len of h_plaintext:")
            # print(len(h_plaintext))
            # print("plaintext:")
            # print(plaintext)
            # print("test_value (key):")
            # print(test_value, "\n\n")

            if keysel_flag == 1:    # defulat key is selected
                key = self.key_tx.get()
                # print("\n\n---> Check point:")
                # print("otr file key is selected:")
                # print(key)
            elif keysel_flag ==2:    # otr file key is selected
                key = arr[4]
                # print("\n\n---> Check point:")
                # print("default key is selected:")
                # print(key)
            else:
                pass
            
            h_key = bytes.fromhex(key.replace(' ', ''))
            iv_raw = "0000000000000000"
            h_iv = bytes.fromhex(iv_raw.replace(' ', ''))
            
            mode  = mode_selection.get()    # ECB:1, CBC:2, CFB:3, xxx:4, OFB:5, CTR:6
            if mode == 1:
                mode = DES.MODE_ECB
            elif mode == 2:
                mode = DES.MODE_CBC
            elif mode == 3:
                mode = DES.MODE_CFB
            elif mode == 4:
                mode = DES.MODE_OFB
            elif mode == 5:
                mode = DES.MODE_CTR
            else:
                pass

            # print("\n\n---> Check point:")
            # print("exe_algo")
            # print(exe_algo)
            # print("mode")
            # print(mode)
            if len(h_plaintext)==8:
                obj = DES3.new(h_key, mode)
                output_raw = obj.encrypt(h_plaintext)
                h_out_data = output_raw.encode('hex')
                # print("h_out_data")
                # print(h_out_data)
            elif len(h_plaintext)==16 or len(h_plaintext)==32:
                if mode == DES.MODE_ECB:
                    obj = DES3.new(h_key, mode)
                else:
                    obj = DES3.new(h_key, mode, h_iv)
                output_raw = obj.encrypt(h_plaintext)
                # h_out_data = output_raw.encode('hex')
                h_out_data = output_raw.hex().upper()
                # print("h_out_data")
                # print(h_out_data)
            else:
                pass

            if h_out_data.upper() != arr[3].upper():
                #time.sleep(0.1)
                newname= arr[0]+'-'+arr[1]+'-'+arr[2]+'-'+h_out_data.upper()+'-'+arr[4]+'-'+arr[5];
                with open("CheckBox.log", "a+") as renaming:
                    renaming.write(log_time_temp + '\n')                    
                    renaming.write(oldname + '\n')
                    renaming.write(newname + '\n\n\n')
                #print "\n>>>>>   There is a WRONG trace !   <<<<<"
                print("The WRONG trace    :", oldname,            "<<<<< Wrong one !")
                print("It should be       :", newname+'-'+arr[5], "<<<<< Corrected !")
                print("time               :", log_time_temp)
                src = join(check_path, oldname)
                dst = join(archive, oldname)
                print("src:", src)
                print("dst:", dst)
                # shutil.move(src, dst)
            newname= arr[0]+'-'+arr[1]+'-'+arr[2]+'-'+h_out_data.upper()+'-'+arr[4]+'-'+arr[5];
            print("CheckBox result:")
            print (newname)
            print("[TDES operation]")
            return newname

        ########################################################
        #   ====================================================
        #   AES operation
        elif exe_algo == 3:	# AES operation
            keysel_flag = MODE_KEY_SELECTOR.get()
            #	there should be 4 modes to be selected
            log_time_temp = time.strftime("%Y/%m/%d  %H:%M:%S")
            arr=oldname.split('-')
                #   arr[0]  The number of traces
                #   arr[1]  The Channel of the CRO
                #   arr[2]  Plaintext value
                #   arr[3]  Ciphertext value
                #   arr[4]  Encryption/Decryption key value
            plaintext= arr[2]
            # h_plaintext = plaintext.replace(' ', '').decode('hex')
            h_plaintext = bytes.fromhex(plaintext.replace(' ', ''))
            test_value = arr[4]
            # print("len of h_plaintext:")
            # print(len(h_plaintext))
            # print("plaintext:")
            # print(plaintext)
            # print("test_value (key):")
            # print(test_value, "\n\n")

            if keysel_flag == 1:
                key = self.key_tx.get()
            elif keysel_flag == 2:
                key = arr[4]
            else:
                pass

            h_key = bytes.fromhex(key.replace(' ', ''))
            iv_raw = "00000000000000000000000000000000"
            h_iv = bytes.fromhex(iv_raw.replace(' ', ''))

            mode  = mode_selection.get()    # ECB:1, CBC:2, CFB:3, xxx:4, OFB:5, CTR:6
            if mode == 1:
                mode = DES.MODE_ECB
            elif mode == 2:
                mode = DES.MODE_CBC
            elif mode == 3:
                mode = DES.MODE_CFB
            elif mode == 4:
                mode = DES.MODE_OFB
            elif mode == 5:
                mode = DES.MODE_CTR
            else:
                pass

            if len(h_plaintext)==16:
                obj = AES.new(h_key, mode)
                output_raw = obj.encrypt(h_plaintext)
                h_out_data = output_raw.hex().upper()
                print("h_out_data")
                print(h_out_data)
            elif len(h_plaintext)==32:
                obj = AES.new(h_key, mode, h_iv)
                output_raw = obj.encrypt(h_plaintext)
                # h_out_data = output_raw.encode('hex')
                h_out_data = output_raw.hex().upper()
                print("\n\n---> Check point:")
                print("h_out_data")
                print(h_out_data)
            else:
                pass

            if h_out_data.upper() != arr[3].upper():
                newname= arr[0]+'-'+arr[1]+'-'+arr[2]+'-'+h_out_data.upper()+'-'+arr[4]+'-'+arr[5];
                with open("CheckBox.log", "a+") as renaming:
                    renaming.write(log_time_temp + '\n')
                    renaming.write(oldname + '\n')
                    renaming.write(newname + '\n\n\n')
                #print "\n>>>>>   There is a WRONG trace !   <<<<<"
                print("The WRONG trace    :", oldname,            "<<<<< Wrong one !")
                print("It should be       :", newname+'-'+arr[5], "<<<<< Corrected !")
                print("time               :", log_time_temp)
                src = join(check_path, oldname)
                dst = join(archive, oldname)
                print("src:", src)
                print("dst:", dst)
                # shutil.move(src, dst)
            newname= arr[0]+'-'+arr[1]+'-'+arr[2]+'-'+h_out_data.upper()+'-'+arr[4]+'-'+arr[5];
            print("CheckBox result:")
            print(newname)
            print("[AES operation]")
            return newname

            ########################################################


    def listfiles(self, dirs, startnum, endnum):
        retlist = [];
        files = os.listdir(dirs);
        for target in files:
            if target.endswith(".otr"):
                nums = int(target.split('-')[0]);
                if nums > startnum-1 and nums < endnum+1:
                    retlist.append(target)
        return retlist



    #   find out the incorrect traces ONLY. Write them into the CheckBox.log file
    def execution_check_des_tdes_aes(self, val=1):
        # print "reserved!"
        print("\n\n")
        print("========================================================================")
        print("================================  Start  ===============================")
        get_path_msgBox = self.path_conf_tx.get(1.0, END)
        sorted_path = ''.join(get_path_msgBox.splitlines())
        dirs =  sorted_path
        rt = self.listfiles(dirs, int(self.begin_tx.get()), int(self.end_tx.get()))
        
        print("Traces directory   :", dirs)
        index = 1
        for tg in rt:
            newname = self.srename(tg)  # -> jump to srename() func
            index = int(newname.split('-')[0])
            self.var_det.set(int(index*100/int(self.end_tx.get())))
            self.set( self.var_det.get() )
            self.update_labels()
            root.update_idletasks() # very important function to update GUI
        print("\n\n")
        print("========================================================================")
        print("==========  Results have be recorded in the 'CheckBox.log' file  =======")
        print("==========         Thanks for using UL_CheckBox program          =======")

    def execution_move_des_tdes_aes(self, val=1):
        print ("reserved!")


    #   add-on function - 20108/08/13 - move the incorrect traces to archive folder:
    def execution_rename_des_tdes_aes(self, val=1):
        
        if tkMessageBox.askyesno("Warning!", "Are you sure to rename the incorrect *.otr file(s)?"):
            time.sleep(0.5)
            if tkMessageBox.askyesno("Warning!", "Have you reported your behaviour to your team leader??"):
                time.sleep(0.5)
                if tkMessageBox.showinfo("Warning!", "I am watching you!!!!"):
                    time.sleep(0.5)
                    if tkMessageBox.askyesno("Warning!", "This is the last chance!!! \nAre you going to change the captured *.otr name(s)?????"):

                        get_path_msgBox = self.path_conf_tx.get()
                        # dirs =  check_path
                        dirs =  get_path_msgBox
                        # dirs =  check_path
                        start = int(self.begin_tx.get())
                        end   = int(self.end_tx.get())
                        rt = self.listfiles(dirs, start, end)
        

                        print("Traces directory   :", dirs)
                        index = 1
                        for tg in rt:
                            newname = self.srename(tg)
                            index = int(newname.split('-')[0])
                            self.var_det.set(int(index*100/end))
                            self.set( self.var_det.get() )
                            self.update_labels()

                            #   debug:
                            #print "index:", index # This is Correct! The next step is calculate the .set() based on index
                            #print "self.var_det.get()", self.var_det.get()
            
                            root.update_idletasks() # very important function to update GUI
            
                            #   if you need to rename all trace file names, enable the following lien:
                            os.rename(dirs+os.sep+tg,dirs+os.sep+newname)
        print("\n\n Results would be recorded in the 'CheckBox.log' file.")
        print(" ALL INCORRECT *.otr FILES HAVE BEEN RENAMED!\n Thanks for using UL_CheckBox program.\n\n")
	

	#	what is this function for ?
    def set(self, val):
        self.var_det.set( val )
        self.update_labels()

    
    def open_dirc(self):
        global check_path
        check_path = filedialog.askdirectory()
        print("check_path:", check_path)
        self.path_conf_tx.delete(1.0, END)
        self.path_conf_tx.insert(1.0, check_path)

        global archive
        archive = check_path+"/archive"
        print("archive   :", archive)
        

    def tell_me(self):
        print("reserved!")

    def rename_me(self):
        print("reserved!")


    def update_labels(self):
        self.lab_det_var.config(text='%d%%' %  (self.var_det.get())  )
        #self.lab_det_max.config(text='MAX: %d' % (self.pbar_det.cget('maximum')))



        #self.lab_det_max.config(text='MAX: %d' % (self.pbar_det.cget('maximum')))

    '''
    def creatMessageBar(self):
        frame = self.createcomponent('bottomtray', (), None, Frame, (), relief=SUNKEN)
        self.__messageBar = self.createcomponent('messagebar', (), None, (frame,), entry_relief=SUNKEN, entry_bd=1, labelpos=None)
        self.__messageBar.pack(side=LEFT, expand=YES, fill=X)
        self.__progressBar = ProgressBar.ProgressBar(frame, fillColor='slateblue', doLabel=1, width=150)
        self.__progressBar.frame.pack(side=LEFT, expand=NO, fill=NONE)
        self.updateProgress(0)
        frame.pack(side=BOTTOM, expand=NO, fill=X)
        self.__balloon.configure(statuscommand = \
        self.__messageBar.helpmessage)
    '''

    def __init__(self):
        #   directory
        self.path_lb = Label(tag_checking, text="Directory:")
        self.path_lb.grid(row=0, column=0, sticky=E)
        self.path_bt = Button(tag_checking, text="Open", width=6, command=self.open_dirc)
        self.path_bt.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #   path confirmation
        self.path_conf_lb = Label(tag_checking, text="Selected path:")
        self.path_conf_lb.grid(row=1, column=0, sticky=E)
        self.path_conf_tx = Text(tag_checking, font = "Courier 9", height=1, width=48)
        self.path_conf_tx.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky=W)

        #   trace checking
        #   start num
        self.begin_lb = Label(tag_checking, text="Begin with:")
        self.begin_lb.grid(row=2, column=0, sticky=E)
        self.begin_tx = Entry(tag_checking, textvariable = default_begin, font = "Courier 9", width=7)
        self.begin_tx.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky=W)
        self.begin_lb_eg = Label(tag_checking, text="e.g.: 1          ")
        self.begin_lb_eg.grid(row=3, column=1, sticky=E)
        #   end num
        self.end_lb = Label(tag_checking, text="End with:")
        self.end_lb.grid(row=3, column=0, sticky=E)
        self.end_tx = Entry(tag_checking, textvariable = default_end, font = "Courier 9", width=7)
        self.end_tx.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky=W)
        self.end_lb_eg = Label(tag_checking, text="e.g.: 100000")
        self.end_lb_eg.grid(row=3, column=1, sticky=E)
        
        #   key selector
        self.keystr_lb = Label(tag_checking, text="Key selector:")
        self.keystr_lb.grid(row=4, column=0, sticky=E)
        self.keystr_bt_int = Radiobutton(tag_checking, text="Default key", indicatoron=0, value=1, width=15, variable=MODE_KEY_SELECTOR)
        self.keystr_bt_int.grid(row=4, column=1, padx=12, pady=5, sticky=W)
        self.keystr_bt_ext = Radiobutton(tag_checking, text="Keys in OTR files", indicatoron=0, value=2, width=15, variable=MODE_KEY_SELECTOR)
        self.keystr_bt_ext.grid(row=4, column=2, padx=12, pady=5, sticky=W)

        #   key
        self.key_lb = Label(tag_checking, text="Default Key:")
        self.key_lb.grid(row=5, column=0, sticky=E)
        self.key_tx = Entry(tag_checking, textvariable = default_key, font = "Courier 9", width=48)
        self.key_tx.grid(row=5, column=1, columnspan=5, padx=5, pady=5, sticky=W)
        
        #   ruler
        self.ruler = Label(tag_checking, text="|----8 Bytes---||----8 Bytes---||----8 Bytes---|", font="Courier 9", width=48)
        self.ruler.grid(row=6, column=1, columnspan=5, padx=4, sticky=W)
        
        #   progress bar
        self.check_progressbar_lb = Label(tag_checking, text="Progressing:")
        self.check_progressbar_lb.grid(row=7, column=0, sticky=E)
        self.var_det = IntVar()
        #self.var_det = int(self.end_tx.get())
        self.pbar_det = ttk.Progressbar(tag_checking, style='text.Horizontal.TProgressbar', length=340, mode="determinate", variable=self.var_det, maximum=100)
        self.pbar_det.grid(row=7, column=1, pady=5, padx=5, sticky=W, columnspan=3)
        self.lab_det_var = Label(tag_checking, text=" ")
        self.lab_det_var.grid(row=8, column=1, columnspan=4, pady=0, padx=5, sticky=E+W+N+S)

        #self.lab_det_max = Label(tag_checking, text="MAX:")
        #self.lab_det_max.grid(row=6, column=3, pady=5, padx=5, sticky=E+W+N+S)



        '''
        self.canvas = tk.Canvas(tag_checking, relief = tk.FLAT, background = "#D2D2D2", width = 340, height =18)
        self.progressbar = Progressbar(self.canvas, orient=tk.HORIZONTAL, length=340, mode="determinate", variable=50,)
        #self.check_progressbar = ttk.Progressbar(tag_checking, orient='horizontal', mode='determinate')
        #self.progressbar.grid(row=5, column=1, columnspan=3, padx=5, pady=8, sticky=W)
        self.canvas.create_window(1, 1, anchor=tk.NW, window=self.progressbar)
        self.canvas.grid(row=5, column=1, columnspan=3, padx=5, pady=8, sticky=W)
        self.progressbar.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
        self.progressbar.start(5)
        '''
        # Action buttons - Checking incorrectness ONLY
        self.go_for_telling = Button(tag_checking, text="File\nchecking", width=8, bg='#D1FFBD', command=self.execution_check_des_tdes_aes)
        self.go_for_telling.grid(row=9, column=1, columnspan=2, padx=5, pady=5, sticky=W)
		
        # Action buttons - 
        self.go_for_moving = Button(tag_checking, text="File\nmoving", width=8, bg='#D1FFBD', command=self.execution_move_des_tdes_aes)
        self.go_for_moving.grid(row=9, column=2, columnspan=2, padx=5, pady=5, sticky=W)
        
        # Action buttons - 
        self.go_for_renaming = Button(tag_checking, text="Flie\nrenaming", width=8, bg='#D1FFBD', command=self.execution_rename_des_tdes_aes)
        self.go_for_renaming.grid(row=9, column=3, columnspan=2, padx=5, pady=5, sticky=W)



        #self.algo_lb = Label(tag_algo, text="Algorithm:")
        #self.algo_lb.grid(row=1, column=0, sticky=E)
        self.algo_lb_fr = LabelFrame(tag_algo, text="Algorithms", font=("Helvetica", 12, "bold"), padx=5, pady=5, bd=4)
        self.algo_lb_fr.grid(row=0, column=1, rowspan=3, columnspan=2, sticky=E)
        self.algo_des = Radiobutton(self.algo_lb_fr, text="DES", indicatoron=0, value=1, width=7, variable=algo_selection)
        self.algo_des.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        self.algo_tdes = Radiobutton(self.algo_lb_fr, text="TDES", indicatoron=0, value=2, width=7, variable=algo_selection)
        self.algo_tdes.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.algo_aes = Radiobutton(self.algo_lb_fr, text="AES", indicatoron=0, value=3, width=7, variable=algo_selection)
        self.algo_aes.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        #self.mode_lb = Label(tag_algo, text="Mode:")
        #self.mode_lb.grid(row=2, column=0, sticky=E)
        self.mode_lb_fr = LabelFrame(tag_algo, text="Modes", font=("Helvetica", 12, "bold"), padx=5, pady=5, bd=4)
        self.mode_lb_fr.grid(row=0, column=3, rowspan=2, columnspan=3, sticky=E)
        self.mode_ECB = Radiobutton(self.mode_lb_fr, text="ECB", indicatoron=0, value=1, width=7, variable=mode_selection)
        self.mode_ECB.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        self.mode_CBC = Radiobutton(self.mode_lb_fr, text="CBC", indicatoron=0, value=2, width=7, variable=mode_selection)
        self.mode_CBC.grid(row=1, column=4, padx=5, pady=5, sticky=W)
        self.mode_CFB = Radiobutton(self.mode_lb_fr, text="CFB", indicatoron=0, value=3, width=7, variable=mode_selection)
        self.mode_CFB.grid(row=2, column=3, padx=5, pady=5, sticky=W)
        self.mode_OFB = Radiobutton(self.mode_lb_fr, text="OFB", indicatoron=0, value=4, width=7, variable=mode_selection)
        self.mode_OFB.grid(row=2, column=4, padx=5, pady=5, sticky=W)
        self.mode_CTR = Radiobutton(self.mode_lb_fr, text="CTR", indicatoron=0, value=5, width=7, variable=mode_selection)
        self.mode_CTR.grid(row=3, column=3, padx=5, pady=5, sticky=W)


        self.update_labels()        
        

def quit():
    global root
    root.quit()

app = CheckBox()

root.iconbitmap('C:/Python311/UL_logo_64.ico')
app.update_labels()
root.mainloop()