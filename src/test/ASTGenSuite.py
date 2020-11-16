import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_1(self):
        """Simple program: int main() {} """
        input = """Var:x,y;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_2(self):
        """Simple program: int main() {} """
        input = """Var:x,y[1];"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_3(self):
        """Simple program: int main() {} """
        input = """Var:x,y[1]=1;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],IntLiteral(1))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_4(self):
        """Simple program: int main() {} """
        input = """Var:x = True;"""
        expect = Program([VarDecl(Id("x"),[],BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_5(self):
        """Simple program: int main() {} """
        input = """Var:x = False;"""
        expect = Program([VarDecl(Id("x"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_6(self):
        """Simple program: int main() {} """
        input = """Var:x = "False";"""
        expect = Program([VarDecl(Id("x"),[],StringLiteral("False"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_7(self):
        """Simple program: int main() {} """
        input = """Var:x = 1.2;"""
        expect = Program([VarDecl(Id("x"),[],FloatLiteral(1.2))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_8(self):
        """Simple program: int main() {} """
        input = """Var:x[1] = 1.2;"""
        expect = Program([VarDecl(Id("x"),[1],FloatLiteral(1.2))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_9(self):
        """Simple program: int main() {} """
        input = """Var:x[1][2][3], y[1][2] = {1,2};"""
        expect = Program([VarDecl(Id("x"),[1,2,3],None),VarDecl(Id("y"),[1,2],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_10(self):
        """Simple program: int main() {} """
        input = """Var:x[1][2][3], y[3] = {1,2,{1,2,3}};"""
        expect = Program([VarDecl(Id("x"),[1,2,3],None),VarDecl(Id("y"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_11(self):
        input = """Var: m, n[10], e[1][2] = {{},{5}};"""
        expect = Program([VarDecl(Id("m"),[],None), VarDecl(Id("n"),[10],None), VarDecl(Id("e"),[1,2],ArrayLiteral([ArrayLiteral([]), ArrayLiteral([IntLiteral(5)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_12(self):
        """Simple program: int main() {} """
        input = """Var: m, n[20], b[2][3][5] = {2,{4},"d"};"""
        expect = Program([VarDecl(Id("m"),[],None), VarDecl(Id("n"),[20],None), VarDecl(Id("b"),[2,3,5],ArrayLiteral([IntLiteral(2), ArrayLiteral([IntLiteral(4)]), StringLiteral("d")]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_13(self):
        input = """Var:x = 0x3, y = 0X3;"""
        expect = Program(
            [
                VarDecl(
                    Id("x"),
                    [],
                    IntLiteral(3)
                ),
                VarDecl(
                    Id("y"),
                    [],
                    IntLiteral(3)
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_14(self):
        input = """Var: a = 0o123, b = 0O123;"""
        expect = Program(
            [
                VarDecl(
                    Id("a"),
                    [],
                    IntLiteral(83)
                ),
                VarDecl(
                    Id("b"),
                    [],
                    IntLiteral(83)
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_15(self):
        input = """Var: x = 1e3, y[5] = {0x2, 0o4, 1.e2, 24, 9}, z = 2.e3;"""
        expect = Program(
            [
                VarDecl(
                    Id("x"),
                    [],
                    FloatLiteral(1000.0)
                ),
                VarDecl(
                    Id("y"),
                    [5],
                    ArrayLiteral(
                        [
                            IntLiteral(2),
                            IntLiteral(4),
                            FloatLiteral(100.0),
                            IntLiteral(24),
                            IntLiteral(9)
                        ]
                    )
                ),
                VarDecl(
                    Id("z"),
                    [],
                    FloatLiteral(2000.0)
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_16(self):
        input = """Var: a[2][3] = {{},{4,"text"},{}};"""
        expect = Program(
            [
                VarDecl(
                    Id("a"),
                    [2,3],
                    ArrayLiteral(
                        [
                            ArrayLiteral([]),
                            ArrayLiteral(
                                [
                                    IntLiteral(4),
                                    StringLiteral("text")
                                ]
                            ),
                            ArrayLiteral([])
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_17(self):
        input = """Function: main 
Body:
    foo();
