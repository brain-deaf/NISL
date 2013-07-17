#include <Python.h>

int main(int argc, char *argv[]){
  Py_Initialize();
  PyRun_SimpleString("from hello_world import say_hello\n"
                     "say_hello()\n");
  Py_Finalize();
  return 0;
}