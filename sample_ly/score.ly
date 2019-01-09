date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in B♭ Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key bes \major \tempo "Moderato" \repeat volta 2{bes'4. d''8 bes'4 g' c''8 d'' ees'' c'' d''4 bes'4. d''8 c''2. \break bes'4. f'8 bes'4 g' bes'8 a' g' c'' c''4 e''4. g''8 f''2. } \break \repeat volta 2{f'8 c' c' f' f' a' g'4 bes'4. g'8 bes' c'' d'' c'' bes'4 bes' a'2 \break bes'4. d''8 bes'4 g' c''8 g' g' c'' a'4 f'4. a'8 bes'2. } }
\new Staff { \clef "bass" \key bes \major bes,4 f,8 ees, d,4 ees ees8 f g4 f8 ees d ees f4 f c f, \break bes,8 c d4 d8 c bes, a, g, a, bes,4 e8 f g f e4 f c8 a, f,4 \break f8 g a4 a bes,8 c d c bes, c d c bes, c d ees f2. \break bes,4 f,8 ees, d,4 ees ees ees f a,8 g, f,4 bes, f,8 d, bes,,4 } >>}\markup{\date}