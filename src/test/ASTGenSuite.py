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
                                    CallStmt(Id("foo"),[])
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
                                      CallStmt(
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
