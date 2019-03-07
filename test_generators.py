import unittest
from generators import process_generators


class TestGenerators(unittest.TestCase):
	def setUp(self):
		self.cases = None

	def test_create_dict(self):
		self.cases = (
			(1, 1, 1, 5, 0), 
			(1, 2, 1, 5, 1), 
			(0, 5, 10, 5, 2), 
			(0, 3, 6, 5, 3), 
		)
		self.expected_result = (
			{'1': 3, '2': 6, '3': 9, '4': 12, '5': 15},

			{'1': 2, '2': 6, '3': 9, '4': 12, '5': 15, '6': 6}, 

			{
				'0': 0, '5': 5, '10': 10, '1': 1, '6': 6, '11': 11, 
				'2': 2, '7': 7, '12': 12, '3': 3, '8': 8, '13': 13, 
				'4': 4, '9': 9, '14': 14
			},

			{
				'0': 0, '3': 6, '6': 12, '1': 1, '4': 8, '7': 14, 
				'2': 2, '5': 5, '8': 8, '9': 9, '10': 10
			},
		)

		for b in self.cases:
			with self.subTest(case=b):
				print(b)
				A_INIT, B_INIT, C_INIT, QUANTITY, RESULT_NUMBER = b

				src_a = ({str(i): i} for i in range(A_INIT, A_INIT + QUANTITY))
				src_b = ({str(i): i} for i in range(B_INIT, B_INIT + QUANTITY))
				src_c = ({str(i): i} for i in range(C_INIT, C_INIT + QUANTITY))

				result = process_generators(src_a, src_b, src_c)
				self.assertEqual(result, self.expected_result[RESULT_NUMBER])


	def tearDown(self):
		self.cases = None



if __name__ == "__main__":
	unittest.main()

	