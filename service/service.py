import os
import socket
import subprocess

from flask import abort
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)
serviceOutput = "/tmp/service.out"


@app.route("/", methods=["GET"])
def list_employees():
    if os.path.exists(serviceOutput):
        os.remove(serviceOutput)
    start = request.args.get("s")
    number = request.args.get("n")
    # Need unique filenames to handle multiple requests
    f = open("/tmp/service.in", "w")
    if not start is None:
        f.write("s=" + start + "\n")
    if not number is None:
        f.write("n=" + number + "\n")
    f.write("\n")
    f.close()
    p = subprocess.Popen("natural etid=$$ madio=0 batchmode cmsynin=/service/list_employees.cmd cmobjin=/service/list_employees.cmd cmprint=/tmp/out natlog=err",
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    retval = p.wait()
    if retval != 0:
        abort(500)
        abort(Response("Natural returned with code " + retval))
    f = open(serviceOutput, "r")
    return f.read()


@app.route("/<personnelId>", methods=["GET"])
def get_employee(personnelId):
    if os.path.exists(serviceOutput):
        os.remove(serviceOutput)
    # Need unique filenames to handle multiple requests
    f = open("/tmp/service.in", "w")
    f.write(personnelId)
    f.close()
    p = subprocess.Popen("natural etid=$$ madio=0 batchmode cmsynin=/service/get_employee.cmd cmobjin=/service/get_employee.cmd cmprint=/tmp/out natlog=err",
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    retval = p.wait()
    if retval != 0:
        abort(500)
        abort(Response("Natural returned with code " + retval))
    f = open(serviceOutput, "r")
    return f.read()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
