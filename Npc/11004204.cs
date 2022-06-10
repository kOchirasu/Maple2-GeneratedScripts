using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004204: Miani
/// </summary>
public class _11004204 : NpcScript {
    internal _11004204(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010656$ 
                // - What is it? 
                return true;
            case 10:
                // $script:0806025707010657$ 
                // - Are you looking for friends, too? 
                return true;
            default:
                return true;
        }
    }
}
