using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004058: Orde
/// </summary>
public class _11004058 : NpcScript {
    internal _11004058(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010089$ 
                // - I'm... sorry about what happened to the leaders of Terrun Calibre.
                return true;
            case 10:
                // $script:0614185307010090$ 
                // - I'm... sorry about what happened to the leaders of Terrun Calibre.
                return true;
            default:
                return true;
        }
    }
}
