import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class OperaBrowser:
    def __init__(self, port_no, session):
        self.port_no = port_no
        self.session = session
        self.driver = None

    def start_opera(self):
        print("Opening Opera Session-6")
        # Launch Opera with remote debugging enabled on the specified port and session
        command = f'"C:\\Users\\xcien\\AppData\\Local\\Programs\\Opera\\Opera.exe" --remote-debugging-port={self.port_no} --user-data-dir="C:/Opera_Session{self.session}"'
        subprocess.Popen(command, shell=True)

    def get_driver(self):
        # Start Opera browser process
        self.start_opera()

        # Define paths
        driver_path = r'D:\Work\Scrapper Scripts\opera_session\operadriver_win64\operadriver.exe'  # Update as needed
        opera_path = r"C:\Users\xcien\AppData\Local\Programs\Opera\Opera.exe"  # Path to Opera browser

        # Setup ChromeOptions for Opera
        options = Options()
        options.binary_location = opera_path
        options.add_experimental_option("debuggerAddress", f"localhost:{self.port_no}")

        # Initialize WebDriver with the Opera driver
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver