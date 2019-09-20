# Python CLI

## Steps
1. Create a Virtual env. ``` python3 -m virtualenv clienv ```. This creates the local copy of python and pip in the folder `clienv`.
2. Activate the virtual environment ``` . clienv/bin/activate ```. This activates the virtualenv so that python and pip commands now use the locally installed modules within folders: ```clienv/bin; clienv/include; clienv/lib```.
3. After the above command you would now see `(clienv)` added in your terminal indicating use of local env. You can also run `which python3` or `which pip` to confirm these are now using your local versions of pip and python.
4. Create a python package by creating a `setup.py` file.
5. In `setup.py`, the `py_modules` will look for the `hello.py` file. In `entry_points`,  `hello:cli` will look for the `cli` method in `hello.py`.
6. Run the command `pip install --editable .` This command basically looks for the `setup.py` file and installs the executable in local machine. *Read more on this later*.
7. Here is what happens when you run this command:
```
$ pip3 install --editable .
Obtaining file:///Users/manyu/ws/sandbox/pyCLIs
Collecting Click (from HelloWorld==1.0.0)
  Using cached https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl
Installing collected packages: Click, HelloWorld
  Running setup.py develop for HelloWorld
Successfully installed Click-7.0 HelloWorld
```
8. Now the executable `hello` has been created:
```
$ hello
Hello World!
```
9. The executable is installed to local: 
``` 
/Users/manyu/ws/sandbox/pyCLIs/clienv/bin/hello
```
10. Note that print has some problems with click, so use echo instead which works much better with Unicode chars with click framework. For example use ``.

11. NOTE that click.arguments cannot have help text added at the annotation. They must be defined within the documentation tags instead.


