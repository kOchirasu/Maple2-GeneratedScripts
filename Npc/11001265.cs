using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001265: Eupheria
/// </summary>
public class _11001265 : NpcScript {
    internal _11001265(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;60;70
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1203182807004707$ 
                // - Have you come to see me?
                return true;
            case 30:
                // $script:1206005307004760$ 
                // - Though I deeply wish to pursue $npcName:11001231[gender:0]$, for now I will follow $npcName:11001246[gender:0]$'s advice and bide my time.
                switch (selection) {
                    // $script:1206005307004761$
                    // - What advice is that?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1206005307004762$ 
                // - He said I'd need another ten years' training to have a hope of defeating $npcName:11001231[gender:0]$. I can't put into words how much that stings, but deep down, I know he's right.
                return true;
            case 40:
                // $script:1216035207005142$ 
                // - Can I help you with something, $MyPCName$?
                switch (selection) {
                    // $script:1216035207005143$
                    // - I'm looking for something.
                    case 0:
                        Id = 41;
                        return false;
                    // $script:1216035207005144$
                    // - No.
                    case 1:
                        Id = 100;
                        return false;
                }
                return true;
            case 41:
                // $script:1216035207005145$ 
                // - If you've come to me, then you must have a problem that only I can assist you with. Speak.
                switch (selection) {
                    // $script:1216035207005146$
                    // - Do you have a spare $item:40000022$?
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:1216035207005147$ 
                // - You're here for the $item:40000022$? Please wait a moment.
                switch (selection) {
                    // $script:1216035207005148$
                    // - (Wait several moments.)
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1216035207005149$ 
                // - Is this what you're looking for? It's what was written in that copy of the Wisdom of the Baaz you showed me.
                switch (selection) {
                    // $script:1216035207005150$
                    // - That's right.
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1216035207005151$ 
                // - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
                switch (selection) {
                    // $script:1216035207005152$
                    // - Sure.
                    case 0:
                        Id = 0; // TODO: 53 | 90
                        return false;
                }
                return true;
            case 53:
                // $script:1216035207005153$ functionID=1 
                // - Here, take it. You're lucky I transcribed an extra copy.
                return true;
            case 60:
                // $script:1216035207005154$ 
                // - Can I help you with something, $MyPCName$?
                switch (selection) {
                    // $script:1216035207005155$
                    // - I'm looking for something.
                    case 0:
                        Id = 61;
                        return false;
                    // $script:1216035207005156$
                    // - No.
                    case 1:
                        Id = 100;
                        return false;
                }
                return true;
            case 61:
                // $script:1216035207005157$ 
                // - If you've come to me, then you must have a problem that only I can assist you with. Speak.
                switch (selection) {
                    // $script:1216035207005158$
                    // - Do you have a spare $item:40000024$?
                    case 0:
                        Id = 62;
                        return false;
                    // $script:1216113507005178$
                    // - Do you have a spare $item:40000022$?
                    case 1:
                        Id = 50;
                        return false;
                }
                return true;
            case 62:
                // $script:1216035207005159$ 
                // - You're here for the $item:40000024$? Please wait a moment.
                switch (selection) {
                    // $script:1216035207005160$
                    // - (Wait several moments.)
                    case 0:
                        Id = 0; // TODO: 63 | 69
                        return false;
                }
                return true;
            case 63:
                // $script:1216035207005161$ 
                // - Is this what you're looking for? It's what was written in that copy of the Wisdom of the Baaz you showed me.
                switch (selection) {
                    // $script:1216035207005162$
                    // - That's right.
                    case 0:
                        Id = 64;
                        return false;
                }
                return true;
            case 64:
                // $script:1216035207005163$ 
                // - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
                switch (selection) {
                    // $script:1216035207005164$
                    // - Sure.
                    case 0:
                        Id = 0; // TODO: 65 | 90
                        return false;
                }
                return true;
            case 65:
                // $script:1216035207005165$ functionID=2 
                // - Here, take it. You're lucky I transcribed an extra copy.
                return true;
            case 69:
                // $script:1216035207005166$ 
                // - According to the documents we've restored, it's likely that the writings in this $item:40000024$ originated from the second volume of the Wisdom of the Baaz. If you want to complete it, you need that volume.
                return true;
            case 70:
                // $script:1216040007005167$ 
                // - Can I help you with something, $MyPCName$?
                switch (selection) {
                    // $script:1216040007005168$
                    // - I'm looking for something.
                    case 0:
                        Id = 71;
                        return false;
                    // $script:1216040007005169$
                    // - No.
                    case 1:
                        Id = 100;
                        return false;
                }
                return true;
            case 71:
                // $script:1216040007005170$ 
                // - If you've come to me, then you must have a problem that only I can assist you with. Speak.
                switch (selection) {
                    // $script:1216040007005171$
                    // - Do you have a spare $item:40000023$?
                    case 0:
                        Id = 72;
                        return false;
                    // $script:1216113507005179$
                    // - Do you have a spare $item:40000024$?
                    case 1:
                        Id = 62;
                        return false;
                    // $script:1216113507005180$
                    // - Do you have a spare $item:40000022$?
                    case 2:
                        Id = 50;
                        return false;
                }
                return true;
            case 72:
                // $script:1216031507005132$ 
                // - You're here for the $item:40000023$? Please wait a moment.
                switch (selection) {
                    // $script:1216031507005133$
                    // - (Wait several moments.)
                    case 0:
                        Id = 0; // TODO: 73 | 79
                        return false;
                }
                return true;
            case 73:
                // $script:1216031507005134$ 
                // - Is this what you're looking for? It's what was written in that copy of the Wisdom of the Baaz you showed me.
                switch (selection) {
                    // $script:1216031507005135$
                    // - That's right.
                    case 0:
                        Id = 74;
                        return false;
                }
                return true;
            case 74:
                // $script:1216031507005136$ 
                // - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
                switch (selection) {
                    // $script:1216031507005137$
                    // - Sure.
                    case 0:
                        Id = 0; // TODO: 75 | 90
                        return false;
                }
                return true;
            case 75:
                // $script:1216031507005138$ functionID=3 
                // - Here, take it. You're lucky I transcribed an extra copy.
                return true;
            case 79:
                // $script:1216031507005139$ 
                // - According to the documents we've restored, it's likely that the writings in this $item:40000023$ originated from the third volume of the Wisdom of the Baaz. If you want to complete it, you need that volume.
                return true;
            case 90:
                // $script:1216031507005140$ 
                // - I do not believe you have room in your bag for this. Why not clear some space?
                return true;
            case 100:
                // $script:1216031507005141$ 
                // - Hmm? Well, come back when you need my help.
                return true;
            default:
                return true;
        }
    }
}
