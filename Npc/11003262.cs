using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003262: Kaitlyn
/// </summary>
public class _11003262 : NpcScript {
    internal _11003262(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008202$ 
                // - Professor $npcName:11003251[gender:0]$... 
                return true;
            case 30:
                // $script:0403155707008203$ 
                // - Where is he? I have to find him. He isn't himself!
                switch (selection) {
                    // $script:0403155707008204$
                    // - What do you know about this?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0403155707008205$ 
                // - N-nothing! I... I don't know anything...
                //   <font color="#909090">($npcName:11003146[gender:1]$ shakes her head in frustration.)</font>
                return true;
            default:
                return true;
        }
    }
}
