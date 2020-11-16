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
                listIndex.append(valueIndex)
            return [Id(ctx.ID().getText()),listIndex]
        else:
            return [Id(ctx.ID().getText()),[]]

    def visitIndexVarInt(self,ctx:BKITParser.Index_var_intContext):
        valueBase = ctx.INTLIT().getText()
        flag = 0
        for x in valueBase:
            if (x == "x") or (x == "X"):
                flag = 1
                break
            if (x == "o") or (x == "O"):
                flag = 2
                break
        if flag == 0:
            return int(valueBase)
        if flag == 1:
            return int(valueBase, 16)
        if flag == 2:
            return int(valueBase, 8)

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
        temp_var = []
        temp_stmt = []
        for x in ctx.body():
            temp = self.visitBody(x)
            if temp[0] == 0:
                if isinstance(temp[1], list):
                    temp_var.extend(temp[1])
                else:
                    temp_var.append(temp[1])
            else:
                if isinstance(temp[1], list):
                   temp_stmt.extend(temp[1])
                else:
                    temp_stmt.append(temp[1])
        temp = []
        temp.append(temp_var)
        temp.append(temp_stmt)
        return [temp_var, temp_stmt]

    def visitBody(self,ctx:BKITParser.BodyContext):
        if ctx.var_declare():
            return [0,self.visitVarDecl(ctx.var_declare())]
        else:
            temp = self.visitStmt(ctx.stmt())
            arr = [1]
            if isinstance(temp, list):
                arr.extend(temp if temp else [])
            else:
                arr.append(temp)
            return arr

    def visitStmt(self,ctx:BKITParser.StmtContext):
        if ctx.stmt_notfunc():
            return self.visitStmtNotFunc(ctx.stmt_notfunc())
        else:
            return self.visitStmtSpecial(ctx.stmt_spe())

    def visitStmtNotFunc(self,ctx:BKITParser.Stmt_notfuncContext):
        if ctx.if_stmt():
            return self.visitIf(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visitFor(ctx.for_stmt())
        elif ctx.while_stmt():
            return self.visitWhile(ctx.while_stmt())
        elif ctx.doWhile_stmt():
            return self.visitDowhile(ctx.doWhile_stmt())

    def visitStmtSpecial(self,ctx:BKITParser.Stmt_speContext):
        if ctx.assign_stmt():
            return self.visitAssign(ctx.assign_stmt())
        elif ctx.break_stmt():
            return self.visitBreak(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visitContinue(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visitReturn(ctx.return_stmt())
        elif ctx.call_stmt():
            return self.visitCallStmt(ctx.call_stmt())

    def visitCallExpr(self, ctx:BKITParser.ExpContext):
        if ctx.RELATIONAL():
            return BinaryOp(
                ctx.RELATIONAL().getText(),
                self.visitExp1(ctx.exp1(0)),
                self.visitExp1(ctx.exp1(1))
            )
        else:
            return self.visitExp1(ctx.exp1(0))

    def visitExp1(self,ctx:BKITParser.Exp1Context):
        if ctx.AND():
            return BinaryOp(
                ctx.AND().getText(),
                self.visitExp1(ctx.exp1()),
                self.visitExp2(ctx.exp2())
            )
        elif ctx.OR():
            return BinaryOp(
                ctx.OR().getText(),
                self.visitExp1(ctx.exp1()),
                self.visitExp2(ctx.exp2())
            )
        else:
            return self.visitExp2(ctx.exp2())

    def visitExp2(self,ctx:BKITParser.Exp2Context):
        if ctx.ADD():
            return BinaryOp(
                ctx.ADD().getText(),
                self.visitExp2(ctx.exp2()),
                self.visitExp3(ctx.exp3())
            )
        elif ctx.SUB():
            return BinaryOp(
                ctx.SUB().getText(),
                self.visitExp2(ctx.exp2()),
                self.visitExp3(ctx.exp3())
            )
        elif ctx.ADDDOT():
            return BinaryOp(
                ctx.ADDDOT().getText(),
                self.visitExp2(ctx.exp2()),
                self.visitExp3(ctx.exp3())
            )
        elif ctx.SUBDOT():
            return BinaryOp(
                ctx.SUBDOT().getText(),
                self.visitExp2(ctx.exp2()),
                self.visitExp3(ctx.exp3())
            )
        else:
            return self.visitExp3(ctx.exp3())

    def visitExp3(self,ctx:BKITParser.Exp3Context):
        if ctx.MUL():
            return BinaryOp(
                ctx.MUL().getText(),
                self.visitExp3(ctx.exp3()),
                self.visitExp4(ctx.exp4())
            )
        elif ctx.DIV():
            return BinaryOp(
                ctx.DIV().getText(),
                self.visitExp3(ctx.exp3()),
                self.visitExp4(ctx.exp4())
            )
        elif ctx.MOD():
            return BinaryOp(
                ctx.MOD().getText(),
                self.visitExp3(ctx.exp3()),
                self.visitExp4(ctx.exp4())
            )
        elif ctx.MULDOT():
            return BinaryOp(
                ctx.MULDOT().getText(),
                self.visitExp3(ctx.exp3()),
                self.visitExp4(ctx.exp4())
            )
        elif ctx.DIVDOT():
            return BinaryOp(
                ctx.DIVDOT().getText(),
                self.visitExp3(ctx.exp3()),
                self.visitExp4(ctx.exp4())
            )
        else:
            return self.visitExp4(ctx.exp4())

    def visitExp4(self,ctx:BKITParser.Exp4Context):
        if ctx.NOT():
            return UnaryOp(
                ctx.NOT().getText(),
                self.visitExp4(ctx.exp4())
            )
        else:
            return self.visitExp5(ctx.exp5())

    def visitExp5(self,ctx:BKITParser.Exp5Context):
        if ctx.SUB():
            return UnaryOp(
                ctx.SUB().getText(),
                self.visitExp5(ctx.exp5())
            )
        elif ctx.SUBDOT():
            return UnaryOp(
                ctx.SUBDOT().getText(),
                self.visitExp5(ctx.exp5())
            )
        else:
            return self.visitExp6(ctx.exp6())

    def visitExp6(self,ctx:BKITParser.Exp6Context):
        if ctx.op_index():
            valueArrCell = ArrayCell(
                self.visitExp6(ctx.exp6()),
                [self.visitOpIndex(ctx.op_index())]
            )
            return valueArrCell
        else:
            return self.visitOperands(ctx.operands())

    def visitOpIndex(self,ctx:BKITParser.Op_indexContext):
        return self.visitCallExpr(ctx.exp())

    def visitOperands(self,ctx:BKITParser.OperandsContext):
        if ctx.LP():
            return self.visitCallExpr(ctx.exp())
        elif ctx.func_call():
            value = self.visitFuncCall(ctx.func_call())
            return CallExpr(value[0], value[1])
        elif ctx.LCB():
            listLiteral = []
            for x in ctx.all_lit():
                temp = self.visitAllLiteral(x)
                if isinstance(temp, list):
                    listLiteral.extend(temp if temp else [])
                else:
                    listLiteral.append(temp)
            return ArrayLiteral(listLiteral)
        elif ctx.all_lit(0):
            return self.visitAllLiteral(ctx.all_lit(0))
        elif ctx.ID():
            return Id(ctx.ID().getText())

    def visitArrayCell(self, ctx:BKITParser.Array_cellContext):
        temp = []
        for x in ctx.var_vp():
            valueCell = self.visitVarVP(x)
            if isinstance(valueCell, list):
                temp.extend(valueCell if valueCell else [])
            else:
                temp.append(valueCell)
        return temp

    def visitAssign(self, ctx:BKITParser.Assign_stmtContext):
        temp_lhs = self.visitCallExpr(ctx.exp(0))
        temp_rhs = self.visitCallExpr(ctx.exp(1))
        return Assign(temp_lhs, temp_rhs)

    def visitScalarVar(self,ctx:BKITParser.Scalar_varContext):
        temp_expr = Id(ctx.ID().getText())
        if ctx.index_var():
            temp_index = []
            for x in ctx.index_var():
                value = self.visitIndexVar(ctx.index_var())
                if isinstance(value, list):
                    temp_index.extend(value if value else [])
                else:
                    temp_index.append(value)
            return ArrayCell(temp_expr,temp_index)
        else:
            return temp_expr

    def visitIndexVar(self,ctx:BKITParser.Index_varContext):
        return self.visitCallExpr(ctx.exp())

    def visitIf(self, ctx:BKITParser.If_stmtContext):
        tempExpr = self.visitCallExpr(ctx.exp())

        tempBody = []
        tempElseIf = []
        tempElse = ([],[])

        temp_var = []
        temp_stmt = []

        listIfThenStmt = []
        for x in ctx.body():
            temp = self.visitBody(x)
            if temp[0] == 0:
                if isinstance(temp[1], list):
                    temp_var.extend(temp[1])
                else:
                    temp_var.append(temp[1])
            else:
                if isinstance(temp[1], list):
                    temp_stmt.extend(temp[1])
                else:
                    temp_stmt.append(temp[1])
        tempBody.append(temp_var)
        tempBody.append(temp_stmt)
        tupleIfStmt = (tempExpr, tempBody[0], tempBody[1])
        listIfThenStmt.append(tupleIfStmt)

        for x in ctx.elseif_stmt():
            temp = self.visitElseIf(x)
            if isinstance(temp, list):
                tempElseIf.extend(temp if temp else [])
            else:
                tempElseIf.append(temp)
        if not (tempElseIf is None):
            listIfThenStmt.extend(tempElseIf)

        if ctx.else_stmt():
            tempElse = self.visitElse(ctx.else_stmt())
        tupleElseStmt = tempElse

        return If(listIfThenStmt,tupleElseStmt)

    def visitElseIf(self,ctx:BKITParser.Elseif_stmtContext):
        tempExpr = self.visitCallExpr(ctx.exp())
        tempBody = []
        temp_var = []
        temp_stmt = []
        for x in ctx.body():
            temp = self.visitBody(x)
            if temp[0] == 0:
                if isinstance(temp[1], list):
                    temp_var.extend(temp[1])
                else:
                    temp_var.append(temp[1])
            else:
                if isinstance(temp[1], list):
                    temp_stmt.extend(temp[1])
                else:
                    temp_stmt.append(temp[1])
        tempBody.append(temp_var)
        tempBody.append(temp_stmt)
        return (tempExpr, tempBody[0], tempBody[1])

    def visitElse(self,ctx:BKITParser.Else_stmtContext):
        tempBody = []
        temp_var = []
        temp_stmt = []
        for x in ctx.body():
            temp = self.visitBody(x)
            if temp[0] == 0:
                if isinstance(temp[1], list):
                    temp_var.extend(temp[1])
                else:
                    temp_var.append(temp[1])
            else:
                if isinstance(temp[1], list):
                    temp_stmt.extend(temp[1])
                else:
                    temp_stmt.append(temp[1])
        tempBody.append(temp_var)
        tempBody.append(temp_stmt)
        return (tempBody[0], tempBody[1])

    def visitFor(self, ctx:BKITParser.For_stmtContext):
        """
        idx1: Id
        expr1:Expr
        expr2:Expr
        expr3:Expr
        loop: Tuple[List[VarDecl],List[Stmt]]
        """
        getID = Id(ctx.ID().getText())
        getExpr1 = self.visitCallExpr(ctx.exp())
        getExpr2 = self.visitConditionExpr(ctx.conditionExpr())
        getExpr3 = self.visitUpdateExpr(ctx.updateExpr())
        tempBody = []
        temp_var = []
        temp_stmt = []
        for x in ctx.body():
            temp = self.visitBody(x)
            if temp[0] == 0:
                if isinstance(temp[1], list):
                    temp_var.extend(temp[1])
                else:
                    temp_var.append(temp[1])
            else:
                if isinstance(temp[1], list):
                    temp_stmt.extend(temp[1])
                else:
                    temp_stmt.append(temp[1])
        tempBody.append(temp_var)
        tempBody.append(temp_stmt)
        getLoop = (tempBody[0], tempBody[1])
        return For(getID, getExpr1, getExpr2, getExpr3, getLoop)

    def visitConditionExpr(self,ctx:BKITParser.ConditionExprContext):
        return self.visitCallExpr(ctx.exp())

    def visitUpdateExpr(self,ctx:BKITParser.UpdateExprContext):
        return self.visitCallExpr(ctx.exp())

    def visitContinue(self, ctx:BKITParser.Continue_stmtContext):
        return Continue()

    def visitBreak(self, ctx:BKITParser.Break_stmtContext):
        return Break()

    def visitReturn(self, ctx:BKITParser.Return_stmtContext):
        temp = None
        if ctx.exp():
            temp = self.visitCallExpr(ctx.exp())
        return Return(temp)

    def visitDowhile(self, ctx:BKITParser.DoWhile_stmtContext):
        """
        sl:Tuple[List[VarDecl],List[Stmt]]
        exp: Expr
        """
        getExpr = self.visitCallExpr(ctx.exp())
        tempBody = []
        temp_var = []
        temp_stmt = []
        for x in ctx.body():
            temp = self.visitBody(x)
            if temp[0] == 0:
                if isinstance(temp[1], list):
                    temp_var.extend(temp[1])
                else:
                    temp_var.append(temp[1])
            else:
                if isinstance(temp[1], list):
                    temp_stmt.extend(temp[1])
                else:
                    temp_stmt.append(temp[1])
        tempBody.append(temp_var)
        tempBody.append(temp_stmt)
        getBody = (tempBody[0], tempBody[1])
        return Dowhile(getBody, getExpr)

    def visitWhile(self, ctx:BKITParser.While_stmtContext):
        """
        exp: Expr
        sl:Tuple[List[VarDecl],List[Stmt]]
        """
        getExpr = self.visitCallExpr(ctx.exp())
        tempBody = []
        temp_var = []
        temp_stmt = []
        for x in ctx.body():
            temp = self.visitBody(x)
            if temp[0] == 0:
                if isinstance(temp[1], list):
                    temp_var.extend(temp[1])
                else:
                    temp_var.append(temp[1])
            else:
                if isinstance(temp[1], list):
                    temp_stmt.extend(temp[1])
                else:
                    temp_stmt.append(temp[1])
        tempBody.append(temp_var)
        tempBody.append(temp_stmt)
        getBody = (tempBody[0], tempBody[1])
        return While(getExpr, getBody)

    def visitCallStmt(self, ctx:BKITParser.Call_stmtContext):
        value = self.visitFuncCall(ctx.func_call())
        return CallStmt(value[0], value[1])

    def visitFuncCall(self,ctx:BKITParser.Func_callContext):
        if ctx.func_call_cell():
            return [Id(ctx.ID().getText()),self.visitFuncCallCell(ctx.func_call_cell())]
        else:
            return [Id(ctx.ID().getText()),[]]

    def visitFuncCallCell(self,ctx:BKITParser.Func_call_cellContext):
        temp = []
        for x in ctx.var_vp():
            valueCell = self.visitVarVP(x)
            if isinstance(valueCell, list):
                temp.extend(valueCell if valueCell else [])
            else:
                temp.append(valueCell)
        return temp

    def visitVarVP(self,ctx:BKITParser.Var_vpContext):
        if ctx.exp():
            return self.visitCallExpr(ctx.exp())
        elif ctx.array_cell():
            return self.visitArrayCell(ctx.array_cell())
        elif ctx.scalar_var():
            return self.visitScalarVar(ctx.scalar_var())

    def visitIntLiteral(self, ctx:BKITParser.Int_litContext):
        valueBase = ctx.INTLIT().getText()
        flag = 0
        for x in valueBase:
            if (x == "x") or (x == "X"):
                flag = 1
                break
            if (x == "o") or (x == "O"):
                flag = 2
                break
        if flag == 0:
            return IntLiteral(int(valueBase))
        if flag == 1:
            return IntLiteral(int(valueBase, 16))
        if flag == 2:
            return IntLiteral(int(valueBase, 8))

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

