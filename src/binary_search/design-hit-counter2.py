import bisect


class HitCounter:

    def __init__(self):
        self.hit_record = []


    def hit(self, timestamp: int) -> None:
        self.hit_record.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        hit_before_5mins = timestamp - 300

        pre_insert = bisect.bisect(self.hit_record, hit_before_5mins)

        return len(self.hit_record) - pre_insert


def test_case_1():
    hitcounter = HitCounter()
    hitcounter.hit(1)
    hitcounter.hit(2)
    hitcounter.hit(3)
    result = hitcounter.getHits(4)
    print(result)
    hitcounter.hit(300)
    result = hitcounter.getHits(300)
    print(result)
    result = hitcounter.getHits(301)
    print(result)

if __name__ == '__main__':
    test_case_1()


