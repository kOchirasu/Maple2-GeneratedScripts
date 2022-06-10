using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001711: Tinchai
/// </summary>
public class _11001711 : NpcScript {
    internal _11001711(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006963$ 
                // - Mm? What is it?
                return true;
            case 30:
                // $script:0728024507006995$ 
                // - The more I look at this place, the more mystified I am. Almost as if... it yearns for something...
                return true;
            default:
                return true;
        }
    }
}
