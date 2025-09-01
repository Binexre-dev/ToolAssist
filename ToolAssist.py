#!/usr/bin/env python
import sys
import magic

def suggest_tools(filetype: str):
	filetype = filetype.lower()
	static = []
	dynamic = []
	if 'python' in filetype or 'py' in filetype:
		static = ['uncompyle6', 'pyinstxtractor', 'strings', 'hex editor']
		dynamic = ['Cuckoo Sandbox', 'Any.run', 'Sandboxie']
	elif 'pe32' in filetype or 'exe' in filetype:
		static = ['PEStudio', 'CFF Explorer', 'Detect It Easy', 'FLOSS', 'Ghidra', 'IDA Pro', 'strings', 'Resource Hacker']
		dynamic = ['Cuckoo Sandbox', 'Any.run', 'Procmon', 'Process Explorer', 'Sandboxie']
	elif 'dotnet' in filetype or '.net' in filetype:
		static = ['dnSpy', 'ILSpy', 'FLOSS', 'Detect It Easy', 'strings']
		dynamic = ['Cuckoo Sandbox', 'Any.run', 'Procmon', 'Process Explorer']
	elif 'elf' in filetype:
		static = ['readelf', 'objdump', 'Ghidra', 'radare2', 'strings', 'hex editor']
		dynamic = ['Cuckoo Sandbox', 'strace', 'ltrace']
	elif 'pdf' in filetype:
		static = ['pdfid', 'peepdf', 'pdf-parser', 'strings', 'hex editor']
		dynamic = ['Cuckoo Sandbox', 'Any.run']
	elif 'java' in filetype or 'jar' in filetype:
		static = ['JD-GUI', 'CFR', 'JADX', 'strings', 'hex editor']
		dynamic = ['Cuckoo Sandbox', 'Any.run']
	elif 'ms office' in filetype or 'doc' in filetype or 'xls' in filetype:
		static = ['oletools', 'oleid', 'msoffcrypto-tool', 'strings', 'hex editor']
		dynamic = ['Cuckoo Sandbox', 'Any.run']
	else:
		static = ['No specific tools found. Try a generic hex editor or strings.']
		dynamic = []
	return {'static': static, 'dynamic': dynamic}

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
	print('\nSuggested analysis tools:')
	print('Static Analysis Tools:')
	for tool in tools['static']:
		print(f'- {tool}')
	if tools['dynamic']:
		print('\nDynamic Analysis Tools:')
		for tool in tools['dynamic']:
			print(f'- {tool}')

if __name__ == '__main__':
	main()

