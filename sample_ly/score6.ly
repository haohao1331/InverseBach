date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
title = "Menuet in G♭ Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key ges \major \tempo "Moderato" \repeat volta 2{ges'4. bes'8 des''4 bes' ees''8 f'' ges'' des'' des''4 bes' des'' des''2. \break ges'4. des'8 bes4 ees' aes'8 bes' b' aes' bes'4 ges' bes' b'2. } \break \repeat volta 2{b'4 ees''8 des'' b'4 des'' e'' aes''8 e'' ges'' des'' des''4 bes' bes' aes'2 \break ges'4. des'8 bes4 ees' bes8 ees' ees' ges' f'4 aes' des'' bes'2. } }
\new Staff { \clef "bass" \key ges \major ges4 ges bes, ges ges8 f ees4 bes,8 aes, ges, aes, bes, b, des4 aes, des, \break ges bes,8 b, des4 b, b,8 bes, aes,4 des8 b, bes, b, des4 b, ges,8 ees, b,,4 \break b, ges,8 f, ees,4 e8 ees des ees e4 bes, bes,8 aes, ges,4 des2. \break ges4 bes,8 aes, ges,4 ges ges ges aes, f f ges des ges, } >>}\markup{\date}