import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^<iframe src="(.+)\"></iframe>$', s):
        url = matches.group(1)
        if not re.search(r"(.+)youtube(.+)", url):
            return None
        url = re.sub(r"https?://(?:www\.)?youtube\.com/embed/", "https://youtu.be/", url)
        return url
    else:
        return "None"


if __name__ == "__main__":
    main()