EndBody."""
        expect = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            CallStmt(
                                Id("foo"),
                                []
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_18(self):
        input = """Function: main
Body:
    a = foo();
EndBody."""
        expect = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(
                                Id("a"),
                                CallExpr(
                                    Id("foo"),
                                    []
                                )
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_19(self):
        input = """Function: main
Body:
    Var: id[0x2][0X3];
    Var: id[0o2][0O10];
    foo();
    a = foo();
EndBody."""
        expect = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [
                            VarDecl(Id("id"),[2,3],None),
                            VarDecl(Id("id"),[2,8],None)
                        ],
                        [
                            CallStmt(
                                Id("foo"),
                                []
                            ),
                            Assign(
                                Id("a"),
                                CallExpr(
                                    Id("foo"),
                                    []
                                )
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_20(self):
        """Simple program: int main() {} """
        input = """Function: foo
Parameter: x
Body:
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_21(self):
        """Simple program: int main() {} """
        input = """Function: foo
Parameter: x, y[5][2]
Body:
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[5,2],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_22(self):
        """Simple program: int main() {} """
        input = """Var:x;
Function: foo
Parameter: x, y[5][2]
Body:
EndBody."""
        expect = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("foo"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [],
                                        []
                                    )
                                 )
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_23(self):
        """Simple program: int main() {} """
        input = """Var:x;
Function: foo
Parameter: x, y[5][2]
Body:
    Var: r = 3.14, e = 2.7e1;
EndBody."""
        expect = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("foo"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [
                                            VarDecl(Id("r"),[],FloatLiteral(3.14)),
                                            VarDecl(Id("e"),[],FloatLiteral(2.7e1))
                                        ],
                                        []
                                    )
                                 )
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_24(self):
        """Simple program: int main() {} """
        input = """Var:x;
Function: foo
Parameter: x, y[5][2]
Body:
    Var: r = 3.14, e = 2.7e1;
    a = x;
