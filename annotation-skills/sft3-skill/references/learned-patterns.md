# Learned Patterns

Use this file as the evolving memory for repeated SFT 三期 task types. Add only stable patterns that appeared repeatedly or were explicitly corrected by the user.

## Update Rules

- Add a pattern when the same task type appears at least 3 times and the pass/fail rule is stable.
- Add a pattern immediately when the user corrects the judgment rule or reason style.
- Do not add one-off observations, task-specific names, or accidental UI details.
- Keep every pattern short: task type, core pass condition, core fail condition, and varied phrase examples.
- Prefer general words like `角色`, `人物`, `车辆`, `目标`, `选项`, `页面`, `图表`, `关卡`.
- If a new pattern conflicts with an old one, update the old pattern instead of duplicating it.
- Treat examples as phrase pools, not fixed reasons. Rewrite them to fit the current page and avoid repeating the same sentence shape across nearby tasks.

## Current Learned Task Types

### 方块建造与破拆

- Core pass: can move, place/destroy blocks or terrain, and switch modes or block types when that is part of the core prompt.
- Core fail: character cannot move, cannot place/destroy, cannot switch required blocks, or start screen loops.
- Pass reasons:
  - 能够进行移动，能够实现破拆与建造元素，核心功能基本实现
  - 可以移动和破拆建造，但无法切换不同方块
  - 人物能放置和破坏方块，游戏核心功能可用
- Fail reasons:
  - 人物无法移动，无法破拆和建造元素
  - 人物无法放置和破坏方块，无法切换不同方块
  - 点击开始后一直循环继续游戏页面，无法正常游戏
  - 游戏提示词一直在屏幕上，无法正常开始

### 射击对战

- Core pass: view or direction can be controlled, player can shoot, enemies exist, and shooting causes attack or damage feedback.
- Core fail: cannot rotate/move view, cannot shoot, no enemies, enemies do not react, or enemy spawning makes the game unusable.
- Pass reasons:
  - 视角可以转动，可以对敌人射击，核心功能基本实现
  - 能控制视角并射击敌人，游戏可以正常进行
  - 页面有敌人和射击反馈，核心玩法可用
- Fail reasons:
  - 页面视角无法转动移动，无法射击，不能正常游戏
  - 点击鼠标无法发射子弹，无法正常游戏
  - 没有实现敌人机制，无法与敌人互相射击
  - 玩家射击对敌人没有效果，不会造成伤害
  - 游戏生成敌人过多，无法正常游戏
  - 未出现的敌人也会射击，玩家无法攻击到他

### 棋子或回合对战

- Core pass: player can place pieces or take turns, opponent responds according to game rules, and win/lose or end-state judgment exists.
- Core fail: opponent never moves, opponent moves repeatedly against rules, or turn flow gets stuck.
- Pass reasons:
  - 能够正常放置棋子，有游戏结束判定机制
  - 可以落子并进入回合流程，核心功能基本实现
- Fail reasons:
  - 对手一直处于思考中，不会落下棋子，无法正常游戏
  - 对手会连续多次落下棋子，不符合游戏设定
  - 进入对手进攻环节后，对手无法正常进攻

### 小车控制

- Core pass: vehicle direction, speed, or left-right movement can be controlled and the game runs normally.
- Core fail: vehicle cannot be controlled, turn flow blocks after player action, or page cannot render.
- Pass reasons:
  - 能够控制小车移动的方向和速度，核心功能实现
  - 能够控制小车左右移动，核心功能基本实现
  - 游戏的核心功能实现，能正常进行游戏
- Fail reasons:
  - 玩家进攻之后进入对手进攻环节，对手无法正常进攻
  - 页面无法正常渲染

### 航海词汇选择

