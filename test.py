def opponent(self):
    return ('Fire', 'Water') if self.p_type = 'Grass' else \
            ('Dark', 'Psychic') if self.p_type = 'Ghost' else \
            ('Water', 'Grass') if self.p_type = 'Fire' else \
            ('Electric', 'Fighting')

opponent('Grass')