\version "2.18.2"{
    \relative c'' {
      \new PianoStaff <<
        \new Staff { \time 2/4 c4 e | g g, | c2 | g4 g \break a4 b | c d | d e | f g }
        \new Staff { \clef "bass" c,,4 c' | e c | a b | c d \break a4 b | c d | d e | f g }
      >>
    }
    
}