- Core pass: can start the game, show a word and four choices, select an answer, and show progress/reward.
- Core fail: options cannot be clicked, no feedback appears, or the game cannot start.
- Pass reasons:
  - 能正常开始词汇选择，有岛屿进度和奖励显示
  - 可以选择同义词答题，有进度和奖励反馈
  - 点开始后能进入答题，选择后有奖励显示
  - 页面有词汇选项和关卡进度，答题流程能进行
- Fail reasons:
  - 选项点击无反馈，无法正常进行答题
  - 点击开始无反应，无法进入答题流程
  - 题目能显示但选项不能点，后续无法推进

### 平台跳跃收集

- Core pass: character can move and jump; obstacles, hazards, collection targets, or level progress are visible.
- Core fail: character cannot move or jump, immediately dies, or the first required obstacle blocks progress.
- Pass reasons:
  - 角色可以移动和跳跃，有机关和收集目标
  - 可以控制角色跳跃移动，核心功能基本实现
  - 人物移动跳跃正常，关卡里有障碍和目标
  - 能进入关卡操作角色，跳跃和收集玩法可用
- Fail reasons:
  - 角色无法跳过首个障碍，后续游戏无法进行
  - 只能移动无法跳跃，不能正常游戏
  - 开始后很快卡住，核心关卡无法推进

### 粒子或流场互动

- Core pass: named visual effect is visible and the main interaction or parameter change works.
- Core fail: the prompt's central effect is absent, especially required click bursts or required generated objects.
- Pass reasons:
  - 实现了粒子流动效果，调节后画面有变化
  - 页面有明显流动效果，核心展示基本实现
  - 画面能看到粒子运动，参数变化有反馈
  - 粒子效果能正常显示，交互后画面会变化
- Fail reasons:
  - 点击后没有明显粒子爆发效果
  - 未实现核心粒子效果，画面变化不明显
  - 页面有动效但缺少要求的点击反馈

### 光束反射绘制

- Core pass: light beam can be emitted and mirrors or reflective surfaces can change the beam path.
- Core fail: cannot draw mirrors, beam does not emit, or reflection has no visible effect.
- Pass reasons:
  - 可以发射光束，并绘制镜面进行反射
  - 实现了光束和镜面反射，核心功能基本实现
  - 光束能正常显示，画镜面后方向会变化
  - 页面支持绘制反射面，光线路径有反馈
- Fail reasons:
  - 无法绘制镜面，光束不能正常反射
  - 光束没有明显变化，未实现反射功能
  - 只能看到光束，画面没有反射效果

### 快速问答或真假判断

- Core pass: question appears, options can be selected, and feedback, score, timer, or progress updates.
- Core fail: options cannot be selected, no answer feedback appears, or timer/flow blocks gameplay.
- Pass reasons:
  - 可以进行真假判断，答题后有解释和加分
  - 能进行快速答题，有倒计时和得分反馈
  - 题目和选项能正常显示，选择后有反馈
  - 点击答案后会更新分数，问答流程能继续
- Fail reasons:
  - 选项点击无反馈，无法正常进行答题
  - 答题后没有反馈，无法推进后续题目
  - 页面有题目但无法选择，核心答题不可用

### Recent SFT Corrections

- Workflow: first read the prompt on the task page, then open the scene URL in a separate browser window/tab for testing. After testing, close the separate test window/tab and return to the task page to fill and submit the annotation. Avoid testing inside the preview drawer/modal unless no direct URL is available.
- Prompt-named behavior outranks general visual quality. Fail a good-looking result when a required named function is missing, for example `日期选择未更新历法`, `路径交叉后未显现符号`, `闭环后LED未点亮`, or `缺少悬浮基座和磁悬浮主体`.
- When listing several similar elements in a reason, use Chinese commas or pauses, not `/`. Prefer `温度、密度、颜色调节有反馈` and `广告、列车等核心元素缺失`.
- For specialized labels like EVA, use more口语 wording when possible: `宇航员出舱装备切换有效`, `宇航员穿戴状态能切换`, or `月球基地里装备切换有反馈`.
