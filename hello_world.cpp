#include <Python.h>

int main(int argc, char *argv[]){
  Py_Initialize();
  PyRun_SimpleString("from hello_world import say_hello\nsay_hello()");
  Py_Finalize();
  return 0;
}