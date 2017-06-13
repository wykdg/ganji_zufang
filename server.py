import web

urls = ("/heihei", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, world!'

    def POST(self):


        data = web.data()
        print data
if __name__ == "__main__":
    app.run()