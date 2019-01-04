date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in D♭ Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key des \major \tempo "Moderato" \repeat volta 2{des''4 aes'8 des'' des''4 bes' ges'8 des' des' ees' f' ees' des'4 f' ees'2. \break des''4 f''8 ees'' des''4 bes' ges'8 des' des' ees' f' ees' des'4 f' ges'2. } \break \repeat volta 2{ges'4 des' bes8 des' b des' ees'4 aes'8 des'' des''4 f''8 ees'' des'' aes' des''4 c''2 \break des''4 aes'8 des'' des''4 bes' des''8 c'' bes' des'' c'' bes' aes'4 c'' des''2. } }
\new Staff { \clef "bass" \key des \major des8 ees f4 f ges bes, bes, aes, f8 ees des4 aes8 ees c ees aes,4 \break des aes,8 ges, f,4 des8 c bes,4 bes, aes, f8 ges aes4 ges8 des bes, des ges,4 \break ges bes,8 aes, ges,4 ees8 des b,4 b, f8 ges aes ges f4 ges8 aes2. \break des8 ees f4 f ges bes,8 aes, ges,4 aes,8 bes, c4 bes,8 aes,4 des aes,8 f, des,4 } >>}\markup{\date}