EndBody."""
        expect = Program(
                    [
                        VarDecl(Id("x"),[],None),
                        FuncDecl(Id("foo"),
                                 [
                                     VarDecl(Id("x"),[],None),
                                     VarDecl(Id("y"),[5,2],None)
                                 ],
                                    (
                                        [
                                            VarDecl(Id("r"),[],FloatLiteral(3.14)),
                                            VarDecl(Id("e"),[],FloatLiteral(2.7e1))
                                        ],
                                        [
                                            Assign
                                            (
                                                Id("a"),
                                                Id("x")
                                            )
                                        ]
                                    )
                                 )
                    ])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_25(self):
        """Simple program: int main() {} """
        input = r"""
        Function: foo
            Body:
                Break;
                Continue;
            EndBody."""
        expect = Program(
                [FuncDecl(Id("foo"),[],(
                              [],
                              [
                                  Break(),
                                  Continue()
                              ]
                            )
                          )
                ]
                )
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_26(self):
        input = r"""
        Function: foo
            Body:
                a = foo();
            EndBody."""
        expect = Program(
                [FuncDecl(Id("foo"),[],
                          (
                              [],
                              [
                                  Assign(
                                    Id("a"),
                                    CallExpr(Id("foo"),[])
                                  )
                              ]
                          )
                          )
                ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_27(self):
        input = r"""
        Function: foo
            Body:
                a = {1,3,5,7};
            EndBody."""
        expect = Program\
                (
                [FuncDecl(Id("foo"),[],
                          (
                              [],
                              [
                                  Assign(
                                    Id("a"),
                                    ArrayLiteral(
                                        [
                                        IntLiteral(1),
                                        IntLiteral(3),
                                        IntLiteral(5),
                                        IntLiteral(7)
                                        ]
                                    )
                                  )
                              ]
                          ))
                ]
                )
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_28(self):
        input = r"""
        Function: foo
            Body:
                {1,2,3}[2] = 5;
            EndBody."""
        expect = Program(
                [FuncDecl(Id("foo"),[],
                          (
                              [],
                              [
                                  Assign(
                                    ArrayCell(
                                    ArrayLiteral(
                                        [
                                        IntLiteral(1),
                                        IntLiteral(2),
                                        IntLiteral(3),
                                        ]
                                    ),
                                    [IntLiteral(2)]
                                    ),
                                    IntLiteral(5)
                                  )
                              ]
                          ))
                ]
                )
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_29(self):
        input = r"""
        Function: foo
            Body:
                Return foo(x+2);
            EndBody."""
        expect = Program(
                [FuncDecl(Id("foo"),[],
                          (
                              [],
                              [
                                  Return(
                                      CallExpr(
                                          Id("foo"),
                                          [BinaryOp(
                                              "+",
                                              Id("x"),
                                              IntLiteral(2)
                                          )]
                                      )
                                  )
                              ]
                          ))
                ]
                )
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_30(self):
        input = r"""
        Function: foo
            Body:
                If True Then
                    foo();
                ElseIf False Then
                    asd();
                ElseIf a < 2 Then
                    Var: x;
                Else
                    Var: x = 3;
                    x = x + 1;
                EndIf.
            EndBody."""
        expect = Program(
                [FuncDecl(Id("foo"),
                          [],
                          (
                              [],
                              [
                                  If(
                                      [
                                       (
                                        BooleanLiteral(True),
                                        [],
                                        [
                                            CallStmt(Id("foo"),[])
                                        ]
                                        ),
                                        (
                                        BooleanLiteral(False),
                                        [],
                                        [
                                            CallStmt(Id("asd"),[])
                                        ]
                                        ),
                                        (
                                        BinaryOp("<",Id("a"),IntLiteral(2)),
                                        [
                                            VarDecl(Id("x"),[],None)
                                        ],
                                        []
                                        )
                                      ],
                                      (
                                          [
                                              VarDecl(Id("x"),[],IntLiteral(3))
                                          ],
                                          [
                                              Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))
                                          ]
                                      )
                                  )
                              ]
                          ))
                ]
                )
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_31(self):
        input = r"""
        Function: foo
            Body:
                If x != y Then
                    x = x+2*y-(3-4)\foo(x+1);
                EndIf.
            EndBody."""
        expect = Program(
                [FuncDecl(Id("foo"),
                          [],
                          (
                              [],
                              [
                                  If(
                                      [
                                       (
                                        BinaryOp("!=",Id("x"),Id("y")),
                                        [],
                                        [
                                            Assign(
                                                Id("x"),
                                                BinaryOp("-",
                                                         BinaryOp("+",
                                                                  Id("x"),
                                                                  BinaryOp("*",
                                                                           IntLiteral(2),
                                                                           Id("y")
                                                                           )
                                                                  ),
                                                         BinaryOp("\\",
                                                                  BinaryOp("-",
                                                                           IntLiteral(3),
                                                                           IntLiteral(4)),
                                                                  CallExpr(
                                                                      Id("foo"),
                                                                      [BinaryOp("+",
                                                                                Id("x"),
                                                                                IntLiteral(1)
                                                                                )
                                                                       ]
                                                                  )
                                                                  )
                                                         )
                                            )
                                        ]
                                        )
                                      ],
                                      (
                                          [],
                                          []
                                      )
                                  )
                              ]
                          ))
                ]
                )
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_32(self):
        input = r"""
            Function: foo
                Body:
                    For (i = 0, i < 5, 1) Do
                        print(i);
                    EndFor.
                EndBody."""
        expect = Program(
            [FuncDecl(
                Id("foo"),
                [],
                (
                    [],
                    [
                        For(
                            Id("i"),
                            IntLiteral(0),
                            BinaryOp("<",
                                     Id("i"),
                                     IntLiteral(5)),
                            IntLiteral(1),
                            (
                                [],
                                [
                                    CallStmt(Id("print"),[Id("i")])
                                ]
                            )
                        )
                    ]
                )
            )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_333(self):
        """Simple program: int main() {} """
        input = r"""
            Function: testWhile
                Body:
                    While (i > 10) Do
                        i = i - 1;
                    EndWhile.
                EndBody."""
        expect = Program(
            [
                FuncDecl(
                    Id("testWhile"),
                    [],
                    (
                        [],
                        [
                            While(
                                BinaryOp(
                                    ">",
                                    Id("i"),
                                    IntLiteral(10)
                                ),
                                (
                                    [],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp(
                                                "-",
                                                Id("i"),
                                                IntLiteral(1)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_334(self):
        """Simple program: int main() {} """
        input = r"""
            Function: testWhile
                Body:
                    While (i > 10) Do
                    EndWhile.
                EndBody."""
        expect = Program(
            [
                FuncDecl(
                    Id("testWhile"),
                    [],
                    (
                        [],
                        [
                            While(
                                BinaryOp(
                                    ">",
                                    Id("i"),
                                    IntLiteral(10)
                                ),
                                (
                                    [],
                                    []
                                )
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_335(self):
        """Simple program: int main() {} """
        input = r"""
            Function: testWhile
                Body:
                    While (i < 10) Do
                        Var: x = 10;
                        i = x + 1;
                    EndWhile.
                EndBody."""
        expect = Program(
            [
                FuncDecl(
                    Id("testWhile"),
                    [],
                    (
                        [],
                        [
                            While(
                                BinaryOp(
                                    "<",
                                    Id("i"),
                                    IntLiteral(10)
                                ),
                                (
                                    [
                                        VarDecl(Id("x"),[],IntLiteral(10))
                                    ],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp(
                                                "+",
                                                Id("x"),
                                                IntLiteral(1)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_36(self):
        """Simple program: int main() {} """
        input = r"""
        Function: testDowhile
            Body:
                Do
                    i = i * 2;
                    Break;
                While (i < 10)
                EndDo.
            EndBody."""
        expect = Program(
            [
                FuncDecl(
                    Id("testDowhile"),
                    [],
                    (
                        [],
                        [
                            Dowhile(
                                (
                                    [],
                                    [
                                        Assign(
                                            Id("i"),
                                            BinaryOp("*",Id("i"),IntLiteral(2))
                                        ),
                                        Break()
                                    ]
                                ),
                                BinaryOp("<",Id("i"),IntLiteral(10))
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_37(self):
        input = r"""Function: main 
