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
## <a name="useful"></a> Useful Links

| **Sl. No.** | **Link** | **Remarks** |
----------|--------------|--------------
1| [Pytest Tutorial](https://www.youtube.com/watch?v=byaxg00Gf9I&feature=emb_logo)| Python Virtual Environment Guide |
