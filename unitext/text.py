from unitext import parsers

def replace(source_path, replace_dict, dest_path=None,
			file_extension='', **kwargs):
	parser = get_parser(source_path, file_extension)
	parser.replace(replace_dict)
	parser.write(dest_path or source_path)
	
def get_parser(source_path, file_extension):
	file_format = file_extension
	if not file_format:
		split_path = source_path.split('.')
		if len(split_path) > 1:
			file_format = split_path[-1]
		else:
			file_format = 'txt' # plain text is default format
	parser_map = {
		'txt': parsers.PlainTextParser
	}
	return parser_map[file_format](source_path)