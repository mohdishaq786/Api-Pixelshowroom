from rembg.bg import remove, new_session

my_session = new_session("birefnet-general-lite")
def remove_bg(input):
    output = remove(input, session=my_session)#, bgcolor=[255, 255, 0])
    return output