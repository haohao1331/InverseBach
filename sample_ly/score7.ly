date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in B Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key b \major \tempo "Moderato" \repeat volta 2{b'4. ees''8 b'4 e''4. aes''8 e''4 ees''4. ges''8 ees''4 des''2. \break b'4. ees''8 ges''4 e''4. des''8 e''4 ges''4. ees''8 b'4 aes'2. } \break \repeat volta 2{e''8 b' b' bes' aes'4 a'8 aes' ges'4 a'8 des'' b' ges' ges'4 ees' ees' des'2 \break b'4. ees''8 b'4 e''4. b'8 aes'4 ges'4. des'8 ges'4 ees'2. } }
\new Staff { \clef "bass" \key b \major b,4 ges,8 e, ees,4 aes,8 ges, e, ges, aes, bes, b, des ees des b,4 ges des ges, \break b, b,8 des ees4 des8 ees e ees des4 ees8 e ges e ees4 e b,8 aes, e,4 \break e8 ges aes4 b, ges a,8 b, des4 ees ees8 e ges4 ges2. \break b,4 ges,8 e, ees,4 aes, aes,8 bes, b,4 bes, bes, bes, b, ges,8 ees, b,,4 } >>}\markup{\date}