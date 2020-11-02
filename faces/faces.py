import random
from random import choice

import discord
from redbot.core import commands

FACES = [
    "¢‿¢",
    "©¿© o",
    "ª{•̃̾_•̃̾}ª",
    "¬_¬",
    "¯＼(º_o)/¯",
    "¯\\(º o)/¯",
    "¯\\_(⊙︿⊙)_/¯",
    "¯\\_(ツ)_/¯",
    "°ω°",
    "°Д°",
    "°‿‿°",
    "°ﺑ°",
    "´ ▽ ` )ﾉ",
    "¿ⓧ_ⓧﮌ",
    "Ò,ó",
    "ó‿ó",
    "ô⌐ô",
    "ôヮô",
    "ŎםŎ",
    "ŏﺡó",
    "ʕ•̫͡•ʔ",
    "ʕ•ᴥ•ʔ",
    "ʘ‿ʘ",
    "˚•_•˚",
    "˚⌇˚",
    "˚▱˚",
    "̿ ̿̿'̿'\\̵͇̿̿\\=(•̪●)=/̵͇̿̿/'̿̿ ̿ ̿ ̿",
    "͡° ͜ʖ ͡°",
    "Σ ◕ ◡ ◕",
    "Σ (ﾟДﾟ;)",
    "Σ(ﾟДﾟ；≡；ﾟдﾟ)",
    "Σ(ﾟДﾟ )",
    "Σ(||ﾟДﾟ)",
    "Φ,Φ",
    "δﺡό",
    "σ_σ",
    "д_д",
    "ф_ф",
    "щ（ﾟДﾟщ）",
    "щ(ಠ益ಠщ)",
    "щ(ಥДಥщ)",
    "Ծ_Ծ",
    "أ‿أ",
    "ب_ب",
    "ح˚௰˚づ",
    "ح˚ᆺ˚ว",
    "حᇂﮌᇂ)",
    "٩๏̯͡๏۶",
    "٩๏̯͡๏)۶",
    "٩◔̯◔۶",
    "٩(×̯×)۶",
    "٩(̾●̮̮̃̾•̃̾)۶",
    "٩(͡๏̯͡๏)۶",
    "٩(͡๏̯ ͡๏)۶",
    "٩(ಥ_ಥ)۶",
    "٩(•̮̮̃•̃)۶",
    "٩(●̮̮̃•̃)۶",
    "٩(●̮̮̃●̃)۶",
    "٩(｡͡•‿•｡)۶",
    "٩(-̮̮̃•̃)۶",
    "٩(-̮̮̃-̃)۶",
    "۞_۞",
    "۞_۟۞",
    "۹ↁﮌↁ",
    "۹⌤_⌤۹",
    "॓_॔",
    "१✌◡✌५",
    "१|˚–˚|५",
    "ਉ_ਉ",
    "ଘ_ଘ",
    "இ_இ",
    "ఠ_ఠ",
    "రృర",
    "ಠ¿ಠi",
    "ಠ‿ಠ",
    "ಠ⌣ಠ",
    "ಠ╭╮ಠ",
    "ಠ▃ಠ",
    "ಠ◡ಠ",
    "ಠ益ಠ",
    "ಠ益ಠ",
    "ಠ︵ಠ凸",
    "ಠ , ಥ",
    "ಠ.ಠ",
    "ಠoಠ",
    "ಠ_ృ",
    "ಠ_ಠ",
    "ಠ_๏",
    "ಠ~ಠ",
    "ಡ_ಡ",
    "ತಎತ",
    "ತ_ತ",
    "ಥдಥ",
    "ಥ‿ಥ",
    "ಥ⌣ಥ",
    "ಥ◡ಥ",
    "ಥ﹏ಥ",
    "ಥ_ಥ",
    "ಭ_ಭ",
    "ರ_ರ",
    "ಸ , ໖",
    "ಸ_ಸ",
    "ക_ക",
    "อ้_อ้",
    "อ_อ",
    "โ๏௰๏ใ ื",
    "๏̯͡๏﴿",
    "๏̯͡๏",
    "๏̯͡๏﴿",
    "๏[-ิิ_•ิ]๏",
    "๏_๏",
    "໖_໖",
    "༺‿༻",
    "ლ(´ڡ`ლ)",
    "ლ(́◉◞౪◟◉‵ლ)",
    "ლ(ಠ益ಠლ)",
    "ლ(╹◡╹ლ)",
    "ლ(◉◞౪◟◉‵ლ)",
    "ლ,ᔑ•ﺪ͟͠•ᔐ.ლ",
    "ᄽὁȍ ̪ őὀᄿ",
    "ᕕ( ᐛ )ᕗ",
    "ᕙ(⇀‸↼‶)ᕗ",
    "ᕦ(ò_óˇ)ᕤ",
    "ᶘ ᵒᴥᵒᶅ",
    "‘︿’",
    "•▱•",
    "•✞_✞•",
    "•ﺑ•",
    "•(⌚_⌚)•",
    "•_•)",
    "‷̗ↂ凸ↂ‴̖",
    "‹•.•›",
    "‹› ‹(•¿•)› ‹›",
    "‹(ᵒᴥᵒ­­­­­)›",
    "‹(•¿•)›",
    "ↁ_ↁ",
    "⇎_⇎",
    "∩(︶▽︶)∩",
    "∩( ・ω・)∩",
    "≖‿≖",
    "≧ヮ≦",
    "⊂•⊃_⊂•⊃",
    "⊂⌒~⊃｡Д｡)⊃",
    "⊂(◉‿◉)つ",
    "⊂(ﾟДﾟ,,⊂⌒｀つ",
    "⊙ω⊙",
    "⊙▂⊙",
    "⊙▃⊙",
    "⊙△⊙",
    "⊙︿⊙",
    "⊙﹏⊙",
    "⊙０⊙",
    "⊛ठ̯⊛",
    "⋋ō_ō`",
    "━━━ヽ(ヽ(ﾟヽ(ﾟ∀ヽ(ﾟ∀ﾟヽ(ﾟ∀ﾟ)ﾉﾟ∀ﾟ)ﾉ∀ﾟ)ﾉﾟ)ﾉ)ﾉ━━━",
    "┌∩┐(◕_◕)┌∩┐",
    "┌( ಠ_ಠ)┘",
    "┌( ಥ_ಥ)┘",
    "╚(•⌂•)╝",
    "╭╮╭╮☜{•̃̾_•̃̾}☞╭╮╭╮",
    "╭✬⌢✬╮",
    "╮(─▽─)╭",
    "╯‵Д′)╯彡┻━┻",
    "╰☆╮",
    "□_□",
    "►_◄",
    "◃┆◉◡◉┆▷",
    "◉△◉",
    "◉︵◉",
    "◉_◉",
    "○_○",
    "●¿●\\ ~",
    "●_●",
    "◔̯◔",
    "◔ᴗ◔",
    "◔ ⌣ ◔",
    "◔_◔",
    "◕ω◕",
    "◕‿◕",
    "◕◡◕",
    "◕ ◡ ◕",
    "◖♪_♪|◗",
    "◖|◔◡◉|◗",
    "◘_◘",
    "◙‿◙",
    "◜㍕◝",
    "◪_◪",
    "◮_◮",
    "☁ ☝ˆ~ˆ☂",
    "☆¸☆",
    "☉‿⊙",
    "☉_☉",
    "☐_☐",
    "☜ق❂Ⴢ❂ق☞",
    "☜(⌒▽⌒)☞",
    "☜(ﾟヮﾟ☜)",
    "☜-(ΘLΘ)-☞",
    "☝☞✌",
    "☮▁▂▃▄☾ ♛ ◡ ♛ ☽▄▃▂▁☮",
    "☹_☹",
    "☻_☻",
    "☼.☼",
    "☾˙❀‿❀˙☽",
    "♀ح♀ヾ",
    "♥‿♥",
    "♥╣[-_-]╠♥",
    "♥╭╮♥",
    "♥◡♥",
    "✌♫♪˙❤‿❤˙♫♪✌",
    "✌.ʕʘ‿ʘʔ.✌",
    "✌.|•͡˘‿•͡˘|.✌",
    "✖‿✖",
    "✖_✖",
    "❐‿❑",
    "⨀_⨀",
    "⨀_Ꙩ",
    "⨂_⨂",
    "〆(・∀・＠)",
    "《〠_〠》",
    "【•】_【•】",
    "〠_〠",
    "〴⋋_⋌〵",
    "の� �の",
    "ニガー? ━━━━━━(ﾟ∀ﾟ)━━━━━━ ニガー?",
    "ペ㍕˚\\",
    "ヽ(´ｰ｀ )ﾉ",
    "ヽ(๏∀๏ )ﾉ",
    "ヽ(｀Д´)ﾉ",
    "ヽ(ｏ`皿′ｏ)ﾉ",
    "ヽ(`Д´)ﾉ",
    "ㅎ_ㅎ",
    "乂◜◬◝乂",
    "凸ಠ益ಠ)凸",
    "句_句",
    "Ꙩ⌵Ꙩ",
    "Ꙩ_Ꙩ",
    "ꙩ_ꙩ",
    "Ꙫ_Ꙫ",
    "ꙫ_ꙫ",
    "ꙮ_ꙮ",
    "흫_흫",
    "句_句",
    "﴾͡๏̯͡๏﴿ O'RLY?",
    "¯\\(ºдಠ)/¯",
    "（·×·）",
    "（⌒Д⌒）",
    "（╹ェ╹）",
    "（♯・∀・）⊃",
    "（　´∀｀）☆",
    "（　´∀｀）",
    "（゜Д゜）",
    "（・∀・）",
    "（・Ａ・）",
    "（ﾟ∀ﾟ）",
    "（￣へ￣）",
    "（ ´☣///_ゝ///☣｀）",
    "（ つ Д ｀）",
    "＿☆（ ´_⊃｀）☆＿",
    "｡◕‿‿◕｡",
    "｡◕ ‿ ◕｡",
    "!⑈ˆ~ˆ!⑈",
    "!(｀･ω･｡)",
    "(¬‿¬)",
    "(¬▂¬)",
    "(¬_¬)",
    "(°ℇ °)",
    "(°∀°)",
    "(´ω｀)",
    "(´◉◞౪◟◉)",
    "(´ヘ｀;)",
    "(´・ω・｀)",
    "(´ー｀)",
    "(ʘ‿ʘ)",
    "(ʘ_ʘ)",
    "(˚இ˚)",
    "(͡๏̯͡๏)",
    "(ΘεΘ;)",
    "(ι´Д｀)ﾉ",
    "(Ծ‸ Ծ)",
    "(॓_॔)",
    "(० ्०)",
    "(ு८ு_ .:)",
    "(ಠ‾ಠ)",
    "(ಠ‿ʘ)",
    "(ಠ‿ಠ)",
    "(ಠ⌣ಠ)",
    "(ಠ益ಠ ╬)",
    "(ಠ益ಠ)",
    "(ಠ_ృ)",
    "(ಠ_ಠ)",
    "(ಥ﹏ಥ)",
    "(ಥ_ಥ)",
    "(๏̯͡๏ )",
    "(ღ˘⌣˘ღ) ♫･*:.｡. .｡.:*･",
    "(ღ˘⌣˘ღ)",
    "(ᵔᴥᵔ)",
    "(•ω•)",
    "(•‿•)",
    "(•⊙ω⊙•)",
    "(• ε •)",
    "(∩▂∩)",
    "(∩︵∩)",
    "(∪ ◡ ∪)",
    "(≧ω≦)",
    "(≧◡≦)",
    "(≧ロ≦)",
    "(⊙ヮ⊙)",
    "(⊙_◎)",
    "(⋋▂⋌)",
    "(⌐■_■)",
    "(─‿‿─)",
    "(┛◉Д◉)┛┻━┻",
    "(╥_╥)",
    "(╬ಠ益ಠ)",
    "(╬◣д◢)",
    "(╬ ಠ益ಠ)",
    "(╯°□°）╯︵ ┻━┻",
    "(╯ಊ╰)",
    "(╯◕_◕)╯",
    "(╯︵╰,)",
    "(╯3╰)",
    "(╯_╰)",
    "(╹◡╹)凸",
    "(▰˘◡˘▰)",
    "(●´ω｀●)",
    "(●´∀｀●)",
    "(◑‿◐)",
    "(◑◡◑)",
    "(◕‿◕✿)",
    "(◕‿◕)",
    "(◕‿-)",
    "(◕︵◕)",
    "(◕ ^ ◕)",
    "(◕_◕)",
    "(◜௰◝)",
    "(◡‿◡✿)",
    "(◣_◢)",
    "(☞ﾟ∀ﾟ)☞",
    "(☞ﾟヮﾟ)☞",
    "(☞ﾟ ∀ﾟ )☞",
    "(☼◡☼)",
    "(☼_☼)",
    "(✌ﾟ∀ﾟ)☞",
    "(✖╭╮✖)",
    "(✪㉨✪)",
    "(✿◠‿◠)",
    "(✿ ♥‿♥)",
    "(　・∀・)",
    "(　･ัω･ั)？",
    "(　ﾟ∀ﾟ)o彡゜えーりんえーりん!!",
    "(。・_・。)",
    "(つд｀)",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ益ಠ)ノ彡┻━┻",
    "(ノ ◑‿◑)ノ",
    "(ノ_・。)",
    "(・∀・ )",
    "(屮ﾟДﾟ)屮",
    "(︶ω︶)",
    "(︶︹︺)",
    "(ﺧ益ﺨ)",
    "(；一_一)",
    "(｀・ω・´)”",
    "(｡◕‿‿◕｡)",
    "(｡◕‿◕｡)",
    "(｡◕ ‿ ◕｡)",
    "(｡♥‿♥｡)",
    "(｡･ω..･)っ",
    "(･ｪ-)",
    "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
    "(ﾟДﾟ)",
    "(ﾟДﾟ)y─┛~~",
    "(ﾟ∀ﾟ)",
    "(ﾟヮﾟ)",
    "(￣□￣)",
    "(￣。￣)",
    "(￣ー￣)",
    "(￣(エ)￣)",
    "( °٢° )",
    "( ´_ゝ｀)",
    "( ͡° ͜ʖ ͡°)",
    "( ͡~ ͜ʖ ͡°)",
    "( ಠ◡ಠ )",
    "( •_•)>⌐■-■",
    "( 　ﾟ,_ゝﾟ)",
    "( ･ิз･ิ)",
    "( ﾟдﾟ)､",
    "( ^▽^)σ)~O~)",
    "((((゜д゜;))))",
    "(*´д｀*)",
    "(*..Д｀)",
    "(*..д｀*)",
    "(*~▽~)",
    "(-’๏_๏’-)",
    "(-＿- )ノ",
    "(/◔ ◡ ◔)/",
    "(///_ಥ)",
    "(;´Д`)",
    "(=ω=;)",
    "(=゜ω゜)",
    "(>'o')>♥<('o'<)",
    "(n˘v˘•)¬",
    "(o´ω｀o)",
    "(V)(°,,°)(V)",
    "(\/) (°,,°) (\/) WOOPwoopwowopwoopwoopwoop!",
    "(^▽^)",
    "(`･ω･´)",
    "(~￣▽￣)~",
    "/╲/\\╭ºoꍘoº╮/\\╱\\",
    "<【☯】‿【☯】>",
    "= (ﾟдﾟ)ｳ",
    "@_@",
    "d(*⌒▽⌒*)b",
    "o(≧∀≦)o",
    "o(≧o≦)o",
    "q(❂‿❂)p",
    "y=ｰ( ﾟдﾟ)･∵.",
    "\\˚ㄥ˚\\",
    "\\ᇂ_ᇂ\\",
    "\\(ಠ ὡ ಠ )/",
    "\\(◕ ◡ ◕\\)",
    "^̮^",
    "^ㅂ^",
    "_(͡๏̯͡๏)_",
    "{´◕ ◡ ◕｀}",
    "{ಠ_ಠ}__,,|,",
    "{◕ ◡ ◕}",
]


class Faces(commands.Cog):
    """
    Generate fun/random unicode faces courtesy of the CIA files
    """

    def __init__(self, bot):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete
        """
        return

    @commands.command(aliases=["japaneseface"])
    async def face(self, ctx, number=None):
        """Japanese Faces at random courtesy of the CIA"""
        if number is None:
            await ctx.send(choice(FACES))
            return
        if "<@" in str(number):
            random.seed(number.strip("<@!>"))
            userface = FACES[random.randint(0, len(FACES))]
            await ctx.send(userface)
            return
        if number.isdigit():
            if int(number) <= len(FACES):
                await ctx.send(FACES[int(number) - 1])
                return
            else:
                await ctx.send("That number is too large, pick less than {}!".format(len(FACES)))
                return
        if not number.isdigit() and "<@!" not in number:
            await ctx.send(FACES[len(number)])
