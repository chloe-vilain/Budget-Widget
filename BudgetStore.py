import abc

class BudgetStore(object):
	"""Abstract base class defining Store methods
	"""
	__metaclass__ = abc.ABCMeta

	field_names = ['id_', 'name', 'from_', 'to', 'current', 'deleted']

	@abc.abstractmethod
	def create(self):
		""" Create a new store
		"""
		return

	@abc.abstractmethod
	def read(self, location):
		""" Read data from store
		"""
		return 

	@abc.abstractmethod
	def write(self, expenses, location):
		""" Save date to store

		parameters:
		 - expense: type?
		 - location - type
		 - name - type - description

		 returns: 
		"""
		return


