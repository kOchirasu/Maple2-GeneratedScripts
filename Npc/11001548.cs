using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001548: Suspicious Individual
/// </summary>
public class _11001548 : NpcScript {
    internal _11001548(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006395$ 
                // - What seems to be the problem? 
                return true;
            case 10:
                // $script:0629000607006396$ 
                // - I've got nothing to say to you. 
                return true;
            default:
                return true;
        }
    }
}
