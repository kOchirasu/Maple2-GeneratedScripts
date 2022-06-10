using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003156: Pippy
/// </summary>
public class _11003156 : NpcScript {
    internal _11003156(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0306155707008047$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0306155707008049$ 
                // - I know, right? All three of us are pretty, but the prettiest one is... oh, you were talking about the flowers. Sure, they're pretty too! Ah, forget what I said earlier.
                return true;
            default:
                return true;
        }
    }
}
