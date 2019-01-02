date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in D Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key d \major \tempo "Moderato" \repeat volta 2{d''4 ges'' d''8 ges'' e''4 g'' e''8 b' d'' a' a'4 ges' e'2. \break d''4 a' ges'8 g' a'4 e' a'8 des'' b' e'' e''4 aes'' a''2. } \break \repeat volta 2{a'8 b' des'' b' a'4 b'8 ges' ges'4 b' a' ges' d' des' b2 \break d''4 ges'' d''8 des'' b'4 g' e'8 a' a' b' des''4 e'' d''2. } }
\new Staff { \clef "bass" \key d \major d2. e d a \break d a e a \break a b d d \break d e a d } >>}\markup{\date}