# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u01e6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\6\2f\n\2\r\2\16")
        buf.write("\2g\3\2\3\2\3\3\3\3\5\3n\n\3\3\4\3\4\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\7\6z\n\6\f\6\16\6}\13\6\3\7\3\7\3\7\3\7")
        buf.write("\5\7\u0083\n\7\5\7\u0085\n\7\3\b\3\b\3\b\5\b\u008a\n\b")
        buf.write("\3\t\3\t\3\t\3\t\7\t\u0090\n\t\f\t\16\t\u0093\13\t\5\t")
        buf.write("\u0095\n\t\3\t\3\t\3\n\3\n\5\n\u009b\n\n\3\13\3\13\3\13")
        buf.write("\3\13\7\13\u00a1\n\13\f\13\16\13\u00a4\13\13\5\13\u00a6")
        buf.write("\n\13\3\13\3\13\3\f\3\f\5\f\u00ac\n\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00b3\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00bc\n\16\3\17\3\17\3\17\7\17\u00c1\n\17\f\17\16")
        buf.write("\17\u00c4\13\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00cd\n\20\3\21\3\21\3\21\3\21\5\21\u00d3\n\21\3\21\7")
        buf.write("\21\u00d6\n\21\f\21\16\21\u00d9\13\21\5\21\u00db\n\21")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00e1\n\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\7\23\u00ea\n\23\f\23\16\23\u00ed\13")
        buf.write("\23\3\24\3\24\3\24\3\24\7\24\u00f3\n\24\f\24\16\24\u00f6")
        buf.write("\13\24\3\24\7\24\u00f9\n\24\f\24\16\24\u00fc\13\24\3\24")
        buf.write("\5\24\u00ff\n\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\7")
        buf.write("\25\u0108\n\25\f\25\16\25\u010b\13\25\3\26\3\26\7\26\u010f")
        buf.write("\n\26\f\26\16\26\u0112\13\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0120\n\27\f")
        buf.write("\27\16\27\u0123\13\27\3\27\3\27\3\27\3\30\3\30\7\30\u012a")
        buf.write("\n\30\f\30\16\30\u012d\13\30\3\31\3\31\3\31\6\31\u0132")
        buf.write("\n\31\r\31\16\31\u0133\3\31\3\31\3\32\3\32\7\32\u013a")
        buf.write("\n\32\f\32\16\32\u013d\13\32\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\36\7\36\u014b\n\36\f")
        buf.write("\36\16\36\u014e\13\36\3\36\3\36\3\36\3\37\3\37\7\37\u0155")
        buf.write("\n\37\f\37\16\37\u0158\13\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0169\n\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\5#\u0171\n#\3#\3#\3#\5#\u0176\n#\7#\u0178")
        buf.write("\n#\f#\16#\u017b\13#\5#\u017d\n#\3#\3#\3$\3$\3$\3%\3%")
        buf.write("\3%\3%\3%\5%\u0189\n%\3&\3&\3&\3&\3&\3&\7&\u0191\n&\f")
        buf.write("&\16&\u0194\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u019c\n\'")
        buf.write("\f\'\16\'\u019f\13\'\3(\3(\3(\3(\3(\3(\7(\u01a7\n(\f(")
        buf.write("\16(\u01aa\13(\3)\3)\3)\5)\u01af\n)\3*\3*\3*\5*\u01b4")
        buf.write("\n*\3+\3+\3+\3+\3+\7+\u01bb\n+\f+\16+\u01be\13+\3,\3,")
        buf.write("\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\7-\u01ce\n-\f-\16")
        buf.write("-\u01d1\13-\3-\3-\3-\5-\u01d6\n-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\5\62\u01e4\n\62\3\62\2")
        buf.write("\6JLNT\63\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b\2\7\3\2\36\37")
        buf.write("\4\2 !%&\4\2\"$\'(\4\2!!&&\3\2\32\33\2\u01f3\2e\3\2\2")
        buf.write("\2\4m\3\2\2\2\6o\3\2\2\2\bq\3\2\2\2\nt\3\2\2\2\f~\3\2")
        buf.write("\2\2\16\u0089\3\2\2\2\20\u008b\3\2\2\2\22\u009a\3\2\2")
        buf.write("\2\24\u009c\3\2\2\2\26\u00ab\3\2\2\2\30\u00b2\3\2\2\2")
        buf.write("\32\u00bb\3\2\2\2\34\u00bd\3\2\2\2\36\u00c8\3\2\2\2 \u00da")
        buf.write("\3\2\2\2\"\u00dc\3\2\2\2$\u00e4\3\2\2\2&\u00ee\3\2\2\2")
        buf.write("(\u0103\3\2\2\2*\u010c\3\2\2\2,\u0113\3\2\2\2.\u0127\3")
        buf.write("\2\2\2\60\u012e\3\2\2\2\62\u0137\3\2\2\2\64\u013e\3\2")
        buf.write("\2\2\66\u0142\3\2\2\28\u0144\3\2\2\2:\u0146\3\2\2\2<\u0152")
        buf.write("\3\2\2\2>\u015e\3\2\2\2@\u0161\3\2\2\2B\u0164\3\2\2\2")
        buf.write("D\u016c\3\2\2\2F\u0180\3\2\2\2H\u0188\3\2\2\2J\u018a\3")
        buf.write("\2\2\2L\u0195\3\2\2\2N\u01a0\3\2\2\2P\u01ae\3\2\2\2R\u01b3")
        buf.write("\3\2\2\2T\u01b5\3\2\2\2V\u01bf\3\2\2\2X\u01d5\3\2\2\2")
        buf.write("Z\u01d7\3\2\2\2\\\u01d9\3\2\2\2^\u01db\3\2\2\2`\u01dd")
        buf.write("\3\2\2\2b\u01e3\3\2\2\2df\5\4\3\2ed\3\2\2\2fg\3\2\2\2")
        buf.write("ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7\2\2\3j\3\3\2\2\2kn")
        buf.write("\5\6\4\2ln\5\"\22\2mk\3\2\2\2ml\3\2\2\2n\5\3\2\2\2op\5")
        buf.write("\b\5\2p\7\3\2\2\2qr\5\n\6\2rs\7;\2\2s\t\3\2\2\2tu\7\34")
        buf.write("\2\2uv\7<\2\2v{\5\f\7\2wx\7=\2\2xz\5\f\7\2yw\3\2\2\2z")
        buf.write("}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\13\3\2\2\2}{\3\2\2\2~\u0084")
        buf.write("\5\62\32\2\177\u0082\7)\2\2\u0080\u0083\5\24\13\2\u0081")
        buf.write("\u0083\5b\62\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2")
        buf.write("\u0083\u0085\3\2\2\2\u0084\177\3\2\2\2\u0084\u0085\3\2")
        buf.write("\2\2\u0085\r\3\2\2\2\u0086\u008a\5\20\t\2\u0087\u008a")
        buf.write("\5.\30\2\u0088\u008a\5H%\2\u0089\u0086\3\2\2\2\u0089\u0087")
        buf.write("\3\2\2\2\u0089\u0088\3\2\2\2\u008a\17\3\2\2\2\u008b\u0094")
        buf.write("\7\67\2\2\u008c\u0091\5\16\b\2\u008d\u008e\7=\2\2\u008e")
        buf.write("\u0090\5\16\b\2\u008f\u008d\3\2\2\2\u0090\u0093\3\2\2")
        buf.write("\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0095")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u008c\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\78\2\2")
        buf.write("\u0097\21\3\2\2\2\u0098\u009b\5\24\13\2\u0099\u009b\5")
        buf.write("b\62\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\23")
        buf.write("\3\2\2\2\u009c\u00a5\7\67\2\2\u009d\u00a2\5\22\n\2\u009e")
        buf.write("\u009f\7=\2\2\u009f\u00a1\5\22\n\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3")
        buf.write("\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u009d")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write("\u00a8\78\2\2\u00a8\25\3\2\2\2\u00a9\u00ac\5\30\r\2\u00aa")
        buf.write("\u00ac\5\32\16\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2")
        buf.write("\2\u00ac\27\3\2\2\2\u00ad\u00b3\5\6\4\2\u00ae\u00b3\5")
        buf.write("&\24\2\u00af\u00b3\5,\27\2\u00b0\u00b3\5:\36\2\u00b1\u00b3")
        buf.write("\5<\37\2\u00b2\u00ad\3\2\2\2\u00b2\u00ae\3\2\2\2\u00b2")
        buf.write("\u00af\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b3\31\3\2\2\2\u00b4\u00b5\5\36\20\2\u00b5\u00b6\7")
        buf.write(";\2\2\u00b6\u00bc\3\2\2\2\u00b7\u00bc\5> \2\u00b8\u00bc")
        buf.write("\5@!\2\u00b9\u00bc\5B\"\2\u00ba\u00bc\5F$\2\u00bb\u00b4")
        buf.write("\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\33\3\2\2\2\u00bd")
        buf.write("\u00be\7\n\2\2\u00be\u00c2\7<\2\2\u00bf\u00c1\5\26\f\2")
        buf.write("\u00c0\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3")
        buf.write("\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00c2")
        buf.write("\3\2\2\2\u00c5\u00c6\7\13\2\2\u00c6\u00c7\7>\2\2\u00c7")
        buf.write("\35\3\2\2\2\u00c8\u00c9\5 \21\2\u00c9\u00cc\7)\2\2\u00ca")
        buf.write("\u00cd\5 \21\2\u00cb\u00cd\5H%\2\u00cc\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cb\3\2\2\2\u00cd\37\3\2\2\2\u00ce\u00db\5.\30\2\u00cf")
        buf.write("\u00d3\5D#\2\u00d0\u00d3\7E\2\2\u00d1\u00d3\5\20\t\2\u00d2")
        buf.write("\u00cf\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d7\3\2\2\2\u00d4\u00d6\5\60\31\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00da\u00ce\3\2\2\2\u00da\u00d2\3\2\2\2\u00db!\3\2\2")
        buf.write("\2\u00dc\u00dd\7\b\2\2\u00dd\u00de\7<\2\2\u00de\u00e0")
        buf.write("\7A\2\2\u00df\u00e1\5$\23\2\u00e0\u00df\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\5\34\17")
        buf.write("\2\u00e3#\3\2\2\2\u00e4\u00e5\7\t\2\2\u00e5\u00e6\7<\2")
        buf.write("\2\u00e6\u00eb\5\62\32\2\u00e7\u00e8\7=\2\2\u00e8\u00ea")
        buf.write("\5\62\32\2\u00e9\u00e7\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec%\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ee\u00ef\7\f\2\2\u00ef\u00f0\5H%\2\u00f0")
        buf.write("\u00f4\7\r\2\2\u00f1\u00f3\5\26\f\2\u00f2\u00f1\3\2\2")
        buf.write("\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5")
        buf.write("\3\2\2\2\u00f5\u00fa\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7")
        buf.write("\u00f9\5(\25\2\u00f8\u00f7\3\2\2\2\u00f9\u00fc\3\2\2\2")
        buf.write("\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fe\3")
        buf.write("\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00ff\5*\26\2\u00fe\u00fd")
        buf.write("\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2\u0100")
        buf.write("\u0101\7\20\2\2\u0101\u0102\7>\2\2\u0102\'\3\2\2\2\u0103")
        buf.write("\u0104\7\16\2\2\u0104\u0105\5H%\2\u0105\u0109\7\r\2\2")
        buf.write("\u0106\u0108\5\26\f\2\u0107\u0106\3\2\2\2\u0108\u010b")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write(")\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u0110\7\17\2\2\u010d")
        buf.write("\u010f\5\26\f\2\u010e\u010d\3\2\2\2\u010f\u0112\3\2\2")
        buf.write("\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111+\3\2")
        buf.write("\2\2\u0112\u0110\3\2\2\2\u0113\u0114\7\21\2\2\u0114\u0115")
        buf.write("\7\65\2\2\u0115\u0116\7A\2\2\u0116\u0117\7)\2\2\u0117")
        buf.write("\u0118\5H%\2\u0118\u0119\7=\2\2\u0119\u011a\5\66\34\2")
        buf.write("\u011a\u011b\7=\2\2\u011b\u011c\58\35\2\u011c\u011d\7")
        buf.write("\66\2\2\u011d\u0121\7\23\2\2\u011e\u0120\5\26\f\2\u011f")
        buf.write("\u011e\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f\3\2\2\2")
        buf.write("\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0124\u0125\7\22\2\2\u0125\u0126\7>\2\2\u0126-")
        buf.write("\3\2\2\2\u0127\u012b\7A\2\2\u0128\u012a\5\60\31\2\u0129")
        buf.write("\u0128\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012c/\3\2\2\2\u012d\u012b\3\2\2")
        buf.write("\2\u012e\u0131\79\2\2\u012f\u0132\5.\30\2\u0130\u0132")
        buf.write("\5H%\2\u0131\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0132\u0133")
        buf.write("\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write("\u0135\3\2\2\2\u0135\u0136\7:\2\2\u0136\61\3\2\2\2\u0137")
        buf.write("\u013b\7A\2\2\u0138\u013a\5\64\33\2\u0139\u0138\3\2\2")
        buf.write("\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c")
        buf.write("\3\2\2\2\u013c\63\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f")
        buf.write("\79\2\2\u013f\u0140\7?\2\2\u0140\u0141\7:\2\2\u0141\65")
        buf.write("\3\2\2\2\u0142\u0143\5H%\2\u0143\67\3\2\2\2\u0144\u0145")
        buf.write("\5H%\2\u01459\3\2\2\2\u0146\u0147\7\25\2\2\u0147\u0148")
        buf.write("\5H%\2\u0148\u014c\7\23\2\2\u0149\u014b\5\26\f\2\u014a")
        buf.write("\u0149\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2")
        buf.write("\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3")
        buf.write("\2\2\2\u014f\u0150\7\26\2\2\u0150\u0151\7>\2\2\u0151;")
        buf.write("\3\2\2\2\u0152\u0156\7\23\2\2\u0153\u0155\5\26\f\2\u0154")
        buf.write("\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u0156\3")
        buf.write("\2\2\2\u0159\u015a\7\25\2\2\u015a\u015b\5H%\2\u015b\u015c")
        buf.write("\7\24\2\2\u015c\u015d\7>\2\2\u015d=\3\2\2\2\u015e\u015f")
        buf.write("\7\30\2\2\u015f\u0160\7;\2\2\u0160?\3\2\2\2\u0161\u0162")
        buf.write("\7\31\2\2\u0162\u0163\7;\2\2\u0163A\3\2\2\2\u0164\u0168")
        buf.write("\7\27\2\2\u0165\u0169\5.\30\2\u0166\u0169\5b\62\2\u0167")
        buf.write("\u0169\5H%\2\u0168\u0165\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write("\u0167\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016a\u016b\7;\2\2\u016bC\3\2\2\2\u016c\u016d\7A\2\2")
        buf.write("\u016d\u017c\7\65\2\2\u016e\u0171\5H%\2\u016f\u0171\5")
        buf.write("\16\b\2\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171")
        buf.write("\u0179\3\2\2\2\u0172\u0175\7=\2\2\u0173\u0176\5H%\2\u0174")
        buf.write("\u0176\5\16\b\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2")
        buf.write("\2\u0176\u0178\3\2\2\2\u0177\u0172\3\2\2\2\u0178\u017b")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u0170\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\7")
        buf.write("\66\2\2\u017fE\3\2\2\2\u0180\u0181\5D#\2\u0181\u0182\7")
        buf.write(";\2\2\u0182G\3\2\2\2\u0183\u0184\5J&\2\u0184\u0185\7\3")
        buf.write("\2\2\u0185\u0186\5J&\2\u0186\u0189\3\2\2\2\u0187\u0189")
        buf.write("\5J&\2\u0188\u0183\3\2\2\2\u0188\u0187\3\2\2\2\u0189I")
        buf.write("\3\2\2\2\u018a\u018b\b&\1\2\u018b\u018c\5L\'\2\u018c\u0192")
        buf.write("\3\2\2\2\u018d\u018e\f\4\2\2\u018e\u018f\t\2\2\2\u018f")
        buf.write("\u0191\5L\'\2\u0190\u018d\3\2\2\2\u0191\u0194\3\2\2\2")
        buf.write("\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193K\3\2\2")
        buf.write("\2\u0194\u0192\3\2\2\2\u0195\u0196\b\'\1\2\u0196\u0197")
        buf.write("\5N(\2\u0197\u019d\3\2\2\2\u0198\u0199\f\4\2\2\u0199\u019a")
        buf.write("\t\3\2\2\u019a\u019c\5N(\2\u019b\u0198\3\2\2\2\u019c\u019f")
        buf.write("\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("M\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a1\b(\1\2\u01a1")
        buf.write("\u01a2\5P)\2\u01a2\u01a8\3\2\2\2\u01a3\u01a4\f\4\2\2\u01a4")
        buf.write("\u01a5\t\4\2\2\u01a5\u01a7\5P)\2\u01a6\u01a3\3\2\2\2\u01a7")
        buf.write("\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a9O\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\7\35\2")
        buf.write("\2\u01ac\u01af\5P)\2\u01ad\u01af\5R*\2\u01ae\u01ab\3\2")
        buf.write("\2\2\u01ae\u01ad\3\2\2\2\u01afQ\3\2\2\2\u01b0\u01b1\t")
        buf.write("\5\2\2\u01b1\u01b4\5R*\2\u01b2\u01b4\5T+\2\u01b3\u01b0")
        buf.write("\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4S\3\2\2\2\u01b5\u01b6")
        buf.write("\b+\1\2\u01b6\u01b7\5X-\2\u01b7\u01bc\3\2\2\2\u01b8\u01b9")
        buf.write("\f\4\2\2\u01b9\u01bb\5V,\2\u01ba\u01b8\3\2\2\2\u01bb\u01be")
        buf.write("\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write("U\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf\u01c0\79\2\2\u01c0")
        buf.write("\u01c1\5H%\2\u01c1\u01c2\7:\2\2\u01c2W\3\2\2\2\u01c3\u01c4")
        buf.write("\7\65\2\2\u01c4\u01c5\5H%\2\u01c5\u01c6\7\66\2\2\u01c6")
        buf.write("\u01d6\3\2\2\2\u01c7\u01d6\5D#\2\u01c8\u01d6\5b\62\2\u01c9")
        buf.write("\u01ca\7\67\2\2\u01ca\u01cf\5H%\2\u01cb\u01cc\7=\2\2\u01cc")
        buf.write("\u01ce\5H%\2\u01cd\u01cb\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2\3\2\2\2")
        buf.write("\u01d1\u01cf\3\2\2\2\u01d2\u01d3\78\2\2\u01d3\u01d6\3")
        buf.write("\2\2\2\u01d4\u01d6\7A\2\2\u01d5\u01c3\3\2\2\2\u01d5\u01c7")
        buf.write("\3\2\2\2\u01d5\u01c8\3\2\2\2\u01d5\u01c9\3\2\2\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6Y\3\2\2\2\u01d7\u01d8\t\6\2\2\u01d8")
        buf.write("[\3\2\2\2\u01d9\u01da\7?\2\2\u01da]\3\2\2\2\u01db\u01dc")
        buf.write("\7@\2\2\u01dc_\3\2\2\2\u01dd\u01de\7E\2\2\u01dea\3\2\2")
        buf.write("\2\u01df\u01e4\5\\/\2\u01e0\u01e4\5^\60\2\u01e1\u01e4")
        buf.write("\5`\61\2\u01e2\u01e4\5Z.\2\u01e3\u01df\3\2\2\2\u01e3\u01e0")
        buf.write("\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4")
        buf.write("c\3\2\2\2\62gm{\u0082\u0084\u0089\u0091\u0094\u009a\u00a2")
        buf.write("\u00a5\u00ab\u00b2\u00bb\u00c2\u00cc\u00d2\u00d7\u00da")
        buf.write("\u00e0\u00eb\u00f4\u00fa\u00fe\u0109\u0110\u0121\u012b")
        buf.write("\u0131\u0133\u013b\u014c\u0156\u0168\u0170\u0175\u0179")
        buf.write("\u017c\u0188\u0192\u019d\u01a8\u01ae\u01b3\u01bc\u01cf")
        buf.write("\u01d5\u01e3")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Function'", "'Parameter'", 
                     "'Body'", "'EndBody'", "'If'", "'Then'", "'ElseIf'", 
                     "'Else'", "'EndIf'", "'For'", "'EndFor'", "'Do'", "'EndDo'", 
                     "'While'", "'EndWhile'", "'Return'", "'Break'", "'Continue'", 
                     "'True'", "'False'", "'Var'", "'!'", "'&&'", "'||'", 
                     "'+'", "'-'", "'*'", "'\\'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'='", "<INVALID>", "<INVALID>", 
                     "'<'", "<INVALID>", "'>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", 
                     "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "RELATIONAL", "RELATIONAL_INT", "RELATIONAL_FLOAT", 
                      "WS", "BCMT", "FUNCTION", "PARAMETER", "BODY", "ENDBODY", 
                      "IF", "THEN", "ELSEIF", "ELSE", "ENDIF", "FOR", "ENDFOR", 
                      "DO", "ENDDO", "WHILE", "ENDWHILE", "RETURN", "BREAK", 
                      "CONTINUE", "TRUE", "FALSE", "VAR", "NOT", "AND", 
                      "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "ADDDOT", 
                      "SUBDOT", "MULDOT", "DIVDOT", "EQ", "EQINT", "NEQINT", 
                      "LTINT", "LTEINT", "GTINT", "GTEINT", "NEQF", "LTF", 
                      "LTEF", "GTF", "GTEF", "LP", "RP", "LCB", "RCB", "LSB", 
                      "RSB", "SEMI", "COLON", "COMMA", "DOT", "INTLIT", 
                      "FLOATLIT", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "UNTERMINATED_COMMENT", "STRINGLIT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_main = 1
    RULE_var_declare = 2
    RULE_var_list = 3
    RULE_var_normal = 4
    RULE_var_normal_list = 5
    RULE_var_vp = 6
    RULE_array_cell = 7
    RULE_array_lit_cell = 8
    RULE_array_lit = 9
    RULE_stmt = 10
    RULE_stmt_notfunc = 11
    RULE_stmt_spe = 12
    RULE_body_declare = 13
    RULE_assign_stmt = 14
    RULE_assign_part = 15
    RULE_func_declare = 16
    RULE_parameter_func = 17
    RULE_if_stmt = 18
    RULE_elseif_stmt = 19
    RULE_else_stmt = 20
    RULE_for_stmt = 21
    RULE_scalar_var = 22
    RULE_index_var = 23
    RULE_scalar_var_int = 24
    RULE_index_var_int = 25
    RULE_conditionExpr = 26
    RULE_updateExpr = 27
    RULE_while_stmt = 28
    RULE_doWhile_stmt = 29
    RULE_break_stmt = 30
    RULE_continue_stmt = 31
    RULE_return_stmt = 32
    RULE_func_call = 33
    RULE_call_stmt = 34
    RULE_exp = 35
    RULE_exp1 = 36
    RULE_exp2 = 37
    RULE_exp3 = 38
    RULE_exp4 = 39
    RULE_exp5 = 40
    RULE_exp6 = 41
    RULE_op_index = 42
    RULE_operands = 43
    RULE_bool_lit = 44
    RULE_int_lit = 45
    RULE_float_lit = 46
    RULE_string_lit = 47
    RULE_all_lit = 48

    ruleNames =  [ "program", "main", "var_declare", "var_list", "var_normal", 
                   "var_normal_list", "var_vp", "array_cell", "array_lit_cell", 
                   "array_lit", "stmt", "stmt_notfunc", "stmt_spe", "body_declare", 
                   "assign_stmt", "assign_part", "func_declare", "parameter_func", 
                   "if_stmt", "elseif_stmt", "else_stmt", "for_stmt", "scalar_var", 
                   "index_var", "scalar_var_int", "index_var_int", "conditionExpr", 
                   "updateExpr", "while_stmt", "doWhile_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "func_call", "call_stmt", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "op_index", "operands", "bool_lit", "int_lit", "float_lit", 
                   "string_lit", "all_lit" ]

    EOF = Token.EOF
    RELATIONAL=1
    RELATIONAL_INT=2
    RELATIONAL_FLOAT=3
    WS=4
    BCMT=5
    FUNCTION=6
    PARAMETER=7
    BODY=8
    ENDBODY=9
    IF=10
    THEN=11
    ELSEIF=12
    ELSE=13
    ENDIF=14
    FOR=15
    ENDFOR=16
    DO=17
    ENDDO=18
    WHILE=19
    ENDWHILE=20
    RETURN=21
    BREAK=22
    CONTINUE=23
    TRUE=24
    FALSE=25
    VAR=26
    NOT=27
    AND=28
    OR=29
    ADD=30
    SUB=31
    MUL=32
    DIV=33
    MOD=34
    ADDDOT=35
    SUBDOT=36
    MULDOT=37
    DIVDOT=38
    EQ=39
    EQINT=40
    NEQINT=41
    LTINT=42
    LTEINT=43
    GTINT=44
    GTEINT=45
    NEQF=46
    LTF=47
    LTEF=48
    GTF=49
    GTEF=50
    LP=51
    RP=52
    LCB=53
    RCB=54
    LSB=55
    RSB=56
    SEMI=57
    COLON=58
    COMMA=59
    DOT=60
    INTLIT=61
    FLOATLIT=62
    ID=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65
    UNTERMINATED_COMMENT=66
    STRINGLIT=67
    ERROR_CHAR=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def main(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.MainContext)
            else:
                return self.getTypedRuleContext(BKITParser.MainContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.main()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.FUNCTION or _la==BKITParser.VAR):
                    break

            self.state = 103
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(BKITParser.Func_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_main

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = BKITParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.var_declare()
                pass
            elif token in [BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.func_declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.var_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_normal(self):
            return self.getTypedRuleContext(BKITParser.Var_normalContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.var_normal()
            self.state = 112
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_normalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_normal_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_normal_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_normal_listContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_normal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_normal" ):
                return visitor.visitVar_normal(self)
            else:
                return visitor.visitChildren(self)




    def var_normal(self):

        localctx = BKITParser.Var_normalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_normal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(BKITParser.VAR)
            self.state = 115
            self.match(BKITParser.COLON)
            self.state = 116
            self.var_normal_list()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 117
                self.match(BKITParser.COMMA)
                self.state = 118
                self.var_normal_list()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_normal_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var_int(self):
            return self.getTypedRuleContext(BKITParser.Scalar_var_intContext,0)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def all_lit(self):
            return self.getTypedRuleContext(BKITParser.All_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_normal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_normal_list" ):
                return visitor.visitVar_normal_list(self)
            else:
                return visitor.visitChildren(self)




    def var_normal_list(self):

        localctx = BKITParser.Var_normal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_normal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.scalar_var_int()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.EQ:
                self.state = 125
                self.match(BKITParser.EQ)
                self.state = 128
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.LCB]:
                    self.state = 126
                    self.array_lit()
                    pass
                elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                    self.state = 127
                    self.all_lit()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_vpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_cell(self):
            return self.getTypedRuleContext(BKITParser.Array_cellContext,0)


        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_vp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_vp" ):
                return visitor.visitVar_vp(self)
            else:
                return visitor.visitChildren(self)




    def var_vp(self):

        localctx = BKITParser.Var_vpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_vp)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.array_cell()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.scalar_var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_cellContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def var_vp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_vpContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_vpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_cell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_cell" ):
                return visitor.visitArray_cell(self)
            else:
                return visitor.visitChildren(self)




    def array_cell(self):

        localctx = BKITParser.Array_cellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_cell)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BKITParser.LCB)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 138
                self.var_vp()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 139
                    self.match(BKITParser.COMMA)
                    self.state = 140
                    self.var_vp()
                    self.state = 145
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 148
            self.match(BKITParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_cellContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def all_lit(self):
            return self.getTypedRuleContext(BKITParser.All_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_lit_cell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_cell" ):
                return visitor.visitArray_lit_cell(self)
            else:
                return visitor.visitChildren(self)




    def array_lit_cell(self):

        localctx = BKITParser.Array_lit_cellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_lit_cell)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.array_lit()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.all_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def array_lit_cell(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Array_lit_cellContext)
            else:
                return self.getTypedRuleContext(BKITParser.Array_lit_cellContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKITParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(BKITParser.LCB)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 155
                self.array_lit_cell()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 156
                    self.match(BKITParser.COMMA)
                    self.state = 157
                    self.array_lit_cell()
                    self.state = 162
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 165
            self.match(BKITParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_notfunc(self):
            return self.getTypedRuleContext(BKITParser.Stmt_notfuncContext,0)


        def stmt_spe(self):
            return self.getTypedRuleContext(BKITParser.Stmt_speContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IF, BKITParser.FOR, BKITParser.DO, BKITParser.WHILE, BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.stmt_notfunc()
                pass
            elif token in [BKITParser.RETURN, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.LCB, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.stmt_spe()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_notfuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def doWhile_stmt(self):
            return self.getTypedRuleContext(BKITParser.DoWhile_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_notfunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_notfunc" ):
                return visitor.visitStmt_notfunc(self)
            else:
                return visitor.visitChildren(self)




    def stmt_notfunc(self):

        localctx = BKITParser.Stmt_notfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stmt_notfunc)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.var_declare()
                pass
            elif token in [BKITParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.if_stmt()
                pass
            elif token in [BKITParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.for_stmt()
                pass
            elif token in [BKITParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.while_stmt()
                pass
            elif token in [BKITParser.DO]:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.doWhile_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_speContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_spe

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_spe" ):
                return visitor.visitStmt_spe(self)
            else:
                return visitor.visitChildren(self)




    def stmt_spe(self):

        localctx = BKITParser.Stmt_speContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt_spe)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.assign_stmt()
                self.state = 179
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.break_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.continue_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.call_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_body_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_declare" ):
                return visitor.visitBody_declare(self)
            else:
                return visitor.visitChildren(self)




    def body_declare(self):

        localctx = BKITParser.Body_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_body_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(BKITParser.BODY)
            self.state = 188
            self.match(BKITParser.COLON)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 189
                self.stmt()
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self.match(BKITParser.ENDBODY)
            self.state = 196
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Assign_partContext)
            else:
                return self.getTypedRuleContext(BKITParser.Assign_partContext,i)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.assign_part()
            self.state = 199
            self.match(BKITParser.EQ)
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 200
                self.assign_part()
                pass

            elif la_ == 2:
                self.state = 201
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def index_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Index_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Index_varContext,i)


        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def array_cell(self):
            return self.getTypedRuleContext(BKITParser.Array_cellContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_part" ):
                return visitor.visitAssign_part(self)
            else:
                return visitor.visitChildren(self)




    def assign_part(self):

        localctx = BKITParser.Assign_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assign_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 204
                self.scalar_var()
                pass

            elif la_ == 2:
                self.state = 208
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.ID]:
                    self.state = 205
                    self.func_call()
                    pass
                elif token in [BKITParser.STRINGLIT]:
                    self.state = 206
                    self.match(BKITParser.STRINGLIT)
                    pass
                elif token in [BKITParser.LCB]:
                    self.state = 207
                    self.array_cell()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.LSB:
                    self.state = 210
                    self.index_var()
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def body_declare(self):
            return self.getTypedRuleContext(BKITParser.Body_declareContext,0)


        def parameter_func(self):
            return self.getTypedRuleContext(BKITParser.Parameter_funcContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




    def func_declare(self):

        localctx = BKITParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(BKITParser.FUNCTION)
            self.state = 219
            self.match(BKITParser.COLON)
            self.state = 220
            self.match(BKITParser.ID)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 221
                self.parameter_func()


            self.state = 224
            self.body_declare()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def scalar_var_int(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Scalar_var_intContext)
            else:
                return self.getTypedRuleContext(BKITParser.Scalar_var_intContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_parameter_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_func" ):
                return visitor.visitParameter_func(self)
            else:
                return visitor.visitChildren(self)




    def parameter_func(self):

        localctx = BKITParser.Parameter_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(BKITParser.PARAMETER)
            self.state = 227
            self.match(BKITParser.COLON)
            self.state = 228
            self.scalar_var_int()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 229
                self.match(BKITParser.COMMA)
                self.state = 230
                self.scalar_var_int()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def elseif_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Elseif_stmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.Elseif_stmtContext,i)


        def else_stmt(self):
            return self.getTypedRuleContext(BKITParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(BKITParser.IF)
            self.state = 237
            self.exp()
            self.state = 238
            self.match(BKITParser.THEN)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 239
                self.stmt()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 245
                self.elseif_stmt()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 251
                self.else_stmt()


            self.state = 254
            self.match(BKITParser.ENDIF)
            self.state = 255
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = BKITParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_elseif_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(BKITParser.ELSEIF)
            self.state = 258
            self.exp()
            self.state = 259
            self.match(BKITParser.THEN)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 260
                self.stmt()
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = BKITParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_else_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(BKITParser.ELSE)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 267
                self.stmt()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def conditionExpr(self):
            return self.getTypedRuleContext(BKITParser.ConditionExprContext,0)


        def updateExpr(self):
            return self.getTypedRuleContext(BKITParser.UpdateExprContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(BKITParser.FOR)
            self.state = 274
            self.match(BKITParser.LP)
            self.state = 275
            self.match(BKITParser.ID)
            self.state = 276
            self.match(BKITParser.EQ)
            self.state = 277
            self.exp()
            self.state = 278
            self.match(BKITParser.COMMA)
            self.state = 279
            self.conditionExpr()
            self.state = 280
            self.match(BKITParser.COMMA)
            self.state = 281
            self.updateExpr()
            self.state = 282
            self.match(BKITParser.RP)
            self.state = 283
            self.match(BKITParser.DO)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 284
                self.stmt()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
            self.match(BKITParser.ENDFOR)
            self.state = 291
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Index_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Index_varContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_scalar_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = BKITParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_scalar_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(BKITParser.ID)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 294
                self.index_var()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def scalar_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Scalar_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Scalar_varContext,i)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_index_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_var" ):
                return visitor.visitIndex_var(self)
            else:
                return visitor.visitChildren(self)




    def index_var(self):

        localctx = BKITParser.Index_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_index_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(BKITParser.LSB)
            self.state = 303 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 303
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 301
                    self.scalar_var()
                    pass

                elif la_ == 2:
                    self.state = 302
                    self.exp()
                    pass


                self.state = 305 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0)):
                    break

            self.state = 307
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_var_intContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_var_int(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Index_var_intContext)
            else:
                return self.getTypedRuleContext(BKITParser.Index_var_intContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_scalar_var_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var_int" ):
                return visitor.visitScalar_var_int(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var_int(self):

        localctx = BKITParser.Scalar_var_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_scalar_var_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(BKITParser.ID)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 310
                self.index_var_int()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_var_intContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_index_var_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_var_int" ):
                return visitor.visitIndex_var_int(self)
            else:
                return visitor.visitChildren(self)




    def index_var_int(self):

        localctx = BKITParser.Index_var_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_index_var_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(BKITParser.LSB)
            self.state = 317
            self.match(BKITParser.INTLIT)
            self.state = 318
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_conditionExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionExpr" ):
                return visitor.visitConditionExpr(self)
            else:
                return visitor.visitChildren(self)




    def conditionExpr(self):

        localctx = BKITParser.ConditionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_conditionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_updateExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateExpr" ):
                return visitor.visitUpdateExpr(self)
            else:
                return visitor.visitChildren(self)




    def updateExpr(self):

        localctx = BKITParser.UpdateExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(BKITParser.WHILE)
            self.state = 325
            self.exp()
            self.state = 326
            self.match(BKITParser.DO)
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 327
                self.stmt()
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 333
            self.match(BKITParser.ENDWHILE)
            self.state = 334
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhile_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_doWhile_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhile_stmt" ):
                return visitor.visitDoWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def doWhile_stmt(self):

        localctx = BKITParser.DoWhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_doWhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(BKITParser.DO)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 337
                    self.stmt() 
                self.state = 342
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 343
            self.match(BKITParser.WHILE)
            self.state = 344
            self.exp()
            self.state = 345
            self.match(BKITParser.ENDDO)
            self.state = 346
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(BKITParser.BREAK)
            self.state = 349
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(BKITParser.CONTINUE)
            self.state = 352
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def all_lit(self):
            return self.getTypedRuleContext(BKITParser.All_litContext,0)


        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(BKITParser.RETURN)
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 355
                self.scalar_var()

            elif la_ == 2:
                self.state = 356
                self.all_lit()

            elif la_ == 3:
                self.state = 357
                self.exp()


            self.state = 360
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def var_vp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_vpContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_vpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = BKITParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(BKITParser.ID)
            self.state = 363
            self.match(BKITParser.LP)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 366
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 364
                    self.exp()
                    pass

                elif la_ == 2:
                    self.state = 365
                    self.var_vp()
                    pass


                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 368
                    self.match(BKITParser.COMMA)
                    self.state = 371
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 369
                        self.exp()
                        pass

                    elif la_ == 2:
                        self.state = 370
                        self.var_vp()
                        pass


                    self.state = 377
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 380
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.func_call()
            self.state = 383
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def RELATIONAL(self):
            return self.getToken(BKITParser.RELATIONAL, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.exp1(0)
                self.state = 386
                self.match(BKITParser.RELATIONAL)
                self.state = 387
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 400
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 395
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 396
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 397
                    self.exp2(0) 
                self.state = 402
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def ADDDOT(self):
            return self.getToken(BKITParser.ADDDOT, 0)

        def SUBDOT(self):
            return self.getToken(BKITParser.SUBDOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 411
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 406
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 407
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.SUB) | (1 << BKITParser.ADDDOT) | (1 << BKITParser.SUBDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 408
                    self.exp3(0) 
                self.state = 413
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def MULDOT(self):
            return self.getToken(BKITParser.MULDOT, 0)

        def DIVDOT(self):
            return self.getToken(BKITParser.DIVDOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 417
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 418
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.DIV) | (1 << BKITParser.MOD) | (1 << BKITParser.MULDOT) | (1 << BKITParser.DIVDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 419
                    self.exp4() 
                self.state = 424
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp4)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.match(BKITParser.NOT)
                self.state = 426
                self.exp4()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUBDOT, BKITParser.LP, BKITParser.LCB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBDOT(self):
            return self.getToken(BKITParser.SUBDOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBDOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.SUBDOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 431
                self.exp5()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LP, BKITParser.LCB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.exp6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operands(self):
            return self.getTypedRuleContext(BKITParser.OperandsContext,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def op_index(self):
            return self.getTypedRuleContext(BKITParser.Op_indexContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.operands()
            self._ctx.stop = self._input.LT(-1)
            self.state = 442
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 438
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 439
                    self.op_index() 
                self.state = 444
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_op_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_index" ):
                return visitor.visitOp_index(self)
            else:
                return visitor.visitChildren(self)




    def op_index(self):

        localctx = BKITParser.Op_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_op_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(BKITParser.LSB)
            self.state = 446
            self.exp()
            self.state = 447
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def all_lit(self):
            return self.getTypedRuleContext(BKITParser.All_litContext,0)


        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKITParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_operands)
        self._la = 0 # Token type
        try:
            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(BKITParser.LP)
                self.state = 450
                self.exp()
                self.state = 451
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.all_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 455
                self.match(BKITParser.LCB)
                self.state = 456
                self.exp()
                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 457
                    self.match(BKITParser.COMMA)
                    self.state = 458
                    self.exp()
                    self.state = 463
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 464
                self.match(BKITParser.RCB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 466
                self.match(BKITParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = BKITParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            _la = self._input.LA(1)
            if not(_la==BKITParser.TRUE or _la==BKITParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_int_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lit" ):
                return visitor.visitInt_lit(self)
            else:
                return visitor.visitChildren(self)




    def int_lit(self):

        localctx = BKITParser.Int_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_int_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(BKITParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_float_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_lit" ):
                return visitor.visitFloat_lit(self)
            else:
                return visitor.visitChildren(self)




    def float_lit(self):

        localctx = BKITParser.Float_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_float_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(BKITParser.FLOATLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_string_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_lit" ):
                return visitor.visitString_lit(self)
            else:
                return visitor.visitChildren(self)




    def string_lit(self):

        localctx = BKITParser.String_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_string_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(BKITParser.STRINGLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_lit(self):
            return self.getTypedRuleContext(BKITParser.Int_litContext,0)


        def float_lit(self):
            return self.getTypedRuleContext(BKITParser.Float_litContext,0)


        def string_lit(self):
            return self.getTypedRuleContext(BKITParser.String_litContext,0)


        def bool_lit(self):
            return self.getTypedRuleContext(BKITParser.Bool_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_all_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_lit" ):
                return visitor.visitAll_lit(self)
            else:
                return visitor.visitChildren(self)




    def all_lit(self):

        localctx = BKITParser.All_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_all_lit)
        try:
            self.state = 481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.int_lit()
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.float_lit()
                pass
            elif token in [BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 479
                self.string_lit()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 480
                self.bool_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[36] = self.exp1_sempred
        self._predicates[37] = self.exp2_sempred
        self._predicates[38] = self.exp3_sempred
        self._predicates[41] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




