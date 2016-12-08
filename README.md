# A Python Based Inventory Management System

### Introduction
* The Inventory Management System has been developed as part of the fulfilment of the Andela Boot Camp 13 in Nairobi, Kenya. The application 
manages the records of a warehouse where Items can be Checked in and out and their availability tracked.

### Commands Used
*   The Following are the commands that the application executes
     *   **item add <item_details>** - Adds an item to the inventory.
     *   **item remove <item_id>** - Removes an item from the inventory.
     *   **item list** - Lists all the items available in the inventory with their status (checked out or checked in).
     *   **item list --export <file_name>** - This command exports the entire inventory as a CSV file with all the fields listed above.
     *   **item checkout <item_id>** - Checkout an item from the warehouse/store.
     *   **item checkin <item_id>** - Checkin an item that was previously checked out.
     *   **item view <id>** - View all the item details for item with id <id>. In addition to that, this command shows a log of all the times this item was checked out and checked in.
     *   **item search <search_query>** - Return a list of all the items that match the search_query.
     *   **compute assetvalue** - Calculate total assets value. The sum of the cost of each item.

### Installation & Status

* Download & Install Python
     *    Go to the Python Downloads Site and download a version compatible with your operating system
     *    To confirm that you have successfully installed Python:
     *    Open the Command Propmpt on Windows or Terminal on Mac/Linux
     *    Type python
     *    If the Python installation was successfull you the Python version will be printed on your screen and the python REPL will start
 
 * Clone the repository to your personal computer to any folder
        * On GitHub, go to the main page of the repository [Inventory Management Appliation](https://github.com/live-beta/bc-13-Inventory-Management-Application)
        * On your right, click the green button 'Clone or download'
        * Copy the URL
        * Enter the terminal on Mac/Linux or Git Bash on Windows
        * Type git clone and paste the URL you copied from GitHub
        * Press Enter to complete the cloning process
        * Virtual Environment Installation
            * Install the virtual environment by typing: pip install virtualenv on your terminal
            * Install the required modules
        * Inside the directory where you cloned the repository run pip install -r requirements.txt
        * Run the Inventory Management Application:
        * On the terminal type python Classes/main.py to start the application
  
