from .utils import notify
class FakeUi(object):

    def __init__(self):
        print("ui init")

    def addstr(self, *args):
        print("add str {}".format(args))

    def notify(self, summary, song, album, artist):
        print("summary {},song {},alblum {},artist {}".format(summary,song,album,artist))
        notify('asdf')

    def build_playinfo(self,
                       song_name,
                       artist,
                       album_name,
                       quality,
                       start,
                       pause=False):
        print("song name {},artist {},album_name {},quality {},start {},pause {}".format(song_name,artist,album_name,quality,start,pause))

    def build_process_bar(self, now_playing, total_length, playing_flag,
                          pause_flag, playing_mode):
        print('build process bar')

    def build_loading(self):
        print('build process bar')

    # start is the timestamp of this function being called
    def build_menu(self, datatype, title, datalist, offset, index, step,
                   start):
        # keep playing info in line 1
        pass

    def build_search(self, stype):
        pass

    def build_login(self):
        pass

    def build_login_bar(self):
        pass

    def build_login_error(self):
        return 1

    def build_timing(self):
        return 100

    def get_account(self):
        return None

    def get_password(self):
        return "abc".decode('utf-8')

    def get_param(self, prompt_string):
        return None

    def update_size(self):
        pass

    def update_space(self):
        pass
