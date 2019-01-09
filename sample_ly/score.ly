date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in A♭ Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key aes \major \tempo "Moderato" \repeat volta 2{aes'8 bes' c'' des'' ees'' des'' c''4 aes'8 bes' c''4 ees''8 aes'' aes''4 ees'' ees''2. \break aes'8 bes' c'' bes' aes' des'' des''4 f''8 ees'' des''4 c''8 des'' ees''4 aes'' f''2. } \break \repeat volta 2{des''4 f'' des'' ees'' bes'8 aes' ges'4 ees'4. aes'8 c'4 c' bes2 \break aes'8 bes' c'' bes' aes' bes' c''4 f''8 g'' aes''4 g''8 f'' ees''4 bes' aes'2. } }
\new Staff { \clef "bass" \key aes \major aes,4 ees,8 des, c,4 aes,8 bes, c bes, aes, bes, c4 c c8 des ees4 bes,8 g, ees,4 \break aes, ees,8 des, c,4 f8 g aes g f4 aes,8 bes, c4 c des aes,8 f, des,4 \break des des8 ees f4 ges ges bes, c c8 des ees4 ees2. \break aes,4 aes,8 bes, c bes, aes,4 aes,8 g, f,4 bes,8 aes, g,4 g, aes8 ees c ees aes,4 } >>}\markup{\date}