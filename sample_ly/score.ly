date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in B♭ Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key bes \major \tempo "Moderato" \repeat volta 2{bes'8 c'' d'' c'' bes' a' g'4 bes'8 c'' d'' c'' bes' f' f' bes' bes' f' a'2. \break bes'8 f' f' bes' bes' c'' d''4 g''8 d'' d'' g'' e'' d'' c'' d'' e'' g'' f''2. } \break \repeat volta 2{f'8 g' a'4 c'' bes'8 c'' d'' c'' bes' c'' d''4 f''8 ees'' d'' bes' d''4 c''2 \break bes'8 c'' d'' ees'' f'' ees'' d''4 g''8 d'' d'' bes' c'' f'' f'' c'' c'' a' bes'2. } }
\new Staff { \clef "bass" \key bes \major bes,4 f,8 ees, d,4 bes,8 c d c bes, c d4 d d8 ees f4 c8 a, f,4 \break bes,8 c d4 d8 c bes,4 bes, bes, c8 d e f g4 f c f, \break f c8 bes, a,4 g,8 a, bes, c d c bes, c d c bes,4 f2. \break bes,4 f,8 ees, d,4 bes, bes, bes, a, a, a, bes,8 f, d, f, bes,,4 } >>}\markup{\date}