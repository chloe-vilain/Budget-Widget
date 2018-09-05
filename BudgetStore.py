import abc

class BudgetStore(object):
	"""Abstract base class defining Store methods
	"""
	__metaclass__ = abc.ABCMeta

	field_names_exp = ['id_', 'name', 'from_', 'to', 'current', 'deleted']

	@abc.abstractmethod
	def create(self, save_name = None):
		""" Create a new store.

		parameters:
		- save_name: str (optional) - name for save file. create must support 
		constructing store using name provided, and constructing store generating
		name if name not provided.

		Returns location_exp - represents save location for expenses data
		"""

	@abc.abstractmethod
	def read(self, location):
		""" Read data from store

		parameters:
		- location: str - location to read data from 

		Returns budget: Budget - The Budget object leveraged by the application.
		"""
		 

	@abc.abstractmethod
	def write(self, budget, location):
		""" Save date to store

		parameters:
		 - budget: Budget object to store.  Note- savings not storable today
		 - location: str - Save location 

		Returns None 
		"""
		


