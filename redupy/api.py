from HttpClient import HttpClient
from binder import bind_api
from models import ModelFactory


class Redu(object):

    def __init__(self, consumer_key, consumer_secret,
        pin=None, model_factory=None, base_url="http://redu.com.br/api/"):
        self.client = HttpClient(consumer_key, consumer_secret, pin)
        self.base_url = base_url
        self.model_factory = model_factory or ModelFactory

    def getAuthorizeUrl(self):
        return self.client.getAuthorizeUrl()

    def initClient(self, pin):
        self.client.initClient(pin)

    getMe = bind_api(path="me", mehtod="get", payload_type="user")

    getUser = bind_api(path="users/{0}", method="get", payload_type="user")

    getUserBySpace = bind_api(path="spaces/{0}/users", method="get",
        payload_type="user")

    getEnvironment = bind_api(path="environments/{0}", method="get",
        payload_type="environment")

    postEnvironment = bind_api(path="environments", method="post",
        payload_type="environment", payload_params=["name", "path", "initials",
        "description"])

    editEnvironment = bind_api(path="environments/{0}", method="put",
        send_type="environment", payload_params=["name", "path", "initials",
        "description"])

    deleteEnvironment = bind_api(path="environments/{0}", method="delete")

    getSubjectsBySpace = bind_api(path="spaces/{0}/subjects", method="get",
        payload_type="subject")

    getSubject = bind_api(path="subjects/{0}", method="get",
        payload_type="subject")

    getSpace = bind_api(path="spaces/{0}", method="get",
        payload_type="space")

    editSpace = bind_api(path="spaces/{0}", method="put",
        payload_params=['name', 'description'], send_type="space")

    postSpace = bind_api(path="courses/{0}/spaces", method="post",
        payload_type='space', payload_params=['name', 'description'])

    getSpaceByCourse = bind_api(path="courses/{0}/spaces", method="get",
        payload_type="space")

    deleteSpace = bind_api(path="spaces/{0}", method="delete")

    getStatus = bind_api(path="statuses/{0}", method="get",
        payload_type="status")

    getAnswers = bind_api(path="statuses/{0}/answers", method="get",
        payload_type="status")

    postAnswer = bind_api(path="statuses/{0}/answers", method="post",
        payload_type="status", payload_params=["text"])

    getStatusByUser = bind_api(path="users/{0}/statuses", method="get",
        payload_type="status", querry_params=["type", "page"])

    getTimelineByUser = bind_api(path="users/{0}/statuses/timeline",
        method="get", payload_type="status", querry_params=["type", "page"])

    postStatusUser = bind_api(path="users/{0}/statuses", method="post",
        payload_type="status", payload_params=["text"])

    getTimelineBySpace = bind_api(path="spaces/{0}/statuses/timeline",
        method="get", payload_type="status", querry_params=["type", "page"])

    getStatusBySpace = bind_api(path="spaces/{0}/statuses", method="get",
        payload_type="status", querry_params=["type", "page"])

    postStatusSpace = bind_api(path="spaces/{0}/statuses", method="post",
        payload_type="status", payload_params=["text"])

    getStatusByLecture = bind_api(path="lectures/{0}/statuses", method="get",
        payload_type="status", querry_params=["type", "page"])

    postStatusLecture = bind_api(path="lectures/{0}/statuses", method="post",
        payload_type="status", payload_params=["text"])

    deleteStatus = bind_api(path="statuses/{0}", method="delete")

    getCourse = bind_api(path="courses/{0}", method="get",
        payload_type="course")

    postCourse = bind_api(path="environments/{0}/courses", method="post",
        payload_type="course", payload_params=["name", "path", "description",
        "workload"])

    editCourse = bind_api(path="courses/{0}", method="put", send_type="course",
        payload_params=["name", "path", "description", "workload"])

    getCoursesByEnvironment = bind_api(path="environments/{0}/courses", method="get",
        payload_type="course")

    deleteCourse = bind_api(path="courses/{0}", method="delete")

    getEnrollment = bind_api(path="enrollments/{0}", method="get",
        payload_type="enrollment")

    postEnrollment = bind_api(path="courses/{0}/enrollments", method="post",
        payload_type="enrollment", payload_params=["email"])

    getEnrolmentsByCourse = bind_api(path="courses/{0}/enrollments",
        method="get", payload_type="enrollment")

    deleteEnrollment = bind_api(path="enrollments/{0}", method="delete")
