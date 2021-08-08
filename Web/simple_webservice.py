import xml.etree.ElementTree as ET

import web  # do easy install here

# simple web service, to run , run this file in the terminal
# use localhost:8080/users to call list_users
# use localhost:8080/users/1 to call get_user

tree = ET.parse('user_data.xml')
root = tree.getroot()
urls = ('/users', 'list_users', '/users/(.*)', 'get_user')

app = web.application(urls, globals())


class list_users:
    def GET(self):
        output = 'users:[';
        for child in root:
            print('child', child.tag, child.attrib)
            output += str(child.attrib) + ','
        output += ']';
        return output


class get_user:
    def GET(self, user):
        for child in root:
            if child.attrib['id'] == user:
                return str(child.attrib)


if __name__ == '__main__':
    app.run()
