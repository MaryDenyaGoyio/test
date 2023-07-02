RATINGS = [1, 2, 3, 4, 5]

FIELDS = {}
FIELDS['개변류'] = ['개변', '펨돔', '더럽', '상식', '꼭지']
FIELDS['개조류'] = ['개조', '기생', '분리', '상변', '탈장']
FIELDS['꼴림류'] = ['꼴림', '모유', '롤리', '캐릭', '후타']

TYPS = ['PX', 'HI', 'TW', 'KM', 'AR']

FORMATS = { site : {} for site in TYPS }

FORMATS['PX']['artist'] = 'https://www.pixiv.net/users/{_id}/artworks?p={page}'
FORMATS['PX']['art'] = 'https://www.pixiv.net/artworks/{_id}'

FORMATS['HI']['artist'] = 'https://hitomi.la/artist/{name}-all.html?page={page}'
FORMATS['HI']['art'] = 'https://hitomi.la/reader/{_id}.html#{page}'

FORMATS['TW']['artist'] = 'https://twitter.com/{name}/media'
FORMATS['TW']['art'] = 'https://twitter.com/{name}/status/{_id}'

FORMATS['KM']['artist'] = 'https://kemono.party/{typ}/user/{_id}?o={page}'
FORMATS['KM']['art'] = 'https://kemono.party/{typ}/user/{_id}/post/{_idd}'

FORMATS['AR']['artist'] = 'https://arca.live/b/breaking?target=nickname&keyword={name}&p={page}'
FORMATS['AR']['art'] = 'https://arca.live/b/breaking/{_id}'

class Artist():
    def __init__(self, name, rating, field, date):
        self.name = name
        self.rating = rating
        self.field = field
        self.date = date

class Gallery():
    def __init__(self, artist, site, url, start, end):
        self.artist = artist
        self.site = site
        self.url = url
        self.start = start
        self.end = end

class Art():
     def __init__(self, name, artist, gallery, date, url, page, check=False):
        self.name = name
        self.artist = artist
        self.gallery = gallery
        self.date = date
        self.url = url
        self.page = page
        self.check = check

class Downloader():
    def __init__(self, ):
        self.artist = None
        self.gallery = None
        self.art = None

    def find_gallery(self, gallery):
        return None
        

