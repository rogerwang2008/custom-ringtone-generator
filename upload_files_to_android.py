import os
import subprocess

ANDROID_ROOT_DIR = "/storage/emulated/0/CustomWechatNotification"

if __name__ == '__main__':
    for entry in os.scandir('./tasker_scripts'):
        if entry.is_file():
            print(entry)
            # device.push(entry.path, f"{ANDROID_ROOT_DIR}/{entry.name}")
            subprocess.call(f"adb -d push {entry.path} {ANDROID_ROOT_DIR}/{entry.name}")

    subprocess.call(f"adb -d shell rm -rf {ANDROID_ROOT_DIR}/Ringtones")

    subprocess.call(f"adb -d push ./output {ANDROID_ROOT_DIR}/")
    subprocess.call(f"adb -d shell mv {ANDROID_ROOT_DIR}/output {ANDROID_ROOT_DIR}/Ringtones")
