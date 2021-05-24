def shinobi(name, *args, **kwargs):
    print ('You have selected the shinobi', name,)
    for a in args:
        print (a)
    for kw in kwargs:
        print (kw, ':', kwargs[kw])

shinobi('Naruto', 'In the hidden leaf village', 'friend of Sasuke', poem_writer='Mathieu', rank='Chunin')