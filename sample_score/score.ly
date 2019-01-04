date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in D Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key d \major \tempo "Moderato" \repeat volta 2{d''8 e'' ges'' e'' d'' des'' b'4. d''8 b'4 a' ges'8 e' d' a des'2. \break d''8 a' a' d'' d'' des'' b'4. g'8 d'4 ges' a'8 g' ges' a' g'2. } \break \repeat volta 2{g'4. b'8 d''4 c'' a'4. c''8 d'' a' a' d'' d'' a' d''4 des''2 \break d''8 a' a' g' ges' b' b'4. d''8 ges''4 a'' e''8 a'' a'' g'' ges''2. } }
\new Staff { \clef "bass" \key d \major d4 d8 e ges e d e ges e d e ges e d e ges g a4 e a, \break d8 e ges4 ges8 e d des b,4 b,8 des d e ges g a4 g8 d b, d g,4 \break g, d,8 des, b,,4 a,8 b, c b, a,4 ges ges ges8 g a2. \break d8 e ges e d4 d8 e ges e d4 des des des d a, d, } >>}\markup{\date}