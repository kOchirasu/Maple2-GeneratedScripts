using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001247: Rejan
/// </summary>
public class _11001247 : NpcScript {
    internal _11001247(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1125194807004500$ 
                // - Hm? You're awake! 
                return true;
            case 30:
                // $script:1125194807004503$ 
                // - Five of the Eight Blades have betrayed us. Are we sure we can trust the remaining three? 
                switch (selection) {
                    // $script:1205185107004725$
                    // - Who are the remaining three Blades?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1205185107004726$ 
                // - If you can't remember that, maybe you're in worse shape than I thought... There's $npcName:11001246[gender:0]$, your teacher, $npcName:11001230[gender:0]$, the current leader of Terrun Calibre, and Vaharin, who's been missing for a pretty long while. 
                switch (selection) {
                    // $script:1205185107004727$
                    // - And the five turncoat Blades?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1205185107004728$ 
                // - Well, there's my teacher and Arazaad's murderer, $npcName:11001231[gender:0]$, and his sworn brothers Zurile, Dalt, Kirisika, and Kahm. They're all in Jibricia and have very little love for the Pelgia sect. 
                switch (selection) {
                    // $script:1205185107004729$
                    // - Is their association with Jibricia a problem?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:1205185107004730$ 
                // - You really are your teacher's student, aren't you? While $npcName:11001246[gender:0]$ has always argued in favor of a strong, united Terrun Calibre, it's always seemed most Runeblades disagree with him, and this recent turn of events proves it. 
                return true;
            case 34:
                // $script:1205185107004731$ 
                // - The man that $npcName:11001231[gender:0]$ killed was both the leader of the Pelgia sect and Terrun Calibre as a whole. While not all of the Jibricia have turned against us entirely turned against us, his actions have us teetering on the edge of civil war. 
                return true;
            default:
                return true;
        }
    }
}
