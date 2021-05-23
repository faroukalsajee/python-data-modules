# Data Module
def get_phone_info_list():
    """ Returns a list of phone data """

    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>
    phones = \
        [
            "1,Samsung,Galaxy S7,32,Android,6.0 Marshmallow,349.99",
            "2,Samsung,Galaxy S8,32,Android,7.0 Nougat,399.99",
            "3,Samsung,Galaxy S9,32,Android,8.0 Oreo,499.99",
            "4,Samsung,Galaxy S10,32,Android,9.0 Pie,599.99",
            "5,LG,Style 2 Plus,8,Android,6.0 Marshmallow,299.00",
            "6,LG,K4,16,Android,5.1.1 Lollipop,349.00",
            "7,Google,Pixel,32,Android,7.1 Nougat,599.99",
            "8,Google,Pixel XL,32,Android,7.1 Nougat,549.99",
            "9,Motorola,Moto G,16,Android,5.0.2 Lollipop,299.99",
            "10,Motorola,Moto G Power,16,Android,5.0.2 Lollipop,249.99"
        ]

    return phones


def get_tablet_info_list():
    """ Returns a list of tablet data """

    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>
    tablets = \
        [
            "1,Apple,iPad Mini,64,iOS,12.3,399.00",
            "2,Apple,iPad,64,iOS,12.3,329.00",
            "3,Apple,iPad Air,64,iOS,12.3,499.00",
            "4,Samsung,Galaxy Tab,8,Android,5.1.1 Lollipop,139.99",
            "5,Samsung,Galaxy Tab S3,64,Android,6.0 Marshmallow,549.99",
            "6,Microsoft,Surface Go,64,Windows,10 Home,469.00",
            "7,Microsoft,Surface Pro,256,Windows,10 Pro,1299.00",
            "8,Microsoft,Surface Book,128,Windows,10 Pro,1599.00",
            "9,Acer,Iconia B3,16,Android,7.0 Nougat,179.99",
            "10,Asus,ZenPad 10,64,Android,7.0 Nougat,401.98",
            "11,Asus,Transformer,64,Windows,10 Home,381.51"
        ]

    return tablets


def get_laptop_info_list():
    """ Returns a list of laptop data """

    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>
    laptops = \
        [
            "1,Apple,MacBook Air,8,MacOS,10.13 High Sierra,1199.00",
            "2,Apple,MacBook,16,MacOS,10.13 High Sierra,1599.00",
            "3,Apple,MacBook Pro,16,MacOS,10.13 High Sierra,1699.00",
            "4,Lenovo,ThinkPad X1 Carbon,16,Windows,10 Home,1147.34",
            "5,Lenovo,ThinkPad X390 Yoga,16,Windows,10 Home,1869.00",
            "6,Lenovo,IdeaPad 130S,2,Windows,10 Home,274.99",
            "7,Dell,XPS 15,8,Windows,10 Pro,1329.99",
            "8,Dell,XPS 13,8,Windows,10 Pro,1199.99",
            "9,Dell,Inspiration 15 3000,4,Windows,10 Home,419.99",
            "10,Google,Pixelbook,8,Chrome OS,74,1299.00",
            "11,Asus,VivoBook F510UA Thin,8,Windows,10 Home,728.43",
            "12,Asus,Chromebook C523,4,Chrome OS,74,349.99"
        ]

    return laptops
