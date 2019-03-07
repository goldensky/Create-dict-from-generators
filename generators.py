import time
import functools

A_INIT = 0
B_INIT = 3
D_INIT = 6

QUANTITY = 5

src_a = ({str(i): i} for i in range(A_INIT, A_INIT + QUANTITY))
src_b = ({str(i): i} for i in range(B_INIT, B_INIT + QUANTITY))
src_c = ({str(i): i} for i in range(D_INIT, D_INIT + QUANTITY))


def count_time(func):
	@functools.wraps(func)
	def inner(*args, **kwargs):
		time_0 = time.time()
		result = func(*args, **kwargs)
		time_delta = time.time() - time_0
		print(time_delta)
		return result
	return inner


@count_time
def process_generators(*generators):
	src_a, src_b, src_c = generators
	result_dict = {}
	for a in src_a:
		b = next(src_b)
		c = next(src_c)
		abc_list = [a, b, c]

		for dct in abc_list:
			for key, value in dct.items():
				result_dict[key] = result_dict.get(key, 0) + value

	return result_dict



if __name__ == "__main__":

	result = process_generators(src_a, src_b, src_c)
	print(result)
	for key, value in sorted(result.items(), key=lambda x: x[1]):
		print(key, value)




