# calabiqiu-auto

卡拉彼丘自动挂机脚本

下载地址
链接：https://pan.baidu.com/s/1CCaJMP2W0UD4yVI0aRuDBw?pwd=2233 
提取码：2233

使用方法
1.下载：src\dist\calabiqiu-auto.exe
2.桌面或者卡拉比丘窗口大小调整为1920 X 1080
3.游戏打开至无限团竞界面，不要点击开始
4.必须以管理员权限运行calabiqiu-auto.exe文件
PS：脚本启动期间不要触碰鼠标键盘，不要离开卡拉比丘全屏界面，否则无法正常运行

项目背景
需求分析：卡拉比丘有完成任务需求，和自动挂机升级需求，和好感度需求
全自动挂机困境：完全不打伤害会被系统检测并不给予任务完成计算和升级经验和好感度

解决方案
无限团竞，基于经验选中奥黛丽，当用户大约挂机 1min 中后会被系统检测到挂机，然后让 AI 打伤害，在最后 45/50 时候，输入按键或者移动鼠标，就会自动连回来，不会受到挂机处罚

自动化的步骤
首先手动进入无限团竞界面， 自动点击开始，等待排进去，排进去后自动点击准备，自动点击奥黛丽，点击锁定
挂机180s，并每间隔 5s 检测一次顶部双方战绩数字，
然后当一方到达或者超过 45 后，输入 w+单击，
等待对局结束，自动点击返回大厅，自动点击离开，
然后开始第二次循环

代码实现
main.py



