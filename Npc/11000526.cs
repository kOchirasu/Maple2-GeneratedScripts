using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000526: Raymon
/// </summary>
public class _11000526 : NpcScript {
    internal _11000526(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002247$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:0831180407002250$ 
                // - I need to find a better place to hide. The Dark Wind would have no trouble finding me here.
                return true;
            default:
                return true;
        }
    }
}
