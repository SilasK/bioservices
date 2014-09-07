from bioservices.wsdbfetch import WSDbfetch
from nose.plugins.attrib import attr


class test_WSDbfetch(object):
    @classmethod
    def setup_class(klass):
        klass.s = WSDbfetch(verbose=False)

    #def __init__(self):
    #    super(test_WSDbfetch, self).__init__(verbose=False)
        

    def test_getSupportedDBs(self):
        res = self.s.getSupportedDBs()
        res = self.s.getSupportedDBs()
        assert len(res) >10

    def test_getSupportedFormats(self):
        res = self.s.getSupportedFormats()
        res = self.s.getSupportedFormats()
        assert len(res) >10

    def test_getSupportedStyles(self):
        res = self.s.getSupportedStyles()
        res = self.s.getSupportedStyles()
        assert len(res) >10

    @attr('fixme')
    def test_fetchBatch(self):
        self.s.fetchBatch("uniprot" ,"wap_mouse", "xml") 

    @attr('skip')
    def test_fetchData(self):
        self.s.fetchData('uniprot:zap70_human')

    @attr('skip')
    def test_getDatabaseInfo(self):
        res = self.s.getDatabaseInfo("uniprotkb")
        assert res.displayName == 'UniProtKB'

    @attr('skip')
    def test_getDatabaseInfoList(self):
        assert len(self.s.getDatabaseInfoList())>10

    @attr('skip')
    def test_getDatavaseInfoList(self):
        self.s.getDatabaseInfoList()

    @attr('skip')
    def test_getDbFormats(self):
        self.s.getDbFormats("uniprotkb")

    @attr('skip')
    def test_getFormat(self):
        assert len(self.s.getFormatStyles("uniprotkb", "fasta")) >= 3
        #['default', 'raw', 'html']

    @attr('skip')
    def test_wrong_db(self):
        try:
            self.s.getDbFormats("uniprot")
            assert False
        except:
            assert True
        