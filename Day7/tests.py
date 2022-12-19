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

    def test_getting_size1(self):
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
        directories_small_enough = {}
        expected_directories = {'directory1': 344,
                                'directory2': 473,
                                'directory3': 470}

        day7.get_directory_size('/', parsed_input, 500, directories_small_enough)
        self.assertEqual(expected_directories, directories_small_enough)

    def test_getting_size2(self):
        test_input = {'/':
                          {'a':
                               {'e': {'i': 584},
                                'f': 29116,
                                'g': 2557,
                                'h.lst': 62596},
                           'b.txt': 14848514,
                           'c.dat': 8504156,
                           'd': {'j': 4060174,
                                 'd.log': 8033020,
                                 'd.ext': 5626152,
                                 'k': 7214296}
                           }
                      }
        directories_small_enough = {}
        expected_directories = {'e': 584,
                                'a': 94853,}

        day7.get_directory_size('/', test_input, 100000, directories_small_enough)
        self.assertEqual(expected_directories, directories_small_enough)

        size_sum = 0
        for size in directories_small_enough.values():
            size_sum += size

        self.assertEqual(size_sum, 95437)

    def test_everything_together(self):
        with open("sample_input.txt", "r") as f:
            test_input = f.readlines()

        parsed_input = day7.parse_input(test_input)
        directories_small_enough = {}
        day7.get_directory_size("/", parsed_input, 100_000, directories_small_enough)

        size_sum = 0
        for size in directories_small_enough.values():
            size_sum += size

        self.assertEqual(size_sum, 95437)


if __name__ == '__main__':
    unittest.main()
