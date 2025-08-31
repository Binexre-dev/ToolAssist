
# ToolAssist

ToolAssist is a Python script that helps you identify useful analysis tools for files, especially for malware analysis. It uses python-magic to detect the file type from its header and suggests relevant tools based on the type.

## Features
- Detects file type using python-magic
- Suggests analysis tools for malware and reverse engineering
- CLI usage: drag-and-drop or command-line argument

## Usage

```powershell
python ToolAssist.py <path_to_file>
```

## Example

```powershell
python ToolAssist.py suspicious.exe
```

## Requirements
- python-magic

Install dependencies:
```powershell
pip install -r requirements.txt
```

## Setup
1. Clone the repository:
	```powershell
	git clone git@github.com:Binexre-dev/ToolAssist.git
	```
2. (Optional) Create and activate a virtual environment.
3. Install requirements as above.

## Notes
- On Windows, you may need to install libmagic binaries. See python-magic documentation for details.

## License
MIT
