# import sys
# sys.path += ["C:\\Users\\new\\Desktop\\java11.jar"]

# # from com.roc.printtest import PrintTest
# # PrintTest.printJava()
# from ideal4j.source.util import DesEncrypt
# DesEncrypt.main


import org.python.util.PythonInterpreter;
import org.python.core;
from org.python.core import *;

public class JythonTest { 
	public static void main(String[] args) {
		PythonInterpreter interp =
			new PythonInterpreter();
			System.out.println("Hello, brave new world");
			interp.exec("import sys");
			interp.exec("print sys");
			interp.set("a", new PyInteger(42));
			interp.exec("print a");
			interp.exec("x = 2+2");
			PyObject x = interp.get("x");
			System.out.println("x: "+x);
			System.out.println("Goodbye, cruel world!");
	}
}