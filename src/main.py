from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter

proptest = {
    "href": "https://www.google.com",
    "target": "_blank",
}
def main():
    try:
        node = TextNode("I'm just gonna write a whole bunch of **BULLSHIT TEXT** and see if _ALL OF THIS MANAGES_ to go `THROUGH THE WAY` im hoping it does.", TextType.TEXT)
        step_1 = split_nodes_delimiter([node], "`", TextType.CODE)
        print(step_1)
        step_2 = split_nodes_delimiter(step_1, "**", TextType.BOLD)
        print(step_2)
        step_3 = split_nodes_delimiter(step_2, "_", TextType.ITALIC)
        print(step_3)
    except Exception as e:
        print(e)
main()