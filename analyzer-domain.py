class AnalyzerDomain:
    
    def __init__(self):
        self.instructions = []
        self._commands = {
            'P': ('ARG', self.doSelectPen),
            'D': ('NO_ARG', self.doPenDown),
            'U': ('NO_ARG', self.doPenUp),
            'N': ('ARG', self.doMoveNorth),
            'S': ('ARG', self.doMoveSouth),
            'E': ('ARG', self.doMoveEast),
            'W': ('ARG', self.doMoveWest),
            'PA': ('ARG', self.doPrintArea)
        }

    def interpret_line(self, line):
        parts = line.split()
        command = parts[0]

        if (len(parts) > 1 and parts[1].isdigit()): value = int(parts[1]) 
        else: value = None

        if command in self._commands:
            args, method = self._commands[command]
            self.instructions.append((args, method.__name__, value))
        else:
            raise ValueError(f"Comando desconhecido: {command}")
    
    def execute_instruction(self, instructions):
        for instruction in instructions:
            args, method_name, value = instruction
            method = getattr(self, method_name)

            if args == 'ARG': method(value)
            elif args == 'NO_ARG': method()
            else: raise ValueError(f"Tipo de argumento desconhecido: {args}")
                

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

    def doSelectPen(self, arg):
        print(f"Selecionou a caneta {arg}")
        return
    
    def doPenDown(self):
        print("Caneta para baixo")
        return
    
    def doPenUp(self):
        print("Caneta para cima")
        return
    
    def doMoveNorth(self, arg):
        print(f"Moveu para norte {arg} unidades")                       
        return
    
    def doMoveSouth(self, arg):
        print(f"Moveu para sul {arg} unidades")
        return

    def doMoveEast(self, arg):
        print(f"Moveu para leste {arg} unidades")
        return
    
    def doMoveWest(self, arg):
        print(f"Moveu para oeste {arg} unidades")
        return

    def doPrintArea(self, arg):
        print(f"Imprimindo área {arg}")
        return

if __name__ == "__main__":
    analyzer = AnalysisLanguage() 
    analyzer.load_from_file('language.txt')
    analyzer.execute_instruction(analyzer.instructions)