# (c) 2021 Leon Luithlen
# This code is licensed under MIT license


def strongly_typed(*args, **kwargs):
	stargs = args 
	stkwargs = kwargs
	def type_strongly(func):
		def wrapper(*args, **kwargs):
			for arg, type_ in zip(args, stargs):
				assert isinstance(arg,type_), f"{arg} should be of type {type_}"
			for kw, arg in kwargs.items():
				assert isinstance(arg, stkwargs[kw]), f"{kw} should be of type {stkwargs[kw]} but is of type {type(arg)}: {arg}"
			return(func(*args, **kwargs))
		return(wrapper)
	return(type_strongly)



@strongly_typed(int, str, i=int, s=str) 	
def check_if_int_and_string(i, s):
	if type(i) == int and type(s) == str:
		print("hi")
	else:
		print("Not a number or not a string")

