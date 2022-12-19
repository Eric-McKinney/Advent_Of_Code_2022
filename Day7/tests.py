import unittest
import day7
import pprint


class MyTestCase(unittest.TestCase):
    def test_parsing(self):
        test_input = ["$ cd /\n",
                     "$ ls\n",
                     "dir directory1\n",
                     "dir directory2\n",
                     "1234 file1.wav\n",
                     "$ cd directory1\n",
                     "$ ls\n",
                     "110 file2.jpg\n",
                     "234 file3.png\n",
                     "$ cd ..\n",
                     "$ cd directory2\n",
                     "$ ls\n",
                     "dir directory3\n",
                     "3 a.txt\n",
                     "$ cd directory3\n",
                     "470 afhj.dfg\n"]
        parsed_input = day7.parse_input(test_input)
        expected_parsed = {'/':
                               {'directory1':
                                    {'file2.jpg': 110, 'file3.png': 234},
                                'directory2':
                                    {'a.txt': 3,
                                     'directory3':
                                         {'afhj.dfg': 470}
                                     },
                                'file1.wav': 1234
                                }
                           }
        self.assertEqual(expected_parsed, parsed_input)


if __name__ == '__main__':
    unittest.main()
