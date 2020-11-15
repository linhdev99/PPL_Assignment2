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
            return self.visitFuncDecl(ctx.func_declare())

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
                valueIndex = self.visitIndexVarInt(x)
                listIndex.append(int(valueIndex))
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
        getIdFunc = Id(ctx.ID().getText())
        if ctx.parameter_func():
            listParameter = self.visitParameterFunc(ctx.parameter_func())
        else:
            listParameter = []
        getBodyDecl = self.visitBodyDecl(ctx.body_declare())
        listVarDecl = getBodyDecl[0]
        listStmt = getBodyDecl[1]
        return FuncDecl(getIdFunc,listParameter,(listVarDecl,listStmt))

    def visitParameterFunc(self,ctx:BKITParser.Parameter_funcContext):
        temp = []
        for x in ctx.scalar_var_int():
            m_getScalarVar = self.visitScalarVarInt(x)
            m_variable = m_getScalarVar[0]
            m_varDimen = m_getScalarVar[1]
            m_varInit = None
            totalValue = VarDecl(m_variable,m_varDimen,m_varInit)
            if isinstance(totalValue, list):
                temp.extend(totalValue)
            else:
                temp.append(totalValue)
        return temp

    def visitBodyDecl(self,ctx:BKITParser.Body_declareContext):
        temp = []
        temp_var = []
        temp_stmt = []
        for x in ctx.body():
            temp = self.visitBody(x)
            if temp[0] == 0:
                temp_var.extend(temp[1])
            else:
                temp_stmt.extend(temp[1])
        return [temp_var, temp_stmt]

    def visitBody(self,ctx:BKITParser.BodyContext):
        if ctx.var_declare():
            return [0,self.visitVarDecl(ctx.var_declare())]
        else:
            return [1,self.visitStmt(ctx.stmt())]

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
        return IntLiteral(int(ctx.INTLIT().getText()))

    def visitFloatLiteral(self, ctx:BKITParser.Float_litContext):
        return FloatLiteral(float(ctx.FLOATLIT().getText()))

    def visitBooleanLiteral(self, ctx:BKITParser.Bool_litContext):
        if ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        else:
            return BooleanLiteral(ctx.FALSE().getText())

    def visitStringLiteral(self, ctx:BKITParser.String_litContext):
        return StringLiteral(ctx.STRINGLIT().getText())

    def visitArrayLiteral(self, ctx:BKITParser.Array_litContext):
        temp = []
        for x in ctx.array_lit_cell():
            # temp.extend(self.visitArrayLitCell(x))
            valueCell = self.visitArrayLitCell(x)
            if isinstance(valueCell, list):
                temp.extend(valueCell if valueCell else [])
            else:
                temp.append(valueCell)
        return ArrayLiteral(temp)

    def visitArrayLitCell(self,ctx:BKITParser.Array_lit_cellContext):
        if ctx.all_lit():
            return self.visitAllLiteral(ctx.all_lit())
        else:
            return self.visitArrayLiteral(ctx.array_lit())

    def getOnlyValueLiteral(self,ctx:BKITParser.All_litContext):
        if ctx.int_lit():
            return self.visitValueIntLiteral(ctx.int_lit())
        elif ctx.float_lit():
            return self.visitValueFloatLiteral(ctx.float_lit())
        elif ctx.string_lit():
            return self.visitValueStringLiteral(ctx.string_lit())
        elif ctx.bool_lit():
            return self.visitValueBooleanLiteral(ctx.bool_lit())

    def visitValueIntLiteral(self, ctx:BKITParser.Int_litContext):
        return int(ctx.INTLIT().getText())

    def visitValueFloatLiteral(self, ctx:BKITParser.Float_litContext):
        return float(ctx.FLOATLIT().getText())

    def visitValueBooleanLiteral(self, ctx:BKITParser.Bool_litContext):
        if ctx.TRUE():
            return ctx.TRUE().getText()
        else:
            return ctx.FALSE().getText()

    def visitValueStringLiteral(self, ctx:BKITParser.String_litContext):
        return ctx.STRINGLIT().getText()

