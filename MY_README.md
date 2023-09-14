### Installation

Clone the repository:
    
    git clone https://github.com/Oomamchur/Ajax_test_task

Change to the project's directory:

    cd Ajax_test_task

Сopy .env_sample file with your examples of env variables to your .env file.

Create virtual environment:

    python -m venv venv

Activate the virtual environment:

On macOS and Linux:
    
    source venv/bin/activate
    
On Windows:
    
    venv\Scripts\activate

Install requirements:

    pip install -r requirements.txt

Open the project in Android Studio. Connect your device or emulator.

Run Appium:
    
    appium

Run tests:
    
    pytest
