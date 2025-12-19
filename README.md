# BHOJYA PROGRAMMING LANGUAGE - SDK v1.0

**भोज्य** (Bhojya) - The Atman Native Language System

A Hindi-based programming language that compiles to native Windows executables with built-in GUI support.

---

## 🖥️ Windows Setup Guide

### Step 1: Install Clang/LLVM

Bhojya requires Clang to compile programs. Here's how to install it:

#### Option A: Using Winget (Recommended - Windows 10/11)
```powershell
winget install LLVM.LLVM
```

#### Option B: Manual Installation
1. Download LLVM from: https://github.com/llvm/llvm-project/releases/latest
2. Look for `LLVM-XX.X.X-win64.exe` (e.g., `LLVM-17.0.6-win64.exe`)
3. Run the installer
4. **IMPORTANT:** Check "Add LLVM to system PATH" during installation

### Step 2: Verify Clang Installation

Open PowerShell or Command Prompt and run:
```powershell
clang --version
```

You should see output like:
```
clang version 17.0.6
Target: x86_64-pc-windows-msvc
```

If you get `'clang' is not recognized`, you need to add it to PATH manually:

1. Search for "Environment Variables" in Windows
2. Click "Environment Variables" button
3. Under "System variables", find "Path" and click "Edit"
4. Click "New" and add: `C:\Program Files\LLVM\bin`
5. Click OK on all dialogs
6. **Restart your terminal** and try `clang --version` again

### Step 3: Download Bhojya SDK

1. Go to [Releases](https://github.com/Adi-Baba/Bhojya/releases)
2. Download the latest `Bhojya_SDK_v1.0.zip`
3. Extract to a folder (e.g., `C:\Bhojya`)

### Step 4: Test Your Installation

Open PowerShell, navigate to the SDK folder, and run:
```powershell
cd C:\Bhojya\Bhojya_SDK\bin
.\lathi.exe
```

You should see the welcome banner:
```
================================================
   BHOJYA COMPILER (LATHI) - V1.0 (PRO)
   The Atman Native Language System
================================================
```

---

## 🚀 Quick Start

### Your First Program

1. Create a file `hello.bjy`:
```bhojya
kaam mukhya() {
    0
}
```

2. Compile and run:
```powershell
cd C:\Bhojya\Bhojya_SDK\bin
.\lathi.exe ..\examples\notepad.bjy
.\output.exe
```

A fully functional Notepad window will appear! 🎉

---

## 📦 What's Inside the SDK

- **`bin/lathi.exe`** - The Bhojya compiler
- **`lib/bhojya_rt.obj`** - Native runtime library (pre-compiled)
- **`std/gui.bjy`** - Standard GUI package
- **`examples/notepad.bjy`** - Professional Notepad clone example

---

## 📚 Language Reference

### Keywords
- `kaam` - function definition
- `chanchal` - variable declaration
- `agar` - if
- `tab` - then
- `varnaa` - else
- `jabtak` - while loop
- `bahari kaam` - external function declaration

### Example: GUI Application
```bhojya
===
My First GUI App
===

kaam mukhya() {
    chanchal win = rt_sijan_khidki(800, 600);
    chanchal editor = rt_sijan_lekh_patra(win);
    
    chanchal running = 1;
    jabtak (running) {
        chanchal ev = rt_intezaar();
        agar (ev < 0) tab {
            running = 0;
        };
    };
    
    0
}
```

---

## 🎨 Features

✨ **Native Compilation** - Direct to Windows .exe via LLVM
🖼️ **Built-in GUI** - Win32 controls with modern aesthetics
⌨️ **Keyboard Shortcuts** - Ctrl+S, Ctrl+O, Ctrl+Backspace support
🎨 **Font Customization** - System font picker integration
📁 **File I/O** - Native Open/Save dialogs

---

## 🔧 Building Your Project

### Single File
```powershell
lathi my_app.bjy
```

### With GUI Package
```powershell
lathi ..\std\gui.bjy my_app.bjy
```

### Output
- Generates `output.exe` in the current directory

---

## 📖 Standard Library (std/gui.bjy)

### Window Management
- `rt_sijan_khidki(width, height)` - Create window
- `rt_set_title(win, code)` - Set window title

### Text Editor
- `rt_sijan_lekh_patra(win)` - Create multi-line editor
- `rt_lekh_set(handle)` - Set text from buffer
- `rt_lekh_lelo(handle)` - Get text to buffer

### Menus
- `rt_banaye_menu()` - Create menu bar
- `rt_banaye_submenu()` - Create popup menu
- `rt_jodo_menu_item(menu, id, code)` - Add menu item

### File Dialogs
- `rt_kholo_dialog()` - Open file dialog
- `rt_surakshit_dialog()` - Save file dialog
- `rt_load_file()` - Load file to buffer
- `rt_panni_par_likho(handle)` - Write editor content to file

### Customization
- `rt_kholo_font_dialog()` - Font picker

### Event Loop
- `rt_intezaar()` - Wait for next event (returns event ID)

---

## 🏆 Example: Notepad Clone

See `examples/notepad.bjy` for a fully functional text editor with:
- File Open/Save
- Font selection
- Keyboard shortcuts (Ctrl+S, Ctrl+O, Ctrl+N)
- Modern UI with Segoe UI font

---

## 🛠️ Troubleshooting

**"clang: command not found"**
- Install LLVM and add to system PATH

**"Cannot find bhojya_rt.obj"**
- Ensure you run `lathi.exe` from the SDK's `bin/` directory
- Or use absolute paths

**GUI doesn't appear**
- Check that output.exe is generated
- Run from command line to see error messages

---

## 🌐 Philosophy

Bhojya follows the **"Atman"** (आत्मन्) philosophy:
- Self-reliance through native compilation
- Zero external dependencies in user code
- Pure `.bjy` development workflow

---

## 📜 License

Open Source - Free for personal and commercial use

---

## 🤝 Contributing

This is the v1.0 release. Future enhancements welcome!

---

**Made with 🕉️ by the Bhojya Community**
