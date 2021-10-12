import sys
import argparse
def cal(item):
    if item.o == 'add':
        return item.x + item.y
    elif item.o == 'mul':
        return item.x * item.y
    elif item.o == 'sub':
        return item.x - item.y
    elif item.o == 'div':
        return item.x / item.y
    else:
        print('enter a valid keyword')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=2.0,help='contact with harry')
    parser.add_argument('--y',type=float,default=3.0,help='Contact with harry')
    parser.add_argument('--o',type=str,default='add',help='contact with harry')

    item = parser.parse_args()
    sys.stdout.write(str(cal(item)))