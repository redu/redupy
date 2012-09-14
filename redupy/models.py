import re
from datetime import datetime


class Model(object):
    def __init__(self):
        self.links = None
        self.created_at = None
        self.updated_at = None
        self.id = None

    def parse(self, data, modelFactory):
        for var in vars(self).keys():
            value = data.get(var)
            if value:
                if var == "created_at" or var == "updated_at":
                    #a expressao regular eh usada para remover a timezone,
                    #ja que datetime nao se da muito bem com isso
                    stringdate = re.match(r"\d+-\d+-[T\d]+:\d+:\d+", value).group(0)
                    value = datetime.strptime(stringdate, "%Y-%m-%dT%H:%M:%S")
                elif hasattr(modelFactory, var):
                    tipo = getattr(modelFactory, var)
                    inner = tipo()
                    inner.parse(value, modelFactory)
                    value = inner
                setattr(self, var, value)

    def __repr__(self):
        ret = u""
        for key, arg in vars(self).items():
            ret = ret + unicode.format(u"{0} : {1}\n", key, arg)
        return ret.encode('ascii', 'replace')


class User(Model):
    def __init__(self):
        super(User, self).__init__()
        self.login = None
        self.mobile = None
        self.email = None
        self.localization = None
        self.friends_count = None
        self.last_name = None
        self.first_name = None
        self.birthday = None
        self.birth_localization = None
        self.social_networks = None

    def parse(self, data, modelFactory):
        super(User, self).parse(data, modelFactory)
        if data.get("birthday"):
            self.birthday = datetime.strptime(data["birthday"], "%Y-%m-%d")


class Subject(Model):
    def __init__(self):
        super(Subject, self).__init__()
        self.title = None
        self.description = None
        self.created_at = None


class Environment(Model):
    def __init__(self):
        super(Environment, self).__init__()
        self.name = None
        self.initials = None
        self.path = None


class Status(Model):
    def __init__(self):
        super(Status, self).__init__()
        self.type = None
        self.user = None
        self.text = None


class Enrollment(Model):
    def __init__(self):
        super(Enrollment, self).__init__()
        self.token = None
        self.state = None
        self.email = None


class Space(Model):
    def __init__(self):
        super(Space, self).__init__
        self.name = None
        self.description = None


class Course(Model):
    def __init__(self):
        super(Course, self).__init__
        self.name = None
        self.created_at = None
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
