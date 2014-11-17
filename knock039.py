import sys
import kyotocabinet as kc

class KyotoCabinet(kc.DB):
    def __del__(self):
        self.close()

    def open(self, *args, **kwds):
        if not super(KyotoCabinet, self).open(*args, **kwds):
            raise IOError("Open error: {0}".format(super(KyotoCabinet, self).error()))

    def set(self, *args, **kwds):
        if not super(KyotoCabinet, self).set(*args, **kwds):
            raise IOError("Set error: {0}".format(super(KyotoCabinet, self).error()))

    def close(self, *args, **kwds):
        if not super(KyotoCabinet, self).close(*args, **kwds):
            raise IOError("Close error: {0}".format(super(KyotoCabinet, self).error()))

    def cursor(self, *args, **kwds):
        cur = super(KyotoCabinet, self).cursor(*args, **kwds)
        cur.jump()
        while 1:
            rec = cur.get_str(True)
            if not rec: break
            yield rec
        cur.disable()


if __name__ == "__main__":
    # open
    db = KyotoCabinet()
    db.open("sample.kch", kc.DB.OWRITER | kc.DB.OCREATE)
    
    # store
    for line in open(sys.argv[1]):
        spl = line.strip().split("\t")
        db.set((spl[1], spl[2]), spl[0])
    
    # print
    for rec in db.cursor():
        print rec[0], " : ", rec[1]

