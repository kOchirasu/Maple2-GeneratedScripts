using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001466: Monliver Olivieta
/// </summary>
public class _11001466 : NpcScript {
    internal _11001466(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1223035407005524$ 
                // - Please put your money right here. Thank you.
                return true;
            case 30:
                // $script:1223035407005527$ 
                // - Don't you know who my brother is?
                return true;
            default:
                return true;
        }
    }
}
