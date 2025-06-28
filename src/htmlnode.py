class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            return self.value
        if self.value is None:
            if self.children:
                children_html = ""
                for child in self.children:
                    children_html += child.to_html()
                return "<" + self.tag + ">" + children_html + "</" + self.tag + ">"
        return "<" + self.tag + ">" + self.value + "</" + self.tag + ">"
    
    def props_to_html(self):
        if self.props:
            props_string = ""
            for key, value in self.props.items():
                props_string += f' {key}="{value}"'
            return props_string
        return ""

    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if not self.value:
            raise ValueError
        
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        children_list = []
        
        if self.tag is None:
            raise ValueError ("No tag found")
        
        elif self.children is None:
            raise ValueError ("No children found")
        elif len(self.children) == 0:
            raise ValueError("Children list is empty")

        for child in self.children:
            if child is None:
                raise ValueError ("Child should not be blank")
            children_list.append(child.to_html())

        children_string = "".join(children_list)
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"

            
