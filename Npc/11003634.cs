using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003634: Becker
/// </summary>
public class _11003634 : NpcScript {
    internal _11003634(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009034$ 
                // - I'm a man on a mission.
                return true;
            case 10:
                // $script:1109121007009035$ 
                // - Let's get to business.
                switch (selection) {
                    // $script:1109121007009036$
                    // - $npcName:11003535[gender:1]$ sent me.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009037$ 
                // - Yeah, likely story. How do I know I can trust you?
                switch (selection) {
                    // $script:1109121007009038$
                    // - There's got to be a way to prove myself.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009039$ 
                // - If $npcName:11003535[gender:1]$ really sent you, then you should know Dark Wind's motto.
                switch (selection) {
                    // $script:1109121007009040$
                    // - All hail $npcName:11000006[gender:0]$!
                    case 0:
                        Id = 13;
                        return false;
                    // $script:1109121007009041$
                    // - All hail $npcName:11000044[gender:0]$!
                    case 1:
                        Id = 14;
                        return false;
                    // $script:1109121007009042$
                    // - (Say nothing.)
                    case 2:
                        Id = 15;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009043$ 
                // - You are a fool.
                switch (selection) {
                    // $script:1109121007009044$
                    // - Give me another chance!
                    case 0:
                        Id = 16;
                        return false;
                }
                return true;
            case 14:
                // $script:1109121007009045$ 
                // - You think I'm stupid? There's no way $npcName:11003535[gender:1]$ would send an idiot like you.
                switch (selection) {
                    // $script:1109121007009046$
                    // - Give me another chance!
                    case 0:
                        Id = 16;
                        return false;
                }
                return true;
            case 15:
                // $script:1109121007009047$ 
                // - Ah, so $npcName:11003535[gender:1]$ did send you, after all. Good. Tell her, "Ducky. Purple slime. Cerbe."
                switch (selection) {
                    // $script:1109121007009048$
                    // - Really?
                    case 0:
                        Id = 17;
                        return false;
                }
                return true;
            case 16:
                // $script:1109121007009049$ 
                // - What's Dark Wind's slogan?
                switch (selection) {
                    // $script:1109121007009050$
                    // - All hail $npcName:11000006[gender:0]$!
                    case 0:
                        Id = 13;
                        return false;
                    // $script:1109121007009051$
                    // - All hail $npcName:11000044[gender:0]$!
                    case 1:
                        Id = 14;
                        return false;
                    // $script:1109121007009052$
                    // - (Say nothing.)
                    case 2:
                        Id = 15;
                        return false;
                }
                return true;
            case 17:
                // $script:1109121007009053$ 
                // - Don't leave anything out! Tell her <i>exactly</i> what I said!
                return true;
            default:
                return true;
        }
    }
}
