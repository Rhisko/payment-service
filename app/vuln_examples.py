import os
import pickle
import subprocess
import tempfile
from xml.etree import ElementTree as ET

import requests

# INTENTIONAL vulnerabilities for scanning pipeline
HARD_CODED_SECRET = "API_KEY=12345-SECRET-KEY"
DATABASE_URL = "postgres://dbuser:dbpass@localhost:5432/payments"


def insecure_exec(payload: str):
    # INTENTIONAL VULNERABILITY: arbitrary code execution
    exec(payload)


def insecure_shell(command: str):
    # INTENTIONAL VULNERABILITY: shell injection
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def insecure_pickle(data: bytes):
    # INTENTIONAL VULNERABILITY: unsafe deserialization
    return pickle.loads(data)


def insecure_tempfile():
    # INTENTIONAL VULNERABILITY: insecure temporary file creation
    path = tempfile.mktemp()
    with open(path, "w") as f:
        f.write("user data")
    return path


def insecure_ssl_request(url: str):
    # INTENTIONAL VULNERABILITY: disabling SSL verification
    return requests.get(url, verify=False)


def insecure_xml_parse(xml_payload: str):
    # INTENTIONAL VULNERABILITY: XML external entity (XXE) style parsing
    parser = ET.XMLParser(resolve_entities=True)
    return ET.fromstring(xml_payload, parser=parser)


if __name__ == "__main__":
    print(insecure_tempfile())
