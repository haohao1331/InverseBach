date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in E Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key e \major \tempo "Moderato" \repeat volta 2{e''8 ges'' aes''4 e'' a'' e''8 ees'' des''4 b' e'' b'8 a' b'2. \break e''8 b' b'4 e'' ees'' ges''8 e'' ees''4 des'' ges'' des''8 bes' b'2. } \break \repeat volta 2{b'8 ges' ges'4 b'8 ees'' des'' ees'' e'' ges'' aes'' ges'' e''4 aes'' e'' e'' ees''2 \break e''8 b' b'4 aes' a' e'8 a' a'4 ges' ees' b8 ees' aes'2. } }
\new Staff { \clef "bass" \key e \major e4 b,8 a, aes,4 des des8 ees e4 aes, aes, aes,8 a, b, ges, ees, ges, b,,4 \break e8 ges aes4 aes ges8 e ees e ges4 bes, bes, bes, b, ges, b,, \break b,8 des ees4 ees e8 ees des ees e4 aes,8 ges, e, ges, aes, a, b,2. \break e8 ges aes ges e ees des4 des des ees8 des b, des ees4 e b,8 aes, e,4 } >>}\markup{\date}