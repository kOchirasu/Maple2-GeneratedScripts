using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001282: Tracker
/// </summary>
public class _11001282 : NpcScript {
    internal _11001282(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1209020507004852$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:1209020507004855$ 
                // - You're $npcName:11001267[gender:0]$'s student, aren't you? So the rumors were wrong... 
                switch (selection) {
                    // $script:1209020507004856$
                    // - Rumors? What rumors?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1209020507004857$ 
                // - W-well... No, I shouldn't. I don't want to upset you. 
                switch (selection) {
                    // $script:1209020507004858$
                    // - Don't tell me and see how upset I get!
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1209020507004859$ 
                // - Fair enough. They say $npcName:11001267[gender:0]$ has one critical weakness: his student. 
                // $script:1209020507004860$ 
                // - They say his student is stubborn, arrogant, and too reckless to be trusted with any important task. 
                switch (selection) {
                    // $script:1209020507004861$
                    // - Well, I don't care <i>what</i> they say!
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:1209020507004862$ 
                // - Good. You shouldn't. You're definitely a worthy student to a man of his stature. 
                return true;
            default:
                return true;
        }
    }
}
