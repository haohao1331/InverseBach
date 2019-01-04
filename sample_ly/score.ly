date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
<<<<<<< HEAD
title = "Menuet in C Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key c \major \tempo "Moderato"c''8 d'' e'' d'' c''4 a'8 d'' d''4 a'8 b' c'' g' g'4 c''8 e'' d''2. \break c''8 g' g' c'' c''4 b'8 c'' d''4 g''8 d'' a'' g'' ges''4 d''8 c'' b'2. \break g'4 b'8 a' g'4 e' a' c'' e'' c''8 d'' e'' c'' e''4 d''2 \break c''8 d'' e'' d'' c''4 d''8 a' a'4 d''8 c'' b' a' g'4 b'8 d'' c''2. }
\new Staff { \clef "bass" \key c \major c4 c e f f f e e e g d g, \break c e e g, b, b, ges a ges g8 d b, d g,4 \break g, d, b,, c c a, g, e c g2. \break c4 c e f f f d b, d c8 g, e, g, c,4 } >>}\markup{\date}
=======
title = "Menuet in D Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key d \major \tempo "Moderato" \repeat volta 2{d''4 ges'' d''8 ges'' e''4 g'' e''8 b' d'' a' a'4 ges' e'2. \break d''4 a' ges'8 g' a'4 e' a'8 des'' b' e'' e''4 aes'' a''2. } \break \repeat volta 2{a'8 b' des'' b' a'4 b'8 ges' ges'4 b' a' ges' d' des' b2 \break d''4 ges'' d''8 des'' b'4 g' e'8 a' a' b' des''4 e'' d''2. } }
\new Staff { \clef "bass" \key d \major d2. e d a \break d a e a \break a b d d \break d e a d } >>}\markup{\date}
>>>>>>> 876d9c11151a1130cd1ec050677e00f0f6a73f59
