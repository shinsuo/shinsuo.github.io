import os

_dir = "game"



_game_title = '<h2>%s</h2><br>'
_game_link = '<a href="%s/%s">%s > %s</a><br>'
  
  
# for path,d,filelist in os.walk(_dir):  
#     print '----'+str(d);  
#     for filename in filelist:  
#         print os.path.join(path, filename)

_path = _dir

html_data = ""

for game_list in os.listdir(_path):
    print_title = False

    if(game_list != ".DS_Store"):
        if(~print_title):
            html_data += _game_title%game_list
            print_title = True
        _path = _dir+"/"+game_list
        for game_list2 in os.listdir(_path):
            if(game_list2 != ".DS_Store"):
                # print _path, game_list2
                html_data += _game_link%(_path, game_list2, game_list,game_list2)
    pass

fo = open("game.html", "w")
fo.write(html_data)
fo.close()