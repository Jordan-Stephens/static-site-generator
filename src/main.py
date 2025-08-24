from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

proptest = {
    "href": "https://www.google.com",
    "target": "_blank",
}
def main():
    node = ParentNode("p", None)
    try:
        print(node.to_html())
    except ValueError as e:
        print(e)
main()