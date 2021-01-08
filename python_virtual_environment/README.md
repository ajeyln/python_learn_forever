<h1 align="Center"> Python Virtual Enviornment</h1>

## Table of Content

* [Introduction](#Introduction)
* [Content](#content)
    + [Installation](#Installation)
    + [Creating new directory to work with virtual environment](#directory)
    + [Creating Virtual Environment](#creation)
    + [Activation](#activation)
    + [Managing Packages with pip](#pip)
    + [Deactivation](#deactivation)
* [Useful Links](#useful)

## <a name="Introduction"></a> Introduction

Python applications will often use packages and modules that don’t come as part of the standard library. 
Applications will sometimes need a specific version of a library, That's why we need Python virtual enviornment <br />
Python virtual environments is to create an isolated environment for Python projects.This means that each project can have its own dependencies <br />

## <a name="content"></a>Content

### <a name="Installation"></a>Installation

We can installl virtual environment using the command: <br />
```pip install virtualenv```

### <a name="directory"></a>Creating new directory to work with virtual environment

The below in command line to create directory and moving inside directory<br />
```mkdir python-virtual-environments``` <br />
```cd python-virtual-environments```

### <a name="creation"></a>Creating Virtual Environment

The module used to create and manage virtual environments is called venv. It will usually install most recent version of Python. <br />
If we want multiple versions of Python on your system, we can select a specific Python version we need to mention during creation of virtual envieonment <br />

A sample command to create Virtual environment is : <br />
``` python3 -m venv test_env ```

when we want to install all packages/module same as in system while creating virtual enviornment <br />
```python -m venv test_env --system--site--packages```

This will create the test_env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter, the standard library, and various supporting files. <br />

### <a name="activation"></a>Activation

We can activate Virtual Enviornment using the command : <br />
```test_env/scripts/activate.bat```

After activation of virtual environment the command prompt prefixed with the name of virtual enviornment.

### <a name="pip"></a>Managing Packages with pip

* we can install, check and remove packages using pip. By default pip will install packages from the Python Package <br />

The following command are used to check packages in Virtual enviroment

|Command Name| Description|
|----------|---------|
|pip list | will display all of the packages installed|
|pip install | to install packages |
|pip freeze | list of the installed packages |

* We can maintain what python packages are required to run the scripts in virtual environment in requirements.txt by this command : <br />
```pip freeze > requirements.txt```

* when we received requirements.txt to install packages in virtual packages to run some python packages by using this command: <br />
```pip install -r requirements.txt```

* If we want to check what we installed in virtual environment by using the command: <br />
```pip list --local```

### <a name="deactivation"></a>Deactivation

we can deactivate the virtual environment using the command in command line <br />
```deactivate```

## <a name="useful"></a> Useful Links

| **Sl. No.** | **Link** | **Remarks** |
----------|--------------|--------------
1| [Python Virtual Enviroment Guide](https://docs.python.org/3/tutorial/)| Python Virtual Environment Guide |
2|[Python Virtual Enviroment Tutorial](https://www.youtube.com/watch?v=APOPm01BVrk) | Python Virtual Enviroment Tutorial |
