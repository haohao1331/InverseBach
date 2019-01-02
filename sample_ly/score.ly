date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in C Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key c \major c''4. g'8 c''4 d''8 a' a'4 d''8 a' c'' d'' e'' d'' c'' e'' d''2. \break c''4. e''8 g''4 a''8 g'' f''4 c''8 d'' e'' d'' c'' g' g' e' f'2. \break f'4 a'8 b' c''4 d''8 c'' bes' c'' d'' g'' e''4 c'' e'' d'' c''2 \break c''4. e''8 g''4 a''8 g'' f''4 a''8 f'' g'' d'' d'' g'' g'' f'' e''2. }
\new Staff { \clef "bass" \key c \major c2. d c g \break c f c f \break f g c c \break c d g c } >>}\markup{\date}