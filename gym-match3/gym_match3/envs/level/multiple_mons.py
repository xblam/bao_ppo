from gym_match3.envs.levels import Level, base_hp
from gym_match3.envs.constants import GameObject
from gym_match3.envs.game import Point, Board, DameMonster, BoxMonster

MY_LEVEL =  [
     Level(
        10, 9, 5, 
        [
            [0, 0, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame],
            [0, 0, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
        ], [
        DameMonster(position=Point(0, 7),
                    width=2,
                    height=2,
                    hp=20+base_hp
                    ),
        DameMonster(position=Point(8, 0),
                    width=2,
                    height=2,
                    hp=30+base_hp
                    )
    ]),
    Level(
        10, 9, 5, 
        [
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0],
            [0, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ], [
        DameMonster(position=Point(0, 0),
                    width=2,
                    height=2,
                    hp=15+base_hp
                    ),
        DameMonster(position=Point(7, 6),
                    width=2,
                    height=2,
                    hp=30+base_hp
                    )
    ]),

    Level(10, 9, 5, [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [GameObject.monster_box_box, GameObject.monster_box_box, 0, 0, 0, 0, 0, 0, 0],
        [GameObject.monster_box_box, GameObject.monster_box_box, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
        [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ], [
        BoxMonster(GameObject.monster_box_box,
                   position=Point(1, 0),
                   width=2,
                   height=2,
                   hp=15+base_hp
                   ),
        DameMonster(position=Point(7, 0),
                    width=2,
                    height=2,
                    hp=30+base_hp
                    )
    ]),
     Level(
        10, 9, 5,
        [
            [0, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0],
            [0, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ], [
        DameMonster(position=Point(0, 6),
                    width=2,
                    height=2,
                    hp=18+base_hp
                    ),
        DameMonster(position=Point(5, 0),
                    width=2,
                    height=2,
                    hp=30+base_hp
                    )
    ]),
          Level(
        10, 9, 5,
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0],
            [0, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0],
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ], [
        DameMonster(position=Point(3, 6),
                    width=2,
                    height=2,
                    hp=30+base_hp
                    ),
        DameMonster(position=Point(5, 0),
                    width=2,
                    height=2,
                    hp=30+base_hp
                    )
    ]),
          
        Level(
        10, 9, 5,
        [
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0],
            [0, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ], [
        DameMonster(position=Point(0, 0),
                    width=2,
                    height=2,
                    hp=25+base_hp
                    ),
        DameMonster(position=Point(7, 6),
                    width=2,
                    height=2,
                    hp=30+base_hp
                    )
    ]),
    Level(
        10,9,5,
         [
            [0, 0, 0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, -1],
            [-1, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0, 0, -1, -1],
            [-1, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0, 0, -1, -1],
            [0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, -1]
        ], [
        DameMonster(position=Point(3, 3),
                    width=2,
                    height=2,
                    hp=25+base_hp
                    ),
        DameMonster(position=Point(5,3),
                    width=2,
                    height=2,
                    hp=30+base_hp
                    )
        ]
    ),
    Level(
        10,9,5,
       [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, -1, -1, 0, 0, 0],
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame],
            [GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame],
            [0, 0, 0, -1, -1, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ], [
        DameMonster(position=Point(4,0),
                    width=2,
                    height=2,
                    hp=25+base_hp
                    ),
        DameMonster(position=Point(4,7),
                    width=2,
                    height=2,
                    hp=25+base_hp
                    )
        ]
    ),
      Level(
        10,9,5,
    [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [0, 0, 0, 0, 0, 0, 0, -1, -1],
    [0, 0, 0, 0, 0, 0, 0, -1, -1],
    [0, 0, GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0],
    [0, 0, GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0, 0],
    [0, 0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0, 0],
    [-1, -1, 0, 0, 0, 0, 0, 0, 0],
    [-1, -1, 0, 0, 0, 0, 0, 0, 0]
    ], [
        DameMonster(position=Point(3,2),
                    width=2,
                    height=2,
                    hp=25+base_hp
                    ),
        DameMonster(position=Point(6,5),
                    width=2,
                    height=2,
                    hp=25+base_hp
                    )
        ]
    ),
          Level(
        10,9,5,
   [
    [0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0],
    [-1, -1, GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, -1, -1, -1],
    [0, 0, 0, 0, GameObject.monster_dame, GameObject.monster_dame, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0]
], [
        DameMonster(position=Point(3,2),
                    width=2,
                    height=2,
                    hp=25+base_hp
                    ),
        DameMonster(position=Point(5,4),
                    width=2,
                    height=2,
                    hp=25+base_hp
                    )
        ]
    ),
    
    
]


level_1 = MY_LEVEL