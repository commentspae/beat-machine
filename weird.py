import beatmachine as bm

a = bm.Beats.from_song('./smashmouth.mp3')
b = bm.Beats.from_song('./lightsoff.mp3')
a.apply(bm.effects.multisong.WeaveBeats(dst_sr=a.sr, other=b)).save('wtf.mp3')
