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
        buf.write("\u01a6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\6\2d\n\2\r\2\16\2e\3\2\3")
        buf.write("\2\3\3\3\3\5\3l\n\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\7\6x\n\6\f\6\16\6{\13\6\3\7\3\7\3\7\3\7\5\7\u0081")
        buf.write("\n\7\5\7\u0083\n\7\3\b\3\b\5\b\u0087\n\b\3\t\3\t\3\t\3")
        buf.write("\t\7\t\u008d\n\t\f\t\16\t\u0090\13\t\5\t\u0092\n\t\3\t")
        buf.write("\3\t\3\n\7\n\u0097\n\n\f\n\16\n\u009a\13\n\3\n\7\n\u009d")
        buf.write("\n\n\f\n\16\n\u00a0\13\n\3\13\3\13\5\13\u00a4\n\13\3\f")
        buf.write("\3\f\3\f\3\f\5\f\u00aa\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00b3\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\7\17\u00bd\n\17\f\17\16\17\u00c0\13\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\5\20\u00c9\n\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\7\21\u00d2\n\21\f\21\16\21\u00d5\13")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\7\22\u00dc\n\22\f\22\16\22")
        buf.write("\u00df\13\22\3\22\5\22\u00e2\n\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\7\26\u0100\n\26\f\26\16\26\u0103\13\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\7\30\u010b\n\30\f\30\16\30\u010e")
        buf.write("\13\30\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \5 \u012e")
        buf.write("\n \3 \3 \3!\3!\3!\5!\u0135\n!\3!\3!\3\"\3\"\3\"\7\"\u013c")
        buf.write("\n\"\f\"\16\"\u013f\13\"\3#\3#\3#\3$\3$\3$\3$\3$\5$\u0149")
        buf.write("\n$\3%\3%\3%\3%\3%\3%\7%\u0151\n%\f%\16%\u0154\13%\3&")
        buf.write("\3&\3&\3&\3&\3&\7&\u015c\n&\f&\16&\u015f\13&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\7\'\u0167\n\'\f\'\16\'\u016a\13\'\3(\3")
        buf.write("(\3(\5(\u016f\n(\3)\3)\3)\5)\u0174\n)\3*\3*\3*\3*\3*\7")
        buf.write("*\u017b\n*\f*\16*\u017e\13*\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\7,\u018e\n,\f,\16,\u0191\13,\3,\3,\3")
        buf.write(",\5,\u0196\n,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\61\5\61\u01a4\n\61\3\61\2\6HJLR\62\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`\2\7\3\2\36\37\4\2 !%&\4\2\"$\'(\4\2!!&")
        buf.write("&\3\2\32\33\2\u01a0\2c\3\2\2\2\4k\3\2\2\2\6m\3\2\2\2\b")
        buf.write("o\3\2\2\2\nr\3\2\2\2\f|\3\2\2\2\16\u0086\3\2\2\2\20\u0088")
        buf.write("\3\2\2\2\22\u0098\3\2\2\2\24\u00a3\3\2\2\2\26\u00a9\3")
        buf.write("\2\2\2\30\u00b2\3\2\2\2\32\u00b4\3\2\2\2\34\u00ba\3\2")
        buf.write("\2\2\36\u00c4\3\2\2\2 \u00cc\3\2\2\2\"\u00d6\3\2\2\2$")
        buf.write("\u00e6\3\2\2\2&\u00eb\3\2\2\2(\u00ee\3\2\2\2*\u00fd\3")
        buf.write("\2\2\2,\u0104\3\2\2\2.\u0108\3\2\2\2\60\u010f\3\2\2\2")
        buf.write("\62\u0113\3\2\2\2\64\u0115\3\2\2\2\66\u0117\3\2\2\28\u011e")
        buf.write("\3\2\2\2:\u0125\3\2\2\2<\u0128\3\2\2\2>\u012b\3\2\2\2")
        buf.write("@\u0131\3\2\2\2B\u0138\3\2\2\2D\u0140\3\2\2\2F\u0148\3")
        buf.write("\2\2\2H\u014a\3\2\2\2J\u0155\3\2\2\2L\u0160\3\2\2\2N\u016e")
        buf.write("\3\2\2\2P\u0173\3\2\2\2R\u0175\3\2\2\2T\u017f\3\2\2\2")
        buf.write("V\u0195\3\2\2\2X\u0197\3\2\2\2Z\u0199\3\2\2\2\\\u019b")
        buf.write("\3\2\2\2^\u019d\3\2\2\2`\u01a3\3\2\2\2bd\5\4\3\2cb\3\2")
        buf.write("\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2fg\3\2\2\2gh\7\2\2\3")
        buf.write("h\3\3\2\2\2il\5\6\4\2jl\5\36\20\2ki\3\2\2\2kj\3\2\2\2")
        buf.write("l\5\3\2\2\2mn\5\b\5\2n\7\3\2\2\2op\5\n\6\2pq\7;\2\2q\t")
        buf.write("\3\2\2\2rs\7\34\2\2st\7<\2\2ty\5\f\7\2uv\7=\2\2vx\5\f")
        buf.write("\7\2wu\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\13\3\2\2")
        buf.write("\2{y\3\2\2\2|\u0082\5.\30\2}\u0080\7)\2\2~\u0081\5\20")
        buf.write("\t\2\177\u0081\5`\61\2\u0080~\3\2\2\2\u0080\177\3\2\2")
        buf.write("\2\u0081\u0083\3\2\2\2\u0082}\3\2\2\2\u0082\u0083\3\2")
        buf.write("\2\2\u0083\r\3\2\2\2\u0084\u0087\5\20\t\2\u0085\u0087")
        buf.write("\5`\61\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\17\3\2\2\2\u0088\u0091\7\67\2\2\u0089\u008e\5\16\b\2")
        buf.write("\u008a\u008b\7=\2\2\u008b\u008d\5\16\b\2\u008c\u008a\3")
        buf.write("\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f")
        buf.write("\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0091")
        buf.write("\u0089\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2")
        buf.write("\u0093\u0094\78\2\2\u0094\21\3\2\2\2\u0095\u0097\5\6\4")
        buf.write("\2\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009e\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009b\u009d\5\24\13\2\u009c\u009b\3\2\2")
        buf.write("\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\23\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a4")
        buf.write("\5\26\f\2\u00a2\u00a4\5\30\r\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a4\25\3\2\2\2\u00a5\u00aa\5\"\22\2\u00a6")
        buf.write("\u00aa\5(\25\2\u00a7\u00aa\5\66\34\2\u00a8\u00aa\58\35")
        buf.write("\2\u00a9\u00a5\3\2\2\2\u00a9\u00a6\3\2\2\2\u00a9\u00a7")
        buf.write("\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\27\3\2\2\2\u00ab\u00ac")
        buf.write("\5\34\17\2\u00ac\u00ad\7;\2\2\u00ad\u00b3\3\2\2\2\u00ae")
        buf.write("\u00b3\5:\36\2\u00af\u00b3\5<\37\2\u00b0\u00b3\5> \2\u00b1")
        buf.write("\u00b3\5D#\2\u00b2\u00ab\3\2\2\2\u00b2\u00ae\3\2\2\2\u00b2")
        buf.write("\u00af\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b3\31\3\2\2\2\u00b4\u00b5\7\n\2\2\u00b5\u00b6\7<\2")
        buf.write("\2\u00b6\u00b7\5\22\n\2\u00b7\u00b8\7\13\2\2\u00b8\u00b9")
        buf.write("\7>\2\2\u00b9\33\3\2\2\2\u00ba\u00be\7A\2\2\u00bb\u00bd")
        buf.write("\5T+\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc")
        buf.write("\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c1\u00c2\7)\2\2\u00c2\u00c3\5F$\2\u00c3")
        buf.write("\35\3\2\2\2\u00c4\u00c5\7\b\2\2\u00c5\u00c6\7<\2\2\u00c6")
        buf.write("\u00c8\7A\2\2\u00c7\u00c9\5 \21\2\u00c8\u00c7\3\2\2\2")
        buf.write("\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\5")
        buf.write("\32\16\2\u00cb\37\3\2\2\2\u00cc\u00cd\7\t\2\2\u00cd\u00ce")
        buf.write("\7<\2\2\u00ce\u00d3\5.\30\2\u00cf\u00d0\7=\2\2\u00d0\u00d2")
        buf.write("\5.\30\2\u00d1\u00cf\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4!\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d6\u00d7\7\f\2\2\u00d7\u00d8\5F$\2\u00d8")
        buf.write("\u00d9\7\r\2\2\u00d9\u00dd\5\22\n\2\u00da\u00dc\5$\23")
        buf.write("\2\u00db\u00da\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e1\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00e0\u00e2\5&\24\2\u00e1\u00e0\3\2\2\2")
        buf.write("\u00e1\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\7")
        buf.write("\20\2\2\u00e4\u00e5\7>\2\2\u00e5#\3\2\2\2\u00e6\u00e7")
        buf.write("\7\16\2\2\u00e7\u00e8\5F$\2\u00e8\u00e9\7\r\2\2\u00e9")
        buf.write("\u00ea\5\22\n\2\u00ea%\3\2\2\2\u00eb\u00ec\7\17\2\2\u00ec")
        buf.write("\u00ed\5\22\n\2\u00ed\'\3\2\2\2\u00ee\u00ef\7\21\2\2\u00ef")
        buf.write("\u00f0\7\65\2\2\u00f0\u00f1\7A\2\2\u00f1\u00f2\7)\2\2")
        buf.write("\u00f2\u00f3\5F$\2\u00f3\u00f4\7=\2\2\u00f4\u00f5\5\62")
        buf.write("\32\2\u00f5\u00f6\7=\2\2\u00f6\u00f7\5\64\33\2\u00f7\u00f8")
        buf.write("\7\66\2\2\u00f8\u00f9\7\23\2\2\u00f9\u00fa\5\22\n\2\u00fa")
        buf.write("\u00fb\7\22\2\2\u00fb\u00fc\7>\2\2\u00fc)\3\2\2\2\u00fd")
        buf.write("\u0101\7A\2\2\u00fe\u0100\5,\27\2\u00ff\u00fe\3\2\2\2")
        buf.write("\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3")
        buf.write("\2\2\2\u0102+\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105")
        buf.write("\79\2\2\u0105\u0106\5F$\2\u0106\u0107\7:\2\2\u0107-\3")
        buf.write("\2\2\2\u0108\u010c\7A\2\2\u0109\u010b\5\60\31\2\u010a")
        buf.write("\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2")
        buf.write("\u010c\u010d\3\2\2\2\u010d/\3\2\2\2\u010e\u010c\3\2\2")
        buf.write("\2\u010f\u0110\79\2\2\u0110\u0111\7?\2\2\u0111\u0112\7")
        buf.write(":\2\2\u0112\61\3\2\2\2\u0113\u0114\5F$\2\u0114\63\3\2")
        buf.write("\2\2\u0115\u0116\5F$\2\u0116\65\3\2\2\2\u0117\u0118\7")
        buf.write("\25\2\2\u0118\u0119\5F$\2\u0119\u011a\7\23\2\2\u011a\u011b")
        buf.write("\5\22\n\2\u011b\u011c\7\26\2\2\u011c\u011d\7>\2\2\u011d")
        buf.write("\67\3\2\2\2\u011e\u011f\7\23\2\2\u011f\u0120\5\22\n\2")
        buf.write("\u0120\u0121\7\25\2\2\u0121\u0122\5F$\2\u0122\u0123\7")
        buf.write("\24\2\2\u0123\u0124\7>\2\2\u01249\3\2\2\2\u0125\u0126")
        buf.write("\7\30\2\2\u0126\u0127\7;\2\2\u0127;\3\2\2\2\u0128\u0129")
        buf.write("\7\31\2\2\u0129\u012a\7;\2\2\u012a=\3\2\2\2\u012b\u012d")
        buf.write("\7\27\2\2\u012c\u012e\5F$\2\u012d\u012c\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\7;\2\2")
        buf.write("\u0130?\3\2\2\2\u0131\u0132\7A\2\2\u0132\u0134\7\65\2")
        buf.write("\2\u0133\u0135\5B\"\2\u0134\u0133\3\2\2\2\u0134\u0135")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137\7\66\2\2\u0137")
        buf.write("A\3\2\2\2\u0138\u013d\5F$\2\u0139\u013a\7=\2\2\u013a\u013c")
        buf.write("\5F$\2\u013b\u0139\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013eC\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u0140\u0141\5@!\2\u0141\u0142\7;\2\2\u0142E\3")
        buf.write("\2\2\2\u0143\u0144\5H%\2\u0144\u0145\7\3\2\2\u0145\u0146")
        buf.write("\5H%\2\u0146\u0149\3\2\2\2\u0147\u0149\5H%\2\u0148\u0143")
        buf.write("\3\2\2\2\u0148\u0147\3\2\2\2\u0149G\3\2\2\2\u014a\u014b")
        buf.write("\b%\1\2\u014b\u014c\5J&\2\u014c\u0152\3\2\2\2\u014d\u014e")
        buf.write("\f\4\2\2\u014e\u014f\t\2\2\2\u014f\u0151\5J&\2\u0150\u014d")
        buf.write("\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152")
        buf.write("\u0153\3\2\2\2\u0153I\3\2\2\2\u0154\u0152\3\2\2\2\u0155")
        buf.write("\u0156\b&\1\2\u0156\u0157\5L\'\2\u0157\u015d\3\2\2\2\u0158")
        buf.write("\u0159\f\4\2\2\u0159\u015a\t\3\2\2\u015a\u015c\5L\'\2")
        buf.write("\u015b\u0158\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3")
        buf.write("\2\2\2\u015d\u015e\3\2\2\2\u015eK\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u0160\u0161\b\'\1\2\u0161\u0162\5N(\2\u0162\u0168")
        buf.write("\3\2\2\2\u0163\u0164\f\4\2\2\u0164\u0165\t\4\2\2\u0165")
        buf.write("\u0167\5N(\2\u0166\u0163\3\2\2\2\u0167\u016a\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169M\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016b\u016c\7\35\2\2\u016c\u016f\5N(\2")
        buf.write("\u016d\u016f\5P)\2\u016e\u016b\3\2\2\2\u016e\u016d\3\2")
        buf.write("\2\2\u016fO\3\2\2\2\u0170\u0171\t\5\2\2\u0171\u0174\5")
        buf.write("P)\2\u0172\u0174\5R*\2\u0173\u0170\3\2\2\2\u0173\u0172")
        buf.write("\3\2\2\2\u0174Q\3\2\2\2\u0175\u0176\b*\1\2\u0176\u0177")
        buf.write("\5V,\2\u0177\u017c\3\2\2\2\u0178\u0179\f\4\2\2\u0179\u017b")
        buf.write("\5T+\2\u017a\u0178\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017dS\3\2\2\2\u017e\u017c")
        buf.write("\3\2\2\2\u017f\u0180\79\2\2\u0180\u0181\5F$\2\u0181\u0182")
        buf.write("\7:\2\2\u0182U\3\2\2\2\u0183\u0184\7\65\2\2\u0184\u0185")
        buf.write("\5F$\2\u0185\u0186\7\66\2\2\u0186\u0196\3\2\2\2\u0187")
        buf.write("\u0196\5@!\2\u0188\u0196\5`\61\2\u0189\u018a\7\67\2\2")
        buf.write("\u018a\u018f\5`\61\2\u018b\u018c\7=\2\2\u018c\u018e\5")
        buf.write("`\61\2\u018d\u018b\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192\3\2\2\2\u0191")
        buf.write("\u018f\3\2\2\2\u0192\u0193\78\2\2\u0193\u0196\3\2\2\2")
        buf.write("\u0194\u0196\7A\2\2\u0195\u0183\3\2\2\2\u0195\u0187\3")
        buf.write("\2\2\2\u0195\u0188\3\2\2\2\u0195\u0189\3\2\2\2\u0195\u0194")
        buf.write("\3\2\2\2\u0196W\3\2\2\2\u0197\u0198\t\6\2\2\u0198Y\3\2")
        buf.write("\2\2\u0199\u019a\7?\2\2\u019a[\3\2\2\2\u019b\u019c\7@")
        buf.write("\2\2\u019c]\3\2\2\2\u019d\u019e\7E\2\2\u019e_\3\2\2\2")
        buf.write("\u019f\u01a4\5Z.\2\u01a0\u01a4\5\\/\2\u01a1\u01a4\5^\60")
        buf.write("\2\u01a2\u01a4\5X-\2\u01a3\u019f\3\2\2\2\u01a3\u01a0\3")
        buf.write("\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4a")
        buf.write("\3\2\2\2#eky\u0080\u0082\u0086\u008e\u0091\u0098\u009e")
        buf.write("\u00a3\u00a9\u00b2\u00be\u00c8\u00d3\u00dd\u00e1\u0101")
        buf.write("\u010c\u012d\u0134\u013d\u0148\u0152\u015d\u0168\u016e")
        buf.write("\u0173\u017c\u018f\u0195\u01a3")
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
    RULE_array_lit_cell = 6
    RULE_array_lit = 7
    RULE_body = 8
    RULE_stmt = 9
    RULE_stmt_notfunc = 10
    RULE_stmt_spe = 11
    RULE_body_declare = 12
    RULE_assign_stmt = 13
    RULE_func_declare = 14
    RULE_parameter_func = 15
    RULE_if_stmt = 16
    RULE_elseif_stmt = 17
    RULE_else_stmt = 18
    RULE_for_stmt = 19
    RULE_scalar_var = 20
    RULE_index_var = 21
    RULE_scalar_var_int = 22
    RULE_index_var_int = 23
    RULE_conditionExpr = 24
    RULE_updateExpr = 25
    RULE_while_stmt = 26
    RULE_doWhile_stmt = 27
    RULE_break_stmt = 28
    RULE_continue_stmt = 29
    RULE_return_stmt = 30
    RULE_func_call = 31
    RULE_func_call_cell = 32
    RULE_call_stmt = 33
    RULE_exp = 34
    RULE_exp1 = 35
    RULE_exp2 = 36
    RULE_exp3 = 37
    RULE_exp4 = 38
    RULE_exp5 = 39
    RULE_exp6 = 40
    RULE_op_index = 41
    RULE_operands = 42
    RULE_bool_lit = 43
    RULE_int_lit = 44
    RULE_float_lit = 45
    RULE_string_lit = 46
    RULE_all_lit = 47

    ruleNames =  [ "program", "main", "var_declare", "var_list", "var_normal", 
                   "var_normal_list", "array_lit_cell", "array_lit", "body", 
                   "stmt", "stmt_notfunc", "stmt_spe", "body_declare", "assign_stmt", 
                   "func_declare", "parameter_func", "if_stmt", "elseif_stmt", 
                   "else_stmt", "for_stmt", "scalar_var", "index_var", "scalar_var_int", 
                   "index_var_int", "conditionExpr", "updateExpr", "while_stmt", 
                   "doWhile_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "func_call", "func_call_cell", "call_stmt", "exp", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "op_index", "operands", 
                   "bool_lit", "int_lit", "float_lit", "string_lit", "all_lit" ]

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
            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self.main()
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.FUNCTION or _la==BKITParser.VAR):
                    break

            self.state = 101
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
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.var_declare()
                pass
            elif token in [BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
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
            self.state = 107
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
            self.state = 109
            self.var_normal()
            self.state = 110
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
            self.state = 112
            self.match(BKITParser.VAR)
            self.state = 113
            self.match(BKITParser.COLON)
            self.state = 114
            self.var_normal_list()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 115
                self.match(BKITParser.COMMA)
                self.state = 116
                self.var_normal_list()
                self.state = 121
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
            self.state = 122
            self.scalar_var_int()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.EQ:
                self.state = 123
                self.match(BKITParser.EQ)
                self.state = 126
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.LCB]:
                    self.state = 124
                    self.array_lit()
                    pass
                elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                    self.state = 125
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
        self.enterRule(localctx, 12, self.RULE_array_lit_cell)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.array_lit()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
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
        self.enterRule(localctx, 14, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(BKITParser.LCB)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 135
                self.array_lit_cell()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 136
                    self.match(BKITParser.COMMA)
                    self.state = 137
                    self.array_lit_cell()
                    self.state = 142
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 145
            self.match(BKITParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 147
                self.var_declare()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 153
                    self.stmt() 
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_stmt)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IF, BKITParser.FOR, BKITParser.DO, BKITParser.WHILE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.stmt_notfunc()
                pass
            elif token in [BKITParser.RETURN, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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
        self.enterRule(localctx, 20, self.RULE_stmt_notfunc)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.if_stmt()
                pass
            elif token in [BKITParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.for_stmt()
                pass
            elif token in [BKITParser.WHILE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.while_stmt()
                pass
            elif token in [BKITParser.DO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
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
        self.enterRule(localctx, 22, self.RULE_stmt_spe)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.assign_stmt()
                self.state = 170
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.break_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.continue_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
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

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_body_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_declare" ):
                return visitor.visitBody_declare(self)
            else:
                return visitor.visitChildren(self)




    def body_declare(self):

        localctx = BKITParser.Body_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_body_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(BKITParser.BODY)
            self.state = 179
            self.match(BKITParser.COLON)
            self.state = 180
            self.body()
            self.state = 181
            self.match(BKITParser.ENDBODY)
            self.state = 182
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

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def op_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Op_indexContext)
            else:
                return self.getTypedRuleContext(BKITParser.Op_indexContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assign_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(BKITParser.ID)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 185
                self.op_index()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
            self.match(BKITParser.EQ)
            self.state = 192
            self.exp()
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
        self.enterRule(localctx, 28, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(BKITParser.FUNCTION)
            self.state = 195
            self.match(BKITParser.COLON)
            self.state = 196
            self.match(BKITParser.ID)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 197
                self.parameter_func()


            self.state = 200
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
        self.enterRule(localctx, 30, self.RULE_parameter_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(BKITParser.PARAMETER)
            self.state = 203
            self.match(BKITParser.COLON)
            self.state = 204
            self.scalar_var_int()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 205
                self.match(BKITParser.COMMA)
                self.state = 206
                self.scalar_var_int()
                self.state = 211
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

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

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
        self.enterRule(localctx, 32, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(BKITParser.IF)
            self.state = 213
            self.exp()
            self.state = 214
            self.match(BKITParser.THEN)
            self.state = 215
            self.body()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 216
                self.elseif_stmt()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 222
                self.else_stmt()


            self.state = 225
            self.match(BKITParser.ENDIF)
            self.state = 226
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

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = BKITParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(BKITParser.ELSEIF)
            self.state = 229
            self.exp()
            self.state = 230
            self.match(BKITParser.THEN)
            self.state = 231
            self.body()
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

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = BKITParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(BKITParser.ELSE)
            self.state = 234
            self.body()
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

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(BKITParser.FOR)
            self.state = 237
            self.match(BKITParser.LP)
            self.state = 238
            self.match(BKITParser.ID)
            self.state = 239
            self.match(BKITParser.EQ)
            self.state = 240
            self.exp()
            self.state = 241
            self.match(BKITParser.COMMA)
            self.state = 242
            self.conditionExpr()
            self.state = 243
            self.match(BKITParser.COMMA)
            self.state = 244
            self.updateExpr()
            self.state = 245
            self.match(BKITParser.RP)
            self.state = 246
            self.match(BKITParser.DO)
            self.state = 247
            self.body()
            self.state = 248
            self.match(BKITParser.ENDFOR)
            self.state = 249
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
        self.enterRule(localctx, 40, self.RULE_scalar_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(BKITParser.ID)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 252
                self.index_var()
                self.state = 257
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

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_index_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_var" ):
                return visitor.visitIndex_var(self)
            else:
                return visitor.visitChildren(self)




    def index_var(self):

        localctx = BKITParser.Index_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_index_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(BKITParser.LSB)
            self.state = 259
            self.exp()
            self.state = 260
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
        self.enterRule(localctx, 44, self.RULE_scalar_var_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(BKITParser.ID)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 263
                self.index_var_int()
                self.state = 268
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
        self.enterRule(localctx, 46, self.RULE_index_var_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(BKITParser.LSB)
            self.state = 270
            self.match(BKITParser.INTLIT)
            self.state = 271
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
        self.enterRule(localctx, 48, self.RULE_conditionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
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
        self.enterRule(localctx, 50, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
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

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(BKITParser.WHILE)
            self.state = 278
            self.exp()
            self.state = 279
            self.match(BKITParser.DO)
            self.state = 280
            self.body()
            self.state = 281
            self.match(BKITParser.ENDWHILE)
            self.state = 282
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

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_doWhile_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhile_stmt" ):
                return visitor.visitDoWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def doWhile_stmt(self):

        localctx = BKITParser.DoWhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_doWhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(BKITParser.DO)
            self.state = 285
            self.body()
            self.state = 286
            self.match(BKITParser.WHILE)
            self.state = 287
            self.exp()
            self.state = 288
            self.match(BKITParser.ENDDO)
            self.state = 289
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
        self.enterRule(localctx, 56, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(BKITParser.BREAK)
            self.state = 292
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
        self.enterRule(localctx, 58, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(BKITParser.CONTINUE)
            self.state = 295
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
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(BKITParser.RETURN)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 298
                self.exp()


            self.state = 301
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

        def func_call_cell(self):
            return self.getTypedRuleContext(BKITParser.Func_call_cellContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = BKITParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(BKITParser.ID)
            self.state = 304
            self.match(BKITParser.LP)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 305
                self.func_call_cell()


            self.state = 308
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_cellContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_func_call_cell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_cell" ):
                return visitor.visitFunc_call_cell(self)
            else:
                return visitor.visitChildren(self)




    def func_call_cell(self):

        localctx = BKITParser.Func_call_cellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_func_call_cell)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.exp()
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 311
                self.match(BKITParser.COMMA)
                self.state = 312
                self.exp()
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 66, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.func_call()
            self.state = 319
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
        self.enterRule(localctx, 68, self.RULE_exp)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.exp1(0)
                self.state = 322
                self.match(BKITParser.RELATIONAL)
                self.state = 323
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 333
                    self.exp2(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.SUB) | (1 << BKITParser.ADDDOT) | (1 << BKITParser.SUBDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 344
                    self.exp3(0) 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 353
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 354
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.DIV) | (1 << BKITParser.MOD) | (1 << BKITParser.MULDOT) | (1 << BKITParser.DIVDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 355
                    self.exp4() 
                self.state = 360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 76, self.RULE_exp4)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(BKITParser.NOT)
                self.state = 362
                self.exp4()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUBDOT, BKITParser.LP, BKITParser.LCB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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
        self.enterRule(localctx, 78, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBDOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.SUBDOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 367
                self.exp5()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LP, BKITParser.LCB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.operands()
            self._ctx.stop = self._input.LT(-1)
            self.state = 378
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    self.op_index() 
                self.state = 380
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_op_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(BKITParser.LSB)
            self.state = 382
            self.exp()
            self.state = 383
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

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def all_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.All_litContext)
            else:
                return self.getTypedRuleContext(BKITParser.All_litContext,i)


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
        self.enterRule(localctx, 84, self.RULE_operands)
        self._la = 0 # Token type
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(BKITParser.LP)
                self.state = 386
                self.exp()
                self.state = 387
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
                self.all_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 391
                self.match(BKITParser.LCB)
                self.state = 392
                self.all_lit()
                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 393
                    self.match(BKITParser.COMMA)
                    self.state = 394
                    self.all_lit()
                    self.state = 399
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 400
                self.match(BKITParser.RCB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 402
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
        self.enterRule(localctx, 86, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
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
        self.enterRule(localctx, 88, self.RULE_int_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
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
        self.enterRule(localctx, 90, self.RULE_float_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
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
        self.enterRule(localctx, 92, self.RULE_string_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
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
        self.enterRule(localctx, 94, self.RULE_all_lit)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.int_lit()
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.float_lit()
                pass
            elif token in [BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 415
                self.string_lit()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 416
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
        self._predicates[35] = self.exp1_sempred
        self._predicates[36] = self.exp2_sempred
        self._predicates[37] = self.exp3_sempred
        self._predicates[40] = self.exp6_sempred
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
         




