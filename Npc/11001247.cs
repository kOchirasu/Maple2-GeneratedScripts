using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001247: Rejan
/// </summary>
public class _11001247 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1125194807004500$
    // - Hm? You're awake!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1125194807004503$
                // - Five of the Eight Blades have betrayed us. Are we sure we can trust the remaining three?
                switch (selection) {
                    // $script:1205185107004725$
                    // - Who are the remaining three Blades?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1205185107004726$
                // - If you can't remember that, maybe you're in worse shape than I thought... There's $npcName:11001246[gender:0]$, your teacher, $npcName:11001230[gender:0]$, the current leader of Terrun Calibre, and Vaharin, who's been missing for a pretty long while.
                switch (selection) {
                    // $script:1205185107004727$
                    // - And the five turncoat Blades?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1205185107004728$
                // - Well, there's my teacher and Arazaad's murderer, $npcName:11001231[gender:0]$, and his sworn brothers Zurile, Dalt, Kirisika, and Kahm. They're all in Jibricia and have very little love for the Pelgia sect.
                switch (selection) {
                    // $script:1205185107004729$
                    // - Is their association with Jibricia a problem?
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:1205185107004730$
                // - You really are your teacher's student, aren't you? While $npcName:11001246[gender:0]$ has always argued in favor of a strong, united Terrun Calibre, it's always seemed most Runeblades disagree with him, and this recent turn of events proves it.
                return -1;
            case (34, 0):
                // $script:1205185107004731$
                // - The man that $npcName:11001231[gender:0]$ killed was both the leader of the Pelgia sect and Terrun Calibre as a whole. While not all of the Jibricia have turned against us entirely turned against us, his actions have us teetering on the edge of civil war.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
