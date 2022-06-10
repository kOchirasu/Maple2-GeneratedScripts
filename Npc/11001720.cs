using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001720: Junta
/// </summary>
public class _11001720 : NpcScript {
    internal _11001720(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006971$ 
                // - You have something to say to me? 
                return true;
            case 30:
                // $script:0728024507007019$ 
                // - Lava and ice... an unlikely, but breathtaking, view. It reminds me of you, $npcName:11001711[gender:1]$, and myself. 
                return true;
            default:
                return true;
        }
    }
}
