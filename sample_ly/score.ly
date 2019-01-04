date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in A♭ Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key aes \major \tempo "Moderato"aes'8 bes' c''4 aes'8 bes' c''4 aes' f'8 c' ees'4 c'8 des' ees' f' ees'2. \break aes'8 ees' ees'4 c'8 ees' bes4 des' f'8 g' aes'4 c''8 des'' ees'' c'' des''2. \break des''4 aes'4. des''8 bes' ees'' ees''4 ges'' aes'' ees''8 aes'' aes''4 aes'' g''2 \break aes'8 ees' ees'4 aes'8 bes' c''4 f'' c''8 aes' bes'4 g'8 aes' bes' g' aes'2. }
\new Staff { \clef "bass" \key aes \major aes,4 aes, c aes, c aes, c ees c ees8 bes, g, bes, ees,4 \break aes, c ees des f des c ees c des aes,8 f, des,4 \break des f f ges ges bes, c c c ees2. \break aes,4 c c aes, aes, aes, g, bes, g, aes ees aes, } >>}\markup{\date}