# key-logger
Keylogger implemented using python

You can run main.py or you can have subproc.py internally call main.py
calling main.py directly is safer as it is easier to terminate. 
To terminate subproc is complicated as Interrupt keys will also be logged to file, so the current shell being used must be terminated.
