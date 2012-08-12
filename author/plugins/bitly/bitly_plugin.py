from pelican import signals

def test(sender, **kwargs):
    import pdb;pdb.set_trace()
    pass

def register():
    signals.article_generator_init.connect(test)
