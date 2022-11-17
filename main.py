
import smtplib
import random
from tkinter import *

win=Tk()
win.minsize(height=600,width=600)
win.title("BANK OF PEOPLE")
photo=PhotoImage(file ='images/bank.png')
photo=photo.subsample(2,2)
l=Label(win, text="WELCOME\n     TO     \n BANK OF PEOPLE",font=('bold',25),fg="red3",bg="grey15")
l.pack(pady=20)
l1=Label(win,image=photo,bg="grey15")
l1.pack(pady=25)


def choose_option():
    global b4,b5,b6,b7,b8,b9
    s="BROCHURE FOR ACCOUNT HOLDER\n\n|  REGISTER NEW ACCOUNT  |\n|  DELETE ACCOUNT  |\n|  DEPOSIT AMOUNT  |\n|  ACCOUNT STATUS  |\n|  WITHDRAW AMOUNT  |\n|  EXIT FROM APP  |\n\n\n ENTER THE BUTTON"
    l.config(text=s,font=(12))
    l.pack()
    l1.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4 = Button(win, text="REGISTER",command=create_acc,bg="red3",fg="white",font=("bold",10))
    b5 = Button(win, text="DELETE",command=delete_acc,bg="red3",fg="white",font=("bold",10))
    b6 = Button(win, text="DEPOSIT AMOUNT", command=deposit_amount,bg="red3",fg="white",font=("bold",10))
    b7 = Button(win, text="ACC DETAIL", command=account_detail,bg="red3",fg="white",font=("bold",10))
    b8 = Button(win, text="WITHDRAW AMOUNT", command=withdraw_amount,bg="red3",fg="white",font=("bold",10))
    b9 = Button(win, text="EXIT",command=exit,bg="red3",fg="white",font=("bold",10))
    b4.pack(pady=5)
    b5.pack(pady=5)
    b6.pack(pady=5)
    b7.pack(pady=5)
    b8.pack(pady=5)
    b9.pack()

def create_acc():
    SUBJECT = "RIKU BANK OF PEOPLE  BOP"
    all_acc = {}
    win1 = Tk()
    win1.minsize(height=600, width=600)
    win1.title("BANK OF PEOPLE")
    win1.configure(bg="grey15")
    l = Label(win1, text="ENTER YOUR NAME PLEASE SIR/MAAM \n\n ALSO PUT YOUR EMAIL ID:",font=(13),fg="red3",bg="grey15")
    l.pack(pady=50)
    entry=Entry(win1,width=25,font=20)
    entry.focus_set()
    entry.pack(pady=5)
    entry1 = Entry(win1, width=30,font=20)
    entry1.focus_set()
    entry1.pack(pady=5)
    def A():
        name = entry.get()
        email=entry1.get()
        with open("acc.txt", "r") as f:
            c = f.read()
            if name=="":
                pass
            elif name in c:
                s="YOU ALREADY HAVE A ACCOUNT TRY TO CHECK THE ACCOUNT DETAILS"
                l.config(text=s)
            else:
                b4.destroy()
                all_acc[name] = random.randint(111111, 999999)
                for i, j in all_acc.items():
                    new_acc = str(i) + " : " + str(j)
                    s="REMEMBER THE NAME AND ACCOUNT NUMBER. VERY IMPORTANT.\n\n\n"+new_acc+"\n\nDO YOU WANT TO ADD THIS ACCOUNT PRESS[+] FOR CHANGING ACCOUNT NUMBER  PRESS[-]\n"
                    l.config(text=s)
                    l.pack()
                    def add_acc():
                        sms=smtplib.SMTP('smtp.gmail.com',587)
                        sms.starttls()
                        sms.login(user="bankofpeoplebop@gmail.com",password="byoofebjsppicrrd")
                        messege="Subject: {}\n\n acc detail is  {}".format(SUBJECT, new_acc)
                        s = str((new_acc) + "\n")
                        file = open("acc.txt", "a")
                        s1 = str(i)
                        s2 = str(j)
                        file.writelines([s1, " : ", s2, "\n"])
                        file.close()
                        file = open("acc.txt")
                        fw=open("amount.txt", "a")
                        amount=0
                        total = str(new_acc+ " : $ " + '{}'.format(amount) + "\n")
                        fw.write(total)
                        sms.sendmail(from_addr="bankofpeoplebop@gmail.com", to_addrs=email, msg=messege)
                        sms.close()
                        string="ACCOUNT ADDED THANK U SIR/MAAM. THIS IS YOUR ACCOUNT INFO\n\n\n"+s+"\n\n A ZERO BALACE ACCOUNT IS CREATED AND ADDED TO OUR AMOUNT PANEL.:\n\n\n"+total+"\n\n WE HAVE SENT YOU AN EMAIL PLEASE CHECK IT."
                        l.config(text=string)
                        l.pack()
                        entry.destroy()
                        entry1.destroy()
                        b6.destroy()
                        b7.destroy()
                        b4.destroy()
                        file.close()
                    def conf_acc():
                        A()
                        b4.destroy()
                        b6.destroy()
                        b7.destroy()
                    b6=Button(win1,text= "ADD ACC +",command=add_acc,bg="red3",fg="white",font=("bold",10))
                    b6.pack(pady=5)
                    b7=Button(win1,text="CHANGE ACC -",command=conf_acc,bg="red3",fg="white",font=("bold",10))
                    b7.pack(pady=5)
    b4 = Button(win1,text="REGISTER",command=A,bg="red3",fg="white",font=("bold",10))
    b4.pack(pady=5)
    b5 = Button(win1,text="MAIN PAGE",command=win1.destroy,bg="red3",fg="white",font=("bold",10))
    b5.pack(pady=5)


