date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in B Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key b \major ges'4 ges'8 e' ees'4 aes' aes'8 ges' e'4 ges' ges'8 e' ees' e' ges'2. \break ees'8 e' ges' e' ees'4 e' b' e' ees' ees'8 des' b'4 e'2. \break e'8 ges' aes' a' b'4 ges' ges' des' ges'8 e' ees' des' b'4 b' bes'2 \break ges'4 ges' b' e'8 ges' aes'4 des' bes'8 b' des'4 des' b'2. }
\new Staff { \clef "bass" \key b \major b2. des b ges \break b e b e \break e ges b b \break b des ges b } >>}\markup{\date}