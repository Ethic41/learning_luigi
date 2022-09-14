import luigi # type: ignore


class GenerateWords(luigi.Task):
    def output(self):
        return luigi.LocalTarget("data/words.txt")
    
    def run(self):
        words = [
            'apple',
            'banana',
            'grapefruit'
        ]

        with self.output().open('w') as f:
            for word in words:
                print(f"{word}", file=f)


class CountLetters(luigi.Task):
    
    def requires(self):
        return GenerateWords()
    
    def output(self):
        return luigi.LocalTarget('data/letters_count.txt')
    
    def run(self):
        with self.input().open('r') as infile:
            words = infile.read().splitlines()
        
        with self.output().open('w') as outfile:
            for word in words:
                letter_count = len(word)
                outfile.write(f"{word} | {letter_count}\n")


if __name__ == "__main__":
    counter = CountLetters()
    counter.run()

