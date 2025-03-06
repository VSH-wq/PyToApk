[app]
# (str) Title of your application
title = Clinic Manager

# (str) Package name
package.name = clinicmgr

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py (or your entry point) is located
source.dir = .

# (list) Source files to include (let Buildozer know what files to package)
source.include_exts = py, kv, png, jpg

# (str) The main .py file to use as the entry point.
# Since your file is named "Clinic MGR38.py", we specify it here.
entrypoint = main.py

# (list) Application requirements
requirements = python3, kivy==2.0.0

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (str) Application versioning
version = 0.1

# (list) Permissions required by the app.
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
# (int) Log level (2 = debug)
log_level = 2

# (bool) Raise an error if running as root (0 to disable)
warn_on_root = 1

[android]
# (int) Target Android API, use a recent API level for modern devices.
android.api = 33

# (str) Android NDK version to use (adjust if necessary)
android.ndk = 21b

# (str) Android bootstrap to use; sdl2 is recommended for Kivy apps.
android.bootstrap = sdl2

# Enable universal APK to include support for all architectures
android.universal_apk = True
