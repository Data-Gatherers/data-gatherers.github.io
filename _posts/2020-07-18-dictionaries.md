---
layout: post
title:  "Dictionaries in python"
author: wale
categories: [ Saturday Meetup - Week 3 ]
image: assets/images/18-07-2020-sm3-july/key-value.jpg
tags: featured

---

Please find here the video for the discussion on Saturday, 18th of July.

<iframe src="https://drive.google.com/file/d/1Qz_-06E0mN0mqs8ji6Gn-rq7goZL9PyB/preview" width="640" height="480"></iframe>

You can get the source code for the "game inventory" task discussed in the session [here](/assets/code/saturday-meetup3-july/game-inventory.py){:target="blank"}.

Alternatively, you can go through it below.

``` python
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
     - Loop through the items in the list and :
       -   If the list item does not exist, add it to the dictionary and attach a value of 0 to it
       -   If it exists, increase the count of that particular item
    """
    updatedInventory = dict(inventory) # dict() creates a new empty dictionary with appropriate mapping
    # loop throught the items in the list
    for item in addedItems:
        # if item from list does not exist in the dictionary, create a key for it and assign a default value of 0 to it.
        updatedInventory.setdefault(item, 0)
        # increase the count, since we want to count the number of items in inventory.
        updatedInventory[item] += 1

    return updatedInventory

if __name__ == "__main__":

    stuff = {'rope': 2, 'torch': 9, 'gold coin': 412, 'dagger': 2, 'arrow': 22}
    displayInventory(stuff)

    #inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'emerald']
    inv = addToInventory(stuff, dragonLoot)
    displayInventory(inv)

```
