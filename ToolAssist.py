#!/usr/bin/env python
import sys
import magic

def suggest_tools(filetype: str):
	filetype = filetype.lower()
	suggestions = []
	# Prioritize Python detection
	if 'pe32' in filetype or 'exe' in filetype:
		return ['PEStudio', 'CFF Explorer', 'Detect It Easy', 'FLOSS', 'Ghidra', 'IDA Pro']
	if 'dotnet' in filetype or '.net' in filetype:
		return ['dnSpy', 'ILSpy', 'FLOSS']
	if 'elf' in filetype:
		return ['readelf', 'objdump', 'Ghidra', 'radare2']
	if 'pdf' in filetype:
		return ['pdfid', 'peepdf', 'pdf-parser']
	if 'java' in filetype or 'jar' in filetype:
		return ['JD-GUI', 'CFR', 'JADX']
	if 'ms office' in filetype or 'doc' in filetype or 'xls' in filetype:
		return ['oletools', 'oleid', 'msoffcrypto-tool']
	if 'python' in filetype or 'py' in filetype:
		return ['uncompyle6', 'pyinstxtractor']
	if not suggestions:
		suggestions.append('No specific tools found. Try a generic hex editor or strings.')
	return suggestions

def main():
	if len(sys.argv) != 2:
		print('Usage: python ToolAssist.py <file_path>')
		sys.exit(1)
	filepath = sys.argv[1]
	print(filepath)
	try:
		filetype = magic.from_file(filepath)
	except Exception as e:
		print(f'Error reading file: {e}')
		sys.exit(1)
	print(f'File type detected: {filetype}')
	tools = suggest_tools(filetype)
	print('Suggested analysis tools:')
	for tool in tools:
		print(f'- {tool}')

if __name__ == '__main__':
	main()

