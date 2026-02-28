


''' todo:

import win32print
import subprocess
from escpos.printer import Usb

from AppUtils import Log


class Printer:

    # Windows: Using win32print: This module, part of the pywin32 library, allows direct interaction with the Windows printing system.
    #
    # printOnWindows("Your Printer Name", "Hello from Python!") 
    #
    def printOnWindows( printer_name, text_to_print ):

        try:
     
            # Open the printer
            hPrinter = win32print.OpenPrinter( printer_name )
            
            # Start a print job
            hJob = win32print.StartDocPrinter( hPrinter, 1, ("Python Print Job", None, "RAW") )
            
            # Start a page
            win32print.StartPagePrinter(hPrinter)
            
            # Write the text to the printer
            win32print.WritePrinter( hPrinter, text_to_print.encode('utf-8') )
            
            # End the page and job
            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hJob)
            win32print.ClosePrinter(hPrinter)

        except Exception as e:
            errMsg = f"Error printing  via printOnWindows: {e}"
            print( errMsg )
            Log.error( errMsg )


    #
    # Linux: Using subprocess with lpr: The lpr command-line utility. Python's subprocess module can be used to execute this command.
    #
    def printOnLinux(text_to_print):

        try:

            lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
            lpr.stdin.write(text_to_print.encode('utf-8'))
            lpr.stdin.close()

        except Exception as e:
            errMsg = f"Error printing via printOnLinux: {e}"
            print( errMsg )
            Log.error( errMsg )


    # Thermal Printers (ESC/POS compatible)
    #
    # printOnThermal(0x04b8, 0x0202, "Thermal print test!") 
    #
    # Replace with your specific vendor_id and product_id.
    #
    def printOnThermal( vendor_id, product_id, text_to_print ):
    
        try:
            
            p = Usb(vendor_id, product_id)  # Replace with your printer's Vendor ID and Product ID
            p.text(text_to_print)
            p.cut()

        except Exception as e:
            errMsg = f"Error printing via printOnThermal: {e}"
            print( errMsg )

'''
