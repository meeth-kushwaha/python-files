"""Program 100: Interactive CLI Menu & System Dashboard."""
import platform
import sys

def display_dashboard():
    print("=" * 45)
    print("        PYTHON SYSTEM DASHBOARD        ")
    print("=" * 45)
    print(f"Python Version : {platform.python_version()}")
    print(f"OS Platform    : {platform.system()} {platform.release()}")
    print(f"Architecture   : {platform.machine()}")
    print(f"Byte Order     : {sys.byteorder}")
    print("-" * 45)
    print("[1] Run Health Check")
    print("[2] View Memory Stats")
    print("[3] Exit")
    print("=" * 45)
    print("Dashboard initialized successfully.")

if __name__ == "__main__":
    print("--- 100: Interactive CLI Menu Dashboard ---")
    display_dashboard()
