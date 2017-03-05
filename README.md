My Resume
=========

This repo holds my resume as a restructuredText file and the code needed to turn it into a PDF.

Due to [rst2pdf not running on python3](https://github.com/rst2pdf/rst2pdf/issues/600), build.py requires python2 to run.

To generate the PDF
-------------------

1. Create a file named `secrets.yaml`:

   Here's an example of how it should look:

   ```
   ---
   address: "123 Main Street, Somewhere, CA 12345"
   phone: "555-867-5309"
   email: "noneya@example.com"
   ```

2. Install the requirements for the python script

   ```
   pip install -r requirements.py
   ```

3. Run build.py

   ```
   python2 build.py
   ```


