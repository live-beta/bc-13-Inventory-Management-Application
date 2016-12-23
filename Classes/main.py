#!/usr/bin/env python
"""
Usage:
    inventory item_add <itemname> <cost> <productcode> <status> <description>...
    inventory item_remove <itemid>
    inventory item_list
    inventory product_type <product_code>
    inventory compute_assetvalue
    inventory (-i | --interactive)
    inventory (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
        --export
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from inventory import Item_console


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive(cmd.Cmd):
    intro = 'Welcome to My Inventory'
    prompt = 'Inventory_Manager>> '
    file = None

    @docopt_cmd
    def do_item_add(self, args):
        """
        Usage: item_add <itemname> <cost> <productcode> <status> <description>...
        """
        item_name = args["<itemname>"]
        description = args["<description>"]
        cost = args["<cost>"]
        productcode = args["<productcode>"]
        status = args["<status>"]
        description_info = ''
        for word in description:
            description_info += word + ''

        add_obj = Item_console()
        #print "this is to show that this function has a heart"
        add_obj.add_item(item_name, description_info.strip(), cost, productcode, status)

    @docopt_cmd
    def do_item_remove(self, args):
        """
        Usage: itemid <itemid>
        """
        item_id = args["<itemid>"]
        add_obj = Item_console()
        #add_obj.remove_item(item_id)
        print(add_obj.remove_item(item_id))

    @docopt_cmd
    def do_export(self, args):
        """
        Usage: item -- export
        """
        add_obj = Item_console()
        add_obj.list_export(itemid)

    @docopt_cmd
    def do_item_checkout(self, args):
        """
        Usage: item_checkout <itemid>
        """
        item_id = args["<itemid>"]
        add_obj = Item_console()
        add_obj.item_check_out(item_id)
        print
        "Item Checked Out"

    @docopt_cmd
    def do_item_checkin(self, args):
        """
        Usage: item_checkin <itemid>
        """
        item_id = args["<itemid>"]
        add_obj = Item_console()
        add_obj.item_check_in(item_id)
        print
        "Item Checked In"

    @docopt_cmd
    def do_item_list(self, args):
        """
        Usage: item_list
        """
        add_obj = Item_console()
        add_obj.list_item()

    @docopt_cmd
    def do_product_type(self,args):
        """
        Usage: product_type <product_code>
        """
        product_code=args["<product_code>"]
        add_obj=Item_console()
        print(add_obj.view_type_item(product_code))

    @docopt_cmd
    def do_compute_assetvalue(self, args):
        """
        Usage: compute_assetvalue
        """
        add_obj = Item_console()
        print(add_obj.compute_value())

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    print(__doc__)
    MyInteractive().cmdloop()
