
import ConfigParser

class MyIni:
    def __init__(self, conf_path='my_ini.conf'):
        self.conf_path = conf_path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(conf_path)

    def get_kakou(self):
        conf = {}
        section = 'KAKOU'
        conf['host'] = self.cf.get(section, 'host')
        conf['port'] = self.cf.getint(section, 'port')
        conf['username']  = self.cf.get(section, 'username')
        conf['password']  = self.cf.get(section, 'password')
        conf['id_flag'] = self.cf.getint(section, 'id_flag')
        conf['id_step'] = self.cf.getint(section, 'id_step')
        conf['time_flag'] = self.cf.get(section, 'time_flag')
        conf['time_step'] = self.cf.getint(section, 'time_step')
        conf['kkdd'] = self.cf.get(section, 'kkdd')
        conf['city'] = self.cf.get(section, 'city')
        return conf

    def get_hbc(self):
        conf = {}
        section = 'HBC'
        conf['host'] = self.cf.get(section, 'host')
        conf['port'] = self.cf.getint(section, 'port')
        return conf


    def set_id(self, id_flag):
        self.cf.set('KAKOU', 'id_flag', id_flag)
        self.cf.write(open(self.conf_path, 'w'))

    def set_time(self, time_flag):
        self.cf.set('KAKOU', 'time_flag', time_flag)
        self.cf.write(open(self.conf_path, 'w'))

if __name__ == '__main__':
    ini = MyIni()
    print ini.get_kakou()
    print ini.get_hbc()
    #ini.set_time('2015-10-01 00:10:23')
    #print hbc
