from textnode import TextNode
from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception(f'Invalid Markdown: No closing delimiter: "{delimiter}" in "{node.text}"')
        
        temp_list = []
        for i in range(0, len(sections)):
            if i % 2 == 0:
                if not sections[i]:
                    continue
                temp_list.append(TextNode(sections[i], TextType.TEXT))
            else:
                if not sections[i]:
                    raise Exception(f'Invalid Markdown: Empty delimiters: "{delimiter}" in "{node.text}"')
                temp_list.append(TextNode(sections[i], text_type))
        new_nodes.extend(temp_list)

        
    return new_nodes