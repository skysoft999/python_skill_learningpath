#Authour: Sanu


preheat_oven = lambda : print('Preheating oven')
put_croissants_in = lambda: print('putting croissants in')
wait_five_min = lambda: print('Waiting five mins')
take_croissants_out = lambda: print('Take croissants out (and eat them!)')

#preheat_oven()
#put_croissants_in()
#wait_five_min()
#take_croissants_out()


"""
def perform_steps(*function):
    for function in function:
        function()


perform_steps(preheat_oven,
        put_croissants_in,
        wait_five_min,
        take_croissants_out)

"""

def create_recipe(*functions):
    def run_all():
        for function in functions:
            function()
    return run_all


recipe = create_recipe(preheat_oven,
        put_croissants_in,
        wait_five_min,
        take_croissants_out)

recipe()

