date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in F Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff {\time 3/4 \clef "treble" \key f \major \tempo "Moderato" f'4. a'8 f'4 bes' d'' bes'8 d'' c''4 a'8 g' f'4 g'2. \break f'4. c'8 f'4 d' g' bes'8 g' a'4 c''8 bes' a'4 bes'2. \break bes'4 d'' f''8 d'' ees''4 c''8 g' g'4 f'8 g' a' g' f'4 e' d'2 \break f'4. a'8 c''4 d'' bes' f'8 d' e'4 g'8 f' e'4 f'2. }
\new Staff { \clef "bass" \key f \major f2. bes f c \break f g f bes \break bes c f f \break f bes c f } >>}\markup{\date}