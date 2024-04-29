from baseball_team import BaseballTeam

practice_list = [1,2,3,4]
list_iterator = iter(practice_list)

#iterオブジェクトであることの確認
print(list_iterator)
#iterオブジェクト内のattribute(変数及び関数)の確認
print(dir(list_iterator))
#next()を用いると、先頭の値が取り除かれる
print(next(list_iterator))
#先頭の値が取り除かれていることの確認
print(list(list_iterator))

baseball_team = BaseballTeam('阪神タイガース', '兵庫県', '120')
baseball_team._player.extend(['西勇輝', '青柳晃洋', '佐藤輝明'])

print(baseball_team._player)
print(baseball_team.get_region_by_prefecture())

#BaseballTeamクラスの中で__iter__を定義したためオブジェクトをそのままinの中で使える。
for player in baseball_team:
    print(player)

#BaseballTeamクラスの中で__str__を用いてprintの結果を定義できる
print(baseball_team)
