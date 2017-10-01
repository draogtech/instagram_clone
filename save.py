import post


class Save:
    def save_post(self):
        post_file = open('post.csv', 'w', newline='').
        post_reader = csv.writerow([self.title, self.date_time, self.content])

        post_file.close()
