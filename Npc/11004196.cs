using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004196: Luanna
/// </summary>
public class _11004196 : NpcScript {
    internal _11004196(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010640$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:0806025707010641$ 
                // - The world relies on the strength of heroes like you. May the empress's blessing be with you. 
                return true;
            default:
                return true;
        }
    }
}
