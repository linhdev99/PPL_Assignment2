from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        # return Program([VarDecl(Id(ctx.ID().getText()),[],None)])
        mainList = []
        for x in ctx.main():
            mainCell = self.visitMain(x)
            if isinstance(mainCell, list):
                mainList.extend(mainCell if mainCell else [])
            else:
                mainList.append(mainCell)
        return Program(mainList)

    def visitMain(self, ctx:BKITParser.MainContext):
        if ctx.var_declare():
            return self.visitVarDecl(ctx.var_declare())
        else:
            return self.visit(ctx.func_declare())

    def visitVarDecl(self, ctx:BKITParser.Var_declareContext):
        return self.visitVarList(ctx.var_list())

    def visitVarList(self, ctx:BKITParser.Var_listContext):
        return self.visitVarNormal(ctx.var_normal())

    def visitVarNormal(self, ctx:BKITParser.Var_normalContext):
        varListDecl = []
        for x in ctx.var_normal_list():
            temp = self.visitVarNormalList(x)
            if isinstance(temp, list):
                varListDecl.extend(temp if temp else [])
            else:
                varListDecl.append(temp)
        return varListDecl

    def visitVarNormalList(self, ctx:BKITParser.Var_normal_listContext):
        m_getScalarVar = self.visitScalarVarInt(ctx.scalar_var_int())
        m_variable = m_getScalarVar[0]
        m_varDimen = m_getScalarVar[1]
        m_varInit = None
        if ctx.array_lit():
            m_varInit = self.visitArrayLiteral(ctx.array_lit())
            return VarDecl(m_variable,m_varDimen,m_varInit)
        elif ctx.all_lit():
            m_varInit = self.visitAllLiteral(ctx.all_lit())
            return VarDecl(m_variable,m_varDimen,m_varInit)
        else:
            return VarDecl(m_variable,m_varDimen,m_varInit)

    def visitScalarVarInt(self, ctx:BKITParser.Scalar_var_intContext):
        if ctx.getChildCount() > 1:
            listIndex = []
            for x in ctx.index_var_int():
                listIndex.extend(self.visitIndexVarInt(x))
            return [Id(ctx.ID().getText()),listIndex]
        else:
            return [Id(ctx.ID().getText()),[]]

    def visitIndexVarInt(self,ctx:BKITParser.Index_var_intContext):
        return ctx.INTLIT().getText()

    def visitAllLiteral(self,ctx:BKITParser.All_litContext):
        if ctx.int_lit():
            return self.visitIntLiteral(ctx.int_lit())
        elif ctx.float_lit():
            return self.visitFloatLiteral(ctx.float_lit())
        elif ctx.string_lit():
            return self.visitStringLiteral(ctx.string_lit())
        elif ctx.bool_lit():
            return self.visitBooleanLiteral(ctx.bool_lit())

    def visitFuncDecl(self, ctx:BKITParser.Func_declareContext):
        return None

    def visitCallExpr(self, ctx:BKITParser.ExpContext):
        return None

    def visitArrayCell(self, ctx:BKITParser.Array_cellContext):
        return None

    def visitAssign(self, ctx:BKITParser.Assign_stmtContext):
        return None

    def visitIf(self, ctx:BKITParser.If_stmtContext):
        return None

    def visitFor(self, ctx:BKITParser.For_stmtContext):
        return None

    def visitContinue(self, ctx:BKITParser.Continue_stmtContext):
        return None

    def visitBreak(self, ctx:BKITParser.Break_stmtContext):
        return None

    def visitReturn(self, ctx:BKITParser.Return_stmtContext):
        return None

    def visitDowhile(self, ctx:BKITParser.DoWhile_stmtContext):
        return None

    def visitWhile(self, ctx:BKITParser.While_stmtContext):
        return None

    def visitCallStmt(self, ctx:BKITParser.Func_callContext):
        return None

    def visitIntLiteral(self, ctx:BKITParser.Int_litContext):
        return IntLiteral(ctx.INTLIT().getText())

    def visitFloatLiteral(self, ctx:BKITParser.Float_litContext):
        return FloatLiteral(ctx.FLOATLIT().getText())

    def visitBooleanLiteral(self, ctx:BKITParser.Bool_litContext):
        if ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        else:
            return BooleanLiteral(ctx.FALSE().getText())

    def visitStringLiteral(self, ctx:BKITParser.String_litContext):
        return StringLiteral(ctx.STRINGLIT().getText())

    def visitArrayLiteral(self, ctx:BKITParser.Array_litContext):
        return None


    

