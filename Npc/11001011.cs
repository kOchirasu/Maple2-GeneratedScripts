using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001011: Navue
/// </summary>
public class _11001011 : NpcScript {
    internal _11001011(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003450$ 
                // - Well, there goes the neighborhood.
                return true;
            case 30:
                // $script:0831180407003453$ 
                // - My realtor said that I'd only hear the sound of waves. I wouldn't have come here if I knew my neighbors would be so terrible.
                return true;
            default:
                return true;
        }
    }
}
