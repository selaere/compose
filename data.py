# -*- coding: utf-8 -*-
"""
customize this

i recommend Unifont to be able to see all of these weird characters
"""

custom_dia: dict[str, tuple[str, str]] = {
    "STROKE": ("ГгКкОоРрХхҮүҞҟϱρ" "DdHhLlTtBbIiOZz2GgUuJjRrYyȷoʃʔʕʙıɩpᴜʊPꜸꜹKkꝂꝃƟɵⱣᵽQqÞþCcFfɑeꭎ",
               "ҒғҞҟӨөҎҏӾӿҰұԞԟϼϼ" "ĐđĦħŁłŦŧɃƀƗɨƟƵƶƻǤǥɄʉɈɉɌɍɎɏɟɵʄʡʢᴃᵻᵼᵽᵾᵿⱣꜺꜻꝀꝁꝄꝅꝊꝋꝐꝑꝖꝗꝤꝥꞒꞓꞘꞙꬰꬳꭏ"),
    "STROKE2": ("BbDdlLȽƚÞþКкЧч", "ƂƃƋƌƚȽⱠⱡꝦꝧҜҝҸҹ"),
    "OBLIQUESTROKE": ("GgKkNnRrSs", "ꞠꞡꞢꞣꞤꞥꞦꞧꞨꞩ"),
    "SLASH": ("OoACcTEeatKkQqVvUuþɔ",
              "ØøȺȻȼȾɆɇⱥⱦꝂꝃꝘꝙꝞꝟꞸꞹᵺꬿ"),
    "ASCENDER": ("ГгBbCcDdGgKkPpRTtYydɖhꜧɢqHʈ",
                 "ҐґƁɓƇƈƊɗƓɠƘƙƤƥƦƬƭƳƴɗᶑɦɧʛʠꞪ𝼉"),
    "DESCENDER": ("ЙйЛлМмНнҒғХxЗзСсӅӆ" "mFfQqdnrszltƭTʮɯɹaɗeɛɜəiɔʃuʒRMHhɬʀꭓꭗɮɺǃʤɨoʧc",
                  "ҊҋӅӆӍӎӉӊӺӻӼӽҘҙҪҫԒԓ" "ɱƑƒɊɋɖɳɽʂʐɭʈ𝼉ƮʯɰɻᶏᶑᶒᶓᶔᶕᶖᶗᶘᶙᶚⱤⱮꜦꜧꞎꭆꭕꭙ𝼅𝼈𝼊𝼙𝼚𝼛𝼜𝼝"),
    "PALATAL": ("tbdfgklmnprsʃvxzchCSZʤɬŋɹɾʧʒ",
                "ƫᶀᶁᶂᶃᶄᶅᶆᶇᶈᶉᶊᶋᶌᶍᶎꞔꞕꟄꟅꟆ𝼒𝼓𝼔𝼕𝼖𝼗𝼘"),
    "MOLODSTOVPALATAL": ("ԀԁЗзЛлНнТт", "ԂԃԄԅԈԉԊԋԎԏ"),
    "CYRDESCENDER": ("ГгҼҽЖжКкНнПпТтХхЧчЗзҺһЛл" "HhKkZzNn",
                     "ӶӷҾҿҖҗҚқҢңԤԥҬҭҲҳҶҷԆԇԦԧԮԯ" "ⱧⱨⱩⱪⱫⱬꞐꞑ"),
    "FLIPPED": ("∈∉∊∼≒≔¬⊂⊏⊆⊑" "!?‽23ẟEeʒƷɘvVɾaɑɛhrʀʃtwyʔkæœgFfAⱭᵋɽᴇᵹꝽLlHƐKTⱵⱶmℲPMɞꭐ&YGιΩᵷɡⱵⱶʞŋᴋ" "ЗзϲϹͼϾϵ",
                "∋∌∍∽≓≕⌐⊃⊐⊇⊒" "¡¿⸘↊↋ƍƎɘƹƸǝʌɅɿɐɒɜɥɹʁʅʇʍʎʖʞᴂᴔᵷℲɟⱯⱰᵌⱹⱻꝾꝿꞀꞁꞍꞫꞰꞱꟵꟶɯꟻꟼꟽʚꭑ⅋⅄⅁℩℧𝼁𝼁Ꟶꟶ𝼃𝼇𝼐" "ԐԑͻϽͽϿ϶"),
    "SIDEWAYS": ("oɔøuüɯIQ", "ᴑᴒᴓᴝᴞᴟꟷ℺"),
    "SMALLCAPS": ("ginrybhlœaæcdðđɖejkłmoȣɔptuvwzʒfsqγλπρψлωɯɬ𝼁Ⅎ",
                  "ɢɪɴʀʏʙʜʟɶᴀᴁᴄᴅᴆᴆᴆᴇᴊᴋᴌᴍᴏᴕᴐᴘᴛᴜᴠᴡᴢᴣꜰꜱꞯᴦᴧᴨᴩᴪᴫꭥꟺ𝼄𝼂ⅎ"),
    "RING": ("dlntcʃzʒjYyvoJgmȵŋrꭈꭋꭓxꭗ𝼋ʇʖʗs",
             "ȡȴȵȶɕʆʑʓʝỾỿⱴⱺꞲꬶꬺꬻꬼꭉꭊꭌꭔꭖꭘ𝼌𝼍𝼎𝼏𝼞"),
    "HOOK": ("ГгКкНнПпЛлӇӈ", "ҔҕӃӄӇӈҦҧԠԡԢԣ"),
    "TILDE": ("lbdfmnprɾstzLɫɹ∧∨∇0|", "ɫᵬᵭᵮᵯᵰᵱᵲᵳᵴᵵᵶⱢꬸꭨ⍱⍲⍫⍬⍭"),
    "LONG": ("sNnrxcɹIɯ", "ſȠƞɼꭗʗɺꟾɰ"),
    "UM": ("dlmnrʀtꝚꝛ", "ꝱꝲꝳꝴꝶꝵꝷꝜꝝ"),
    "INSULAR": ("GgDdFfRrSsTt", "ꝽᵹꝹꝺꝻꝼꞂꞃꞄꞅꞆꞇ"),
    "QUAD": (" =÷⋄∘○/\\<>←→∨∆↑∧∇↓':≠?", "⎕⌸⌹⌺⌻⌼⍁⍂⍃⍄⍇⍈⍌⍍⍐⍓⍔⍗⍞⍠⍯⍰"),
    "UNDERBAR": ("⊥⍺α∈ι⍳ω⍵'∆⋄∘○=≠;/\\,", "⍊⍶⍶⍷⍸⍸⍹⍹⍘⍙⍚⍛⍜≡≢⍮⌿⍀⍪"),
    "CIRCLED": ("⊕⊖⊖⊗⊘⊙⊚⊛⊛⊜⊝⎊⚇", "+-−×/·∘*⋆=-∇¨"),
    "DIAERESIS": ("⊤∇*⋆∘○~>", "⍡⍢⍣⍣⍤⍥⍨⍩"),

    # no these dont decompose. i dont know either
    "GLOTTAL": ("AaIiUu", "ꞺꞻꞼꞽꞾꞿ"),

    # ά GREEK SMALL LETTER ALPHA WITH TONOS and
    # ά GREEK SMALL LETTER ALPHA WITH OXIA are encoded differently but decompose to the same
    # sequence α + ◌́ for ??? reasons
    "OXIA": ("αεηιουωΑΕΗϊΙϋΥΟΩ¨", "άέήίόύώΆΈΉΐΊΰΎΌΏ΅"),

    # i dont think there's any way of automating this
    "BOLD": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡϴΣΤΥΦΧΨΩ∇αβγδεζηθικλμνξοπρςστυφχψω∂ϵϑϰϕϱϖϜϝ0123456789",
             "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝚨𝚩𝚪𝚫𝚬𝚭𝚮𝚯𝚰𝚱𝚲𝚳𝚴𝚵𝚶𝚷𝚸𝚹𝚺𝚻𝚼𝚽𝚾𝚿𝛀𝛁𝛂𝛃𝛄𝛅𝛆𝛇𝛈𝛉𝛊𝛋𝛌𝛍𝛎𝛏𝛐𝛑𝛒𝛓𝛔𝛕𝛖𝛗𝛘𝛙𝛚𝛛𝛜𝛝𝛞𝛟𝛠𝛡𝟊𝟋𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"),
    "ITALIC": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡϴΣΤΥΦΧΨΩ∇αβγδεζηθικλμνξοπρςστυφχψω∂ϵϑϰϕϱϖıȷ",
               "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝛢𝛣𝛤𝛥𝛦𝛧𝛨𝛩𝛪𝛫𝛬𝛭𝛮𝛯𝛰𝛱𝛲𝛳𝛴𝛵𝛶𝛷𝛸𝛹𝛺𝛻𝛼𝛽𝛾𝛿𝜀𝜁𝜂𝜃𝜄𝜅𝜆𝜇𝜈𝜉𝜊𝜋𝜌𝜍𝜎𝜏𝜐𝜑𝜒𝜓𝜔𝜕𝜖𝜗𝜘𝜙𝜚𝜛𝚤𝚥"),
    "BOLD_ITALIC": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡϴΣΤΥΦΧΨΩ∇αβγδεζηθικλμνξοπρςστυφχψω∂ϵϑϰϕϱϖ",
                    "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝜜𝜝𝜞𝜟𝜠𝜡𝜢𝜣𝜤𝜥𝜦𝜧𝜨𝜩𝜪𝜫𝜬𝜭𝜮𝜯𝜰𝜱𝜲𝜳𝜴𝜵𝜶𝜷𝜸𝜹𝜺𝜻𝜼𝜽𝜾𝜿𝝀𝝁𝝂𝝃𝝄𝝅𝝆𝝇𝝈𝝉𝝊𝝋𝝌𝝍𝝎𝝏𝝐𝝑𝝒𝝓𝝔𝝕"),
    "SANS": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
             "𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"),
    "SANS_BOLD": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡϴΣΤΥΦΧΨΩ∇αβγδεζηθικλμνξοπρςστυφχψω∂ϵϑϰϕϱϖ0123456789",
                  "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝝖𝝗𝝘𝝙𝝚𝝛𝝜𝝝𝝞𝝟𝝠𝝡𝝢𝝣𝝤𝝥𝝦𝝧𝝨𝝩𝝪𝝫𝝬𝝭𝝮𝝯𝝰𝝱𝝲𝝳𝝴𝝵𝝶𝝷𝝸𝝹𝝺𝝻𝝼𝝽𝝾𝝿𝞀𝞁𝞂𝞃𝞄𝞅𝞆𝞇𝞈𝞉𝞊𝞋𝞌𝞍𝞎𝞏𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"),
    "SANS_ITALIC": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                    "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"),
    "SANS_BOLD_ITALIC": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡϴΣΤΥΦΧΨΩ∇αβγδεζηθικλμνξοπρςστυφχψω∂ϵϑϰϕϱϖ",
                         "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝞐𝞑𝞒𝞓𝞔𝞕𝞖𝞗𝞘𝞙𝞚𝞛𝞜𝞝𝞞𝞟𝞠𝞡𝞢𝞣𝞤𝞥𝞦𝞧𝞨𝞩𝞪𝞫𝞬𝞭𝞮𝞯𝞰𝞱𝞲𝞳𝞴𝞵𝞶𝞷𝞸𝞹𝞺𝞻𝞼𝞽𝞾𝞿𝟀𝟁𝟂𝟃𝟄𝟅𝟆𝟇𝟈𝟉"),
    "SCRIPT": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
               "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"),
    "SCRIPT_BOLD": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                    "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"),
    "FRAKTUR": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"),
    "FRAKTUR_BOLD": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                     "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"),
    "MONO": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
             "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"),
    "DOUBLE": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789πγΓΠ∏∑",
               "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡ℼℽℾℿℿ⅀"),
}

