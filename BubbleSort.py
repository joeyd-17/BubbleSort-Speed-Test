import matplotlib.pyplot as plt
import os
import platform
import subprocess
from subprocess import Popen, PIPE, check_output
import time

# Flags to determine which part of the file to run and how much to print to the console
debug = True
#Change these to True when you are ready to run the Python and C++ simulations
runPython = True
runCpp = True
runOcaml = True
runJava = True
runC = False

# Create empty lists that will store the bubble sort runtimes
pythonTimes = []
cppTimes = []
ocamlTimes = []
javaTimes =[]
cTimes = []


# Python sorting
if runPython:
    # Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
            print(f"Let's see how long it takes Python to bubble sort {size} random integers from a file!")

        # Start the clock
        tic = time.time()

        # Read numbers from file
        nums = []
        with open('numbers.txt') as file:
            # Make sure we only read in size integers
            nums = [int(next(file)) for x in range(size)]

        # If debug is true, print vector size to make sure it matches number in previous print statement
        if debug:
            print(f"Vector size: {len(nums)}")

        # Bubble sort algorithm
        haveSwapped = True
        maxIndex = len(nums) - 1
        while haveSwapped:
            haveSwapped = False
            for i in range(maxIndex):
                if nums[i+1] < nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    haveSwapped = True
            maxIndex -= 1
        
        # If debug is true, print the first and last ten numbers to demonstrate correct sorting
        if debug:
            print("To show that it worked, here are the first ten and last ten numbers:")
            print(nums[:10])
            print("...")
            print(nums[-10:])

        # End clock
        toc = time.time()

        # If debug is true, print the time it took Python to sort the integers
        if debug:
            print(f"Python Bubble Sort finished in {(toc - tic):0.6f} seconds")
        
        # Add the runtime to the list
        pythonTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of Python runtimes
    if debug:
        print("Python times:")
        print(pythonTimes)

