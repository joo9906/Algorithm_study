import socket
from collections import deque
import heapq

HOST = '127.0.0.1'
PORT = 8747

# 입력 데이터 분류
char_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
allies = {}  # 아군 정보. 예) allies['A'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

sock = socket.socket()


def init(nickname) -> str:
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}')
        sock.connect((HOST, PORT))
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}'

        return submit(init_command)

    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')
        print(e)


def submit(string_to_send) -> str:
    try:
        sock.send((string_to_send + ' ').encode('utf-8'))

        return receive()

    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')

    return None


def receive() -> str:
    try:
        game_data = (sock.recv(1024)).decode()

        if int(game_data[0]) > 0:
            return game_data

        close()
    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')


def close():
    try:
        if sock is not None: sock.close()
        print('[STATUS] Connection closed')

    except Exception as e:
        print('[ERROR] Network connection has been corrupted.')


# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])  # 맵의 세로 크기
    map_width = int(header[1])  # 맵의 가로 크기
    num_of_allies = int(header[2])  # 아군의 수
    num_of_enemies = int(header[3])  # 적군의 수
    num_of_codes = int(header[4])  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([['' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, map_width):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])


def find_enenmy(my_position, enemy_position):
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    max_row = len(map_data)
    max_col = len(map_data[0])
    x0, y0 = my_position

    for dx, dy in delta:
        for i in range(1, 4):  # 1칸, 2칸, 3칸
            nx = x0 + dx * i
            ny = y0 + dy * i

            # 맵 밖으로 나가면 무시
            if not (0 <= nx < max_row and 0 <= ny < max_col):
                break

            if map_data[nx][ny] == 'X':  # 적이 있다면 True
                return True

    return False  # 없으면 False



import heapq


def caesar_decrypt(text: str, shift: int = 3) -> str:
    decrypted_text = []
    for char in text:
        if char.isalpha():  # 알파벳만 처리
            new_char = chr(((ord(char.upper()) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text.append(new_char)
        else:
            decrypted_text.append(char)  # 공백 또는 다른 문자 그대로 추가
    return ''.join(decrypted_text)


def route(map, start, end):
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_map = ['U A', 'R A', 'D A', 'L A']
    weight_map = [[float('inf')] * len(map[0]) for _ in range(len(map))]

    sx, sy = start
    ex, ey = end
    q = [(0, sx, sy, [])]
    weight_map[sx][sy] = 0
    result = []

    while q:
        weight, x, y, save_route = heapq.heappop(q)

        if weight > weight_map[x][y]:
            continue

        if x == ex and y == ey:
            result.append((len(save_route), save_route))
            continue

        for i in range(4):
            nx, ny = x + delta[i][0], y + delta[i][1]
            if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
                if map[nx][ny] in ['G', 'X']:
                    if weight + 1 < weight_map[nx][ny]:
                        weight_map[nx][ny] = weight + 1
                        new_route = save_route + [dir_map[i]]
                        heapq.heappush(q, (weight + 1, nx, ny, new_route))

    if result:
        result.sort(key=lambda x: x[0])
        return result[0][1]
    else:
        return []


NICKNAME = '서울5_왕주영'
game_data = init(NICKNAME)

# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:
    # 자기 차례가 되어 받은 게임정보를 파싱
    print(f'----입력데이터----\n{game_data}\n----------------')
    parse_data(game_data)

    # 파싱한 데이터를 화면에 출력하여 확인
    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(allies)})')
    for k, v in allies.items():
        if k == 'A':
            print(f'A (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 메가 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(enemies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'X (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])

    # 탱크의 동작을 결정하기 위한 알고리즘을 구현하고 원하는 커맨드를 output 변수에 담기
    # 코드 구현 예시: '아래쪽으로 전진'하되, 아래쪽이 지나갈 수 있는 길이 아니라면 '오른쪽로 전진'하라

    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'X':
                enemy_spot = (i, j)

    # 가중치를 판단하기 위해 deque을 사용해서 우선순위큐로 밀어넣으면서 할거임
    # 처음에는 가중치 0, 현재 위치를 넣고 돌릴 것
    output = 'A'  # 알고리즘에 의해 커맨드를 결정하기 전 임시로 A 지정

    if codes:
        for code in codes:
            decrypted_code = caesar_decrypt(code)
            print(f'암호문: {code}, 해독된 암호문: {decrypted_code}')

    my_position = [-1, -1]
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'A':
                my_position[0] = i
                my_position[1] = j
                break
        if my_position[0] > 0: break

    mx, my = my_position
    ex, ey = enemy_spot

    menhaten_x = mx - ex
    menhaten_y = my - ey

    abc = route(map_data, my_position, enemy_spot)

    if find_enenmy(my_position, enemy_spot):
        if mx - ex > 0 and my - ey == 0:
            output = 'U F'
        elif mx - ex < 0 and my - ey == 0:
            output = 'D F'
        elif mx - ex == 0 and my - ey > 0:
            output = 'L F'
        elif mx - ex == 0 and my - ey < 0:
            output = 'R F'
    else:
        output = abc[0]


    # while 문의 끝에는 다음 코드가 필수로 존재하여야 함
    # output에 담긴 값은 submit 함수를 통해 배틀싸피 메인 프로그램에 전달
    game_data = submit(output)

# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()