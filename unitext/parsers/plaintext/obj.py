from unitext.parsers.baseparser import BaseParser

class PlainTextParser(BaseParser):
	
	def __init__(self, source_file):
		super().__init__(source_file)
		self.file_handle = open(source_file)
		
	def replace(self, replace_dict):
		try:
			text_content = self.file_handle.read()
			print(replace_value)
			for search_value, replace_value in replace_dict.items():
				self.write_content = text_content.replace(search_value, replace_value)
		finally:
			self.file_handle.close()
			
	def write(self, outfile_path):
		with open(outfile_path, 'w') as f:
			f.write(self.write_content)