# C++ sorting
if runCpp:
    # Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        #If debug is true, print statement to show where you are in the program
        if debug:
            print(size)

        #Start the clock
        tic = time.time()

        try:
            # This is Python's way of calling the command line. We use it to compile the C++ files.
            subprocess.check_output("g++ -std=c++17 BubbleSort.cpp",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in BubbleSort.cpp. Print out the error message and exit the program.
            print("<p>",e.output,"</p>")
            raise SystemExit

        # Depending on your OS, different executable files will be produced. Run the executable.
        if platform.system() == 'Windows':
            p = Popen('a.exe '+str(size), shell=True, stdout=PIPE, stdin=PIPE)
            # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
            if debug:
                print(p.stdout.read().decode('utf-8'))
            os.remove("a.exe")
        else: # Mac and Linux case
            p = Popen(['./a.out '+str(size)], shell=True, stdout=PIPE, stdin=PIPE)
            # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
            if debug:
                print(p.stdout.read().decode('utf-8'))
            os.remove("a.out")
        
        #End clock
        toc = time.time()

        #If debug is true, print the time it took C++ to sort the integers
        if debug:
            print(f"C++ bubble sort finished in {(toc - tic):0.6f} seconds")
        
        #Add the runtime to the list
        cppTimes.append(toc - tic)

    #If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("c++ times:")
        print(cppTimes)
        

# Java Sorting
if runJava:
    # Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        #If debug is true, print statement to show where you are in the program
        if debug:
            print(size)

        #Start the clock
        tic = time.time()
        
        try:
<<<<<<< HEAD
            # Compile the Java file
            subprocess.run(["javac", "BubbleSort.java"], check=True)
            
            # Run the Java program, passing size as a command-line argument
            p = Popen(["java", "BubbleSort", str(size)], stdout=PIPE, stderr=PIPE)
            output, error = p.communicate()

            if debug:
                print(output.decode("utf-8"))
                if error:
                    print("Java error output:", error.decode("utf-8"))
=======
            #subprocess.run(["javac", "BubbleSort.java"])
            subprocess.run(["java", "BubbleSort"])
            # Depending on your OS, different executable files will be produced. Run the executable.
            if platform.system() == 'Windows':
                p = Popen('a.exe '+str(size), shell=True, stdout=PIPE, stdin=PIPE)
                # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
                if debug:
                    print(p.stdout.read().decode('utf-8'))
                #os.remove("a.exe")
            else: # Mac and Linux case javac HelloWorld.java java HelloWorld
                p = Popen(['./a.out '+str(size)], shell=True, stdout=PIPE, stdin=PIPE)
                # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
                if debug:
                    print(p.stdout.read().decode('utf-8'))
                os.remove("a.out")
>>>>>>> 364c672575b038fcf7438a6121fd92ffd551c57b
        except subprocess.CalledProcessError as e:
            print("<p>", e.output, "</p>")
            raise SystemExi
        
        #End clock
        toc = time.time()

        #If debug is true, print the time it took Java to sort the integers
        if debug:
            print(f"Java bubble sort finished in {(toc - tic):0.6f} seconds")
        
        #Add the runtime to the list
        javaTimes.append(toc - tic)

    #If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("Java times:")
        print(javaTimes)

# Ocaml Sorting
if runOcaml:
    for size in range(1000, 10001, 1000):
        if debug:
            print(size)
        
        #start the clock
        tic = time.time()

        try:
            #compile and run the ocaml file
            if platform.system() == "Windows":
                subprocess.run(["ocamlc", "-o", "a.exe", "BubbleSort.ml"])
                p = Popen("a.exe "+str(size), shell=True, stdout=PIPE, stdin=PIPE)

                if debug:
                    print(p.stdout.read().decode('utf-8'))
                os.remove("a.exe")
                os.remove("BubbleSort.cmi")
                os.remove("BubbleSort.cmo")

            else:
                subprocess.run(["ocamlc", "-o", "./a.out", "BubbleSort.ml"])
                p = Popen("./a "+str(size), shell=True, stdout=PIPE, stdin=PIPE)

                if debug:
                    print(p.stdout.read().decode('utf-8'))
                os.remove("./a")
                os.remove("a.exe")
                os.remove("BubbleSort.cmi")
                os.remove("BubbleSort.cmo")

        except subprocess.CalledProcessError as e:
            print("<p>",e.output,"</p>")
            raise SystemExit
        
        #End clock
        toc = time.time()

        #If debug is true, print the time it took ocaml to sort the integers
        if debug:
            print(f"Ocaml bubble sort finished in {(toc - tic):0.6f} seconds")
        
        #Add the runtime to the list
        ocamlTimes.append(toc - tic)

    #If debug is true, after all test runs, print the list of ocaml runtimes
    if debug:
        print("ocaml Times:")
        print(ocamlTimes)

# C Sorting
if runC:
    # Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        #If debug is true, print statement to show where you are in the program
        if debug:
            print(size)

        #Start the clock
        tic = time.time()

        try:
            # This is Python's way of calling the command line. We use it to compile the C++ files.
            subprocess.check_output("gcc BubbleSort.c -o sort",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in BubbleSort.c. Print out the error message and exit the program.
            print("<p>",e.output,"</p>")
            raise SystemExit

        # Depending on your OS, different executable files will be produced. Run the executable.
        if platform.system() == 'Windows':
            p = Popen('sort.exe '+str(size), shell=True, stdout=PIPE, stdin=PIPE)
            # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting====
            if debug:
                print(p.stdout.read().decode('utf-8'))
            os.remove("sort.exe")
        else: # Mac and Linux case
            p = Popen(['./sort '+str(size)], shell=True, stdout=PIPE, stdin=PIPE)
            # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
            if debug:
                print(p.stdout.read().decode('utf-8'))
            os.remove("./sort")
        
        #End clock
        toc = time.time()
        #If debug is true, print the time it took C++ to sort the integers
        if debug:
            print(f"C bubble sort finished in {(toc - tic):0.6f} seconds")
        
        #Add the runtime to the list
        cTimes.append(toc - tic)

    #If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("C times:")
        print(cTimes)

# Graph the results

# Create a list of the sizes to use for the x axis tick marks
sizes = range(1000, 10001, 1000)
# Create lists that are offset so the Python bars aren't overlapping with C++ bars in the graph
pythonX = [x - 400 for x in sizes]
cppX = [x - 240 for x in sizes]
ocamlX = [x - 80 for x in sizes]
cX = [x + 80 for x in sizes]
rustX = [x + 240 for x in sizes]
javaX = [x + 400 for x in sizes]
# Create a graph plot with one (1) row and one (1) column.
# The third 1 signals to start at the first subplot (aka subplot 1 out of 1)
ax = plt.subplot(111)
# If not all of the data has been collected, use dummy data
<<<<<<< HEAD
#if len(pythonTimes) < 10 or len(cppTimes) < 10 or len(ocamlTimes) < 10 or len(cTimes) < 10 or len(javaTimes) < 10:
if len(pythonTimes) < 10 or len(cppTimes) < 10 or len(javaTimes) < 10:
=======
if len(pythonTimes) < 10 or len(cppTimes) < 10 or len(ocamlTimes) < 10 or len(cTimes) < 10 or len(rustTimes) < 10 or len(javaTimes) < 10:
>>>>>>> 364c672575b038fcf7438a6121fd92ffd551c57b
    # Plot the dummy values in blue
    print("hello")
    ax.bar(sizes, range(1, 11), width=300, color='b', align='center')
else:
    #Plot the Python bars in red
    ax.bar(pythonX, pythonTimes, width=160, color='r', align='center')
    #Plot the C++ bars in yellow
<<<<<<< HEAD
<<<<<<< HEAD
    ax.bar(sizes, cppTimes, width=300, color='y', align='center')
    #Plot the OCamel bars in green
    #ax.bar(sizes, ocamlTimes, width=300, color='g', align='center')
    #Plot the C bars in purple
    #ax.bar(sizes, cTimes, width=300, color='purple', align='center')
    #Plot the Java bars in orange
    ax.bar(sizes, javaTimes, width=300, color='orange', align='center')
=======
    ax.bar(cppX, cppTimes, width=200, color='y', align='center')
=======
    ax.bar(cppX, cppTimes, width=160, color='y', align='center')
>>>>>>> b0ab7e46c920ef934038fb1529beabe40fbb1368
    #Plot the OCaml bars in green
    ax.bar(ocamlX, ocamlTimes, width=160, color='g', align='center')
    #Plot the C bars in purple
    ax.bar(cX, cTimes, width=160, color='purple', align='center')
    #Plot the Java bars in blue
    ax.bar(sizes, javaTimes, width=160, color='b', align='center')
    #Plot rust bars in brown
<<<<<<< HEAD
    ax.bar(rustX, rustTimes, width=200, color='brown', align='center') 
>>>>>>> 364c672575b038fcf7438a6121fd92ffd551c57b
=======
    ax.bar(rustX, rustTimes, width=160, color='brown', align='center') 
>>>>>>> b0ab7e46c920ef934038fb1529beabe40fbb1368

# Set the window title
plt.gcf().canvas.manager.set_window_title('Speed Test')
# Set the graph title
<<<<<<< HEAD
plt.title('Python vs. C++ vs. Ocaml vs. C')
=======
plt.title('Python vs. C++ vs. Ocaml vs. C vs. Rust vs. Java')
>>>>>>> b0ab7e46c920ef934038fb1529beabe40fbb1368
# Label the x axis
plt.xlabel('Number of integers to sort')
# Make sure the x-axis tick marks/labels are at each 1000
plt.xticks(sizes)
# Label the y axis
<<<<<<< HEAD
<<<<<<< HEAD
plt.ylabel('Times in seconds (Python in red, C++ in yellow, Ocaml in Green, C in Purple)')
=======
plt.ylabel('Times in seconds (Python in red, C++ in yellow, Ocaml in Green, C in Purple, Rust in brown)')
>>>>>>> 364c672575b038fcf7438a6121fd92ffd551c57b
=======
plt.ylabel('Times in seconds (Python in red, C++ in yellow, Ocaml in Green, C in Purple, Rust in brown, Java in blue)')
>>>>>>> b0ab7e46c920ef934038fb1529beabe40fbb1368
# Save the graph to a file
plt.savefig('BattleOfTheBubbleSorts.png')
# Display the graph in a new window
plt.show()