from Crypto.Util.number import *

ps = '9 259086 589771 420433 × 9 432696 100372 252597 × 9 905427 204516 677719 × 10 742738 836573 593721 × 10 877171 163758 298473 × 10 883245 204809 972317 × 11 387559 472005 576439 × 12 361513 190006 588813 × 13 008299 345314 386241 × 13 137124 577721 543913 × 14 444818 318379 665457 × 15 197175 261867 744269 × 15 313323 964021 172371 × 16 259675 972299 142689 × 16 659580 147621 910407 × 17 447808 094538 811767'
ps = ps.split(' × ')

phi = 1
ps = [el.replace(' ', '') for el in ps]

for el in ps:
    phi *= int(el) - 1

d = inverse(65537, phi)
c = 301134324702979101601229980817712305679459272403009847977905797426967147301009753074163263516519121214477239813381651880610545484766224816075639817078022502740923937485967968414814571266684481074873719521522276878916473424098420305091570571671905697759107642819692889627538051932664261696505877765760765011
n = 420485447340750276798905009197900250076472236951029771396372239960455176076395356078018304176360377601355361640360458283456532642841066439541542468492600074303505516012322941130021941063141150150454719702821666531692873286236281808915376205692263441233138891193279355717503716920577044748917446320341294227

print(long_to_bytes(pow(c, d, n)))
# b'CCIT{more_primes=more_security}'
