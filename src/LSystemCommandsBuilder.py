class LSystemCommandsBuilder:
    def iterate(self, n):
        s = self.axiom()
        for _ in range(0, n):
            s = self.next_iteration(s)
        return s

    def axiom(self):
        raise NotImplementedError('Subclasses must override axiom()')

    def next_iteration(self, s):
        raise NotImplementedError('Subclasses must override next_iteration()')
