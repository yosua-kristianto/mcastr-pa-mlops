from pathlib import Path
import time;
import os;

class Log:
    @staticmethod
    def _write_log(log, type):
        """ Writing things like [2023-10-01T00:00][INFO] Some message
        The log file can be seen at logs folder

        File name is current time session with format of [McAstr MLOps - Session Ymd H:i]
        """
        log_path = "logs/" + "McAstr MLOps - Session" + time.strftime("%Y%m%d") + ".log";
        
        if(Path(log_path).is_file()):
            operation = "a"
            
        full_log = "[" + time.strftime("%Y-%m-%d %H:%M:%S") + "]" + "["+ type +"]"+ log
        
        print(full_log)

        fopen = open(log_path, operation);
        fopen.write(full_log + "\n");
        fopen.close();

    @staticmethod
    def i(log):
        Log._write_log(log, "INFO");

    @staticmethod
    def e(log):
        Log._write_log(log, "ERROR");

    @staticmethod
    def d(log):
        Log._write_log(log, "DEBUG");

    @staticmethod
    def v(log):
        Log._write_log(log, "VERBOSE");