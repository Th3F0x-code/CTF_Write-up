require 'json'

n, e, cf = 0, 0, 0
File.open("pubkey.json") do |f|
  hash = JSON.load(f)
  n = hash["n"].to_i
  e = hash["e"].to_i
  cf = hash["cf"].to_i
end
d = n
n = nil

enc = 17320751473362084127402636657144071375427833219607663443601124449781249403644322557541872089652267070211212915903557690040206709235417332498271540915493529128300376560226137139676145984352993170584208658625255938806836396696141456961179529532070976247738546045494839964768476955634323305122778089058798906645471526156569091101098698045293624474978286797899191202843389249922173166570341752053592397746313995966365207638042347023262633148306194888008613632757146845037310325643855138147271259215908333877374609302786041209284422691820450450982123612630485471082506484250009427242444806889873164459216407213750735305784

for k in 1...100000
  next if (d*e-1)%k != 0
  phi = (d*e-1)/k
  next if phi.to_s(2).length > 2050

  kn = cf*phi - cf + 1
  next if kn <= 0

  # recover p
  keyp = kn
  for m in 2...10
    keyp = keyp.gcd(m.pow(phi,keyp) - 1)
  end
  next if keyp.to_s(2).length != 1024

  # recover q
  next if phi % (keyp-1) != 0
  keyq = phi / (keyp-1) + 1

  # recover n
  keyn = keyp * keyq

 #puts keyn
  flag = enc.pow(d, keyn)
  flaghex = flag.to_s(16)
  flaghex = "0" + flaghex if flaghex.length % 2 == 1
  puts [flaghex].pack("H*")
end
# FLAG --> TSGCTF{Okay_this_flag_will_be_quite_long_so_listen_carefully_Happiness_is_our_bodys_default_setting_Please_dont_feel_SAd_in_all_sense_Be_happy!_Anyway_this_challenge_is_simple_rewrite_of_HITCON_CTF_2019_Lost_Modulus_Again_so_Im_very_thankful_to_the_author}
