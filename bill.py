from tkinter import *
from tkinter import messagebox

import math
import random
import os

class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", border=12, relief=GROOVE,
                        bg=bg_color, fg="white", font=("calibri", 30, "italic"), pady=2).pack(fill=X)

        self.soap = IntVar()
        self.fcream = IntVar()
        self.fwash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()

        self.rice = IntVar()
        self.foodoil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        self.maaza = IntVar()
        self.cocacola = IntVar()
        self.mountaindew = IntVar()
        self.thumpsup = IntVar()
        self.appyfizz = IntVar()
        self.fruit = IntVar()

        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.colddrink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.colddrink_tax = StringVar()

        self.cname = StringVar()
        self.cnumber = StringVar()

        self.billno = StringVar()
        x = random.randint(1000, 9999)
        self.billno.set(str(x))
        self.search = StringVar()

        F1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=(
            "calibri", 15, "italic"), fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=(
            "calibri", 18, "italic")).grid(row=0, column=0, padx=20, pady=5)
        cnameE = Entry(F1, width=18, textvariable=self.cname, font="arial 15",
                        bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cnumber = Label(F1, text="Customer Contact", bg=bg_color, fg="white", font=(
            "calibri", 18, "italic")).grid(row=0, column=2, padx=20, pady=5)
        cnumberE = Entry(F1, width=18, textvariable=self.cnumber, font="arial 15",
                            bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        cbill = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=(
            "calibri", 18, "italic")).grid(row=0, column=4, padx=20, pady=5)
        cbillE = Entry(F1, width=18, textvariable=self.search, font="arial 15",
                        bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", bg="white", fg=bg_color, command=self.find_bill, width=18,
                            bd=7, relief=GROOVE, font=('arial 12 bold')).grid(row=0, column=6, pady=10, padx=20)

        F2 = LabelFrame(self.root, text="Cosmetics", bd=10, relief=GROOVE, font=(
            "calibri", 15, "italic"), fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=380, height=380)

        bath = Label(F2, text="Bath Soap", font=("calibri", 14, "italic"), bg=bg_color,
                        fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bathE = Entry(F2, width=12, textvariable=self.soap, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        fcream = Label(F2, text="Face Cream", font=("calibri", 14, "italic"), bg=bg_color,
                        fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        fcreamE = Entry(F2, width=12, textvariable=self.fcream, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        fwash = Label(F2, text="Face Wash", font=("calibri", 14, "italic"), bg=bg_color,
                        fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        fwashE = Entry(F2, width=12, textvariable=self.fwash, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        Hspray = Label(F2, text="Hair Spray", font=("calibri", 14, "italic"), bg=bg_color,
                        fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        HsprayE = Entry(F2, width=12, textvariable=self.spray, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Hgel = Label(F2, text="Hair Gel", font=("calibri", 14, "italic"), bg=bg_color,
                        fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        HgelE = Entry(F2, width=12, textvariable=self.gel, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        blotion = Label(F2, text="Bath Lotion", font=("calibri", 14, "italic"), bg=bg_color,
                        fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        blotionE = Entry(F2, width=12, textvariable=self.lotion, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        F3 = LabelFrame(self.root, text="Groceries", bd=10, relief=GROOVE, font=(
            "calibri", 15, "italic"), fg="gold", bg=bg_color)
        F3.place(x=385, y=180, width=380, height=380)
        entriies = []

        g1 = Label(F3, text="Rice", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1E = Entry(F3, width=12, textvariable=self.rice, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        entriies.append(g1E)

        g2 = Label(F3, text="Food Oil", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2E = Entry(F3, width=12, textvariable=self.foodoil, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        entriies.append(g2E)
        # g2E.bind('<Down>', lambda e, x=i: move_entry(x + 1))
        # g2E.bind('<Up>', lambda e, x=i: move_entry(x - 1))

        g3 = Label(F3, text="Daal", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3E = Entry(F3, width=12, textvariable=self.daal, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        entriies.append(g3E)
        # g3E.bind('<Down>', lambda e, x=i: move_entry(x + 1))
        # g3E.bind('<Up>', lambda e, x=i: move_entry(x - 1))

        g4 = Label(F3, text="Wheat", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4E = Entry(F3, width=12, textvariable=self.wheat, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        entriies.append(g4E)
        # g4E.bind('<Down>', lambda e, x=i: move_entry(x + 1))
        # g4E.bind('<Up>', lambda e, x=i: move_entry(x - 1))

        g5 = Label(F3, text="Sugar", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5E = Entry(F3, width=12, textvariable=self.sugar, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        entriies.append(g5E)
        # g5E.bind('<Down>', lambda e, x=i: move_entry(x + 1))
        # g5E.bind('<Up>', lambda e, x=i: move_entry(x - 1))

        g6 = Label(F3, text="Tea", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6E = Entry(F3, width=12, textvariable=self.tea, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)
        entriies.append(g6E)
        # g6E.bind('<Down>', lambda e, x=0: move_entry(x + 1))
        # g6E.bind('<Up>', lambda e, x=i: move_entry(x - 1))

        # e = []

        # def move_entry(x):
        #     e[x].focus()
        # for i in range(6):
        #     e.append(entriies[i])

        #     if i == 0:
        #         e[-1].bind('<Down>', lambda e, x=i: move_entry(x+1))
        #     elif i == 5:
        #         e[-1].bind('<Up>', lambda e, x=i: move_entry(x-1))
        #     else:
        #         e[-1].bind('<Down>', lambda e, x=i: move_entry(x + 1))
        #         e[-1].bind('<Up>', lambda e, x=i: move_entry(x-1))

        F4 = LabelFrame(self.root, text="Cold Drinks", bd=10, relief=GROOVE, font=(
            "calibri", 15, "italic"), fg="gold", bg=bg_color)
        F4.place(x=765, y=180, width=380, height=380)

        c1 = Label(F4, text="Maaza", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1E = Entry(F4, width=12, textvariable=self.maaza, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2 = Label(F4, text="Coca Cola", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2E = Entry(F4, width=12, textvariable=self.cocacola, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        c3 = Label(F4, text="Mountain Dew", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3E = Entry(F4, width=12, textvariable=self.mountaindew, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        c4 = Label(F4, text="Thumps Up", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4E = Entry(F4, width=12, textvariable=self.thumpsup, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        c5 = Label(F4, text="Appy Fizz", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5E = Entry(F4, width=12, textvariable=self.appyfizz, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        c6 = Label(F4, text="Fruit Beer", font=("calibri", 14, "italic"), bg=bg_color,
                    fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6E = Entry(F4, width=12, textvariable=self.fruit, font=(
            "calibri", 14, "italic"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        F5 = Frame(self.root, bd=10, relief=GROOVE,)
        F5.place(x=1150, y=180, width=390, height=380)
        billtitle = Label(F5, text="Bill Area", font=(
            "calibri", 14, "italic"), bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        F6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=(
            "calibri", 15, "italic"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=220)

        m1 = Label(F6, text="Total Cosmetic Price", font=("calibri", 14, "italic"),
                    bg=bg_color, fg="White").grid(row=0, column=0, padx=5, pady=10, sticky="w")
        m1E = Entry(F6, width=12, textvariable=self.cosmetic_price, font=(
            "calibri", 14, "italic"), bd=7, relief=SUNKEN).grid(row=0, column=1, padx=5, pady=10)

        m2 = Label(F6, text="Total Grocery Price", font=("calibri", 14, "italic"),
                    bg=bg_color, fg="White").grid(row=1, column=0, padx=5, pady=10, sticky="w")
        m2E = Entry(F6, width=12, textvariable=self.grocery_price, font=(
            "calibri", 14, "italic"), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=5, pady=10)

        m3 = Label(F6, text="TOtal Cold Drink Price", font=("calibri", 14, "italic"),
                    bg=bg_color, fg="White").grid(row=2, column=0, padx=5, pady=10, sticky="w")
        m3E = Entry(F6, width=12, textvariable=self.colddrink_price, font=(
            "calibri", 14, "italic"), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=5, pady=10)

        mc1 = Label(F6, text="Total Cosmetic Tax", font=("calibri", 14, "italic"),
                    bg=bg_color, fg="White").grid(row=0, column=2, padx=10, pady=10, sticky="w")
        mc1E = Entry(F6, width=12, textvariable=self.cosmetic_tax, font=(
            "calibri", 14, "italic"), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=10)

        mc2 = Label(F6, text="Total Grocery TAX", font=("calibri", 14, "italic"),
                    bg=bg_color, fg="White").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        mc2E = Entry(F6, width=12, textvariable=self.grocery_tax, font=(
            "calibri", 14, "italic"), bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=10)

        mc3 = Label(F6, text="TOtal Cold Drink Tax", font=("calibri", 14, "italic"),
                    bg=bg_color, fg="White").grid(row=2, column=2, padx=10, pady=10, sticky="w")
        mc3E = Entry(F6, width=12, textvariable=self.colddrink_tax, font=(
            "calibri", 14, "italic"), bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=10)

        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=740, y=10, width=750, height=150)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="cadetblue", fg="white", pady=40,
                            width=13, bd=5, relief=GROOVE, font="aria; 14 bold").grid(row=0, column=0, padx=5, pady=5)
        Exit_btn = Button(btn_f, command=self.exit, text="Exit", bg="cadetblue", fg="white", pady=40,
                            width=13, bd=5, relief=GROOVE, font="aria; 14 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_f, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=40,
                            width=13, bd=5, relief=GROOVE, font="aria; 14 bold").grid(row=0, column=2, padx=5, pady=5)
        Gb_btn = Button(btn_f, command=self.BillArea, text="Generate bill", bg="cadetblue", fg="white",
                        pady=40, width=13, bd=5, relief=GROOVE, font="aria; 14 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcomebill()

    def total(self):
        self.c_s_p = self.soap.get()*49
        self.c_fc_p = self.fcream.get()*129
        self.c_fw_p = self.fwash.get()*159
        self.c_hs_p = self.spray.get()*199
        self.c_hg_p = self.gel.get()*59
        self.c_l_p = self.lotion.get()*169

        self.g_r_p = self.rice.get()*59
        self.g_f_p = self.foodoil.get()*99
        self.g_d_p = self.daal.get()*89
        self.g_w_p = self.wheat.get()*25
        self.g_s_p = self.sugar.get()*38
        self.g_t_p = self.tea.get()*85

        self.c_m_p = self.maaza.get()*39
        self.c_cc_p = self.cocacola.get()*35
        self.c_md_p = self.mountaindew.get()*39
        self.c_t_p = self.thumpsup.get()*39
        self.c_a_p = self.appyfizz.get()*59
        self.c_fr_p = self.fruit.get()*169

        self.totalcosmeticprice = float(self.c_s_p+self.c_hg_p
                                        + self.c_fc_p
                                        + self.c_fw_p
                                        + self.c_hg_p
                                        + self.c_l_p

                                        )
        self.cosmetic_price.set("Rs "+str(self.totalcosmeticprice))
        self.c_t = round(self.totalcosmeticprice*0.18, 2)
        self.cosmetic_tax.set(str(self.c_t))

        self.totalgroceryprice = float((self.g_f_p) +
                                    (self.g_s_p) +
                                    (self.g_r_p) +
                                    (self.g_d_p) +
                                    (self.g_t_p) +
                                    (self.g_w_p)
                                    )

        self.grocery_price.set("Rs "+str(self.totalgroceryprice))
        self.g_t = round(self.totalgroceryprice*0.18, 2)
        self.grocery_tax.set(str(self.g_t))

        self.totalcolddrinkprice = float((self.c_cc_p) +
                                        (self.c_m_p) +
                                        (self.c_md_p) +
                                        (self.c_t_p) +
                                        (self.c_a_p) +
                                        (self.c_fr_p)
                                        )
        self.colddrink_price.set("Rs "+str(self.totalcolddrinkprice))
        self.cd_t = round(self.totalcolddrinkprice*0.0, 2)
        self.colddrink_tax.set(str(self.cd_t))

        self.Total_bill = round((self.totalgroceryprice+self.totalcosmeticprice +
                                self.totalcolddrinkprice+self.cd_t+self.c_t+self.g_t), 2)

    def welcomebill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\tWelcome Webcode Retail\n")
        self.textarea.insert(END, f"\nBill Number : {self.billno.get()}")
        self.textarea.insert(END, f"\nCustomer Name : {self.cname.get()}")
        self.textarea.insert(END, f"\nPhone Number : {self.cnumber.get()}")
        self.textarea.insert(
            END, f"\n===========================================")
        self.textarea.insert(END, f"\n Product\t\t QTY\t\t Price ")
        self.textarea.insert(
            END, f"\n===========================================")

    def BillArea(self):
        if self .cname.get() == "" or self.cnumber.get() == "":
            messagebox.showerror("Error", "customer Details are must")
        elif self.colddrink_price.get() == "Rs  0.0" and self.colddrink_price.get() == "Rs  0.0" and self.colddrink_price.get() == "Rs  0.0":
            messagebox.showerror("Error", "choose any product")
        else:
            self.welcomebill()
            if self.soap.get() != 0:
                self.textarea.insert(
                    END, f"\n Bath Soap\t\t {self.soap.get()}\t\t {self.c_s_p}")
            if self.fcream.get() != 0:
                self.textarea.insert(
                    END, f"\n Face Cream\t\t {self.fcream.get()}\t\t {self.c_fc_p}")
            if self.fwash.get() != 0:
                self.textarea.insert(
                    END, f"\n Face wash\t\t {self.fwash.get()}\t\t {self.c_fw_p}")
            if self.spray.get() != 0:
                self.textarea.insert(
                    END, f"\n Hair spray\t\t {self.spray.get()}\t\t {self.c_hs_p}")
            if self.gel.get() != 0:
                self.textarea.insert(
                    END, f"\n Hair Gel\t\t {self.gel.get()}\t\t {self.c_hg_p}")
            if self.lotion.get() != 0:
                self.textarea.insert(
                    END, f"\n Lotion\t\t {self.lotion.get()}\t\t {self.c_l_p}")
            if self.rice.get() != 0:
                self.textarea.insert(
                    END, f"\n Rice\t\t {self.rice.get()}\t\t {self.g_r_p}")
            if self.foodoil.get() != 0:
                self.textarea.insert(
                    END, f"\n Food Oil\t\t {self.foodoil.get()}\t\t {self.g_f_p}")
            if self.daal.get() != 0:
                self.textarea.insert(
                    END, f"\n Daal\t\t {self.daal.get()}\t\t {self.g_d_p}")
            if self.wheat.get() != 0:
                self.textarea.insert(
                    END, f"\n Wheat\t\t {self.wheat.get()}\t\t {self.g_w_p}")
            if self.sugar.get() != 0:
                self.textarea.insert(
                    END, f"\n Sugar\t\t {self.sugar.get()}\t\t {self.g_s_p}")
            if self.tea.get() != 0:
                self.textarea.insert(
                    END, f"\n Tea\t\t {self.tea.get()}\t\t {self.g_t_p}")
            if self.maaza.get() != 0:
                self.textarea.insert(
                    END, f"\n Maaza\t\t {self.maaza.get()}\t\t {self.c_m_p}")
            if self.cocacola.get() != 0:
                self.textarea.insert(
                    END, f"\n Coca Cola\t\t {self.cocacola.get()}\t\t {self.c_cc_p}")
            if self.mountaindew.get() != 0:
                self.textarea.insert(
                    END, f"\n Mountain Dew\t\t {self.mountaindew.get()}\t\t {self.c_md_p}")
            if self.thumpsup.get() != 0:
                self.textarea.insert(
                    END, f"\n Thumps Up\t\t {self.thumpsup.get()}\t\t {self.c_t_p}")
            if self.appyfizz.get() != 0:
                self.textarea.insert(
                    END, f"\n Appy Fizz\t\t {self.appyfizz.get()}\t\t {self.c_a_p}")
            if self.fruit.get() != 0:
                self.textarea.insert(
                    END, f"\n Fruit Beer\t\t {self.fruit.get()}\t\t {self.c_fr_p}")

            self.textarea.insert(
                END, f"\n===========================================")

            self.textarea.insert(
                END, f"\n Cosmetic Tax\t\t\t\t{self.cosmetic_tax.get()}")

            self.textarea.insert(
                END, f"\n Grocery Tax\t\t\t\t{self.grocery_tax.get()}")

            self.textarea.insert(
                END, f"\n Cold Drink Tax\t\t\t\t{self.colddrink_tax.get()}")
            self.textarea.insert(
                END, f"\n===========================================")

            self.textarea.insert(
                END, f"\n TOtal Bill\t\t\t\t{self.Total_bill}")
            self.textarea.insert(
                END, f"\n===========================================")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("save Bill", "Do you want to save a bill")
        if op > 0:
            self.billdata = self.textarea.get('1.0', END)
            f1 = open("bills/"+str(self.billno.get())+".txt", "w")
            f1.write(self.billdata)
            f1.close()
            messagebox.showinfo(
                "Saved", f"Bill has been saved : {self.billno.get()}")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search.get():
                f1 = open(f"bills/{i}", "r")
                self.textarea.delete("1.0", END)
                for d in f1:
                    self.textarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "invalid bill no.")

    def clear_data(self):
        self.soap.set(0)
        self.fcream.set(0)
        self.fwash.set(0)
        self.spray.set(0)
        self.gel.set(0)
        self.lotion.set(0)

        self.rice.set(0)
        self.foodoil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)

        self.maaza.set(0)
        self.cocacola.set(0)
        self.mountaindew.set(0)
        self.thumpsup.set(0)
        self.appyfizz.set(0)
        self.fruit.set(0)

        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.colddrink_price.set("")
        self.cosmetic_tax .set("")
        self.grocery_tax .set("")
        self.colddrink_tax.set("")

        self.cname.set("")
        self.cnumber.set("")

        self.billno.set("")
        x = random.randint(1000, 9999)
        self.billno.set(str(x))
        self.search.set("")
        self.welcomebill()

    def exit(self):
        op = messagebox.askyesno("Exit", "Do you Really Want to Exit")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = BillApp(root)
root.mainloop()
