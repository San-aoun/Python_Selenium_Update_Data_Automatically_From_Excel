# Add reference ticket that missing in testrail.
This is a automation framework for python language and before using it you need to install some modules.

# Steps and summaries:

1. Install IDE (visual studio)

2. Get access to necessary repositories/documents

3. Clone automation repository to your local

4. Install libraries that required to run automation code

5. Set environment variables that necessary to run automation code

### Python version : 
Python 3.11.1
pip 23.1.2

1. Cloning the repository:
    git clone ....

2. Installing all the dependencies:
    2.1 cd path/to/testrail_add_reference_ticket
    2.2 pip install -r requirements.txt

### How to run with command :
in case you use VSCode
1. Right-click anywhere in the editor window and select Run Python File "addReferencToTestRail.py" in Terminal (which saves the file automatically)

### Prepare data excel : 
1. Ensure your excel is ready to use with FunctionalTestCases.xlsx with column such as Card Ref and Title

### Architecture
/framework:

    base/
        base_element.py          #Super class to our actual Page Objects and get all the asserts that come with a TestCase

    helper/
        elementVariable.py            #Used to generate de WebDriver driver.
        properties.py              #Used to manage page objects.
        wait_until.py              #Used to manage page objects.

    step/                           #Folder where classes that implement Pages mapping according to PageObjects.
        baseStep.py

    addReferenceToTestRail.py
    FunctionalTestCases.xlsx
