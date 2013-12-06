
class MessageSystem(object):
	"""A message system for game objects"""
	def __init__(self):
		self.receivers = []
		self.messages = []

	def register(self, receiver):
		self.receivers.append(receiver)

	def send_message(self, message):
		self.messages.append(message)

	def propagate_messages(self):
		# Send messages to receivers if there are messages to send
		# and receivers to receive
		if self.messages and self.receivers:
			for r in self.receivers:
				for m in self.messages:
					r.receive_message(m)
		self.messages = []
