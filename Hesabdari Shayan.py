import tkinter as tk
import sqlite3
#from jalali import JalaliCalendar

def get_screen_size():
  """
  این تابع اندازه صفحه نمایش را برمی گرداند.
  """
  root = tk.Tk()
  width = root.winfo_screenwidth()
  height = root.winfo_screenheight()
  root.destroy()  # پنجره را ببندید تا از هدر رفتن حافظه جلوگیری کنید
  return width, height

def set_window_size(window, width, height):
  """
  This function sets the window size of the provided tkinter window.
  """
  window.geometry(f"{width // 3}x{height // 3}")



def submit_data():
  """
  این تابع داده های ورودی را جمع آوری کرده و در پایگاه داده SQLite ذخیره می کند.
  """
  company_name = company_entry.get()
  rep_name = rep_entry.get()
  company_number = company_number_entry.get()
  rep_number = rep_number_entry.get()

  # اتصال به پایگاه داده SQLite
  connection = sqlite3.connect('contacts.db')
  cursor = connection.cursor()

  # درج داده ها در جدول
  cursor.execute("INSERT INTO contacts (company_name, rep_name, company_number, rep_number) VALUES (?, ?, ?, ?)", (company_name, rep_name, company_number, rep_number))
  connection.commit()
  connection.close()

  # نمایش پیام تأیید
  messagebox.showinfo("ذخیره شد", "اطلاعات تماس با موفقیت ذخیره شد!")

# دریافت اندازه صفحه نمایش
width, height = get_screen_size()

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Khoshsanat Reporting")

# تنظیم سایز پنجره
set_window_size(root, width, height)

# راست چین کردن عناصر
#root.config(direction='rtl')

# ایجاد برچسب ها و فیلدهای ورودی
company_label = tk.Label(root, text="نام شرکت:", font=("Arial", 16, "bold"))
company_label.grid(row=0, column=1, sticky='e')

company_entry = tk.Entry(root, font=("Arial", 16, "bold"))
company_entry.grid(row=0, column=0, sticky='w')

rep_label = tk.Label(root, text="نام نماینده:", font=("Arial", 16, "bold"))
rep_label.grid(row=1, column=1, sticky='e')

rep_entry = tk.Entry(root, font=("Arial", 16, "bold"))
rep_entry.grid(row=1, column=0, sticky='w')

company_number_label = tk.Label(root, text="شماره شرکت:", font=("Arial", 16, "bold"))
company_number_label.grid(row=2, column=1, sticky='e')
company_number_entry = tk.Entry(root, font=("Arial", 16, "bold"))
company_number_entry.grid(row=2, column=0, sticky='w')

rep_number_label = tk.Label(root, text="شماره نماینده:", font=("Arial", 16, "bold"))
rep_number_label.grid(row=3, column=1, sticky='e')
rep_number_entry = tk.Entry(root, font=("Arial", 16, "bold"))
rep_number_entry.grid(row=3, column=0, sticky='w')

# ایجاد دکمه های ارسال و ذخیره
submit_button = tk.Button(root, text="ارسال", command=submit_data, font=("Arial", 16, "bold"), padx=20, pady=10)
submit_button.grid(row=4, column=0, sticky='e')

save_button = tk.Button(root, text="ذخیره", command=submit_data, font=("Arial", 16, "bold"), padx=20, pady=10)
save_button.grid(row=4, column=1, sticky='w')

