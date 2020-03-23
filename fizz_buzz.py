def get_reply(nb):

	if not isinstance(nb, int):
		return "Error."
	nb_str = ""
	if not nb % 3 or not nb % 5:
		if not nb % 3:
			nb_str += "Fizz"
		if not nb % 5:
			nb_str += "Buzz"
	else:
		nb_str = str(nb)
	return nb_str
