class AttrDisplay:
	def get_her_attr(self):
		attr = []
		for key in sorted(self.__dict__):
			attr.append('{0} = {1}'.format(key, getattr(self,key)))
		return ', '.join(attr)
	def __str__(self):
		return '[{0}: {1}]'.format(self.__class__.__name__, self.get_her_attr())