def delete_acc():
    SUBJECT = "RIKU BANK OF PEOPLE  BOP"
    win2 = Tk()
    win2.minsize(height=600, width=600)
    win2.title("BANK OF PEOPLE")
    win2.configure(bg="grey15")
    l = Label(win2, text="MAKE SURE TO WITHDRAW THE AMOUNT OF YOUR ACCOUNT\n\nFOR THAT KINDLY CHECK ACCOUNTS DETAILS AND WITHDRAW\n\n IF NOT DONE YOUR ACCOUNT BALANCE AND AMOUNT WILL BE LOST\n\n\nENTER [MAINPAGE] TO GO TO THE MAIN PAGE \n\n\n [CONTINUE] TO CONTINUE\n",font=(13),fg="red3",bg="grey15")
    l.pack(pady=30)
    def dele():
        l.config(text="ENTER YOUR NAME PLEASE SIR/MAAM TO DELETE:\n ENTER YOUR ACCOUNT NO:\n ENTER YOUR MAIL ID:\n")
        l.pack()
        entry1 = Entry(win2,width=25,font=20)
        entry1.focus_set()
        entry1.pack(pady=5)
        entry2 = Entry(win2,width=25,font=20)
        entry2.focus_set()
        entry2.pack(pady=5)
        entry3 = Entry(win2, width=30, font=20)
        entry3.focus_set()
        entry3.pack(pady=5)
        def submit():
            email=entry3.get()
            name = entry1.get()
            acc_no = entry2.get()
            if (name=="" and acc_no==""):
                pass
            else:
                search_acc = str(name) + " : " + str(acc_no)
                search_amt = str(name)+" : "+str(acc_no)+" : $ "+"0"
                with open("acc.txt", "r") as f:
                    c = f.read()
                    if search_acc in c:
                        fc = open("amount.txt", "r")
                        cr = fc.read()
                        if search_amt in cr:
                            delete = c.replace(search_acc, "")
                            with open("acc.txt", "w") as fr:
                                fr.write(str(delete))
                            D = cr.replace(search_amt, "")
                            file = open("amount.txt", "w")
                            file.write(str(D))
                            sms = smtplib.SMTP('smtp.gmail.com', 587)
                            sms.starttls()
                            sms.login(user="bankofpeoplebop@gmail.com", password="byoofebjsppicrrd")
                            messege = "Subject: {}\n\n Account deleted from our bank of people is  {}".format(SUBJECT,search_acc)
                            sms.sendmail(from_addr="bankofpeoplebop@gmail.com", to_addrs=email, msg=messege)
                            sms.close()
                            s = "ACCOUNT FOUND\n\n" + search_acc + "\n\nDELETED FROM OUR BANK CUSTOMER AND AMOUNT PANEL\n\n A ACCOUNT STOPING MAIL HAS BEEN SENT IN YOU EMAIL"
                            l.config(text=s)
                            l.pack()
                        else:
                            l.config(text="YOU HAVE A ACCOUNT BUT \n THERE IS SOME ISSUE IN THE ACCOUNT BALANCE SECTION\n\n CHECK ACCOUNT STATUS\n\n")
                            l.pack()
                            b10.destroy()
                    else:
                        l.config(text="ACCOUNT NOT FOUND\n\nIF YOU HAVE A ACCOUNT THEN TRY THIS OR ELSE DONOT.\n\n PRESS MAIN PAGE")
                        l.pack()
                        b9.destroy()
        b10=Button(win2,text="DELETE ACCOUNT",command=submit,bg="red3",fg="white",font=("bold",10))
        b10.pack(pady=5)
        b9.destroy()
    b8=Button(win2,text="MAIN PAGE",command=win2.destroy,bg="red3",fg="white",font=("bold",10))
    b8.pack(pady=5)
    b9=Button(win2,text="CONTINUE",command=dele,bg="red3",fg="white",font=("bold",10))
    b9.pack(pady=5)


