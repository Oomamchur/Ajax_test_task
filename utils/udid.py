import subprocess


def device_udid() -> str:
    output = subprocess.check_output(["adb", "devices"]).decode("utf-8")
    udid = output.strip().split("\n")[1].split()[0]
    return udid
