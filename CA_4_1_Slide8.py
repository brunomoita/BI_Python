def fun (**args):
    for k, v in args.iteritems():
        print k, '::::',v


fun (a ='apple', b = 'ball')