using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001590: Ishura
/// </summary>
public class _11001590 : NpcScript {
    internal _11001590(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006078$ 
                // - Ah, $MyPCName$!
                return true;
            case 10:
                // $script:0515180307006129$ 
                // - No words can express my gratitude. I only hope that I can repay the empire one day.
                return true;
            case 20:
                // $script:0517210007006145$ 
                // - Why are you staring at me?
                switch (selection) {
                    // $script:0517210007006146$
                    // - I just wanted to see you.
                    case 0:
                        Id = 21;
                        return false;
                    // $script:0517210007006147$
                    // - I missed you so much!
                    case 1:
                        Id = 22;
                        return false;
                    // $script:0517210007006148$
                    // - Play with me.
                    case 2:
                        Id = 23;
                        return false;
                    // $script:0517210007006149$
                    // - There's something I need to tell you.
                    case 3:
                        Id = 24;
                        return false;
                }
                return true;
            case 21:
                // $script:0517210007006150$ 
                // - Ha... You're a strange one... 
                return true;
            case 22:
                // $script:0517210007006151$ 
                // - Y-you did? So did I. Ahem.
                return true;
            case 23:
                // $script:0517210007006152$ 
                // - Now is <i>not</i> the time for such things!
                return true;
            case 24:
                // $script:0517210007006153$ 
                // - I'm a little busy right now.
                return true;
            case 30:
                // $script:0524142307006220$ 
                // - No words can express my gratitude. I only hope that I can repay the empire one day.
                return true;
            default:
                return true;
        }
    }
}
