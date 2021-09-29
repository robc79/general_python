# Meta model.

class Subject():
    def __init__(self, *id_parts):
        self.id = id_parts
        self.tags = []
        self.nvps = {}
        self.nodes = {}


    def __str__(self):
        return f"Subject: {self.id}"


    def add_tag(self, tag):
        if tag is None or tag.strip() == "":
            raise ValueError("Tag must be specified.")
        if tag in self.tags:
            raise ValueError("Tag is already present.")
        self.tags.append(tag)


    def remove_tag(self, tag):
        self.tags.remove(tag)


    def add_or_replace_nvp(self, name, value):
        if name is None or name.strip() == "":
            raise ValueError("Name must be specified.")
        self.nvps[name] = value


    def remove_nvp(self, name):
        del(self.nvps[name])


    def add_node(self, taxonomy, node_name):
        if taxonomy is None or taxonomy.strip() == "":
            raise ValueError("Taxonomy must be specified.")
        try:
            names = self.nodes[taxonomy]
        except KeyError:
            names = []
        if node_name in names:
            raise ValueError("Node is already present.")
        names.append(node_name)
        self.nodes[taxonomy] = names


    def remove_node(self, taxonomy, node_name):
        names = self.nodes[taxonomy]
        names.remove(node_name)

