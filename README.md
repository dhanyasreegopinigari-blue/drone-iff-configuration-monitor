# 🚁 Drone IFF Configuration & Monitoring Application

✅ A PyQt5-based desktop application for configuring and monitoring a Drone IFF system through a modular, hardware-independent architecture.

✅ The application provides configuration management, input validation, device-state management, connection monitoring, persistent configuration storage, logging, and automated testing.

> **Current implementation:** The application operates in simulation mode and is designed with a hardware abstraction layer so that a real device interface can be integrated when the required hardware communication specifications are available.

---

## ✨ Features

- 🖥️ Modern PyQt5 desktop interface
- ⚙️ Device ID and ASS configuration
- ✅ Configuration input validation
- 💾 Persistent configuration using JSON
- 🔄 Configuration reset functionality
- 🔌 Device connection management
- 📡 Real-time connection monitoring
- 🧪 Hardware-independent device simulation
- 📝 Application event logging
- 🛡️ Error handling for configuration and device operations
- 🧩 Modular backend architecture
- 🧪 Automated unit testing with pytest
- 🔧 Hardware abstraction through a device interface

---

## 🏗️ System Architecture

The application follows a modular architecture that separates the user interface from device management and configuration logic.

```text
                    ┌──────────────────────┐
                    │      PyQt5 GUI       │
                    │       main.py        │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
      ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
      │ ConfigManager│ │ConfigValidator│ │  AppLogger   │
      └──────────────┘ └──────────────┘ └──────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    DeviceManager     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   DeviceInterface    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Simulator       │
                    └──────────────────────┘

The DeviceInterface provides an abstraction between the application and the underlying device implementation.

The current Simulator implements this interface for development and testing without requiring physical hardware.

---

## 📂 Project Structure
PYQT5/
│
├── backend/
│   ├── __init__.py
│   ├── config_manager.py
│   ├── device_interface.py
│   ├── device_manager.py
│   ├── logger.py
│   ├── simulator.py
│   └── validator.py
│
├── tests/
│   ├── __init__.py
│   ├── test_config_manager.py
│   ├── test_device_manager.py
│   └── test_validator.py
│
├── main.py
├── main.ui
├── config.json
├── requirements.txt
├── README.md
└── .gitignore

---

## 🛠️ Technologies Used
~ Frontend / GUI
Python
PyQt5
Qt Designer

~ Backend
Python
JSON
Object-Oriented Programming
Abstract Base Classes

~ Testing
pytest

~ Development Tools
Git
GitHub
Virtual Environment

---
## ⚙️ Installation
1. Clone the repository
git clone https://github.com/dhanyasreegopinigari-blue/drone-iff-configuration-monitor.git
2. Navigate to the project
cd drone-iff-configuration-monitor
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment
Windows PowerShell
.\.venv\Scripts\Activate.ps1

If PowerShell blocks script execution:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Then activate again:

.\.venv\Scripts\Activate.ps1
5. Install dependencies
pip install -r requirements.txt
▶️ Running the Application

Run:

python main.py

The PyQt5 desktop application will open.

## 🧪 Running Tests

The project includes automated tests for configuration validation, configuration management, and device management.

Run:

python -m pytest

Current test status:

16 passed
----

## 🔄 Application Workflow

~The main configuration workflow is:

Select Device ID
       ↓
Select ASS
       ↓
Validate Configuration
       ↓
Configure Device
       ↓
Connect Device
       ↓
Monitor Connection
       ↓
Log Device Events

The application also supports saving and resetting configuration data.
---

##🔌 Device Simulation

The project currently uses a simulated device instead of physical hardware.

This allows the application to be developed and tested without requiring a physical Drone IFF device.

The simulation layer supports:

~Device configuration
~Connection
~Disconnection
~Connection status checking
~Simulated connection loss
~Simulated connection recovery

~The simulator is separated from the application through DeviceInterface, allowing a future hardware-specific implementation to replace the simulator without restructuring the entire application.

---

## 🧪 Testing Strategy

The project uses automated unit tests to verify core functionality.

### Configuration Validator

Tests include:

Valid configuration
Missing Device ID
Missing ASS
Invalid Device ID
Invalid ASS

### Configuration Manager

Tests include:

Saving configuration
Loading configuration
Handling missing configuration
Resetting configuration

## Device Manager

Tests include:

Initial device state
Device configuration
Device connection
Connection status checking
Device disconnection
Simulated connection loss
Simulated connection recovery
---

##🛡️ Error Handling

The application includes error handling for important operations such as:

Invalid configuration input
Configuration save failures
Configuration loading errors
Configuration reset failures
Device configuration failures
Device connection failures
Unexpected application errors

Errors are reported through the GUI and recorded using the application logger where appropriate.
---

##🔮 Future Improvements

Potential future development includes:

Integration with a real hardware device
Hardware-specific communication interface
Expanded device diagnostics
Advanced monitoring information
Configuration profiles
More comprehensive integration testing
Windows executable packaging
Additional UI improvements
---

##⚠️ Hardware Integration Note

This project currently does not communicate with a physical Drone IFF device.

The application has been intentionally designed with a hardware abstraction layer and simulation mode so development and testing can be performed without physical hardware.

Actual hardware integration should be implemented only after the required device communication protocol, interface specifications, and hardware documentation are available.
---

##👩‍💻 Author

Dhanyasree Gopinigari

B.Tech Computer Science & Engineering (AI & ML)
---

##📄 License

This project is currently intended as a personal academic and portfolio project.

---