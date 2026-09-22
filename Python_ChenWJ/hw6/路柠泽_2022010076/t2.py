import base64
from tkinter import *
from tkinter import messagebox, ttk
from cryptography.hazmat.primitives.asymmetric import padding, rsa

root = Tk()
root.title("RSA")
root.geometry("900x820")
root.minsize(860, 760)
private_key = None
public_key = None
bit_len = StringVar(value="1024")

def set(w, v):
    w.delete("1.0", "end")
    w.insert("1.0", v)

def has():
    return private_key is not None and public_key is not None

def generate():
    global private_key, public_key
    key_size = int(bit_len.get())
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
    public_key = private_key.public_key()
    pub_numbers = public_key.public_numbers()
    priv_numbers = private_key.private_numbers()
    set(n_txt, str(pub_numbers.n))
    e_ent.delete(0, "end")
    e_ent.insert(0, str(pub_numbers.e))
    set(d_txt, str(priv_numbers.d))
    messagebox.showinfo("Info", "RSA keys generated successfully.")

def encrypt():
    if not has():
        messagebox.showerror("Error", "Please generate RSA keys first.")
        return
    plaintext_input = p_txt.get("1.0", "end").strip()
    if not plaintext_input:
        messagebox.showerror("Error", "Please enter a non-empty plaintext string.")
        return
    ciphertext = public_key.encrypt(
        plaintext_input.encode(),
        padding.PKCS1v15()
    )
    b64_cipher = base64.b64encode(ciphertext).decode()
    set(c_out_txt, b64_cipher)
    set(c_in_txt, b64_cipher)
    messagebox.showinfo("Info", "Encryption successful.")

def decrypt():
    if not has():
        messagebox.showerror("Error", "Please generate RSA keys first.")
        return
    b64_cipher = "".join(c_in_txt.get("1.0", "end").split())
    if not b64_cipher:
        messagebox.showerror("Error", "Please enter a non-empty ciphertext string.")
        return
    try:
        plaintext_output = private_key.decrypt(
            base64.b64decode(b64_cipher, validate=True),
            padding.PKCS1v15()
        ).decode()
    except Exception:
        messagebox.showerror("Error", "Please enter a valid ciphertext string.")
        return
    set(p_out_txt, plaintext_output)
    messagebox.showinfo("Info", "Decryption successful.")

mf = Frame(root, padx=14, pady=12)
mf.pack(fill="both", expand=True)

sf = LabelFrame(mf, text="Key Size", padx=10, pady=10)
sf.grid(row=0, column=0, sticky="ew", pady=(0, 8))
sf.columnconfigure(0, weight=1)
sf.columnconfigure(1, weight=1)
sf.columnconfigure(2, weight=1)
Label(sf, text="Select key size (bits):").grid(row=0, column=0, sticky="w")
bits_cb = ttk.Combobox(
    sf,
    textvariable=bit_len,
    values=("1024", "2048", "4096"),
    state="readonly",
    width=10,
)
bits_cb.grid(row=1, column=0, columnspan=3, pady=3)

kf = LabelFrame(mf, text="Generate RSA Keys", padx=10, pady=10)
kf.grid(row=1, column=0, sticky="nsew", pady=(0, 8))
kf.columnconfigure(0, weight=1)
kf.columnconfigure(1, weight=1)
kf.columnconfigure(2, weight=1)
Button(kf, text="Generate Keys", width=14, command=generate).grid(row=0, column=0, columnspan=3, pady=3)
Label(kf, text="Public Key (n):").grid(row=1, column=0, sticky="nw", pady=6)
n_txt = Text(kf, height=4, wrap="word")
n_txt.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=(8, 0), pady=6)
Label(kf, text="Public Key (e):").grid(row=2, column=0, sticky="w", pady=6)
e_ent = Entry(kf)
e_ent.grid(row=2, column=1, columnspan=2, sticky="ew", padx=(8, 0), pady=6)
Label(kf, text="Private Key (d):").grid(row=3, column=0, sticky="nw", pady=6)
d_txt = Text(kf, height=4, wrap="word")
d_txt.grid(row=3, column=1, columnspan=2, sticky="nsew", padx=(8, 0), pady=6)

ef = LabelFrame(mf, text="Encrypt", padx=10, pady=10)
ef.grid(row=2, column=0, sticky="nsew", pady=(0, 8))
ef.columnconfigure(1, weight=1)
Label(ef, text="Plaintext (string):").grid(row=0, column=0, sticky="nw", pady=6)
p_txt = Text(ef, height=3, wrap="word")
p_txt.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=6)
Button(ef, text="Encrypt", width=12, command=encrypt).grid(row=1, column=0, columnspan=2, pady=6)
Label(ef, text="Ciphertext (Base64 string):").grid(row=2, column=0, sticky="nw", pady=6)
c_out_txt = Text(ef, height=5, wrap="word")
c_out_txt.grid(row=2, column=1, sticky="nsew", padx=(8, 0), pady=6)

df = LabelFrame(mf, text="Decrypt", padx=10, pady=10)
df.grid(row=3, column=0, sticky="nsew")
df.columnconfigure(1, weight=1)
Label(df, text="Ciphertext (Base64 string):").grid(row=0, column=0, sticky="nw", pady=6)
c_in_txt = Text(df, height=5, wrap="word")
c_in_txt.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=6)
Button(df, text="Decrypt", width=12, command=decrypt).grid(row=1, column=0, columnspan=2, pady=6)
Label(df, text="Decrypted Plaintext (string):").grid(row=2, column=0, sticky="nw", pady=6)
p_out_txt = Text(df, height=3, wrap="word")
p_out_txt.grid(row=2, column=1, sticky="nsew", padx=(8, 0), pady=6)

mf.columnconfigure(0, weight=1)
mf.rowconfigure(1, weight=1)
mf.rowconfigure(2, weight=1)
mf.rowconfigure(3, weight=1)

root.mainloop()