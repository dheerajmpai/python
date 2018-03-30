from fractions import gcd
"""P1=27172780977147892526560527068530765473645212174891952721985626883220354100261721834068331769157824392575569521301710045118407987781999493998127997417708087041621440592525055980164546469461545058785727072025659910290799452035326897364999773755224889688962186991286860282972763014607446354450766692284271106562616002486674056667062642570253808482448100707311234322404897621181593157189541005539466869779445906238010983947363843711146513805155014360054236811663970652199452488779120065345813680055799701737519990812659498030879666566855871022405830946828617753031268897566955939456948653203274151868677215934999762983449
P2=27327578620816316185744528694046846973205242929092968061822487374845114416347868976351192879069220879766153551097453082814951113119110568540661057647906810715855034031642477854325614750246385100924875364472341005848752867084449084076084142159070425721598845086328793636596588537157241640332746825811525873403011848157707263882618345289825725668495857584595407359614502193722577262248490550898889515489207450706165801936422797835797861495376471892084449250307311377966491300895431363779478301621053441521168348122576303524173933999956956906778384944279499964214519275963980885841510902675321338661759397337014650192491
Q=23933640657463085802688077306202984660872164501961110571024991428418137322927729112156048164862947070180634212048960170179859760072578885634263010271765338100496612106554975007020849184583943854880703386984290699147227750527974662270350297724508988735818193580320834486630067725341506333263652551334781173174414387064094227582859227495422343219674784753682237118205007609170766789638360518374236882703933401899227920572797034632756688968166997122920760156509925498048561034494449341490395567724631017679841318955009449268689880084146491625796787681535245598917815238587358358932661575856115085249124703317256372536323
N1=650343575571006317565625332438808668959293459226730024364070074139170786870702782439073125245382729629315086005009927787470974247775065186451765650210666813459029351324688426295462570591991001852119980718353287587054103974890720188610988180211994760732559260578746038882115338385090630672172724879103680929808141855981790434905922570620625728265321205689685119439130758391014526908127190201500396576885309009196481908307573956836893329144467442743252923732814827586868522302950972787791450302928804382925732562116126478227224613823474889888958569185843743287116916746785549161879806823581333860858637539215274176728672429995475153684320051431238502191581447115853524513117988670090818449232679354054670039780602756127953118971664623577339728237755654557631718979802111750611685745382555501357264408598686215672494793965717510484627148204190617279804570784982933621007520839417597485719620275038403696975258010613960950400509813810805594505282339739136054094679244108018006860736773956257490793139656893165946774741574329144674195634372292747351300032296809913422622084305937767742519640483889026720586401803855290369039262502660607612424797355695970780535728820788874188898599599398627878055034731577134405750309147542803669600318027
N2=654048446749188385273244680125165382258692192298541908988380898137849782282294013251837692728943807983725397336393341009537692099856708106086220683180652816367685262355037641995842403419003741531763587649522422757656105820270702959078194115516063722681213681928849688967267103639042037374123476432739514656158779902662428344126885851903009004066085963482569690377977108404713136324850715301569870999532414336959864967409595138077722999956894425400465484419515110949974875422939949159916510567175968216308324792615193083195638316505809853278688832512417702343016549003302245425978264339425118661540425797266978302348704944586890748866721070995635262381240906494706004623028794097354457237249738543949849799952666803368347967972876832154147632690542990952449911643763106893504741908948400927800284053651333388946816864858092107502833183815018108488694863258709960740422966070575511479848992366372283129422642216257039731689327648307413765364342599399778940545529594421976431168249493792786742812644685932570777821949220202784721043238378165363021553291810609449359023321907910355400604467708556537928975140357829647237816755536674535794869685549345936106315488738114812517925046441486090379175201141706952313726727694071504537839350593
106.41user 0.00system 1:46.41elapsed 100%CPU (0avgtext+0avgdata 3376maxresident)k
0inputs+0outputs (0major+133minor)pagefaults 0swaps
"""


N1=650343575571006317565625332438808668959293459226730024364070074139170786870702782439073125245382729629315086005009927787470974247775065186451765650210666813459029351324688426295462570591991001852119980718353287587054103974890720188610988180211994760732559260578746038882115338385090630672172724879103680929808141855981790434905922570620625728265321205689685119439130758391014526908127190201500396576885309009196481908307573956836893329144467442743252923732814827586868522302950972787791450302928804382925732562116126478227224613823474889888958569185843743287116916746785549161879806823581333860858637539215274176728672429995475153684320051431238502191581447115853524513117988670090818449232679354054670039780602756127953118971664623577339728237755654557631718979802111750611685745382555501357264408598686215672494793965717510484627148204190617279804570784982933621007520839417597485719620275038403696975258010613960950400509813810805594505282339739136054094679244108018006860736773956257490793139656893165946774741574329144674195634372292747351300032296809913422622084305937767742519640483889026720586401803855290369039262502660607612424797355695970780535728820788874188898599599398627878055034731577134405750309147542803669600318027
N2=654048446749188385273244680125165382258692192298541908988380898137849782282294013251837692728943807983725397336393341009537692099856708106086220683180652816367685262355037641995842403419003741531763587649522422757656105820270702959078194115516063722681213681928849688967267103639042037374123476432739514656158779902662428344126885851903009004066085963482569690377977108404713136324850715301569870999532414336959864967409595138077722999956894425400465484419515110949974875422939949159916510567175968216308324792615193083195638316505809853278688832512417702343016549003302245425978264339425118661540425797266978302348704944586890748866721070995635262381240906494706004623028794097354457237249738543949849799952666803368347967972876832154147632690542990952449911643763106893504741908948400927800284053651333388946816864858092107502833183815018108488694863258709960740422966070575511479848992366372283129422642216257039731689327648307413765364342599399778940545529594421976431168249493792786742812644685932570777821949220202784721043238378165363021553291810609449359023321907910355400604467708556537928975140357829647237816755536674535794869685549345936106315488738114812517925046441486090379175201141706952313726727694071504537839350593
d = gcd(N1,N2);
print (d)
