class Parser:

    def __init__(self, filename):
        self.parser_set_params(filename)

    def parser_set_params(self, filename):
        file = open(filename, 'r')
        line = file.readline()

        while line != "":
            if line[0] == 'N':
                self.N = int(file.readline())
                line = self.get_next_letter(file)

            elif line[0] == 'R':
                self.R = file.readline().split(',')
                self.R = [int(i) for i in self.R]
                line = self.get_next_letter(file)

            elif line[0] == 'T':
                self.T = []
                line = file.readline()
                counter = 0
                while(not (line[0].isalpha())):
                    t = line.split(',')
                    t = [int(i) for i in t]
                    t.append(counter)
                    self.T.append(t)
                    line = file.readline()
                    counter = counter + 1
                    if line == "":
                        break;

            elif line[0] == 'B':
                self.B = []
                line = file.readline()
                while(not (line[0].isalpha())):
                    b = line.split(',')
                    b = [int(i) for i in b]
                    self.B.append(b)
                    line = file.readline()
                    if line == "":
                        break;
            else:
                line = self.get_next_letter(file)

        # print self.N
        # print self.R
        # print self.T
        # print self.B

    def get_N(self):
        return self.N

    def get_R(self):
        return self.R

    def get_T(self):
        return self.T

    def get_B(self):
        return self.B

    def get_next_letter(self, file):
        line = "1"
        while(not (line[0].isalpha())):
            line = file.readline()
            if line == "":
                break;
        return line
