import tkinter as tk

# Create main window
root = tk.Tk()
root.title("e-Registry Mobile")
root.geometry("360x640")   # Mobile-like size
root.configure(bg="#F8F4EE")
root.resizable(False, False)

# Center window on screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (360 // 2)
y = (screen_height // 2) - (640 // 2)
root.geometry(f"360x640+{x}+{y}")

# App Logo (placeholder circle)
logo = tk.Canvas(root, width=120, height=120, bg="#F8F4EE", highlightthickness=0)
logo.create_oval(10, 10, 110, 110, fill="#8B0000")
logo.pack(pady=80)

# App Name
title = tk.Label(
    root,
    text="e-Registry Mobile",
    font=("Times New Roman", 20, "bold"),
    bg="#F8F4EE",
    fg="#2C2C2C"
)
title.pack(pady=10)

# Subtitle
subtitle = tk.Label(
    root,
    text="Legal Document Creator",
    font=("Times New Roman", 14),
    bg="#F8F4EE",
    fg="#2C2C2C"
)
subtitle.pack(pady=5)

# Loading text
loading = tk.Label(
    root,
    text="Loading...",
    font=("Times New Roman", 12, "italic"),
    bg="#F8F4EE",
    fg="#2C2C2C"
)
loading.pack(side="bottom", pady=40)

# Auto close splash after 3 seconds
root.after(3000, root.destroy)

root.mainloop()
