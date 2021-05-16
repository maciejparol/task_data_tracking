from views.dataclass import Resource

from .create_or_update_item import DOC as post_doc
from .create_or_update_item import create_or_update_item

ITEMS = [
    Resource("POST", "/item", create_or_update_item, "Create a item", "CREATE cart", post_doc),
]