diacritics: dict[str, str] = {
    # generated by canonical decomposition. also generates a sequence for the combining character
    "◌̀": "`",     # COMBINING GRAVE ACCENT
    "◌́": "´",     # COMBINING ACUTE ACCENT
    "◌̂": "^",     # COMBINING CIRCUMFLEX ACCENT
    "◌̃": "ñ",     # COMBINING TILDE
    "◌̄": "-",     # COMBINING MACRON
    "◌̅": "¿-",    # COMBINING OVERLINE
    "◌̆": "]",     # COMBINING BREVE
    "◌̇": ":",     # COMBINING DOT ABOVE
    "◌̈": "¨",     # COMBINING DIAERESIS
    "◌̉": "?",     # COMBINING HOOK ABOVE
    "◌̊": "º",     # COMBINING RING ABOVE
    "◌̋": "´´",    # COMBINING DOUBLE ACUTE ACCENT
    "◌̌": "+",     # COMBINING CARON
    "◌̍": ")-",    # COMBINING VERTICAL LINE ABOVE
    "◌̎": ")--",   # COMBINING DOUBLE VERTICAL LINE ABOVE
    "◌̏": "``",    # COMBINING DOUBLE GRAVE ACCENT
    "◌̐": ":]",    # COMBINING CANDRABINDU
    "◌̑": ")]",    # COMBINING INVERTED BREVE
    "◌̒": "*;",    # COMBINING TURNED COMMA ABOVE
    "◌̓": "*,",    # COMBINING COMMA ABOVE
    "◌̔": "*(,",   # COMBINING REVERSED COMMA ABOVE
    "◌̕": ">'",    # COMBINING COMMA ABOVE RIGHT
    "◌̖": "_`",    # COMBINING GRAVE ACCENT BELOW
    "◌̗": "_´",    # COMBINING ACUTE ACCENT BELOW
    "◌̘": "_←",    # COMBINING LEFT TACK BELOW
    "◌̙": "_→",    # COMBINING RIGHT TACK BELOW
    "◌̚": "nr.",   # COMBINING LEFT ANGLE ABOVE
    "◌̛": "'",     # COMBINING HORN
    "◌̜": "_(",    # COMBINING LEFT HALF RING BELOW
    "◌̝": "_↑",    # COMBINING UP TACK BELOW
    "◌̞": "_↓",    # COMBINING DOWN TACK BELOW
    "◌̟": "adv.",  # COMBINING PLUS SIGN BELOW
    "◌̠": "ret.",  # COMBINING MINUS SIGN BELOW
    "◌̡": "pal.",  # COMBINING PALATALIZED HOOK BELOW
    "◌̢": "rtf.",  # COMBINING RETROFLEX HOOK BELOW
    "◌̣": ".",     # COMBINING DOT BELOW
    "◌̤": "_¨",    # COMBINING DIAERESIS BELOW
    "◌̥": "_º",    # COMBINING RING BELOW
    "◌̦": ",",     # COMBINING COMMA BELOW
    "◌̧": "ç",     # COMBINING CEDILLA
    "◌̨": ";",     # COMBINING OGONEK
    "◌̩": "_|",    # COMBINING VERTICAL LINE BELOW
    "◌̪": "dnt.",  # COMBINING BRIDGE BELOW
    "◌̫": "lbl.",  # COMBINING INVERTED DOUBLE ARCH BELOW
    "◌̬": "_+",    # COMBINING CARON BELOW
    "◌̭": "_^",    # COMBINING CIRCUMFLEX ACCENT BELOW
    "◌̮": "_]",    # COMBINING BREVE BELOW
    "◌̯": "_)]",   # COMBINING INVERTED BREVE BELOW
    "◌̰": "_ñ",    # COMBINING TILDE BELOW
    "◌̱": "_-",    # COMBINING MACRON BELOW
    "◌̲": "_¿-",   # COMBINING LOW LINE
    "◌̳": "_--",   # COMBINING DOUBLE LOW LINE
    "◌̴": "~",     # COMBINING TILDE OVERLAY
    "◌̵": "==",    # COMBINING SHORT STROKE OVERLAY
    "◌̶": "=",     # COMBINING LONG STROKE OVERLAY
    "◌̷": "#/",    # COMBINING SHORT SOLIDUS OVERLAY
    "◌̸": "/",     # COMBINING LONG SOLIDUS OVERLAY
    "◌̹": "_)",    # COMBINING RIGHT HALF RING BELOW
    "◌̺": "apc.",  # COMBINING INVERTED BRIDGE BELOW
    "◌̻": "lmn.",  # COMBINING SQUARE BELOW
    "◌̼": "lbd.",  # COMBINING SEAGULL BELOW
    "◌̽": "x.",    # COMBINING X ABOVE
    "◌̾": ")~",    # COMBINING VERTICAL TILDE
    "◌̿": "--",    # COMBINING DOUBLE OVERLINE
    "◌ͅ": "i",     # COMBINING GREEK YPOGEGRAMMENI

    # generated by types of canonical decomposition
    # https://www.unicode.org/reports/tr44/#Character_Decomposition_Mappings
    "<super>": "*",
    "<sub>": "_",
    "<circle>": "(",
    "<wide>": "{",
    "<square>": "[",
    "<compat>": "$",
    "<small>": "}",

    "ascii": "<",
    "parens": "((",

    # diacritics defined in custom_dia
    "STROKE": "=",
    "STROKE2": "-",
    "OBLIQUESTROKE": "~~",
    "SLASH": "/",
    "ASCENDER": "'",
    "DESCENDER": "¡",
    "FLIPPED": ")",
    "SIDEWAYS": "))",
    "SMALLCAPS": ">",
    "RING": "%",
    "HOOK": "%",
    "TILDE": "~",
    "PALATAL": "·",
    "MOLODSTOVPALATAL": "·",
    "CYRDESCENDER": "¬",
    "LONG": "¿",
    "UM": "-/",
    "INSULAR": "#",
    "GLOTTAL": "glt.",
    "QUAD": "[",
    "UNDERBAR": "=",
    "DIAERESIS": "\"",

    "OXIA": "\"",
    "BOLD": "B.",
    "ITALIC": "I.",
    "BOLD_ITALIC": "BI.",
    "SANS": "S.",
    "SANS_BOLD": "SB.",
    "SANS_ITALIC": "SI.",
    "SANS_BOLD_ITALIC": "SBI.",
    "SCRIPT": "C.",
    "SCRIPT_BOLD": "CB.",
    "FRAKTUR": "F.",
    "FRAKTUR_BOLD": "FB.",
    "MONO": "M.",
    "DOUBLE": "D.",
}

