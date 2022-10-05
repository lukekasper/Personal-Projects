import markdown2
import re


def markdown_converter(content):

    lines_list = content.split('\n')
    html_list = []

    for line in lines_list:

        # Headings
        head = re.match(r"^#*", line).end()
        line = re.sub(r"^#*", "", line)
        if head > 0:
            line = html_wrapper(line, f"h{head}", "")

        # List items
        if re.findall(r"\*", line) == ['*']:
            line = re.sub(r"\*", "", line)
            html_wrapper(line, "li", "")

        # Paragraph
        if re.match(r"^\w", line) is not None:
            html_wrapper(line, "p", "")

        # Links
        if re.search(r"\[", line) is not None:
            line_list = re.split(r"\[|\)", line)
            for index, item in enumerate(line_list):
                if re.search(r"\(", item) is not None:
                    item = re.sub(r"\(", "<a href=\"", item) + "\">"
                    sub_list = re.split(r"\]", item)
                    line_list[index] = sub_list[1] + sub_list[0] + "</a>"
            line = ''.join(line_list)

        # Bold Font
        if re.search(r"\*\*", line) is not None:
            index = 1
            line_list = re.split(r"\*\*", line)
            if re.match(r"\*\*", line) is not None:
                index = 0
            line_list.pop(0)
            while index < len(line_list):
                line_list[index] = html_wrapper(line_list[index], "span", " style=\"font-weight: bold;\"")
                index += 2
            line = ''.join(line_list)

        html_list.append(line)

    # Unordered list brackets
    index = 0
    for line in html_list:

        if re.search(r"<li>", html_list[index]) is None and re.search(r"<li>", html_list[index + 1]) is not None:
            html_list[index] = "\n<ul>"
            index += 1
        elif re.search(r"<li>", html_list[index - 1]) is not None and re.search(r"<li>", html_list[index + 1]) is None:
            html_list[index + 1] = "</ul>\n"
            index += 1

        if index == len(html_list) - 1:
            if re.search(r"<li>", html_list[index]) is not None:
                html_list.append("</ul>")
            break
        index += 1

    content = '\n'.join(html_list)


def html_wrapper(line, element, mod):
    line = "<" + element + mod + ">" + line + "</" + element + ">"
    return line
