from textnode import TextNode, TextType
from htmlnode import HTMLNode

proptest = {
    "href": "https://www.google.com",
    "target": "_blank",
}

def main():
    test_node = HTMLNode("<a>", "some text", props=proptest)
    print(test_node)
    print(test_node.props_to_html())

main()