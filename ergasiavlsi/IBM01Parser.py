import pyparsing as pp
import os

# Define the grammar for IBM01 files
file_type = pp.oneOf('.aux.nets.nodes.pl.scl.wts')
meta_key = pp.Word(pp.alphas, pp.alphanums + '_')
meta_value = pp.restOfLine
meta_line = pp.Suppress('@') + meta_key + meta_value
meta = pp.ZeroOrMore(meta_line)

# Define grammar for each file type
aux_grammar = pp.Forward()
aux_line = pp.Word(pp.alphas, pp.alphanums + '_') + pp.restOfLine
aux_grammar << pp.ZeroOrMore(aux_line)

nets_grammar = pp.Forward()
nets_line = pp.Word(pp.alphas, pp.alphanums + '_') + pp.restOfLine
nets_grammar << pp.ZeroOrMore(nets_line)

nodes_grammar = pp.Forward()
nodes_line = pp.Word(pp.alphas, pp.alphanums + '_') + pp.restOfLine
nodes_grammar << pp.ZeroOrMore(nodes_line)

pl_grammar = pp.Forward()
pl_line = pp.Word(pp.alphas, pp.alphanums + '_') + pp.restOfLine
pl_grammar << pp.ZeroOrMore(pl_line)

scl_grammar = pp.Forward()
scl_line = pp.Word(pp.alphas, pp.alphanums + '_') + pp.restOfLine
scl_grammar << pp.ZeroOrMore(scl_line)

wts_grammar = pp.Forward()
wts_line = pp.Word(pp.alphas, pp.alphanums + '_') + pp.restOfLine
wts_grammar << pp.ZeroOrMore(wts_line)

# Define a parser class
class IBM01Parser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        try:
            if not os.access(self.file_path, os.R_OK):
                raise PermissionError("Permission denied: {}".format(self.file_path))
            with open(self.file_path, 'r') as f:
                data = f.read()
            file_type_str = os.path.splitext(self.file_path)[1]
            if file_type_str == '.aux':
                grammar = aux_grammar
            elif file_type_str == '.nets':
                grammar = nets_grammar
            elif file_type_str == '.nodes':
                grammar = nodes_grammar
            elif file_type_str == '.pl':
                grammar = pl_grammar
            elif file_type_str == '.scl':
                grammar = scl_grammar
            elif file_type_str == '.wts':
                grammar = wts_grammar
            else:
                raise ValueError("Unsupported file type: {}".format(file_type_str))
            result = grammar.parseString(data, parseAll=True)
            return self._process_result(result)
        except PermissionError as e:
            print("Error: {}".format(e))
            return None
        except ValueError as e:
            print("Error: {}".format(e))
            return None
        except pp.ParseException as e:
            print("Error: {}".format(e))
            return None
        except Exception as e:
            print("Error: {}".format(e))
            return None

    def _process_result(self, result):
        data = []
        for line in result:
            data.append(line.strip())
        return data

# Example usage
file_path = 'C:/ergasiavlsi/ibm01/ibm01.aux'
if os.access(file_path, os.R_OK):
    parser = IBM01Parser(file_path)
    data = parser.parse()
    if data is not None:
        print(data)
else:
    print("Permission denied: {}".format(file_path))
