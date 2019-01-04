date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in G Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key g \major \tempo "Moderato"g'8 d' d'4 g'8 ges' e'4 c' e' d' b8 c' d'4 d'2. \break g'8 a' b'4 g'8 d' ges'4 a' d'' des'' e''8 d'' des''4 d''2. \break d''4 ges''8 e'' d'' c'' b'4 g'8 a' b'4 d'' g''4. d''8 d''4 c''2 \break g'8 a' b'4 d''8 b' c''4 g' e' d' ges'8 e' d'4 b2. }
\new Staff { \clef "bass" \key g \major g4 d d c e e g g d d a8 ges d4 \break g g g d d d des des a d8 a ges a d4 \break a d d g e b d d b d2. \break d4 b d e g g ges d a g d8 b aes4 } >>}\markup{\date}