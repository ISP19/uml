class Tool:
    def __init__(self, name, func):
        pass


class System:
    """System for paint, including save ,
    load , tool bar etc."""
    def __init__(self, tools=None, path=None):  # List of tools
        if tools is None:
            tools = [Tool("brush", "Draw function"), Tool("eraser", "Erase function")]
        self.tools = tools
        self.path = path

    def add_tool(self, new_tool: Tool):
        """Add tool"""
        pass

    def save(self):
        """Save file"""
        pass

    def change_path(self):
        """Change file path"""
        pass


class Paint:
    def __init__(self, width, height, file_path):
        """Paint interface"""
        self.width, self.height = width, height
        self.system = System(path=file_path)

    def display(self):
        """Display paint interface, able to interact with user"""
        pass

    def button(self):
        """Able to access each tool function"""
        pass
