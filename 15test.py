import curses
from random import randint

# 游戏设置
WIDTH = 40  # 游戏区域宽度
HEIGHT = 20  # 游戏区域高度
SNAKE_CHAR = 'O'  # 蛇的身体字符
FOOD_CHAR = '*'  # 食物的字符
INITIAL_SPEED = 150  # 初始速度（毫秒）
SPEED_INCREMENT = 1  # 每吃一个食物后速度增加

# 方向键映射
DIRECTIONS = {
    curses.KEY_UP: (0, -1),
    curses.KEY_DOWN: (0, 1),
    curses.KEY_LEFT: (-1, 0),
    curses.KEY_RIGHT: (1, 0),
}

def main(stdscr):
    # 初始化curses
    curses.curs_set(0)  # 隐藏光标
    stdscr.nodelay(1)   # 非阻塞输入
    stdscr.timeout(INITIAL_SPEED)  # 设置刷新速度

    # 初始化蛇和食物
    snake = [(WIDTH // 2, HEIGHT // 2)]  # 蛇的初始位置（居中）
    direction = DIRECTIONS[curses.KEY_RIGHT]  # 初始方向向右
    food = (randint(1, WIDTH - 2), randint(1, HEIGHT - 2))  # 食物的初始位置

    score = 0
    speed = INITIAL_SPEED
    paused = False

    while True:
        # 清屏
        stdscr.clear()

        # 绘制游戏边界
        for x in range(WIDTH):
            stdscr.addch(0, x, '#')
            stdscr.addch(HEIGHT - 1, x, '#')
        for y in range(HEIGHT):
            stdscr.addch(y, 0, '#')
            stdscr.addch(y, WIDTH - 1, '#')

        # 绘制蛇
        for segment in snake:
            stdscr.addch(segment[1], segment[0], SNAKE_CHAR)

        # 绘制食物
        stdscr.addch(food[1], food[0], FOOD_CHAR)

        # 显示分数和速度
        stdscr.addstr(HEIGHT, 0, f"Score: {score} | Speed: {INITIAL_SPEED - speed}")

        # 刷新屏幕
        stdscr.refresh()

        # 获取用户输入
        key = stdscr.getch()

        # 处理按键
        if key == ord('p'):  # 暂停/继续
            paused = not paused
            if paused:
                stdscr.addstr(HEIGHT // 2, WIDTH // 2 - 5, "PAUSED")
                stdscr.refresh()
                while True:
                    key = stdscr.getch()
                    if key == ord('p'):
                        paused = not paused
                        break
        elif key == ord('q'):  # 退出游戏
            break
        elif key in DIRECTIONS and not paused:  # 方向键
            # 防止蛇反向移动
            if (key == curses.KEY_UP and direction != DIRECTIONS[curses.KEY_DOWN]) or \
               (key == curses.KEY_DOWN and direction != DIRECTIONS[curses.KEY_UP]) or \
               (key == curses.KEY_LEFT and direction != DIRECTIONS[curses.KEY_RIGHT]) or \
               (key == curses.KEY_RIGHT and direction != DIRECTIONS[curses.KEY_LEFT]):
                direction = DIRECTIONS[key]

        if paused:
            continue

        # 计算蛇头的新位置
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # 碰撞检测
        if (new_head[0] <= 0 or new_head[0] >= WIDTH - 1 or
            new_head[1] <= 0 or new_head[1] >= HEIGHT - 1 or
            new_head in snake):
            break  # 游戏结束

        # 插入新蛇头
        snake.insert(0, new_head)

        # 检查是否吃到食物
        if new_head == food:
            score += 1
            speed = max(50, speed - SPEED_INCREMENT)  # 加快速度
            stdscr.timeout(speed)
            food = (randint(1, WIDTH - 2), randint(1, HEIGHT - 2))  # 生成新食物
        else:
            snake.pop()  # 如果没有吃到食物，移除蛇尾

    # 游戏结束
    stdscr.addstr(HEIGHT // 2, WIDTH // 2 - 5, "GAME OVER!")
    stdscr.addstr(HEIGHT // 2 + 1, WIDTH // 2 - 5, f"Final Score: {score}")
    stdscr.refresh()
    stdscr.getch()  # 等待用户按任意键退出

if __name__ == "__main__":
    curses.wrapper(main)
