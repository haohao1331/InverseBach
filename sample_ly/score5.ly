date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in G Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key g \major \tempo "Moderato" \repeat volta 2{g'4 d' b8 d' c' d' e' d' c' e' d' g' g'4 b'8 g' a'2. \break g'4 d' b8 d' a b c' b a c' b c' d'4 b8 d' c'2. } \break \repeat volta 2{c''8 g' g'4 c'' a' d''8 a' a' f' g' a' b' d'' g''4 g'' ges''2 \break g'4 d' b8 e' e' ges' g' ges' e' c' d' a a4 d'8 c' b2. } }
\new Staff { \clef "bass" \key g \major g,8 a, b, a, g,4 e8 ges g ges e4 b, b,8 a, g,4 d8 a, ges, a, d,4 \break g,8 a, b, a, g,4 c8 d e d c4 g,8 a, b, a, g,4 c8 g, e, g, c,4 \break c8 d e4 e f f f b,8 a, g, a, b, c d2. \break g,8 a, b, c d4 g, e8 ges g4 ges ges ges g d8 b, g,4 } >>}\markup{\date}