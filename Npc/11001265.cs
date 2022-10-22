using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001265: Eupheria
/// </summary>
public class _11001265 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;60;70
    }

    // Select 0:
    // $script:1203182807004707$
    // - Have you come to see me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1206005307004760$
                // - Though I deeply wish to pursue $npcName:11001231[gender:0]$, for now I will follow $npcName:11001246[gender:0]$'s advice and bide my time.
                switch (selection) {
                    // $script:1206005307004761$
                    // - What advice is that?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1206005307004762$
                // - He said I'd need another ten years' training to have a hope of defeating $npcName:11001231[gender:0]$. I can't put into words how much that stings, but deep down, I know he's right.
                return -1;
            case (40, 0):
                // $script:1216035207005142$
                // - Can I help you with something, $MyPCName$?
                switch (selection) {
                    // $script:1216035207005143$
                    // - I'm looking for something.
                    case 0:
                        return 41;
                    // $script:1216035207005144$
                    // - No.
                    case 1:
                        return 100;
                }
                return -1;
            case (41, 0):
                // $script:1216035207005145$
                // - If you've come to me, then you must have a problem that only I can assist you with. Speak.
                switch (selection) {
                    // $script:1216035207005146$
                    // - Do you have a spare $item:40000022$?
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:1216035207005147$
                // - You're here for the $item:40000022$? Please wait a moment.
                switch (selection) {
                    // $script:1216035207005148$
                    // - (Wait several moments.)
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1216035207005149$
                // - Is this what you're looking for? It's what was written in that copy of the Wisdom of the Baaz you showed me.
                switch (selection) {
                    // $script:1216035207005150$
                    // - That's right.
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:1216035207005151$
                // - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
                switch (selection) {
                    // $script:1216035207005152$
                    // - Sure.
                    case 0:
                        // TODO: goto 53
                        // TODO: gotoFail 90
                        return 90;
                }
                return -1;
            case (53, 0):
                // functionID=1 openTalkReward=True 
                // $script:1216035207005153$
                // - Here, take it. You're lucky I transcribed an extra copy.
                return -1;
            case (60, 0):
                // $script:1216035207005154$
                // - Can I help you with something, $MyPCName$?
                switch (selection) {
                    // $script:1216035207005155$
                    // - I'm looking for something.
                    case 0:
                        return 61;
                    // $script:1216035207005156$
                    // - No.
                    case 1:
                        return 100;
                }
                return -1;
            case (61, 0):
                // $script:1216035207005157$
                // - If you've come to me, then you must have a problem that only I can assist you with. Speak.
                switch (selection) {
                    // $script:1216035207005158$
                    // - Do you have a spare $item:40000024$?
                    case 0:
                        return 62;
                    // $script:1216113507005178$
                    // - Do you have a spare $item:40000022$?
                    case 1:
                        return 50;
                }
                return -1;
            case (62, 0):
                // $script:1216035207005159$
                // - You're here for the $item:40000024$? Please wait a moment.
                switch (selection) {
                    // $script:1216035207005160$
                    // - (Wait several moments.)
                    case 0:
                        // TODO: goto 63
                        // TODO: gotoFail 69
                        return 69;
                }
                return -1;
            case (63, 0):
                // $script:1216035207005161$
                // - Is this what you're looking for? It's what was written in that copy of the Wisdom of the Baaz you showed me.
                switch (selection) {
                    // $script:1216035207005162$
                    // - That's right.
                    case 0:
                        return 64;
                }
                return -1;
            case (64, 0):
                // $script:1216035207005163$
                // - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
                switch (selection) {
                    // $script:1216035207005164$
                    // - Sure.
                    case 0:
                        // TODO: goto 65
                        // TODO: gotoFail 90
                        return 90;
                }
                return -1;
            case (65, 0):
                // functionID=2 openTalkReward=True 
                // $script:1216035207005165$
                // - Here, take it. You're lucky I transcribed an extra copy.
                return -1;
            case (69, 0):
                // $script:1216035207005166$
                // - According to the documents we've restored, it's likely that the writings in this $item:40000024$ originated from the second volume of the Wisdom of the Baaz. If you want to complete it, you need that volume.
                return -1;
            case (70, 0):
                // $script:1216040007005167$
                // - Can I help you with something, $MyPCName$?
                switch (selection) {
                    // $script:1216040007005168$
                    // - I'm looking for something.
                    case 0:
                        return 71;
                    // $script:1216040007005169$
                    // - No.
                    case 1:
                        return 100;
                }
                return -1;
            case (71, 0):
                // $script:1216040007005170$
                // - If you've come to me, then you must have a problem that only I can assist you with. Speak.
                switch (selection) {
                    // $script:1216040007005171$
                    // - Do you have a spare $item:40000023$?
                    case 0:
                        return 72;
                    // $script:1216113507005179$
                    // - Do you have a spare $item:40000024$?
                    case 1:
                        return 62;
                    // $script:1216113507005180$
                    // - Do you have a spare $item:40000022$?
                    case 2:
                        return 50;
                }
                return -1;
            case (72, 0):
                // $script:1216031507005132$
                // - You're here for the $item:40000023$? Please wait a moment.
                switch (selection) {
                    // $script:1216031507005133$
                    // - (Wait several moments.)
                    case 0:
                        // TODO: goto 73
                        // TODO: gotoFail 79
                        return 79;
                }
                return -1;
            case (73, 0):
                // $script:1216031507005134$
                // - Is this what you're looking for? It's what was written in that copy of the Wisdom of the Baaz you showed me.
                switch (selection) {
                    // $script:1216031507005135$
                    // - That's right.
                    case 0:
                        return 74;
                }
                return -1;
            case (74, 0):
                // $script:1216031507005136$
                // - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
                switch (selection) {
                    // $script:1216031507005137$
                    // - Sure.
                    case 0:
                        // TODO: goto 75
                        // TODO: gotoFail 90
                        return 90;
                }
                return -1;
            case (75, 0):
                // functionID=3 openTalkReward=True 
                // $script:1216031507005138$
                // - Here, take it. You're lucky I transcribed an extra copy.
                return -1;
            case (79, 0):
                // $script:1216031507005139$
                // - According to the documents we've restored, it's likely that the writings in this $item:40000023$ originated from the third volume of the Wisdom of the Baaz. If you want to complete it, you need that volume.
                return -1;
            case (90, 0):
                // $script:1216031507005140$
                // - I do not believe you have room in your bag for this. Why not clear some space?
                return -1;
            case (100, 0):
                // $script:1216031507005141$
                // - Hmm? Well, come back when you need my help.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.SelectableDistractor,
            (63, 0) => NpcTalkButton.SelectableDistractor,
            (64, 0) => NpcTalkButton.SelectableDistractor,
            (65, 0) => NpcTalkButton.Close,
            (69, 0) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.SelectableDistractor,
            (71, 0) => NpcTalkButton.SelectableDistractor,
            (72, 0) => NpcTalkButton.SelectableDistractor,
            (73, 0) => NpcTalkButton.SelectableDistractor,
            (74, 0) => NpcTalkButton.SelectableDistractor,
            (75, 0) => NpcTalkButton.Close,
            (79, 0) => NpcTalkButton.Close,
            (90, 0) => NpcTalkButton.Close,
            (100, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
