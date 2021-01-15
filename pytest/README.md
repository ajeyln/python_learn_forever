<h1 align="Center"> Pytest</h1>

## Table of Content

* [Background](#background)
* [Content](#content)
    + [Installation](#Installation)
    + [Creating test case](#testcase)
    + [Running Pytest](#running)
    + [Pytest Code Coverage](#code_coverage)
    + [Types of Test Cases](#test_cases)
        * [Assertions](#assertion)
        * [Assert no exception](#assert_no)
        * [Assert exception](#assert_exc)
        * [Input function](#input)
        * [Output function](#output)
        * [Monkey Patching](#monkey)
        * [Monkey Patching set attribute](#setattr)
        * [Monkey Patching add items to dictionary](#setitem)
        * [Monkey Patching delete items from dictionary](#delitem)
    + [Fixtures](#fix)
        * [parameterized fixture](#param)
* [Useful Links](#useful)

## <a name="background"></a> Background

pytest is a mature full-featured Python testing tool that helps us to write better programs.<br />
The pytest framework makes it easy to write small tests, yet scales to support complex functional
testing for applications and libraries.<br />

## <a name="content"></a>Content

### 1. <a name="Installation"></a>Installation

We can installl Pytest using the command: <br />
```pip install -U pytest```

### 2. <a name="testcase"></a>Creating a test case

The following script is to add a number to given number and return
``` python
def func(x):
    return x + 1 
```
for the above script, we are creating a test case as follows

```python
def test_answer():
    assert func(3) == 4
```
when we execute the test case, the function test_answer calls the function of other file (func) <br />
when the test function passes the value as 3 to func function and it will execute and return the value as 4 <br />
assert will compare, <br />
+ If the condition is true then test case passes condition.
+ If condition fails, test case fails and display as AssertionError

### 3. <a name="running"></a> Running Pytest

+ If we have multiple test files and want to run all the tests from all the files in the folder and subfolders <br />
we need to just run the pytest command: <br />
```pytest ```

+ If we want to run tests only from a specific file, we can use <br />
```pytest <test_sample1.py>```

+ If we want to know which are all test cases are executed in file, we can use <br />
```pytest -s -v``` <br/>
![pytest_test_result](/images/pytest_s_v.PNG)

### 4. <a name="code_coverage"></a> Pytest Code Coverage

Code coverage is a software testing metric that determines the number of lines of code that is successfully validated under a test procedure. <br />
It helps in analyzing how comprehensively a software is verified.

+ We can installe the Pytest coverage using the command: <br />
```pip install pytest-cov```

+ If we want check the code coverage Pytest, we can use the following command: <br />
```pytest --cov= <source> test ```
<br />here source is the set of files or a file, which we want to check the code coverage

+ If we need Pytest Code Coverage in html format, we can use the following command: <br />
```Pytest --cov-report html --cov=<source> test```
<br /> one we are running this comman,It will generate a folder with the name "htmlcov" <br />
It has html formatted file with file name, We can open on browser and we can check the code coverage the perticular file. <br />
![pytest_code_coverage](/images/pytest_code_coverage.PNG)

### <a name="test_cases"></a> Types of Test Cases
+ <a name="assertion"></a> Assertions

    + Assertions are checks that return either True or False status. <br />
In pytest, if an assertion fails in a test method, then that method execution is stopped. <br />
The remaining code in that test method is not executed and pytest will continue with the next test method. <br />

    Error methods if,
``` python
assert "hello" == "Hai" is an assertion failure.
assert 4==4 is a successful assertion
assert True is a successful assertion
assert False is an assertion failure.
```
+ <a name="assert_no"></a>**Assert no exception** <br />

    In any script raises exception during pytest and we want to disbale those exception 

Eg:
```python
PERSON_DET = {'Name':'Sachin', "Surname" : "Singh"}

def del_info_dict(config=None):
    '''to find person info'''
    return f"Name={PERSON_DET['Name']}; Surname={PERSON_DET['Surname']};"

def test_missing_user(monkeypatch):
    "to check dictionary after deleting key values"
    monkeypatch.delitem(sociallife.PERSON_DET, "Name", raising=False)

    with pytest.raises(KeyError):
        _ = del_info_dict()
```
In the above the example, the items in the dictionary PERSON_DET are getting deleted while we are using the function monkeypatch.delitem() <br />
we can avoid the exception error using raising=False method.

+ <a name="assert_exc"></a>**Assert Exception** <br />

    when script is throwing an exception error and source file is manipulated by someone. We can create an exception.

Eg:
```python
'''This function will multiply two integer numbers'''
def mul_num(a,b):
    temp = a * b
    # If someone change multiplication(*) to division(/),it will generate zero division error
    return temp

def test_mul_num():
    ''' to test mul_num function in libraries.operation file'''
    try:
        mul_num(10, 0)
    except Exception as exc:
        pytest.fail(f"Test is failed due to {exc}")
```
In the above the example when source code is manipulated the pytest will throw an error with the exception.

+ <a name="input"></a>**Input function**

    When we want to test the scripts by giving input in test file using <br />
``` built.input``` in monkeypath.setattr()

Eg:
```python
def test_find_friend_surname(monkeypatch):
    ''' to find the friends surname in dict'''
    monkeypatch.setattr('builtins.input', lambda prompt="":"Bharat")
    # here we have set the input as "Bharat"
    expected_value = "Pai"
    assert expected_value == find_friend_surname()
```

+ <a name="output"></a>Output function

    When we want to know the output while running pytest, we can check using <br/> 
``` capsys.readouterr()```.

Eg:
```python
def test_base_file(capsys):
    "to check greetings"
    say_hello()
    out,err = capsys.readouterr()
    expected_value = "Hello World\n"
    assert out == expected_value
    assert err ==""
```
+ <a name="monkey"></a> **Monkey Patching** <br />
Sometimes in tests we need to invoke code which cannot be easily tested such as Operating system, System configuration etc <br />

+ <a name="setattr"></a> **Monkey Patching Set Attribute** <br />
    When we want to modify the behaviour of functions for test cases,
we can do this by using ```monkeypatch.setattr()``` <br />
Syntax: 
```
monkeypatch.setattr(obj, name, value, raising=True)
```
Eg:
```python 
def test_find_windows_path_separator(monkeypatch):
    ''' this function is to check the os information'''
    monkeypatch.setattr(platform, "system", lambda : "Windows")
    expected_value = "\\"
    assert expected_value == find_os_path_separator()
```
+ <a name="setitem"></a> **Monkey Patching Set Items**<br />
    When we to add an item to dictionary in test cases <br />
we can do this by using  ```monkeypatch.setitem()``` <br/>
Syntax: 
```python
monkeypatch.setitem(mapping, name, value)
```
Eg:
```python
def test_mod_info_dict(monkeypatch):
    "to check dictionary with values"
    monkeypatch.setitem(sociallife.PERSON_INFO, "Name", "Akash")
    monkeypatch.setitem(sociallife.PERSON_INFO, "Surname", "Sharma")
    expected_value = "Name=Akash; Surname=Sharma;"
    assert expected_value == mod_info_dict()
```
+ <a name="delitem"></a> **Monkey Patching Delete Items**<br />
 
When we to delete an item in dictionary in test cases. <br />
we can do this by using  ```monkeypatch.setitem()```
Syntax: 
``` python
monkeypatch.setattr(obj, name, value)
```
Eg:
```python
def test_missing_user(monkeypatch):
    "to check dictionary after deleting key values"
    monkeypatch.delitem(sociallife.PERSON_DET, "Name", raising=False)

    with pytest.raises(KeyError):
        _ = del_info_dict()
```
### <a name="fix"></a> Fixtures

Fixtures are functions, which will run before each test function and are used to feed some data to the tests <br />

Eg : In below example, when we run the pytest, the function input_value will execute first , as the function is marked as fixtured.
```python
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
```
+ <a name="param"></a></a>**Parametrizing fixtures** <br />
The decorator enables parametrization of arguments for a test function.

    Eg: While running pytest for the below script, It will take arguments from parameterized fixture <br />
    There are totally 3 sets of argument in below example and based on this arguments pytest will generate test results.

```python
import pytest
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

## <a name="useful"></a> Useful Links

| **Sl. No.** | **Link** | **Remarks** |
----------|--------------|--------------
1| [Pytest Tutorial](https://www.youtube.com/watch?v=byaxg00Gf9I&feature=emb_logo)| Pytest Tutorial |
2| [Pytest Tutorial - 2](https://www.tutorialspoint.com/pytest/index.htm) | Pytest Tutorial |
3 | [Pytest Tutorial - 3](https://docs.pytest.org/en/stable/)| Pytest Tutorial|
4| [Pytest Code Coverage](https://pypi.org/project/pytest-cov/)| Pytest Code Coverage Tutorial
