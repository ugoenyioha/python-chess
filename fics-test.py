import chess.pgn
from io import StringIO

pgn = StringIO("""\
[Event "FICS rated blitz game"]
[Site "FICS freechess.org"]
[FICSGamesDBGameNo "411189932"]
[White "Helmsman"]
[Black "AntaresLight"]
[WhiteElo "1583"]
[BlackElo "1577"]
[WhiteRD "18.5"]
[BlackRD "25.7"]
[TimeControl "180+0"]
[Date "2017.02.07"]
[Time "12:24:00"]
[WhiteClock "0:03:00.000"]
[BlackClock "0:03:00.000"]
[ECO "B29"]
[PlyCount "44"]
[Result "0-1"]

1. e4 {[%emt 0.0]} Nf6 {[%emt 0.0]} 2. e5 {[%emt 1.748]} Nd5 {[%emt 0.697]} 3. Nf3 {[%emt 0.802]} c5 {[%emt 1.349]} 4. c4 {[%emt 0.809]} Nb6 {[%emt 0.729]} 5. d4 {[%emt 9.27]} cxd4 {[%emt 1.593]} 6. Nxd4 {[%emt 2.239]} Nc6 {[%emt 0.882]} 7. Bf4 {[%emt 3.774]} d6 {[%emt 5.921]} 8. Nxc6 {[%emt 3.512]} bxc6 {[%emt 0.756]} 9. Nc3 {[%emt 2.793]} Be6 {[%emt 6.416]} 10. b3 {[%emt 4.804]} d5 {[%emt 8.219]} 11. cxd5 {[%emt 2.61]} cxd5 {[%emt 3.719]} 12. Bb5+ {[%emt 3.501]} Bd7 {[%emt 1.82]} 13. e6 {[%emt 3.693]} fxe6 {[%emt 6.182]} 14. Qe2 {[%emt 2.396]} Bxb5 {[%emt 3.097]} 15. Nxb5 {[%emt 2.619]} Rc8 {[%emt 16.832]} 16. Qxe6 {[%emt 3.869]} Qd7 {[%emt 0.808]} 17. Qe5 {[%emt 9.046]} Qxb5 {[%emt 2.379]} 18. Rd1 {[%emt 6.251]} Qb4+ {[%emt 6.457]} 19. Bd2 {[%emt 1.133]} Qe4+ {[%emt 2.026]} 20. Qxe4 {[%emt 0.886]} dxe4 {[%emt 0.696]} 21. O-O {[%emt 0.738]} g6 {[%emt 3.404]} 22. Bc3 {[%emt 1.976]} Rxc3 {[%emt 1.846]} {White resigns} 0-1
""")

game = chess.pgn.read_game(pgn, Visitor=chess.pgn.FicsGameModelCreator)

print(game.variations[0].variations[0].variations[0].emt)
