# Author: Wale Opakunle
# Source: Automate the Boring stuff with python Ch. 5 Practice Project

def displayInventory(inventory):
    """ Displays how much of what a player has in inventory
        
    Args:
        inventory (dict): Inventory containing items and their counts

    Returns: 
        None
    """
    print("Player Inventory:")
    # initialize the number of items
    all_items = 0

    # for loop to increase the number of all_items based on the dictionary values 
    for k, v in inventory.items():
        print(v, ' ', k)
        all_items += v

    print("Total number of items: " + str(all_items))

def addToInventory(inventory, addedItems):
    """ Add Items to inventory
        Args:
            inventory (dict):  Inventory containing items and their counts
            addedItems (list): Items to add to inventory

        Returns:
            updatedInventory (dict): Inventory containing updated items and their counts
    """
    """ 
    Procedure:
    - Ensure that the parameter passed is a dictionary
     - Loop through the items in the list and :.
       -   If the list item does not exist, add it to the dictionary and attach a value of 0 to it
       -   If it exists, increase the count of that particular item
    """
    updatedInventory = dict(inventory)
    # your code goes here
    for item in addedItems:
        updatedInventory.setdefault(item, 0)
        updatedInventory[item] += 1

    return updatedInventory
    


if __name__ == "__main__":

    stuff = {'rope': 2, 'torch': 9, 'gold coin': 412, 'dagger': 2, 'arrow': 22}
    displayInventory(stuff)

    #inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'emerald']
    inv = addToInventory(stuff, dragonLoot)
    displayInventory(inv)