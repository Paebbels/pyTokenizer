# =============================================================================
#              _____     _              _
#   _ __  _   |_   _|__ | | _____ _ __ (_)_______ _ __
#  | '_ \| | | || |/ _ \| |/ / _ \ '_ \| |_  / _ \ '__|
#  | |_) | |_| || | (_) |   <  __/ | | | |/ /  __/ |
#  | .__/ \__, ||_|\___/|_|\_\___|_| |_|_/___\___|_|
#  |_|    |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python unittest:    Testing the pyCallBy module
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
"""
pyTokenizer
###########

:copyright: Copyright 2007-2021 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from unittest     import TestCase

from pyTokenizer import Tokenizer, StartOfDocumentToken, ValuedToken, StringToken, SpaceToken


if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class CallByReference_AnyParam(TestCase):
	def test_HelloWorld(self):
		sequence = "hello world"
		world = None
		end = None
		try:
			tokenGenerator = Tokenizer.GetWordTokenizer(sequence)
			tokenIterator = iter(tokenGenerator)

			start = next(tokenIterator)
			self.assertTrue(isinstance(start, StartOfDocumentToken))
			self.assertEqual(len(start), 0)

			hello = next(tokenIterator)
			self.assertTrue(isinstance(hello, StringToken))
			self.assertEqual(hello.Value, "hello")

			space = next(tokenIterator)
			self.assertTrue(isinstance(space, SpaceToken))

			world = next(tokenIterator)
			self.assertTrue(isinstance(world, StringToken))
			self.assertEqual(world.Value, "world")

#			end = next(tokenIterator)
# 		self.assertTrue(isinstance(end, EndOfDocumentToken))
#			self.assertEqual(len(end), 0)
		except StopIteration as ex:
			pass
			# XXX:
#			self.assertIsNotNone(world, "Iterator stopped before end of document.")
