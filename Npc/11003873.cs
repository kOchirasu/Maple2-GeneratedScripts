using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003873: Huckleson
/// </summary>
public class _11003873 : NpcScript {
    internal _11003873(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009862$ 
                // - This is good enough... right?
                return true;
            case 10:
                // $script:0417135107009863$ 
                // - Oh, do you need help?
                return true;
            default:
                return true;
        }
    }
}
