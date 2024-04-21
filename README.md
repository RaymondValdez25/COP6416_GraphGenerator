Description:
This was an assignment for the University of West Florida where we had to create a GUI that demonstrates graph traversal methods and minimum spanning trees.

Please use Python 3.8.10 or above.

Steps to run the GUI:
1. Install the requirements by running command "pip install -r requirements.txt"
2. Run the GUI by running command "Python GraphUI.py"

Steps to run the data analysis:
1. Run data_analysis.py. This will generate a new data_analysis.csv and input_vs_time.csv
    Note: Feel free to modify the data analysis parameters as described in the "if __main__" area. With the default large number of tests/input sizes, it will take a moment to run. If it takes more than a couple minutes, try reducing the input sizes.
2. Run results_visualization.ipynb. This will display the data from the newly-generated csv files

Current Issues:

When you run the command "Python GraphUI.py" and encounter the error "RuntimeError: module compiled against API version 0x10 but this version of numpy is 0xf" run the command: "pip install numpy --upgrade"
