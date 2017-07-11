__author__ = 'med-pvo'


class FastqcSummaryParser():
    def __init__(self, summary_str):
        self.__summary_data = self.parse_summary_str(summary_str.decode("utf8"))

    @property
    def summary_data(self):
        return self.__summary_data

    def passed_basic_statistics(self):
        return self.summary_data['Basic Statistics']

    def passed_per_base_seq_quality(self):
        return self.summary_data['Per base sequence quality']

    def passed_per_tile_seq_quality(self):
        return self.summary_data['Per tile sequence quality']

    def passed_per_sequence_quality_scores(self):
        return self.summary_data['Per sequence quality scores']

    def passed_per_base_sequence_content(self):
        return self.summary_data['Per base sequence content']

    def passed_per_sequence_gc_content(self):
        return self.summary_data['Per sequence GC content']

    def passed_per_base_n_content(self):
        return self.summary_data['Per base N content']

    def passed_sequence_length_distribution(self):
        return self.summary_data['Sequence Length Distribution']

    def passed_sequence_dupication_levels(self):
        return self.summary_data['Sequence Duplication Levels']

    def passed_overrepresented_sequences(self):
        return self.summary_data['Overrepresented sequences']

    def passed_adapter_content(self):
        return self.summary_data['Adapter Content']

    def passed_kmer_content(self):
        return self.summary_data['Kmer Content']

    def parse_summary_str(self, summary_str):
        return {line.split("\t")[1]:line.split("\t")[0] for line in str.splitlines(str(summary_str))}
