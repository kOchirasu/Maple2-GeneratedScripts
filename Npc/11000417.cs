using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000417: Sid
/// </summary>
public class _11000417 : NpcScript {
    internal _11000417(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000837$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:1121222006000838$ 
                // - How may I help you?
                return true;
            default:
                return true;
        }
    }
}
