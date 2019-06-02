
class RouteTrieNode:
    def __init__(self):
        self.title = None
        self.children = {}

    def insert(self, path):
        if path not in self.children:
            self.children[path] = RouteTrieNode()

class RouteTrie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = RouteTrieNode()

    def insert(self, url_list, title):
        current_path = self.root
        for path in url_list:
            current_path.insert(path)
            current_path = current_path.children[path]
        current_path.title = title

    def find(self, url_list):
        current_path = self.root
        if url_list==['']:
            return current_path.title
        for path in url_list:
            if path not in current_path.children:
                return 'not found handler'
            current_path = current_path.children[path]
        return current_path.title 

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie()
        self.trie.root.title = 'root handler'

    def add_handler(self, url, title):
        url_list = self.split_path(url)
        self.trie.insert(url_list, title)

    def lookup(self, url):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        url_list = self.split_path(url)
        return self.trie.find(url_list)


    def split_path(self, url):
        # trim
        if url[-1]=='/':
            url = url[:-1]

        url_list = url.split('/')
        return url_list[1:]

# create the router and add a route
router = Router("root handler") 
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

## result
# root handler
# None
# about handler
# about handler
# not found handler