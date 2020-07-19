from collections import defaultdict


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

class RouteTrie:
    def __init__(self, root_handler=None):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        path_parts = self.get_path_parts(path)
        node = self.root
        for part in path_parts:
            if part != '':
                # node.insert(part)
                node = node.children[part]

        node.handler = handler

    def find(self, path):

        path_parts = self.get_path_parts(path)
        node = self.root

        for part in path_parts:
            if part != '':
                node = node.children[part]

        return node.handler

    def get_path_parts(self, path):
        return path.split('/')


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler):  self.route_trie = RouteTrie(root_handler)

    def add_handler(self, path, handler): self.route_trie.insert(path, handler)

    def lookup(self, path): return self.route_trie.find(path)


if __name__ == '__main__':
    # Here are some test cases and expected outputs you can use to test your implementation

    # create the router and add a route
    router = Router("root handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home", "home handler")  # add a route
    router.add_handler("/home/about", "about handler")  # add a route
    router.add_handler("/home/about/me/edit", "edit handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'home handler'
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler'
    print(router.lookup("/home/about/me/edit"))  # should print 'edit handler'
