import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # width height optional, an additional optional space, first capture element from src="" second = https to convert http to httpss
    if match := re.search(
        r"^<iframe (?:width=\"\d*\" height=\"\d*\")?\s?src=\"((https?)\://(?:www\.)?youtube\.com/embed/\w*)\"(.*)?></iframe>$",
        s,
        re.IGNORECASE,
    ):
        # converting http to https
        if match.group(2) == "http":
            return (
                match.group(1)
                .replace("http", "https")
                .replace("www.", "")
                .replace("embed/", "")
                .replace("youtube.com", "youtu.be")
            )
        else:
            return (
                match.group(1)
                .replace("www.", "")
                .replace("embed/", "")
                .replace("youtube.com", "youtu.be")
            )
    else:
        return None


if __name__ == "__main__":
    main()
