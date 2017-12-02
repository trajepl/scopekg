import time
import random
import string

def run_time(func):
    def wrapper(*argv):
        s = time.time()
        f = func(*argv)
        e = time.time()
        print(func.__name__ + ' runtime: ' + str(e-s))
        return f
    return wrapper

def extract_info(fn):
    player, team, position, birth_place = set(), set(), set(), set()

    with open(fn, 'r') as info_out:
        info_out.readline()
        for line in info_out.readlines():
            line = line.strip().split(',')
            player.add(line[0])
            team.add(line[1])
            position.add(line[2])
            birth_place.add(line[-3])

    return player, team, position, birth_place

@run_time
def str_random(fn, fn_t, max_num):
    players, teams, positions, birth_places = extract_info(fn)
    cnt = 0
    with open(fn_t, 'w') as t_out:
        for player in range(99999999):
            r_birthday = random.randint(1973, 2000)
            r_year_e = r_birthday + random.randint(16, 20)
            constant_year = random.randint(10, 25)

            for i in range(random.randint(1, 10)):
                r_team = random.choice(list(teams))
                r_position = random.choice(list(positions))
                r_bplace = random.choice(list(birth_places))
                
                # time random
                r_year_s = r_year_e
                gap_year = random.randint(0, 8)
                constant_year -= gap_year
                r_year_e = r_year_s + random.randint(0, gap_year)

                line_list = [player, r_team, r_position, r_birthday, r_bplace, r_year_s, r_year_e]
                
                line = ''
                for item in line_list:
                    line += str(item) + ','
                line = line[:-1]
                
                t_out.write(line + '\n')

                cnt += 1
                if constant_year < 0: 
                    break
            
            if cnt > max_num:
                return 


if __name__ == '__main__':
    str_random('../origin_data/line', '../origin_data/line_1kw', 10000 * 1000)