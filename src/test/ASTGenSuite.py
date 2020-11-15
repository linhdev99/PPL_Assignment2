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
        expect = Program([VarDecl(Id("x"),[1,2,3],None),VarDecl(Id("y"),[1,2],ArrayLiteral([1,2]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
