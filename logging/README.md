<h1 align="Center"> Logging</h1>

## Table of Content

* [Background](#background)
* [Content](#content)
    + [Levels](#levels)
    + [Basic Configuration](#testcase)
        * [Level](#level)
        * [File Name](#filename)
        * [Format](#format)
    + [Handler](#handler)
    + [Configuration for Pytest files](#test)
    + [Useful Links](#useful)



## <a name="background"></a> Background

Logging is a very useful tool. It helps us to develop a better understanding of the flow of a program and discover 
scenarios.<br />

Logs provide developers with an extra set of information that are constantly looking at the flow.
It can store information, like If an error occurs, then they can provide more insights than a stack trace. <br />

## <a name="content"></a>Content

### <a name="levels"></a>Levels <br />

There are 5 standard levels indicating the severity of events.

+ DEBUG - Detailed information, typically of intrest only when diagnosing problems.<br />

+ INFO - Confirmation that things are working as expected <br />

+ WARNING - An indication that something unexpected happend, or indication of the some problems in the near fututure ("Disk space low"). The software is still working as expected. <br />

+ ERROR - Due to more serious problem, the software has not been able to perform some functions <br />

+ CRITICAL - A serious error, indicating that the program itself may be unable to to continue running.<br />

Eg: 

```python
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```
The Log file is generated for the above script is : <br />

```WARNING:root:This is a warning message``` <br />
```ERROR:root:This is an error message``` <br />
```CRITICAL:root:This is a critical message``` <br />

Note: by default, the logging module logs the messages with a severity level of WARNING and above <br />

### <a name="basic"></a> Basic Configuration <br />
This is the configuration method, how the log file should be generated using the various parameters <br />

Some of the commonly used parameters for ```basicConfig()``` are the following:

+ **level** The root logger will be set to the specified severity level. <br />
+ **filename** This specifies the file. <br />
+ **format** This is the format of the log message <br />

+ <a name="level"></a> **Level** <br />
By using the level parameter, we can set what level of log messages.
Eg:
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
```
The Log file is generated for the above script is : <br />
```DEBUG:root:This will get logged```<br />
All events at or above DEBUG level will now get logged as the level is set to debug.

+ <a name="filename"></a> **Filename** <br />
By using the filename parameter, we can save the log with specific file name

Eg: 
```python
import logging

logging.basicConfig(filename='app.log', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
```
The Log file is generated for the above script is : <br />
```root - ERROR - This will get logged to a file``` <br />
The log messages are saved in app.log file <br />

+ <a name="format"></a> **Format** <br />
By using the format parameter, we can update the format of generated log files.

The common attribute for the formats as follows <br>
|Attribute name | Format | Description|
|------------|-----------|-----------|
|message |%(message)s |The logged message |
| asctime | %(asctime)s |Human-readable time when the LogRecord was created.|
|created |%(created)f |Time when the LogRecord was created |
| filename |%(filename)s |Filename portion of pathname. |
|funcName | %(funcName)s | Name of function containing the logging call.|
| levelname |%(levelname)s |Text logging level for the message |

Eg:
```python
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')
```
The Log file is generated for the above script is : <br />

```2018-07-11 20:12:06,288 - Admin logged in```

### <a name="handler"></a> Handler <br />
When we want to configure the logs output as per the level, we can do by using file handler <br />

We need to add the handler after the it is created using ```<logger name>.addHandler(<handler name>)```

Threre are two handler in logging 
+ File Handling - The log files will be generated in file.<br />
We can generate logs in files using the file handler ```logging.FileHandler(<file name>)```

+ Stream Handling - The log files will be generated in console. <br />
We can generate logs inconsole usinng stream handler ```logging.StreamHandler()```

Eg: 
```python
import logging

# Create a custom logger, 
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler() # Generating stream handler
f_handler = logging.FileHandler('file.log') # Generating File handler
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
```

### <a name="test"></a> Configuration for Pytest files <br />
If we need to configure log for test cases, we need to do as follows

+ Create a file with file name "pytest.ini" and write on that as shown below:
```
[pytest]
log_file = <file path>
log_file_level = DEBUG 
log_file_format = %(pathname)s %(asctime)s %(message)s
log_file_date_format = %Y-%m-%d %H:%M:%S
```
+  Update in the test file as follows :
```python 
<logger name> = logging.getLogger(__name__)
logging.basicConfig(level=logging.<level name>)
```

## <a name="useful"></a> Useful Links

| **Sl. No.** | **Link** | **Remarks** |
----------|--------------|--------------
1| [Logging Basic](https://www.youtube.com/watch?v=-ARI4Cz-awo)| Python logging - Basic Tutorial |
2| [Logging Advanced](https://www.tutorialspoint.com/pytest/index.htm) | Python logging - Advanced Tutorial |
3 | [Python Logging](https://docs.python.org/3/library/logging.html)| Python logging Tutorial|