def account_detail():
    win3 = Tk()
    win3.minsize(height=600, width=600)
    win3.title("BANK OF PEOPLE")
    win3.configure(bg="grey15")
    l=Label(win3,text="WHAT IS YOUR ACCOUNT DETAIL. PLEASE ENTER\n\nENTER YOUR NAME:\n\nENTER YOUR ACCOUNT NUMBER:\n\n",font=(13),fg="red3",bg="grey15")
    l.pack(pady=20)
    entry1 = Entry(win3, width=25,font=20)
    entry1.focus_set()
    entry1.pack(pady=5)
    entry2 = Entry(win3, width=25,font=20)
    entry2.focus_set()
    entry2.pack(pady=5)
    def submit():
        name=entry1.get()
        acc=entry2.get()
        if (name == "" and acc == ""):
            pass
        else:
            with open("acc.txt") as f:
                i = f.read()
                if acc in i:
                    s="YOU HAVE A ACCOUNT\n\nACCOUNT DETAIL IS \n\n"+name+" : "+acc+"\n\nFOR ACCOUNT BALANCE PRESS ACCBALANCE"
                    l.config(text=s)
                    l.pack()
                    b11.destroy()
                    entry1.destroy()
                    entry2.destroy()
                    def accbalance():
                        A = acc
                        with open("amount.txt", "r") as f:
                            line = f.read()
                            if A in line:
                                with open("amount.txt", "r") as f:
                                    for num, line in enumerate(f, 1):
                                        if A in line:
                                            s="YES ACCOUNT AVAILABLE.  YOUR ACCOUNT DETAIL IS :\n\n"+line
                                            l.config(text=s)
                                            l.pack()
                                            entry1.destroy()
                                            entry2.destroy()
                                            b11.destroy()
                                            b13.destroy()
                    b13=Button(win3,text="ACCBALANCE",command=accbalance,bg="red3",fg="white",font=("bold",10))
                    b13.pack(pady=5)
                else:
                    l.config(text="PROBABLY YOU DONOT HAVE A ACCOUNT. TRY FROM MAIN BROCHURE")
                    l.pack()
                    b11.destroy()
    b11=Button(win3,text="LOGIN",command=submit,bg="red3",fg="white",font=("bold",10))
    b11.pack(pady=5)
    b12=Button(win3,text="MAIN PAGE",command=win3.destroy,bg="red3",fg="white",font=("bold",10))
    b12.pack(pady=5)



