using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000109: Julie
/// </summary>
public class _11000109 : NpcScript {
    internal _11000109(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000446$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407000448$ 
                // - Aren't you scared to be here? It's too high up for my liking...
                return true;
            default:
                return true;
        }
    }
}
