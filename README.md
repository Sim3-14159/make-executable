# make-executable
make-executable is a simple Raspberry Pi command-line tool that allows you to make a Python script executable. It can be used like this: `make-executable [option] your file name`. It also has a tool option (`-t`/`--tool`) which allows you to run the script from any directory like a built in tool.

---
<br>

## 🎬 Getting Started
1. Pull the file [`make-executable.py`](make-executable.py) onto your computer.
    ```bash
    cd "whatever/directory/you put your GitHub projects"
    ```
    ```bash
    git clone "https://github.com/Sim3-14159/make-executable.git"
    ```
1. Enter these commands:
    ```bash
    cd make-executable/
    ```
    ```bash
    chmod +x make-executable.py
    ```
    ```bash
    sudo mv make-executable.py /usr/local/bin/make-executable
    ```

1. Now you can use *make-executable* to make your own command-line tools!
1. You can use it like this:

   ```bash
   make-executable your file name.py
   ```
   or
   ```bash
   make-executable -t your-file-name.py
   ```
   ###### Notes
   ###### - You can leave the spaces in between `your file name.py` without enclosing it in quotation marks (`"your file name.py"`)
   ###### - Before entering `make-executable -t your file name.py`, you may want to remove the `.py` extention from the file, or your tool will end with that same extention.
---
<br>

## 💻 Dependencies
- Python 3.*x* as your default version of Python.

---
<br>

## 📝 Notes
- `make-executable` automatically adds the line `!# /usr/bin/env python` at the beginning of the file if not present. If your default version of Python is Python 2.*x*, not 3.*x*, and you want to make a Python 3 script executable, it may not work.
