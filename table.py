import gi
import cmc_api
import const
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def create_row_values(self):
    for i, d in enumerate(cmc_api.get_data()['data']):
        self.list_store.append([
            f"{d['name']}",
            f"{d['symbol']}",
            "${:,.4f}".format(d['quote']['USD']['price']),
            f"{round(d['quote']['USD']['percent_change_24h'], 2)}",
            f"{round(d['quote']['USD']['percent_change_7d'], 2)}",
            "${:,.2f}".format(d['quote']['USD']['market_cap']),
            "${:,.2f}".format(d['quote']['USD']['volume_24h']),
            "{:,.2f}".format(d['circulating_supply'])
        ])


def create_column_headers(self):
    self.list_store = Gtk.ListStore(str, str, str, str, str, str, str, str)
    tree_view = Gtk.TreeView(model=self.list_store)
    [tree_view.append_column(Gtk.TreeViewColumn(c, Gtk.CellRendererText(), text=i))
        for i, c in enumerate(const.column_headers)]

    self.add(tree_view)