using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000183: Queen Bee
/// </summary>
public class _11000183 : NpcScript {
    internal _11000183(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000768$ 
                // - What izzz it?
                return true;
            case 30:
                // $script:0831180407000771$ 
                // - Honey izz very preciouz to uzz honeybeezz! We won't let anyone take it away!
                return true;
            default:
                return true;
        }
    }
}
