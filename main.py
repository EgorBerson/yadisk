import yadisk
y = yadisk.YaDisk(token = "AQAAAAA6wl8KAAf1Ojb4FhWkek5DiUxVxw6VOeY")
print(y.check_token())
def upload_file (file_path=()):
    file_name = file_path.split('/')[-1]
    y.upload(file_path, file_name)

def main():
    print (upload_file("/Users/EgorBerson_1/Desktop/Project/Files_sort/1.txt.webloc"))

if __name__ == '__main__':
    main()