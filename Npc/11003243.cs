using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003243: Tinnie
/// </summary>
public class _11003243 : NpcScript {
    internal _11003243(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008145$ 
                // - What's wrong? 
                return true;
            case 30:
                // $script:0403155707008146$ 
                // - I understand what $npcName:11003240[gender:0]$ is going through, but it's past time for him to grow up. 
                return true;
            default:
                return true;
        }
    }
}
