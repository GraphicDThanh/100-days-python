# Day 10 - Beginner - Function with Outputs

## Function with Outputs
```python
def my_function():
    return 3 * 2
```

* Example
```python
def format_name(f_name, l_name):
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return `{format_f_name} {format_l_name}`

print(format_name("Thanh", "Nguyen"))
```


## Function with multiple outputs
* Example
```python
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"Result: {format_f_name} {format_l_name}"

print(format_name("Thanh", "Nguyen"))
```

## Practice: day in months
## Final project: caculator