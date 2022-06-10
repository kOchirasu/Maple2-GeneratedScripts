using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004195: Ereve
/// </summary>
public class _11004195 : NpcScript {
    internal _11004195(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010638$ 
                // - $MyPCName$, what brings you to me? 
                return true;
            case 10:
                // $script:0806025707010639$ 
                // - You must always believe in yourself. Though the road is long and difficult, it is our duty to bring peace to this world. 
                return true;
            default:
                return true;
        }
    }
}
