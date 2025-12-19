# Console I/O Guide

## Overview
Bhojya v1.0 includes robust console input/output functions for terminal-based programs.

## Available Functions

### Output Functions

#### `rt_sacho(value)`
Prints an integer to the console.

```bhojya
rt_sacho(42);  +++ Prints: 42
rt_sacho(100 + 50);  +++ Prints: 150
```

#### `rt_sacho_sandesh(0)`
Prints a string from the global buffer.

```bhojya
+++ (String handling requires buffer management)
rt_sacho_sandesh(0);
```

### Input Functions

#### `rt_lelo()`
Reads an integer from the console and returns it.

```bhojya
chanchal x = rt_lelo();
rt_sacho(x * 2);
```

#### `rt_lelo_line()`
Reads a line of text into the global buffer.

```bhojya
rt_lelo_line();
+++ Buffer now contains the line
```

## Examples

### Simple Calculator
```bjoyha
kaam mukhya() {
    rt_sacho(1);  +++ "Enter first number:"
    chanchal a = rt_lelo();
    
    rt_sacho(2);  +++ "Enter second number:"
    chanchal b = rt_lelo();
    
    rt_sacho(a + b);  +++ Print sum
    0
}
```

### Counter
```bhojya
kaam mukhya() {
    rt_sacho(999);  +++ "Count to:"
    chanchal limit = rt_lelo();
    
    chanchal i = 1;
    jabtak (i < limit + 1) {
        rt_sacho(i);
        i = i + 1
    };
    
    0
}
```

## Compiling Console Programs

```powershell
# Include the console module
lathi std/console.bjy my_program.bjy

# Run
.\output.exe
```

## Notes
- Input is buffered (waits for Enter key)
- Invalid input returns 0 for integers
- Error handling clears input buffer automatically
- Use `fflush` is handled internally
