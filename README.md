NISL
====

a Python library

NISL(working title), or, the Native Instruments Support Library is a library for Python that is aimed at trivializing several
support tasks through the use of Python functions. This library aims to be light-weight, only incorporating a small
subset of Python. Most importantly, it is aimed at being accessible. Reading and writing scripts that make use of
the library should be trivial. Creating this library is the first step in the creation of a domain-specific
language optimized for supporters at Native Instruments.


Tasks that will be implemented in this library include the following:

1. moving, copying, or renaming files and directories
2. reading and writing from/to files (.plist, .xml, etc.)
3. reading or editing Windows registry keys/values
4. deleting Windows registry keys/values


Tasks that are being considered for implementation include the following:

1. downloading installer files from a website or FTP server
2. launching installer files that have been downloaded



Consider the following example which demonstrates how NISL trivializes the task of deleting a registry key's value.
(see reg.py for implementation)

reg_key_delete_value(r"HKEY_CURRENT_USER\SOFTWARE\Native Instruments\Massive", r"AB2 AudioDevice")


There are two main options for implementing this library in the NI Support Tool: 

The first is statically linking Python to the Support Tool application itself. This configuration requires zero 
dependencies, making distribution a trivial matter; however, it makes compiling the application more complex.

The second option is dynamically linking a Python interpreter with the application. This would create
dependencies which would need to be included inside the application folder; however, compiling such an application
would be simpler.

Check out hello_world.cpp and hello_world.py to see how to embed a python function into a C++ application.

