import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(csv_file_path, word):
    return search.kimetsu_search(csv_file_path, word)

desktop.start(app_name,end_point,size)
