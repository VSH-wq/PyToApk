[app]
# (str) Title of your application
title = ClinicMGR

# (str) Package name
package.name = clinicmgr

# (str) Package domain (needed for android/ios packaging)
package.domain = org.vish.clinicmgr

# (str) Source code where the main.py (or your entry point) is located
source.dir = .

# (list) Source files to include (let Buildozer know what files to package)
source.include_exts = py, kv, png, jpg

# (str) The main .py file to use as the entry point.
# Since your file is named "Clinic MGR38.py", we specify it here.
entrypoint = main.py

# (list) Application requirements
# Only standard libraries and Kivy are used in your app.
requirements = python3, kivy

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (str) Application versioning
version = 0.1

# (list) Permissions required by the app.
# Even though you’re writing a local JSON file, these permissions may be useful
# if you later expand functionality.
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

# (str) Supported architecture
android.arch = arm64-v8a

# (str) Android bootstrap to use; sdl2 is recommended for Kivy apps.
android.bootstrap = sdl2

# Uncomment the following line if you want to force a full rebuild (useful when debugging crashes)
# p4a.force_build = True
