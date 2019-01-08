date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in A Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key a \major \tempo "Moderato" \repeat volta 2{a'8 b' des''4 e'' ges'' d''4. ges''8 e''4 des'' e'' e''2. \break a'8 e' e'4 des' a des'4. ges'8 ees'4 b ees' e'2. } \break \repeat volta 2{e''4 aes''8 ges'' e''4 ges''8 aes'' a'' aes'' ges'' aes'' a'' e'' e''4 a'' a'' aes''2 \break a'8 e' e'4 a' ges' d'4. b8 e'4 aes' b' a'2. } }
\new Staff { \clef "bass" \key a \major a,4 a,8 b, des4 d8 des b, des d4 des8 d e d des d e4 b, e, \break a,8 b, des d e d des b, a,4 a, ges8 e ees des b,4 e b,8 aes, e,4 \break e e8 ges aes4 a,8 b, des b, a, b, des4 des des8 d e2. \break a,8 b, des4 des d8 des b, des d4 aes,8 a, b, a, aes,4 a8 e des e a,4 } >>}\markup{\date}