def deposit_amount():
    win4 = Tk()
    win4.minsize(height=600, width=600)
    win4.title("BANK OF PEOPLE")
    win4.configure(bg="grey15")
    s="PLEASE CHECK ACCOUNT STATUS BEFORE TRYING THIS\n\nENTER YOUR NAME SIR/MAAM:\n\nENTER YOUR ACCOUNT NUMBER:\n\nENTER AMOUNT YOU WANT TO DEPOSIT:"
    la=Label(win4,text=s,font=(13),fg="red3",bg="grey15")
    la.pack(pady=20)
    entry1 = Entry(win4, width=25,font=20)
    entry1.focus_set()
    entry1.pack(pady=5)
    entry2 = Entry(win4, width=25,font=20)
    entry2.focus_set()
    entry2.pack(pady=5)
    entry3 = Entry(win4, width=15,font=20)
    entry3.focus_set()
    entry3.pack(pady=5)
    def submit():
        name=entry1.get()
        acc_no=entry2.get()
        if(name=="" and acc_no==""):
            pass
        else:
            with open("acc.txt", "r") as f:
                lines = f.read()
                prev_acc = str(acc_no)
                if acc_no in lines:
                    with open("amount.txt") as f:
                        lines = f.read()
                        if prev_acc in lines:
                            fy = open("amount.txt")
                            for pos, line in enumerate(fy):
                                if prev_acc in line:
                                    l = line.rsplit(' ')[-1]
                                    amount = int(entry3.get())
                                    new_amt = int(l) + amount
                                    new_line = str(name + " : " + acc_no + " : $ " + '{}'.format(new_amt) + "\n")
                                    data = lines.replace(line, new_line)
                                    d = str(data)
                                    with open("amount.txt", "w") as fr:
                                        fr.writelines(d)
                                        s="YES YOU HAVE A ACCOUNT AND A PREVIOUS DEPOSIT OF : \n$ "+l+"\n\n"+"AMOUNT DEPOSITED FOR :\n\n"+name+ " : "+ acc_no+ " : $ "+str(new_amt)
                                        la.config(text=s)
                                        la.pack()
                                        entry1.destroy()
                                        entry2.destroy()
                                        b14.destroy()
                                    fr.close()
                else:
                    s = "ACCOUNT NOT FOUND:\n\n\n" +name+":"+acc_no
                    la.config(text=s)
                    la.pack()
    b14 = Button(win4, text="DEPOSIT", command=submit,bg="red3",fg="white",font=("bold",10))
    b14.pack(pady=5)
    b15 = Button(win4, text="MAIN PAGE", command=win4.destroy,bg="red3",fg="white",font=("bold",10))
    b15.pack(pady=5)

def withdraw_amount():
    win5 = Tk()
    win5.minsize(height=600, width=600)
    win5.title("BANK OF PEOPLE")
    win5.configure(bg="grey15")
    s = "PLEASE CHECK ACCOUNT STATUS BEFORE TRYING THIS\n\nENTER YOUR NAME SIR/MAAM:\n\nENTER YOUR ACCOUNT NUMBER:\n\nENTER AMOUNT YOU WANT TO WITHDRAW:"
    la = Label(win5, text=s,font=(13),fg="red3",bg="grey15")
    la.pack(pady=20)
    entry1 = Entry(win5, width=25,font=20)
    entry1.focus_set()
    entry1.pack(pady=5)
    entry2 = Entry(win5, width=25,font=20)
    entry2.focus_set()
    entry2.pack(pady=5)
    entry3 = Entry(win5, width=15,font=20)
    entry3.focus_set()
    entry3.pack(pady=5)
    def submit():
        name = entry1.get()
        acc_no = entry2.get()
        amt=entry3.get()
        if (name == "" and acc_no == "" and amt == ""):
            pass
        else:
            with open("acc.txt", "r") as f:
                lines = f.read()
                prev_acc = str(acc_no)
                if acc_no in lines:
                    with open("amount.txt") as f:
                        lines = f.read()
                        if prev_acc in lines:
                            fy = open("amount.txt")
                            for pos, line in enumerate(fy):
                                if prev_acc in line:
                                    l = line.rsplit(' ', 1)[-1]
                                    prevamt = int(l)
                                    amt=int(entry3.get())
                                    if (prevamt < amt):
                                        s="YOU HAVE ISSUFICIENT BALANCE OR AMOUNT \n\n you have \n\n $ "+l+"in your bank \n\n TRY PUTTING VALID AMOUNT"
                                        la.config(text=s)
                                        la.pack()
                                    else:
                                        new_amt = str(prevamt - amt)
                                        new_A = str(name + " : " + acc_no + " : $ " + '{}'.format(new_amt) + "\n")
                                        data = lines.replace(line, new_A)
                                        d = str(data)
                                        with open("amount.txt", "w") as f:
                                            f.writelines(d)
                                        s="AMOUNT WITHDRAWN \n $ "+str(amt)+ "\nAMOUNT LEFT AND DETAIL OF YOUR ACCOUNT IS :\n\n"+name+" : "+acc_no+" : $ "+new_amt
                                        la.config(text=s)
                                        la.pack()
                                        b16.destroy()
                                        entry1.destroy()
                                        entry2.destroy()
                else:
                    s = "ACCOUNT NOT FOUND:\n\n\n" + name + ":" + acc_no
                    la.config(text=s)
                    la.pack()
    b16 = Button(win5, text="WITHDRAW", command=submit,bg="red3",fg="white",font=("bold",10))
    b16.pack(pady=5)
    b17 = Button(win5, text="MAIN PAGE", command=win5.destroy,bg="red3",fg="white",font=("bold",10))
    b17.pack(pady=5)