def open_add_invoice_window():
  """
  This function opens the "Add Invoice" window.
  """
  add_invoice_window = tk.Toplevel(root)
  add_invoice_window.title("افزودن فاکتور")

  # Create labels
  invoice_number_label = tk.Label(add_invoice_window, text="1- شماره فاکتور:", font=("Arial", 12, "bold"))
  invoice_number_label.grid(row=0, column=0, sticky='e', pady=5)

  invoice_date_label = tk.Label(add_invoice_window, text="2- تاریخ فاکتور:", font=("Arial", 12, "bold"))
  invoice_date_label.grid(row=1, column=0, sticky='e', pady=5)

  description_label = tk.Label(add_invoice_window, text="3- توضیحات:", font=("Arial", 12, "bold"))
  description_label.grid(row=2, column=0, sticky='e', pady=5)

  amount_label = tk.Label(add_invoice_window, text="4- مبلغ فاکتور:", font=("Arial", 12, "bold"))
  amount_label.grid(row=3, column=0, sticky='e', pady=5)

  # Create entry fields
  def only_numbers(char):
    return char.isdigit() or char == ""

  invoice_number_entry = tk.Entry(add_invoice_window, validate='all', validatecommand=(add_invoice_window.register(only_numbers), '%S'))
  invoice_number_entry.grid(row=0, column=1, padx=10, pady=5)

  def validate_date(char):
    try:
      datetime.strptime(invoice_date_entry.get() + char, "%d/%m/%Y")
      return True
    except ValueError:
      return False

  invoice_date_entry = tk.Entry(add_invoice_window, validate='all', validatecommand=(add_invoice_window.register(validate_date), '%S'))
  invoice_date_entry.grid(row=1, column=1, padx=10, pady=5)

  description_text = tk.Text(add_invoice_window, height=5, width=30)
  description_text.grid(row=2, column=1, padx=10, pady=5)

  amount_entry = tk.Entry(add_invoice_window, validate='all', validatecommand=(add_invoice_window.register(only_numbers), '%S'))
  amount_entry.grid(row=3, column=1, padx=10, pady=5)

  # Create buttons
  save_button = tk.Button(add_invoice_window, text="ذخیره", command=submit_data, font=("Arial", 12, "bold"), padx=10, pady=5)
  save_button.grid(row=4, column=0, sticky='e', padx=10, pady=5)

  cancel_button = tk.Button(add_invoice_window, text="لغو", command=add_invoice_window.destroy, font=("Arial", 12, "bold"), padx=10, pady=5)
  cancel_button

add_invoice_button = tk.Button(root, text="1- افزودن فاکتو", command=lambda: open_add_invoice_window(), font=("Arial", 16, "bold"), padx=20, pady=10)
add_invoice_button.grid(row=5, column=0, sticky='e')


def open_add_deposit_window():
    """
    این تابع پنجره "افزودن واریزی" را باز می کند.
    """
    add_deposit_window = tk.Toplevel(root)
    add_deposit_window.title("افزودن واریزی")

    # Create labels
    deposit_date_label = tk.Label(add_deposit_window, text="1- تاریخ واریزی:", font=("Arial", 12, "bold"))
    deposit_date_label.grid(row=0, column=0, sticky='e', pady=5)

    deposit_amount_label = tk.Label(add_deposit_window, text="2- مبلغ واریزی:", font=("Arial", 12, "bold"))
    deposit_amount_label.grid(row=1, column=0, sticky='e', pady=5)

    # Create entry fields
    def only_numbers(char):
     return char.isdigit() or char == ""

    def validate_date(char):
     try:
       datetime.strptime(invoice_date_entry.get() + char, "%d/%m/%Y")
       return True
     except ValueError:
       return False
    
    deposit_amount_entry = tk.Entry(add_deposit_window, validate='all', validatecommand=(add_deposit_window.register(validate_date), '%S'))
    deposit_amount_entry.grid(row=0, column=1, padx=10, pady=5)

    deposit_amount_entry = tk.Entry(add_deposit_window, validate='all', validatecommand=(add_deposit_window.register(only_numbers), '%S'))
    deposit_amount_entry.grid(row=1, column=1, padx=10, pady=5)

    
     
    

  # Create buttons
    save_button = tk.Button(add_deposit_window, text="ذخیره", command=submit_data, font=("Arial", 12, "bold"), padx=10, pady=5)
    save_button.grid(row=2, column=0, sticky='e', padx=10, pady=5)

    cancel_button = tk.Button(add_deposit_window, text="لغو", command=add_deposit_window.destroy, font=("Arial", 12, "bold"), padx=10, pady=5)
    cancel_button.grid(row=2, column=1, sticky='w', padx=10, pady=5)



    

    # کد مربوط به طراحی و عملکرد پنجره  را در اینجا قرار دهید
add_deposit_button = tk.Button(root, text="2- افزودن واریزی", command=lambda: open_add_deposit_window(), font=("Arial", 16, "bold"), padx=20, pady=10)
add_deposit_button.grid(row=5, column=1, sticky='w')

def open_generate_invoice_window():
    """
    این تابع پنجره صورت حساب را باز می کند.
    """
    add_invoice_window = tk.Toplevel(root)
    add_invoice_window.title("صورت حساب")

    # کد مربوط به طراحی و عملکرد پنجره "افزودن فاکتو" را در اینجا قرار دهید
generate_invoice_button = tk.Button(root, text="3- صورت حساب", command=lambda: open_generate_invoice_window(), font=("Arial", 16, "bold"), padx=20, pady=10)
generate_invoice_button.grid(row=6, column=0, sticky='e')



# اجرای برنامه
root.mainloop()