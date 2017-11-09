
class string(unicode):

    def after(self, substring):
        try:
            return string(self[self.index(substring)+len(substring):])
        except ValueError:
            return string()

    def before(self, substring):
        try:
            return string(self[:self.rindex(substring)])
        except ValueError:
            return self

    def __getitem__(self, i):
        if isinstance(i, slice):
            return self.after(i.start or '').before(i.stop or '')
        if isinstance(i, basestring):
            return self.index(i)
        return unicode.__getitem__(self, i)

