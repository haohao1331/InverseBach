date = #(strftime "%d-%m-%Y" (localtime (current-time)))
\header{
<<<<<<< HEAD
title = "Menuet in A♭ Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key aes \major \tempo "Moderato"aes'8 bes' c''4 aes'8 bes' c''4 aes' f'8 c' ees'4 c'8 des' ees' f' ees'2. \break aes'8 ees' ees'4 c'8 ees' bes4 des' f'8 g' aes'4 c''8 des'' ees'' c'' des''2. \break des''4 aes'4. des''8 bes' ees'' ees''4 ges'' aes'' ees''8 aes'' aes''4 aes'' g''2 \break aes'8 ees' ees'4 aes'8 bes' c''4 f'' c''8 aes' bes'4 g'8 aes' bes' g' aes'2. }
\new Staff { \clef "bass" \key aes \major aes,4 aes, c aes, c aes, c ees c ees8 bes, g, bes, ees,4 \break aes, c ees des f des c ees c des aes,8 f, des,4 \break des f f ges ges bes, c c c ees2. \break aes,4 c c aes, aes, aes, g, bes, g, aes ees aes, } >>}\markup{\date}
=======
title = "Menuet in E Major"
composer = "I. S. baCh"}
\version "2.18.2"{\new PianoStaff 
<< \new Staff { \time 3/4 \clef "treble" \key e \major \tempo "Moderato" \repeat volta 2{e''8 ges'' aes''4 e'' a'' e''8 ees'' des''4 e'' b' e''8 b' ees''2. \break e''8 ges'' aes''4 e'' ges'' a''8 aes'' ges''4 e'' aes'' e''8 ees'' des''2. } \break \repeat volta 2{a'4 des'' e''8 a'' ges'' e'' d''4 b'8 e'' e''4 b'8 a' aes'4 aes' ges'2 \break e''8 ges'' aes''4 e'' des'' a'8 e' e'4 ees' ges' ees'8 ges' e'2. } }
\new Staff { \clef "bass" \key e \major e4 b, aes, des des a, aes, aes, aes, b, ges,8 ees, b,,4 \break e b, aes, a, ges, a, aes, b, aes, a8 e des e a,4 \break a, e, des, d ges d aes, aes, b, b,2. \break e4 e aes e des des b, ees ges e b, e, } >>}\markup{\date}
>>>>>>> aa876578e8bd1ec2f042fb0685f64498a5e298b0
