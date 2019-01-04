date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in E Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key e \major \tempo "Moderato" \repeat volta 2{e''8 ges'' aes''4 e'' a'' e''8 ees'' des''4 e'' b' e''8 b' ees''2. \break e''8 ges'' aes''4 e'' ges'' a''8 aes'' ges''4 e'' aes'' e''8 ees'' des''2. } \break \repeat volta 2{a'4 des'' e''8 a'' ges'' e'' d''4 b'8 e'' e''4 b'8 a' aes'4 aes' ges'2 \break e''8 ges'' aes''4 e'' des'' a'8 e' e'4 ees' ges' ees'8 ges' e'2. } }
\new Staff { \clef "bass" \key e \major e4 b, aes, des des a, aes, aes, aes, b, ges,8 ees, b,,4 \break e b, aes, a, ges, a, aes, b, aes, a8 e des e a,4 \break a, e, des, d ges d aes, aes, b, b,2. \break e4 e aes e des des b, ees ges e b, e, } >>}\markup{\date}