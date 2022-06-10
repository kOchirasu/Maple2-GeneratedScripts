using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000302: Udra
/// </summary>
public class _11000302 : NpcScript {
    internal _11000302(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001197$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:0831180407001200$ 
                // - $MyPCName$, it must be an act of the divine that you and I met. My name is $npcName:11000302[gender:1]$, and I'm currently studying under $npcName:11000039[gender:1]$.
                return true;
            default:
                return true;
        }
    }
}
