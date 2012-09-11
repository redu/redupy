

class Model(object):
    def parse(self, data):
        for var in vars(self).keys():
            setattr(self, var, data.get(var))

    def __repr__(self):
        ret = u""
        for key, arg in vars(self).items():
            ret = ret + unicode.format(u"{0} : {1}\n", key, arg)
        return ret.encode('UTF-8')


class User(Model):
    def __init__(self):
        self.login = None
        self.mobile = None
        self.email = None
        self.localization = None
        self.friends_count = None
        self.links = None
        self.id = None
        self.last_name = None
        self.first_name = None
        self.birthday = None
        self.birth_localization = None
        self.social_networks = None


class Subject(Model):
    def __init__(self):
        self.id = None
        self.title = None
        self.description = None
        self.created_at = None
        self.links = None


class Environment(Model):
    def __init__(self):
        self.id = None
        self.name = None
        self.created_at = None
        self.initials = None
        self.path = None
        self.links = None


class Status(Model):
    def __init__(self):
        self.type = None
        self.links = None
        self.user = None
        self.id = None
        self.text = None


class Enrollment(Model):
    def __init__(self):
        self.created_at = None
        self.token = None
        self.id = None
        self.links = None
        self.state = None
        self.email = None


class Space(Model):
    def __init__(self):
        self.name = None
        self.created_at = None
        self.links = None
        self.description = None


class Course(Model):
    def __init__(self):
        self.name = None
        self.created_at = None
        self.id = None
        self.workload = None
        self.path = None


class ModelFactory(object):
    user = User
    course = Course
    space = Space
    enrollment = Enrollment
    status = Status
    environment = Environment
    subject = Subject