def ADMIN():
    win6 = Tk()
    win6.minsize(height=600, width=600)
    win6.title("BANK OF PEOPLE")
    win6.configure(bg="grey15")
    l = Label(win6,text="WELCOME     -------    ADMIN\n\n\n ENTER YOUR NAME",font=(13),fg="red3",bg="grey15")
    l.pack(pady=20)
    entry1 = Entry(win6, width=25,show="X",font=20)
    entry1.focus_set()
    entry1.pack(pady=5)
    def submit():
        f=open("admin.txt","r")
        N=f.read()
        name=entry1.get()
        if name=="":
            pass
        elif name in N:
            l.config(text="ENTER PASSWORD :\n\n")
            l.pack()
            entry2=Entry(win6, width=25,show="*",font=20)
            entry2.focus_set()
            entry2.pack(pady=5)
            entry1.destroy()
            b18.destroy()
            def submit2():
                scrollbar=Scrollbar(win6)
                scrollbar.pack(side=RIGHT,fill=Y)
                password=entry2.get()
                if password=="":
                    pass
                elif password in N:
                    with open("acc.txt", "r") as f:
                        lines = f.read()
                    with open("amount.txt", "r") as fr:
                        line = fr.read()
                    s="ALL ACCOUNTS IS :\n\n"+lines+"\n\n\n\n"+"ALL AMOUNT PANEL IS :\n\n"+line
                    l.config(text=s)
                    l.pack()
                    b18.destroy()
                    b20.destroy()
                    entry1.destroy()
                    entry2.destroy()
                    scrollbar.destroy()
                else:
                    l.config(text="WRONG PASSWORD")
                    l.pack()
                    b18.destroy()
                    entry1.destroy()
                    scrollbar.destroy()
            b20 = Button(win6, text="SUBMIT PASSWORD", command=submit2,bg="red3",fg="white",font=("bold",10))
            b20.pack(pady=5)
        else:
            l.config(text="WRONG NAME OF ADMIN\n\n ENTER THE CORRECT PASSWORD OR GET LOST\n")
            l.pack()
    b18 = Button(win6, text="LOGIN", command=submit,bg="red3",fg="white",font=("bold",10))
    b18.pack(pady=5)
    b19 = Button(win6, text="MAIN PAGE", command=win6.destroy,bg="red3",fg="white",font=("bold",10))
    b19.pack(pady=5)
    win6.mainloop()

win.configure(bg="grey15")
b1= Button(win, text="ADMIN",command=ADMIN,bg="red3",fg="white",font=("bold",10))
b1.pack()
b2= Button(win, text="ACCOUNT HOLDER",command=choose_option,bg="red3",fg="white",font=("bold",10))
b2.pack(pady=15)
b3= Button(win, text="EXIT",command=exit,bg="red3",fg="white",font=("bold",10))
b3.pack()
win.mainloop()