Body:
    a[1][2][3] = x[1][a][foo()];
EndBody."""
        expect = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            Assign(
                                ArrayCell(
                                    Id("a"),
                                    [
                                        IntLiteral("1"),
                                        IntLiteral("2"),
                                        IntLiteral("3")
                                    ]
                                ),
                                ArrayCell(
                                    Id("x"),
                                    [
                                        IntLiteral("1"),
                                        Id("a"),
                                        CallExpr(
                                            Id("foo"),
                                            []
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_38(self):
        """Simple program: int main() {} """
        input = r"""
        Function: foo
            Body:
                a[i][1] = a[3][4] + 5 \ (2 * 3) -  a[6][b[1]];
                Return a[4][2];
            EndBody."""
        expect = Program(
            [
                FuncDecl(
                    Id("foo"),
                    [],
                    (
                        [],
                        [
                            Assign(
                                ArrayCell(
                                    Id("a"),
                                    [
                                        Id("i"),
                                        IntLiteral("1")
                                    ]
                                ),
                                BinaryOp(
                                    "-",
                                    BinaryOp(
                                        "+",
                                        ArrayCell(
                                            Id("a"),
                                            [
                                                IntLiteral(3),
                                                IntLiteral(4)
                                            ]
                                        ),
                                        BinaryOp(
                                            "\\",
                                            IntLiteral(5),
                                            BinaryOp(
                                                "*",
                                                IntLiteral(2),
                                                IntLiteral(3)
                                            )
                                        )
                                    ),
                                    ArrayCell(
                                        Id("a"),
                                        [
                                            IntLiteral(6),
                                            ArrayCell(
                                                Id("b"),
                                                [
                                                    IntLiteral(1)
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ),
                            Return(
                                ArrayCell(
                                    Id("a"),
                                    [
                                        IntLiteral(4),
                                        IntLiteral(2)
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_39(self):
        """Simple program: int main() {} """
        input = r"""
        Function: foo
            Body:
                Return a[10][10];
            EndBody."""
        expect = Program(
            [
                FuncDecl(
                    Id("foo"),
                    [],
                    (
                        [],
                        [
                            Return(
                                ArrayCell(
                                    Id("a"),
                                    [
                                        IntLiteral(10),
                                        IntLiteral(10)
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))