ligatures = {
    "Æ": "AE", "æ": "ae",
    "Œ": "OE", "œ": "oe",
    "ꭢ": "ɔe",
    "ꭣ": "uo",
    "ꭦ": "dʐ",
    "ꭧ": "tʂ",
    "ꬱ": "aə",
    "ꭀ": "oə",
    "ꭁ": "əø",
    "ꭂ": "əɵ",
    "ꭃ": "co",
    "ꭄ": "cø",
    "Ꜳ": "AA", "ꜳ": "aa",
    "Ꜵ": "AO", "ꜵ": "ao",
    "Ꜷ": "AU", "ꜷ": "au",
    "Ꜹ": "AV", "ꜹ": "av",
    "Ꜽ": "AY", "ꜽ": "ay",
    "Ꝡ": "WY", "ꝡ": "wy",
    "Ꝏ": "OO", "ꝏ": "oo",
    "ᵫ": "ue",
    "ɮ": "lʒ",
    "ʣ": "dz",
    "ʤ": "dʒ",
    "ʥ": "dʑ",
    "ʦ": "ts",
    "ʧ": "tʃ",
    "ʨ": "tɕ",
    "ʩ": "fŋ",
    "ʪ": "ls",
    "ʫ": "lz",
    "ȸ": "db",
    "ȹ": "qp",
    "ꜩ": "tʒ",
    "𝼑": "lr",
    "ﬀ": "ff",
    "ﬁ": "fi",
    "ﬂ": "fl",
    "ﬃ": "ffi",
    "ﬄ": "ffl",
    "ﬅ": "ſt",
    "ﬆ": "st",
}

spacing_dia: tuple[str, str] = (
    "◌̀◌̈◌̄◌́◌̧◌̂◌̌◌̍◌̩◌̱◌̖◌̗◌̆◌̇◌̊◌̨◌̃◌̋◌̬◌̿◌̥◌̰",
    "`¨¯´¸ˆˇˈˌˍˎˏ˘˙˚˛˜˝ˬ˭˳˷"
)
spacing_dia = (''.join(spacing_dia[0].strip('◌').split('◌')), spacing_dia[1])
