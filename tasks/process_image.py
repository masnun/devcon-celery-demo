from app import app


@app.task(bind=True)
def process_image(self, data):
    print("Task name: {}".format(self.name))
    print("Incoming image file data: {}".format(data))
