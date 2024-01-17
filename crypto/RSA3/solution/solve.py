from Crypto.Util.number import long_to_bytes

e=65537
n=14443714790253725712786089188356106173457774497265828845662658315068025063740567164344985217368981545864887712595489610577462146899462511932740054338518181541423045403951619773244764353530062706212461059059501266838536566664084997230441419015793272619106822190467109409376786458148455343468294318203133444541617084176026622000807679207877351340504931595716883217398118834311385892300959872552588417312347480179197561358000012263443487534992099717488140594195633605059351330729386989974924005945142074447108543693623593801475718375241362871646278979328029790287755807043733609471287028030359439496161963840689686436873
c=11367115610583179509391985365458122558216397522503780354308003182871099443125166580641749421813515948596894471682631715538540685843144022242814843987118047689104067902264746004003816421742963145329967385417920809461325181501235727608005201324403165396450055960453921732660706305518228696283683428210217325736296806232109189661008121264454280949315651716385663253556334737692921932094957851136665087007278490218105730138027745515388494392694364792119922545656481128926491416371146864044951347678107627770421209184729552295067035178846144793206995736831255233626411403986640042567872349758710510666702664771475547287669
gift=241042221143194646393579397754767193590126438206905295823785587290817226537086472715055357269241314647582007976691834785912310025990088174409577000578032477478462008582452664371657613884389339495804842144518351167914669187016845422539426776760711111490429772693283621550830865341323751487566770769603352728074

phi = n - gift + 1

d = pow(e, -1, phi)

flag = pow(c, d, n)

print(long_to_bytes(flag))