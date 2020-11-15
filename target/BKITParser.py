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
        buf.write("\u01eb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\6\2h")
        buf.write("\n\2\r\2\16\2i\3\2\3\2\3\3\3\3\5\3p\n\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\7\6|\n\6\f\6\16\6\177\13\6")
        buf.write("\3\7\3\7\3\7\3\7\5\7\u0085\n\7\5\7\u0087\n\7\3\b\3\b\3")
        buf.write("\b\5\b\u008c\n\b\3\t\3\t\3\t\3\t\7\t\u0092\n\t\f\t\16")
        buf.write("\t\u0095\13\t\5\t\u0097\n\t\3\t\3\t\3\n\3\n\5\n\u009d")
        buf.write("\n\n\3\13\3\13\3\13\3\13\7\13\u00a3\n\13\f\13\16\13\u00a6")
        buf.write("\13\13\5\13\u00a8\n\13\3\13\3\13\3\f\3\f\5\f\u00ae\n\f")
        buf.write("\3\r\3\r\5\r\u00b2\n\r\3\16\3\16\3\16\3\16\5\16\u00b8")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00c1\n")
        buf.write("\17\3\20\3\20\3\20\7\20\u00c6\n\20\f\20\16\20\u00c9\13")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00d2\n\21")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00d8\n\22\3\22\7\22\u00db\n")
        buf.write("\22\f\22\16\22\u00de\13\22\5\22\u00e0\n\22\3\23\3\23\3")
        buf.write("\23\3\23\5\23\u00e6\n\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\7\24\u00ef\n\24\f\24\16\24\u00f2\13\24\3\25\3\25")
        buf.write("\3\25\3\25\7\25\u00f8\n\25\f\25\16\25\u00fb\13\25\3\25")
        buf.write("\7\25\u00fe\n\25\f\25\16\25\u0101\13\25\3\25\5\25\u0104")
        buf.write("\n\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\7\26\u010d\n")
        buf.write("\26\f\26\16\26\u0110\13\26\3\27\3\27\7\27\u0114\n\27\f")
        buf.write("\27\16\27\u0117\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\7\30\u0125\n\30\f\30\16\30")
        buf.write("\u0128\13\30\3\30\3\30\3\30\3\31\3\31\7\31\u012f\n\31")
        buf.write("\f\31\16\31\u0132\13\31\3\32\3\32\3\32\6\32\u0137\n\32")
        buf.write("\r\32\16\32\u0138\3\32\3\32\3\33\3\33\7\33\u013f\n\33")
        buf.write("\f\33\16\33\u0142\13\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\7\37\u0150\n\37\f\37\16")
        buf.write("\37\u0153\13\37\3\37\3\37\3\37\3 \3 \7 \u015a\n \f \16")
        buf.write(" \u015d\13 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3#\3#\5#\u016e\n#\3#\3#\3$\3$\3$\3$\5$\u0176\n$\3$\3")
        buf.write("$\3$\5$\u017b\n$\7$\u017d\n$\f$\16$\u0180\13$\5$\u0182")
        buf.write("\n$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\5&\u018e\n&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\7\'\u0196\n\'\f\'\16\'\u0199\13\'\3(")
        buf.write("\3(\3(\3(\3(\3(\7(\u01a1\n(\f(\16(\u01a4\13(\3)\3)\3)")
        buf.write("\3)\3)\3)\7)\u01ac\n)\f)\16)\u01af\13)\3*\3*\3*\5*\u01b4")
        buf.write("\n*\3+\3+\3+\5+\u01b9\n+\3,\3,\3,\3,\3,\7,\u01c0\n,\f")
        buf.write(",\16,\u01c3\13,\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\7.\u01d3\n.\f.\16.\u01d6\13.\3.\3.\3.\5.\u01db\n")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3")
        buf.write("\63\5\63\u01e9\n\63\3\63\2\6LNPV\64\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bd\2\7\3\2\36\37\4\2 !%&\4\2\"$\'(\4\2!!&&")
        buf.write("\3\2\32\33\2\u01f7\2g\3\2\2\2\4o\3\2\2\2\6q\3\2\2\2\b")
        buf.write("s\3\2\2\2\nv\3\2\2\2\f\u0080\3\2\2\2\16\u008b\3\2\2\2")
        buf.write("\20\u008d\3\2\2\2\22\u009c\3\2\2\2\24\u009e\3\2\2\2\26")
        buf.write("\u00ad\3\2\2\2\30\u00b1\3\2\2\2\32\u00b7\3\2\2\2\34\u00c0")
        buf.write("\3\2\2\2\36\u00c2\3\2\2\2 \u00cd\3\2\2\2\"\u00df\3\2\2")
        buf.write("\2$\u00e1\3\2\2\2&\u00e9\3\2\2\2(\u00f3\3\2\2\2*\u0108")
        buf.write("\3\2\2\2,\u0111\3\2\2\2.\u0118\3\2\2\2\60\u012c\3\2\2")
        buf.write("\2\62\u0133\3\2\2\2\64\u013c\3\2\2\2\66\u0143\3\2\2\2")
        buf.write("8\u0147\3\2\2\2:\u0149\3\2\2\2<\u014b\3\2\2\2>\u0157\3")
        buf.write("\2\2\2@\u0163\3\2\2\2B\u0166\3\2\2\2D\u0169\3\2\2\2F\u0171")
        buf.write("\3\2\2\2H\u0185\3\2\2\2J\u018d\3\2\2\2L\u018f\3\2\2\2")
        buf.write("N\u019a\3\2\2\2P\u01a5\3\2\2\2R\u01b3\3\2\2\2T\u01b8\3")
        buf.write("\2\2\2V\u01ba\3\2\2\2X\u01c4\3\2\2\2Z\u01da\3\2\2\2\\")
        buf.write("\u01dc\3\2\2\2^\u01de\3\2\2\2`\u01e0\3\2\2\2b\u01e2\3")
        buf.write("\2\2\2d\u01e8\3\2\2\2fh\5\4\3\2gf\3\2\2\2hi\3\2\2\2ig")
        buf.write("\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\7\2\2\3l\3\3\2\2\2mp\5")
        buf.write("\6\4\2np\5$\23\2om\3\2\2\2on\3\2\2\2p\5\3\2\2\2qr\5\b")
        buf.write("\5\2r\7\3\2\2\2st\5\n\6\2tu\7;\2\2u\t\3\2\2\2vw\7\34\2")
        buf.write("\2wx\7<\2\2x}\5\f\7\2yz\7=\2\2z|\5\f\7\2{y\3\2\2\2|\177")
        buf.write("\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\13\3\2\2\2\177}\3\2\2\2")
        buf.write("\u0080\u0086\5\64\33\2\u0081\u0084\7)\2\2\u0082\u0085")
        buf.write("\5\24\13\2\u0083\u0085\5d\63\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\u0087\3\2\2\2\u0086\u0081\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\r\3\2\2\2\u0088\u008c\5\20")
        buf.write("\t\2\u0089\u008c\5\60\31\2\u008a\u008c\5J&\2\u008b\u0088")
        buf.write("\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c")
        buf.write("\17\3\2\2\2\u008d\u0096\7\67\2\2\u008e\u0093\5\16\b\2")
        buf.write("\u008f\u0090\7=\2\2\u0090\u0092\5\16\b\2\u0091\u008f\3")
        buf.write("\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0096")
        buf.write("\u008e\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u0099\78\2\2\u0099\21\3\2\2\2\u009a\u009d\5\24")
        buf.write("\13\2\u009b\u009d\5d\63\2\u009c\u009a\3\2\2\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\23\3\2\2\2\u009e\u00a7\7\67\2\2\u009f\u00a4")
        buf.write("\5\22\n\2\u00a0\u00a1\7=\2\2\u00a1\u00a3\5\22\n\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2")
        buf.write("\u00a4\u00a5\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3")
        buf.write("\2\2\2\u00a7\u009f\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\u00aa\78\2\2\u00aa\25\3\2\2\2\u00ab\u00ae")
        buf.write("\5\6\4\2\u00ac\u00ae\5\30\r\2\u00ad\u00ab\3\2\2\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ae\27\3\2\2\2\u00af\u00b2\5\32\16\2")
        buf.write("\u00b0\u00b2\5\34\17\2\u00b1\u00af\3\2\2\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b2\31\3\2\2\2\u00b3\u00b8\5(\25\2\u00b4\u00b8")
        buf.write("\5.\30\2\u00b5\u00b8\5<\37\2\u00b6\u00b8\5> \2\u00b7\u00b3")
        buf.write("\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\33\3\2\2\2\u00b9\u00ba\5 \21\2\u00ba")
        buf.write("\u00bb\7;\2\2\u00bb\u00c1\3\2\2\2\u00bc\u00c1\5@!\2\u00bd")
        buf.write("\u00c1\5B\"\2\u00be\u00c1\5D#\2\u00bf\u00c1\5H%\2\u00c0")
        buf.write("\u00b9\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c0\u00bd\3\2\2\2")
        buf.write("\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\35\3\2")
        buf.write("\2\2\u00c2\u00c3\7\n\2\2\u00c3\u00c7\7<\2\2\u00c4\u00c6")
        buf.write("\5\26\f\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca\3\2\2\2")
        buf.write("\u00c9\u00c7\3\2\2\2\u00ca\u00cb\7\13\2\2\u00cb\u00cc")
        buf.write("\7>\2\2\u00cc\37\3\2\2\2\u00cd\u00ce\5\"\22\2\u00ce\u00d1")
        buf.write("\7)\2\2\u00cf\u00d2\5\"\22\2\u00d0\u00d2\5J&\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2!\3\2\2\2\u00d3\u00e0")
        buf.write("\5\60\31\2\u00d4\u00d8\5F$\2\u00d5\u00d8\7E\2\2\u00d6")
        buf.write("\u00d8\5\20\t\2\u00d7\u00d4\3\2\2\2\u00d7\u00d5\3\2\2")
        buf.write("\2\u00d7\u00d6\3\2\2\2\u00d8\u00dc\3\2\2\2\u00d9\u00db")
        buf.write("\5\62\32\2\u00da\u00d9\3\2\2\2\u00db\u00de\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e0\3\2\2\2")
        buf.write("\u00de\u00dc\3\2\2\2\u00df\u00d3\3\2\2\2\u00df\u00d7\3")
        buf.write("\2\2\2\u00e0#\3\2\2\2\u00e1\u00e2\7\b\2\2\u00e2\u00e3")
        buf.write("\7<\2\2\u00e3\u00e5\7A\2\2\u00e4\u00e6\5&\24\2\u00e5\u00e4")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00e8\5\36\20\2\u00e8%\3\2\2\2\u00e9\u00ea\7\t\2\2\u00ea")
        buf.write("\u00eb\7<\2\2\u00eb\u00f0\5\64\33\2\u00ec\u00ed\7=\2\2")
        buf.write("\u00ed\u00ef\5\64\33\2\u00ee\u00ec\3\2\2\2\u00ef\u00f2")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1")
        buf.write("\'\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\7\f\2\2\u00f4")
        buf.write("\u00f5\5J&\2\u00f5\u00f9\7\r\2\2\u00f6\u00f8\5\26\f\2")
        buf.write("\u00f7\u00f6\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3")
        buf.write("\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00ff\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fc\u00fe\5*\26\2\u00fd\u00fc\3\2\2\2\u00fe")
        buf.write("\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0104\5")
        buf.write(",\27\2\u0103\u0102\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105")
        buf.write("\3\2\2\2\u0105\u0106\7\20\2\2\u0106\u0107\7>\2\2\u0107")
        buf.write(")\3\2\2\2\u0108\u0109\7\16\2\2\u0109\u010a\5J&\2\u010a")
        buf.write("\u010e\7\r\2\2\u010b\u010d\5\26\f\2\u010c\u010b\3\2\2")
        buf.write("\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f")
        buf.write("\3\2\2\2\u010f+\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0115")
        buf.write("\7\17\2\2\u0112\u0114\5\26\f\2\u0113\u0112\3\2\2\2\u0114")
        buf.write("\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116-\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\7\21\2")
        buf.write("\2\u0119\u011a\7\65\2\2\u011a\u011b\7A\2\2\u011b\u011c")
        buf.write("\7)\2\2\u011c\u011d\5J&\2\u011d\u011e\7=\2\2\u011e\u011f")
        buf.write("\58\35\2\u011f\u0120\7=\2\2\u0120\u0121\5:\36\2\u0121")
        buf.write("\u0122\7\66\2\2\u0122\u0126\7\23\2\2\u0123\u0125\5\26")
        buf.write("\f\2\u0124\u0123\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129\3\2\2\2\u0128")
        buf.write("\u0126\3\2\2\2\u0129\u012a\7\22\2\2\u012a\u012b\7>\2\2")
        buf.write("\u012b/\3\2\2\2\u012c\u0130\7A\2\2\u012d\u012f\5\62\32")
        buf.write("\2\u012e\u012d\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131\61\3\2\2\2\u0132\u0130")
        buf.write("\3\2\2\2\u0133\u0136\79\2\2\u0134\u0137\5\60\31\2\u0135")
        buf.write("\u0137\5J&\2\u0136\u0134\3\2\2\2\u0136\u0135\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a\u013b\7:\2\2\u013b\63\3\2\2")
        buf.write("\2\u013c\u0140\7A\2\2\u013d\u013f\5\66\34\2\u013e\u013d")
        buf.write("\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2\2\2\u0140")
        buf.write("\u0141\3\2\2\2\u0141\65\3\2\2\2\u0142\u0140\3\2\2\2\u0143")
        buf.write("\u0144\79\2\2\u0144\u0145\7?\2\2\u0145\u0146\7:\2\2\u0146")
        buf.write("\67\3\2\2\2\u0147\u0148\5J&\2\u01489\3\2\2\2\u0149\u014a")
        buf.write("\5J&\2\u014a;\3\2\2\2\u014b\u014c\7\25\2\2\u014c\u014d")
        buf.write("\5J&\2\u014d\u0151\7\23\2\2\u014e\u0150\5\26\f\2\u014f")
        buf.write("\u014e\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2")
        buf.write("\u0151\u0152\3\2\2\2\u0152\u0154\3\2\2\2\u0153\u0151\3")
        buf.write("\2\2\2\u0154\u0155\7\26\2\2\u0155\u0156\7>\2\2\u0156=")
        buf.write("\3\2\2\2\u0157\u015b\7\23\2\2\u0158\u015a\5\26\f\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u015b\3")
        buf.write("\2\2\2\u015e\u015f\7\25\2\2\u015f\u0160\5J&\2\u0160\u0161")
        buf.write("\7\24\2\2\u0161\u0162\7>\2\2\u0162?\3\2\2\2\u0163\u0164")
        buf.write("\7\30\2\2\u0164\u0165\7;\2\2\u0165A\3\2\2\2\u0166\u0167")
        buf.write("\7\31\2\2\u0167\u0168\7;\2\2\u0168C\3\2\2\2\u0169\u016d")
        buf.write("\7\27\2\2\u016a\u016e\5\60\31\2\u016b\u016e\5d\63\2\u016c")
        buf.write("\u016e\5J&\2\u016d\u016a\3\2\2\2\u016d\u016b\3\2\2\2\u016d")
        buf.write("\u016c\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0170\7;\2\2\u0170E\3\2\2\2\u0171\u0172\7A\2\2")
        buf.write("\u0172\u0181\7\65\2\2\u0173\u0176\5J&\2\u0174\u0176\5")
        buf.write("\16\b\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("\u017e\3\2\2\2\u0177\u017a\7=\2\2\u0178\u017b\5J&\2\u0179")
        buf.write("\u017b\5\16\b\2\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2")
        buf.write("\2\u017b\u017d\3\2\2\2\u017c\u0177\3\2\2\2\u017d\u0180")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0175\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\7")
        buf.write("\66\2\2\u0184G\3\2\2\2\u0185\u0186\5F$\2\u0186\u0187\7")
        buf.write(";\2\2\u0187I\3\2\2\2\u0188\u0189\5L\'\2\u0189\u018a\7")
        buf.write("\3\2\2\u018a\u018b\5L\'\2\u018b\u018e\3\2\2\2\u018c\u018e")
        buf.write("\5L\'\2\u018d\u0188\3\2\2\2\u018d\u018c\3\2\2\2\u018e")
        buf.write("K\3\2\2\2\u018f\u0190\b\'\1\2\u0190\u0191\5N(\2\u0191")
        buf.write("\u0197\3\2\2\2\u0192\u0193\f\4\2\2\u0193\u0194\t\2\2\2")
        buf.write("\u0194\u0196\5N(\2\u0195\u0192\3\2\2\2\u0196\u0199\3\2")
        buf.write("\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198M\3")
        buf.write("\2\2\2\u0199\u0197\3\2\2\2\u019a\u019b\b(\1\2\u019b\u019c")
        buf.write("\5P)\2\u019c\u01a2\3\2\2\2\u019d\u019e\f\4\2\2\u019e\u019f")
        buf.write("\t\3\2\2\u019f\u01a1\5P)\2\u01a0\u019d\3\2\2\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("O\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a6\b)\1\2\u01a6")
        buf.write("\u01a7\5R*\2\u01a7\u01ad\3\2\2\2\u01a8\u01a9\f\4\2\2\u01a9")
        buf.write("\u01aa\t\4\2\2\u01aa\u01ac\5R*\2\u01ab\u01a8\3\2\2\2\u01ac")
        buf.write("\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01aeQ\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\7\35\2")
        buf.write("\2\u01b1\u01b4\5R*\2\u01b2\u01b4\5T+\2\u01b3\u01b0\3\2")
        buf.write("\2\2\u01b3\u01b2\3\2\2\2\u01b4S\3\2\2\2\u01b5\u01b6\t")
        buf.write("\5\2\2\u01b6\u01b9\5T+\2\u01b7\u01b9\5V,\2\u01b8\u01b5")
        buf.write("\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9U\3\2\2\2\u01ba\u01bb")
        buf.write("\b,\1\2\u01bb\u01bc\5Z.\2\u01bc\u01c1\3\2\2\2\u01bd\u01be")
        buf.write("\f\4\2\2\u01be\u01c0\5X-\2\u01bf\u01bd\3\2\2\2\u01c0\u01c3")
        buf.write("\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("W\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\79\2\2\u01c5")
        buf.write("\u01c6\5J&\2\u01c6\u01c7\7:\2\2\u01c7Y\3\2\2\2\u01c8\u01c9")
        buf.write("\7\65\2\2\u01c9\u01ca\5J&\2\u01ca\u01cb\7\66\2\2\u01cb")
        buf.write("\u01db\3\2\2\2\u01cc\u01db\5F$\2\u01cd\u01db\5d\63\2\u01ce")
        buf.write("\u01cf\7\67\2\2\u01cf\u01d4\5J&\2\u01d0\u01d1\7=\2\2\u01d1")
        buf.write("\u01d3\5J&\2\u01d2\u01d0\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2")
        buf.write("\u01d6\u01d4\3\2\2\2\u01d7\u01d8\78\2\2\u01d8\u01db\3")
        buf.write("\2\2\2\u01d9\u01db\7A\2\2\u01da\u01c8\3\2\2\2\u01da\u01cc")
        buf.write("\3\2\2\2\u01da\u01cd\3\2\2\2\u01da\u01ce\3\2\2\2\u01da")
        buf.write("\u01d9\3\2\2\2\u01db[\3\2\2\2\u01dc\u01dd\t\6\2\2\u01dd")
        buf.write("]\3\2\2\2\u01de\u01df\7?\2\2\u01df_\3\2\2\2\u01e0\u01e1")
        buf.write("\7@\2\2\u01e1a\3\2\2\2\u01e2\u01e3\7E\2\2\u01e3c\3\2\2")
        buf.write("\2\u01e4\u01e9\5^\60\2\u01e5\u01e9\5`\61\2\u01e6\u01e9")
        buf.write("\5b\62\2\u01e7\u01e9\5\\/\2\u01e8\u01e4\3\2\2\2\u01e8")
        buf.write("\u01e5\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e7\3\2\2\2")
        buf.write("\u01e9e\3\2\2\2\63io}\u0084\u0086\u008b\u0093\u0096\u009c")
        buf.write("\u00a4\u00a7\u00ad\u00b1\u00b7\u00c0\u00c7\u00d1\u00d7")
        buf.write("\u00dc\u00df\u00e5\u00f0\u00f9\u00ff\u0103\u010e\u0115")
        buf.write("\u0126\u0130\u0136\u0138\u0140\u0151\u015b\u016d\u0175")
        buf.write("\u017a\u017e\u0181\u018d\u0197\u01a2\u01ad\u01b3\u01b8")
        buf.write("\u01c1\u01d4\u01da\u01e8")
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
    RULE_body = 10
    RULE_stmt = 11
    RULE_stmt_notfunc = 12
    RULE_stmt_spe = 13
    RULE_body_declare = 14
    RULE_assign_stmt = 15
    RULE_assign_part = 16
    RULE_func_declare = 17
    RULE_parameter_func = 18
    RULE_if_stmt = 19
    RULE_elseif_stmt = 20
    RULE_else_stmt = 21
    RULE_for_stmt = 22
    RULE_scalar_var = 23
    RULE_index_var = 24
    RULE_scalar_var_int = 25
    RULE_index_var_int = 26
    RULE_conditionExpr = 27
    RULE_updateExpr = 28
    RULE_while_stmt = 29
    RULE_doWhile_stmt = 30
    RULE_break_stmt = 31
    RULE_continue_stmt = 32
    RULE_return_stmt = 33
    RULE_func_call = 34
    RULE_call_stmt = 35
    RULE_exp = 36
    RULE_exp1 = 37
    RULE_exp2 = 38
    RULE_exp3 = 39
    RULE_exp4 = 40
    RULE_exp5 = 41
    RULE_exp6 = 42
    RULE_op_index = 43
    RULE_operands = 44
    RULE_bool_lit = 45
    RULE_int_lit = 46
    RULE_float_lit = 47
    RULE_string_lit = 48
    RULE_all_lit = 49

    ruleNames =  [ "program", "main", "var_declare", "var_list", "var_normal", 
                   "var_normal_list", "var_vp", "array_cell", "array_lit_cell", 
                   "array_lit", "body", "stmt", "stmt_notfunc", "stmt_spe", 
                   "body_declare", "assign_stmt", "assign_part", "func_declare", 
                   "parameter_func", "if_stmt", "elseif_stmt", "else_stmt", 
                   "for_stmt", "scalar_var", "index_var", "scalar_var_int", 
                   "index_var_int", "conditionExpr", "updateExpr", "while_stmt", 
                   "doWhile_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "func_call", "call_stmt", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "op_index", "operands", "bool_lit", 
                   "int_lit", "float_lit", "string_lit", "all_lit" ]

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
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 100
                self.main()
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.FUNCTION or _la==BKITParser.VAR):
                    break

            self.state = 105
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
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.var_declare()
                pass
            elif token in [BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
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
            self.state = 111
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
            self.state = 113
            self.var_normal()
            self.state = 114
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
            self.state = 116
            self.match(BKITParser.VAR)
            self.state = 117
            self.match(BKITParser.COLON)
            self.state = 118
            self.var_normal_list()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 119
                self.match(BKITParser.COMMA)
                self.state = 120
                self.var_normal_list()
                self.state = 125
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
            self.state = 126
            self.scalar_var_int()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.EQ:
                self.state = 127
                self.match(BKITParser.EQ)
                self.state = 130
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.LCB]:
                    self.state = 128
                    self.array_lit()
                    pass
                elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                    self.state = 129
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
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.array_cell()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.scalar_var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
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
            self.state = 139
            self.match(BKITParser.LCB)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 140
                self.var_vp()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 141
                    self.match(BKITParser.COMMA)
                    self.state = 142
                    self.var_vp()
                    self.state = 147
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 150
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
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.array_lit()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
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
            self.state = 156
            self.match(BKITParser.LCB)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 157
                self.array_lit_cell()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 158
                    self.match(BKITParser.COMMA)
                    self.state = 159
                    self.array_lit_cell()
                    self.state = 164
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 167
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

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def stmt(self):
            return self.getTypedRuleContext(BKITParser.StmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_body)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.var_declare()
                pass
            elif token in [BKITParser.IF, BKITParser.FOR, BKITParser.DO, BKITParser.WHILE, BKITParser.RETURN, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.LCB, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.stmt()
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
        self.enterRule(localctx, 22, self.RULE_stmt)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IF, BKITParser.FOR, BKITParser.DO, BKITParser.WHILE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.stmt_notfunc()
                pass
            elif token in [BKITParser.RETURN, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.LCB, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
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
        self.enterRule(localctx, 24, self.RULE_stmt_notfunc)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.if_stmt()
                pass
            elif token in [BKITParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.for_stmt()
                pass
            elif token in [BKITParser.WHILE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.while_stmt()
                pass
            elif token in [BKITParser.DO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
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
        self.enterRule(localctx, 26, self.RULE_stmt_spe)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.assign_stmt()
                self.state = 184
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.break_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.continue_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
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

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.BodyContext)
            else:
                return self.getTypedRuleContext(BKITParser.BodyContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_body_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_declare" ):
                return visitor.visitBody_declare(self)
            else:
                return visitor.visitChildren(self)




    def body_declare(self):

        localctx = BKITParser.Body_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_body_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(BKITParser.BODY)
            self.state = 193
            self.match(BKITParser.COLON)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 194
                self.body()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self.match(BKITParser.ENDBODY)
            self.state = 201
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
        self.enterRule(localctx, 30, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.assign_part()
            self.state = 204
            self.match(BKITParser.EQ)
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 205
                self.assign_part()
                pass

            elif la_ == 2:
                self.state = 206
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
        self.enterRule(localctx, 32, self.RULE_assign_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 209
                self.scalar_var()
                pass

            elif la_ == 2:
                self.state = 213
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.ID]:
                    self.state = 210
                    self.func_call()
                    pass
                elif token in [BKITParser.STRINGLIT]:
                    self.state = 211
                    self.match(BKITParser.STRINGLIT)
                    pass
                elif token in [BKITParser.LCB]:
                    self.state = 212
                    self.array_cell()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.LSB:
                    self.state = 215
                    self.index_var()
                    self.state = 220
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
        self.enterRule(localctx, 34, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(BKITParser.FUNCTION)
            self.state = 224
            self.match(BKITParser.COLON)
            self.state = 225
            self.match(BKITParser.ID)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 226
                self.parameter_func()


            self.state = 229
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
        self.enterRule(localctx, 36, self.RULE_parameter_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(BKITParser.PARAMETER)
            self.state = 232
            self.match(BKITParser.COLON)
            self.state = 233
            self.scalar_var_int()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 234
                self.match(BKITParser.COMMA)
                self.state = 235
                self.scalar_var_int()
                self.state = 240
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

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.BodyContext)
            else:
                return self.getTypedRuleContext(BKITParser.BodyContext,i)


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
        self.enterRule(localctx, 38, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(BKITParser.IF)
            self.state = 242
            self.exp()
            self.state = 243
            self.match(BKITParser.THEN)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 244
                self.body()
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 250
                self.elseif_stmt()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 256
                self.else_stmt()


            self.state = 259
            self.match(BKITParser.ENDIF)
            self.state = 260
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

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.BodyContext)
            else:
                return self.getTypedRuleContext(BKITParser.BodyContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = BKITParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_elseif_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(BKITParser.ELSEIF)
            self.state = 263
            self.exp()
            self.state = 264
            self.match(BKITParser.THEN)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 265
                self.body()
                self.state = 270
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

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.BodyContext)
            else:
                return self.getTypedRuleContext(BKITParser.BodyContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = BKITParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_else_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(BKITParser.ELSE)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 272
                self.body()
                self.state = 277
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

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.BodyContext)
            else:
                return self.getTypedRuleContext(BKITParser.BodyContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(BKITParser.FOR)
            self.state = 279
            self.match(BKITParser.LP)
            self.state = 280
            self.match(BKITParser.ID)
            self.state = 281
            self.match(BKITParser.EQ)
            self.state = 282
            self.exp()
            self.state = 283
            self.match(BKITParser.COMMA)
            self.state = 284
            self.conditionExpr()
            self.state = 285
            self.match(BKITParser.COMMA)
            self.state = 286
            self.updateExpr()
            self.state = 287
            self.match(BKITParser.RP)
            self.state = 288
            self.match(BKITParser.DO)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 289
                self.body()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
            self.match(BKITParser.ENDFOR)
            self.state = 296
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
        self.enterRule(localctx, 46, self.RULE_scalar_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(BKITParser.ID)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 299
                self.index_var()
                self.state = 304
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
        self.enterRule(localctx, 48, self.RULE_index_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(BKITParser.LSB)
            self.state = 308 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 308
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 306
                    self.scalar_var()
                    pass

                elif la_ == 2:
                    self.state = 307
                    self.exp()
                    pass


                self.state = 310 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0)):
                    break

            self.state = 312
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
        self.enterRule(localctx, 50, self.RULE_scalar_var_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(BKITParser.ID)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 315
                self.index_var_int()
                self.state = 320
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
        self.enterRule(localctx, 52, self.RULE_index_var_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(BKITParser.LSB)
            self.state = 322
            self.match(BKITParser.INTLIT)
            self.state = 323
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
        self.enterRule(localctx, 54, self.RULE_conditionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
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
        self.enterRule(localctx, 56, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
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

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.BodyContext)
            else:
                return self.getTypedRuleContext(BKITParser.BodyContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(BKITParser.WHILE)
            self.state = 330
            self.exp()
            self.state = 331
            self.match(BKITParser.DO)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 332
                self.body()
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 338
            self.match(BKITParser.ENDWHILE)
            self.state = 339
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

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.BodyContext)
            else:
                return self.getTypedRuleContext(BKITParser.BodyContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_doWhile_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhile_stmt" ):
                return visitor.visitDoWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def doWhile_stmt(self):

        localctx = BKITParser.DoWhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_doWhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(BKITParser.DO)
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 342
                    self.body() 
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 348
            self.match(BKITParser.WHILE)
            self.state = 349
            self.exp()
            self.state = 350
            self.match(BKITParser.ENDDO)
            self.state = 351
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
        self.enterRule(localctx, 62, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(BKITParser.BREAK)
            self.state = 354
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
        self.enterRule(localctx, 64, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(BKITParser.CONTINUE)
            self.state = 357
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
        self.enterRule(localctx, 66, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(BKITParser.RETURN)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 360
                self.scalar_var()

            elif la_ == 2:
                self.state = 361
                self.all_lit()

            elif la_ == 3:
                self.state = 362
                self.exp()


            self.state = 365
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
        self.enterRule(localctx, 68, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(BKITParser.ID)
            self.state = 368
            self.match(BKITParser.LP)
            self.state = 383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
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


                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 373
                    self.match(BKITParser.COMMA)
                    self.state = 376
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        self.state = 374
                        self.exp()
                        pass

                    elif la_ == 2:
                        self.state = 375
                        self.var_vp()
                        pass


                    self.state = 382
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 385
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
        self.enterRule(localctx, 70, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.func_call()
            self.state = 388
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
        self.enterRule(localctx, 72, self.RULE_exp)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.exp1(0)
                self.state = 391
                self.match(BKITParser.RELATIONAL)
                self.state = 392
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 402
                    self.exp2(0) 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.SUB) | (1 << BKITParser.ADDDOT) | (1 << BKITParser.SUBDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 413
                    self.exp3(0) 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 422
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 423
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.DIV) | (1 << BKITParser.MOD) | (1 << BKITParser.MULDOT) | (1 << BKITParser.DIVDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 424
                    self.exp4() 
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_exp4)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(BKITParser.NOT)
                self.state = 431
                self.exp4()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUBDOT, BKITParser.LP, BKITParser.LCB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
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
        self.enterRule(localctx, 82, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBDOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.SUBDOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 436
                self.exp5()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LP, BKITParser.LCB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.operands()
            self._ctx.stop = self._input.LT(-1)
            self.state = 447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 443
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 444
                    self.op_index() 
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_op_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(BKITParser.LSB)
            self.state = 451
            self.exp()
            self.state = 452
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
        self.enterRule(localctx, 88, self.RULE_operands)
        self._la = 0 # Token type
        try:
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.match(BKITParser.LP)
                self.state = 455
                self.exp()
                self.state = 456
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 459
                self.all_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 460
                self.match(BKITParser.LCB)
                self.state = 461
                self.exp()
                self.state = 466
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 462
                    self.match(BKITParser.COMMA)
                    self.state = 463
                    self.exp()
                    self.state = 468
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 469
                self.match(BKITParser.RCB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 471
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
        self.enterRule(localctx, 90, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
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
        self.enterRule(localctx, 92, self.RULE_int_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
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
        self.enterRule(localctx, 94, self.RULE_float_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
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
        self.enterRule(localctx, 96, self.RULE_string_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
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
        self.enterRule(localctx, 98, self.RULE_all_lit)
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.int_lit()
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.float_lit()
                pass
            elif token in [BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 484
                self.string_lit()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 485
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
        self._predicates[37] = self.exp1_sempred
        self._predicates[38] = self.exp2_sempred
        self._predicates[39] = self.exp3_sempred
        self._predicates[42] = self.exp6_sempred
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
         




