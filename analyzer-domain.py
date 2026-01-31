# Ler o arquivo de definição da linguagem
# Ler linha a linha e interpretar os comandos
# Alguns comandos tem valores associados (ex: N 10, S 5, E 3, W 2)
# O foco dos comandos é montar um desenho baseado nas instruções dadas

class AnalyzerDomain:
    
    _commands = {
        'P': 'select_pen',
        'D': 'pen_down',
        'U': 'pen_up',
        'N': 'move_north',
        'S': 'move_south',
        'E': 'move_east',
        'W': 'move_west',
        'PA': 'print_area'
    }

    def __init__(self):
        self.instructions = []

    def interpret_line(self, line):
        parts = line.split()
        command = parts[0]

        if (len(parts) > 1 and parts[1].isdigit()):
            value = int(parts[1]) 
        else: 
            value = None

        if command in self._commands:
            self.instructions.append((self._commands[command], value))
        else:
            raise ValueError(f"Comando desconhecido: {command}")
    
    def interpret(self, lines):
        for line in lines:
            self.interpret_line(line.strip())

        return self.instructions

    def load_from_file(self, filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
        return self.interpret(lines)
    
    def get_instructions(self):
        print(self.instructions)

if __name__ == "__main__":
    analyzer = AnalysisLanguage() 
    analyzer.load_from_file('language.txt')
    analyzer.get_instructions()