# localscope
gradescope-like testing for local instances via CLion

# Installation
here's what chatGPT has to say about how to install python and pytest in clion and then adding a target: (Added my own own comments, in **bold**)

## Get the program!
First you must download the repository **OR** copy the file `test_run.py` to your root project folder

## Now install Python etc...
1. **Install the Python Plugin:**
   Ensure that the Python plugin is installed and enabled in CLion.

2. **Configure a Python Interpreter:**
   - Open CLion and navigate to `File > Settings` (or `CLion > Preferences` on macOS).
   - In the settings window, go to `Project: <Your Project Name> > Python Interpreter`.
   - Configure a Python interpreter for your project.

3. **Install pytest using pip:**
   - Open the terminal in CLion.
   - Run the following command to install pytest:
     ```bash
     pip install pytest
     ```
   - This will install pytest in your selected Python environment.

4. **Create a Pytest Configuration:**
   - Open the `Run/Debug Configurations` dialog by clicking on the dropdown menu near the top-right corner of the CLion window and selecting `Edit Configurations`.
   - Click the `+` button to add a new configuration and choose `Python tests > pytest`.
   - Configure the pytest run configuration according to your project structure and requirements.

5. **Specify Target Directory:**
   - In the pytest configuration, specify the target directory where your tests are located. **In our case this is the main folder so DO NOTHING**

6. **Run the Pytest Configuration:**
   - After configuring the pytest run, click `OK` to close the configuration dialog.
   - Run the pytest configuration by clicking the green "Run" arrow or use the associated hotkey.

7. **View Test Results:**
   - CLion should execute your pytest tests, and you can view the results in the Run tool window.

By following these steps, you should be able to set up and run pytest tests in CLion, and the pytest package will be installed using pip if it's not already present in your Python environment.

# How To Run
- edit the `test_run.py` file so that:
    - `EXEC_PATH` contains the path to your executable - this should be an executable (.exe, ELF etc..) in `cmake-build-debug` for example
    - `TEST_SPEC` contains the path to your student_test.json file, although the exact name doesn't matter as long as it's a valid json file