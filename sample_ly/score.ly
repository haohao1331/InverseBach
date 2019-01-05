date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in B♭ Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key bes \major \tempo "Moderato" \repeat volta 2{bes'4 f'8 ees' d' bes c' d' ees'4 c'8 ees' d' c' bes4 d'8 bes c'2. \break bes'4 f'8 ees' d' f' ees' d' c'4 ees'8 g' f' ees' d'4 bes8 d' g'2. } \break \repeat volta 2{ees''4 bes'4. ees''8 f''4 aes''4. f''8 d''4 bes' d''8 bes' d''4 c''2 \break bes'4 f'8 bes' bes' a' g' c'' c''4 ees''8 g'' f'' g'' a''4 f''8 ees'' d''2. } }
\new Staff { \clef "bass" \key bes \major bes,8 c d ees f4 ees8 f g f ees4 bes,8 c d c bes,4 f c8 a, f,4 \break bes,8 c d c bes,4 c8 d ees f g4 d8 ees f ees d4 ees bes,8 g, ees,4 \break ees8 f g4 g aes,8 bes, c bes, aes,4 bes,8 c d c bes,4 f2. \break bes,8 c d4 d ees ees8 d c bes, a, bes, c bes, a,4 bes, f, bes,, } >>}\markup{\date}