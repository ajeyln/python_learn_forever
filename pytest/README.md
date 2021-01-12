<h1 align="Center"> Pytest</h1>

## Table of Content

* [Background](#background)
* [Content](#content)
    + [Installation](#Installation)
    + [Creating test case](#testcase)
* [Useful Links](#useful)

## <a name="background"></a> Background

pytest is a mature full-featured Python testing tool that helps us to write better programs.<br />
The pytest framework makes it easy to write small tests, yet scales to support complex functional
testing for applications and libraries.<br />

## <a name="content"></a>Content

### <a name="Installation"></a>Installation

We can installl Pytest using the command: <br />
```pip install -U pytest```

### <a name="testcase"></a>Creating a test case

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

### <a name="assertion"></a> Assertions in PyTest

Assertions are checks that return either True or False status. <br />
In pytest, if an assertion fails in a test method, then that method execution is stopped. <br />
The remaining code in that test method is not executed and pytest will continue with the next test method. <br />

Error methods if,
``` python
assert "hello" == "Hai" is an assertion failure.
assert 4==4 is a successful assertion
assert True is a successful assertion
assert False is an assertion failure.
```

### <a name="multiple_files"></a> Run multiple tests from a specific file and multiple files

If we have multiple test files and want to run all the tests from all the files in the folder and subfolders <br />
we need to just run the pytest command: <br />
```py.test ```

If we want torun tests only from a specific file, we can use py.test <filename><br />
```py.test test_sample1.py```

### <a name="fixture"></a> Pytest fixtures

Fixtures are used when we want to run some code before every test method. <br />
So instead of repeating the same code in every test we define fixtures. <br /> 
Usually, fixtures are used to initialize database connections, pass the base , etc. <br />

A method is marked as a fixture by marking with

```@pytest.fixture```

## <a name="useful"></a> Useful Links

| **Sl. No.** | **Link** | **Remarks** |
----------|--------------|--------------
1| [Pytest Tutorial](https://www.youtube.com/watch?v=byaxg00Gf9I&feature=emb_logo)| Pytest Tutorial |
